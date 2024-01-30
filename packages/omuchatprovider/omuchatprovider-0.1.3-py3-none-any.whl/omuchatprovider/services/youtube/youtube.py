from __future__ import annotations

import asyncio
import json
import re
from collections import Counter
from datetime import datetime
from typing import Dict, List, TypedDict

import bs4

from omuchat import Paid
from omuchat.client import Client
from omuchat.model import (
    MODERATOR,
    OWNER,
    Author,
    Channel,
    Content,
    ImageContent,
    Message,
    Provider,
    Role,
    Room,
    RootContent,
    TextContent,
)

from ...chatprovider import client
from ...helper import HTTP_REGEX, get_session
from ...provider import ProviderService
from ...tasks import Tasks
from .types import api

INFO = Provider(
    id="youtube",
    url="youtube.com",
    name="Youtube",
    version="0.1.0",
    repository_url="https://github.com/OMUCHAT/provider",
    description="Youtube provider",
    regex=HTTP_REGEX
    + r"(youtu\.be\/(?P<video_id_short>[\w-]+))|(m\.)?youtube\.com\/(watch\?v=(?P<video_id>[\w_-]+|)|@(?P<channel_id_vanity>[\w_-]+|)|channel\/(?P<channel_id>[\w_-]+|)|user\/(?P<channel_id_user>[\w_-]+|)|c\/(?P<channel_id_c>[\w_-]+|))",
)
session = get_session(INFO)


class ReactionEvent(TypedDict):
    room_id: str
    reactions: Dict[str, int]


REACTION = client.omu.message.register("youtube-reaction", ReactionEvent)


class YoutubeService(ProviderService):
    def __init__(self, client: Client):
        self.client = client
        self.rooms: Dict[str, YoutubeRoomService] = {}

    @property
    def info(self) -> Provider:
        return INFO

    async def start_channel(self, channel: Channel):
        if channel.url in self.rooms:
            return
        match = re.search(INFO.regex, channel.url)
        if match is None:
            raise RuntimeError("Could not match url")
        options = match.groupdict()

        video_id = options.get("video_id") or options.get("video_id_short")
        if video_id is None:
            channel_id = options.get("channel_id") or await self.channel_id_from_vanity(
                options.get("channel_id_vanity")
                or options.get("channel_id_user")
                or options.get("channel_id_c")
            )
            if channel_id is None:
                raise RuntimeError("Could not find channel id")
            video_id = await self.video_id_from_channel(channel_id)
            if video_id is None:
                raise RuntimeError("Could not find video id")

        room = await YoutubeRoomService.create(self.client, channel, video_id)
        self.rooms[channel.url] = room

    async def channel_id_from_vanity(self, vanity: str | None) -> str | None:
        if vanity is None:
            return None
        vanity_id = re.sub(r"[^a-zA-Z0-9_-]", "", vanity)
        if not vanity_id:
            return None
        res = await session.get(f"https://www.youtube.com/@{vanity_id}")
        soup = bs4.BeautifulSoup(await res.text(), "html.parser")
        meta = soup.select_one('meta[itemprop="identifier"]')
        if meta is None:
            return None
        return meta.attrs.get("content")

    async def video_id_from_channel(self, channel_id: str) -> str | None:
        res = await session.get(
            f"https://www.youtube.com/embed/live_stream?channel={channel_id}",
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
                )
            },
        )
        soup = bs4.BeautifulSoup(await res.text(), "html.parser")
        link = soup.select_one('link[rel="canonical"]')
        if link is None:
            return await self.video_id_from_channel_feeds(channel_id)
        href = link.attrs.get("href")
        if href is None:
            return None
        match = re.search(INFO.regex, href)
        if match is None:
            return None
        options = match.groupdict()
        return options.get("video_id") or options.get("video_id_short")

    async def video_id_from_channel_feeds(self, channel_id: str) -> str | None:
        res = await session.get(
            f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}",
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
                )
            },
        )
        soup = bs4.BeautifulSoup(await res.text(), "xml")
        link = soup.select_one("entry link")
        if link is None:
            return None
        href = link.attrs.get("href")
        if href is None:
            return None
        match = re.search(INFO.regex, href)
        if match is None:
            return None
        options = match.groupdict()
        return options.get("video_id") or options.get("video_id_short")

    async def stop_channel(self, channel: Channel):
        if channel.url not in self.rooms:
            return
        room = self.rooms[channel.url]
        await room.stop()
        del self.rooms[channel.url]


class YoutubeChat:
    def __init__(self, api_key: str, continuation: str):
        self.api_key = api_key
        self.continuation = continuation

    @classmethod
    async def from_url(cls, video_id: str):
        res = await session.get(
            "https://www.youtube.com/live_chat",
            params={"v": video_id},
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
                )
            },
        )
        soup = bs4.BeautifulSoup(await res.text(), "html.parser")
        data = cls.extract_ytcfg(soup)
        api_key = data["INNERTUBE_API_KEY"]
        continuation = cls.extract_continuation(soup)
        return cls(api_key, continuation)

    @classmethod
    def extract_ytcfg(cls, soup: bs4.BeautifulSoup) -> Dict:
        for script in soup.select("script"):
            text = script.text.strip()
            if text.startswith("ytcfg.set"):
                break
        else:
            raise RuntimeError("Could not find ytcfg.set")
        text = text[text.index("{") : text.rindex("}") + 1]
        data = json.loads(text)
        return data

    @classmethod
    def extract_continuation(cls, soup: bs4.BeautifulSoup) -> str:
        for script in soup.select("script"):
            text = script.text.strip()
            if text.startswith('window["ytInitialData"]'):
                break
        else:
            raise RuntimeError("Could not find ytInitialData")
        text = text[text.index("{") : text.rindex("}") + 1]
        data = json.loads(text)
        contents = data["contents"]
        if "liveChatRenderer" not in contents:
            raise RuntimeError("Could not find liveChatRenderer")
        return contents["liveChatRenderer"]["continuations"][0][
            "invalidationContinuationData"
        ]["continuation"]

    async def fetch(self) -> api.Response:
        res = await session.post(
            "https://www.youtube.com/youtubei/v1/live_chat/get_live_chat",
            params={"key": self.api_key},
            json={
                "context": {
                    "client": {
                        "clientName": "WEB",
                        "clientVersion": "2.20230622.06.00",
                    }
                },
                "continuation": self.continuation,
            },
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
                )
            },
        )
        data = await res.json()
        return data

    async def next(self) -> api.Response | None:
        data = await self.fetch()
        if "continuationContents" not in data:
            return None

        continuations = data["continuationContents"]["liveChatContinuation"].get(
            "continuations"
        )
        if continuations is None:
            return data
        continuation = continuations[0]
        if "invalidationContinuationData" not in continuation:
            return data
        self.continuation = continuation["invalidationContinuationData"]["continuation"]
        return data


class YoutubeRoomService:
    def __init__(
        self,
        client: Client,
        channel: Channel,
        room: Room,
        chat: YoutubeChat,
    ):
        self.client = client
        self.channel = channel
        self.room = room
        self.chat = chat
        self.tasks = Tasks(client.loop)

    @classmethod
    async def create(cls, client: Client, channel: Channel, video_id: str):
        room = Room(
            id=video_id,
            provider_id=INFO.key(),
            channel_id=channel.key(),
            name="Youtube",
            online=False,
            url=f"https://www.youtube.com/watch?v={video_id}",
            image_url=f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
        )
        chat = await YoutubeChat.from_url(video_id)
        self = cls(client, channel, room, chat)
        await client.rooms.add(room)

        self.tasks.create_task(self.start())
        return self

    async def start(self):
        self.room.online = True
        await self.client.rooms.update(self.room)
        while True:
            data = await self.chat.next()
            if data is None:
                break
            for action in data["continuationContents"]["liveChatContinuation"].get(
                "actions", []
            ):
                if "addChatItemAction" in action:
                    await self.process_message_item(action["addChatItemAction"]["item"])
                if "markChatItemAsDeletedAction" in action:
                    await self.process_deleted_item(
                        action["markChatItemAsDeletedAction"]
                    )
            await self.process_reactions(data)
            await asyncio.sleep(1 / 3)
        await self.stop()

    async def process_message_item(self, item: api.MessageItemData):
        if "liveChatTextMessageRenderer" in item:
            message = item["liveChatTextMessageRenderer"]
            author = self._parse_author(message)
            content = self._parse_message(message["message"])
            created_at = self._parse_created_at(message)
            await self.client.authors.add(author)
            await self.client.messages.add(
                Message(
                    id=message["id"],
                    room_id=self.room.key(),
                    author_id=author.key(),
                    content=content,
                    created_at=created_at,
                )
            )
        elif "liveChatPaidMessageRenderer" in item:
            message = item["liveChatPaidMessageRenderer"]
            author = self._parse_author(message)
            content = self._parse_message(message["message"])
            paid = self._parse_paid(message)
            created_at = self._parse_created_at(message)
            await self.client.authors.add(author)
            await self.client.messages.add(
                Message(
                    id=message["id"],
                    room_id=self.room.key(),
                    author_id=author.key(),
                    content=content,
                    paid=paid,
                    created_at=created_at,
                )
            )
        elif "liveChatMembershipItemRenderer" in item:
            message = item["liveChatMembershipItemRenderer"]
            author = self._parse_author(message)
            created_at = self._parse_created_at(message)
            content = self._parse_message(
                message["headerSubtext"]
            )  # TODO: システムメッセージとして送信できるようにする。
            await self.client.authors.add(author)
            await self.client.messages.add(
                Message(
                    id=message["id"],
                    room_id=self.room.key(),
                    author_id=author.key(),
                    content=content,
                    created_at=created_at,
                )
            )
        else:
            raise RuntimeError(f"Unknown message type: {list(item.keys())} {item=}")

    async def process_deleted_item(self, item: api.MarkChatItemAsDeletedActionData):
        message = await self.client.messages.get(
            f"{self.room.key()}#{item["targetItemId"]}"
        )
        if message:
            await self.client.messages.remove(message)

    async def process_reactions(self, data: api.Response):
        if "frameworkUpdates" not in data:
            return
        reactions: Counter[str] = Counter()
        for update in data["frameworkUpdates"]["entityBatchUpdate"]["mutations"]:
            if "payload" not in update:
                continue
            payload = update["payload"]
            if "emojiFountainDataEntity" not in payload:
                continue
            emoji = payload["emojiFountainDataEntity"]
            for bucket in emoji["reactionBuckets"]:
                for reaction in bucket.get("reactions", []):
                    reactions[reaction["key"]] += reaction["value"]
                for reaction in bucket.get("reactionsData", []):
                    reactions[reaction["unicodeEmojiId"]] += reaction["reactionCount"]
        if len(reactions) == 0:
            return
        await self.client.omu.message.broadcast(
            REACTION,
            ReactionEvent(
                room_id=self.room.key(),
                reactions=dict(reactions),
            ),
        )

    def _parse_author(self, message: api.LiveChatMessageRenderer) -> Author:
        author = message.get("authorName", {}).get("simpleText")
        author_id = message.get("authorExternalChannelId")
        avatar_url = message.get("authorPhoto", {}).get("thumbnails", [])[0].get("url")
        roles: List[Role] = []
        for badge in message.get("authorBadges", []):
            if "icon" in badge["liveChatAuthorBadgeRenderer"]:
                match badge["liveChatAuthorBadgeRenderer"]["icon"]["iconType"]:
                    case "MODERATOR":
                        roles.append(MODERATOR)
                    case "OWNER":
                        roles.append(OWNER)
                    case type:
                        raise RuntimeError(f"Unknown badge type: {type}")
            elif "customThumbnail" in badge["liveChatAuthorBadgeRenderer"]:
                roles.append(
                    Role(
                        id=badge["liveChatAuthorBadgeRenderer"]["customThumbnail"][
                            "thumbnails"
                        ][0]["url"],
                        name=badge["liveChatAuthorBadgeRenderer"]["tooltip"],
                        icon_url=badge["liveChatAuthorBadgeRenderer"][
                            "customThumbnail"
                        ]["thumbnails"][0]["url"],
                        is_owner=False,
                        is_moderator=False,
                    )
                )

        return Author(
            provider_id=INFO.key(),
            id=author_id,
            name=author,
            avatar_url=avatar_url,
            roles=roles,
        )

    def _parse_message(self, message: api.Message) -> Content:
        runs: api.Runs = message.get("runs", [])
        root = RootContent()
        for run in runs:
            if "text" in run:
                root.add(TextContent.of(run["text"]))
            elif "emoji" in run:
                emoji = run["emoji"]
                root.add(
                    ImageContent.of(
                        url=emoji["image"]["thumbnails"][0]["url"],
                        id=emoji["emojiId"],
                        name=emoji["shortcuts"][0] if emoji.get("shortcuts") else None,
                    )
                )
            else:
                raise RuntimeError(f"Unknown run: {run}")
        return root

    def _parse_paid(self, message: api.LiveChatPaidMessageRenderer) -> Paid:
        _currency = re.search(r"[^0-9]+", message["purchaseAmountText"]["simpleText"])
        if _currency is None:
            raise RuntimeError(
                f"Could not parse currency: {message['purchaseAmountText']['simpleText']}"
            )
        currency = _currency.group(0)
        _amount = re.search(r"[\d,\.]+", message["purchaseAmountText"]["simpleText"])
        if _amount is None:
            raise RuntimeError(
                f"Could not parse amount: {message['purchaseAmountText']['simpleText']}"
            )
        amount = float(_amount.group(0).replace(",", ""))

        return Paid(
            currency=currency,
            amount=amount,
        )

    def _parse_created_at(self, message: api.LiveChatMessageRenderer) -> datetime:
        return datetime.fromtimestamp(
            int(message["timestampUsec"]) / 1000000,
            tz=datetime.now().astimezone().tzinfo,
        )

    async def stop(self):
        self.tasks.terminate()
        self.room.online = False
        await self.client.rooms.update(self.room)
