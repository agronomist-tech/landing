import os
import re
import pathlib
from datetime import date, datetime

import discord
import aiosqlite


DB_PATH = pathlib.Path(__file__).parent.absolute() / "db.sqlite"

intents = discord.Intents.default()
intents.members = True


class AgronomistBot(discord.Client):
    invites = []
    last_invites_date = None
    guild = None

    async def on_ready(self):
        self.guild = self.get_guild(849043304158068767)
        self.invites = await self.guild.invites()
        self.last_invites_date = datetime.now()

    async def verify_twitter_message(self, msg):
        if "https://twitter.com" not in msg.content:
            return
        if not re.match(
            "https://twitter.com/([\w\d]+)/status/\d+(?:\?s\=\d+)?$", msg.content
        ):
            await msg.reply(f"URL incorrect", mention_author=True)
            return
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                f"SELECT * FROM twitter_messages WHERE url='{msg.content.strip()}'"
            )
            exist = await cursor.fetchone()
            if not exist:
                await db.execute(
                    f"""
                        INSERT INTO twitter_messages (user_id, url) VALUES (?, ?);
                    """,
                    (msg.author.id, msg.content.strip()),
                )
                await db.commit()
                await msg.reply(f"Thank you!", mention_author=True)

    async def get_invites_count(self, msg):
        if (
            self.last_invites_date
            and (datetime.now() - self.last_invites_date).total_seconds() > 180
        ):
            self.invites = await self.guild.invites()
            self.last_invites_date = datetime.now()

        invites = 0
        user_found = False
        for invite in self.invites:
            if invite.inviter.id == msg.author.id:
                user_found = True
                invites += invite.uses

        if user_found:
            await msg.reply(f"You have invited {invites} people")
        else:
            await msg.reply(f"You don't have any invite codes")

    async def on_connect(self):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS message_counter (
                    user_id TEXT PRIMARY KEY,
                    counter INTEGER DEFAULT 0
                );
                """
            )
            await db.execute(
                """
                 CREATE TABLE IF NOT EXISTS twitter_messages (
                    user_id TEXT PRIMARY KEY,
                    url TEXT
                );
                """
            )
            await db.commit()

    async def on_message(self, message):
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                f"SELECT * FROM message_counter WHERE user_id='{message.author.id}'"
            )
            user = await cursor.fetchone()

            if user:
                await db.execute(
                    f"UPDATE message_counter SET counter=counter + 1 WHERE user_id={message.author.id}"
                )
            else:
                await db.execute(
                    f"INSERT INTO message_counter (user_id, counter) VALUES ({message.author.id}, 1)"
                )
            await db.commit()

        if message.channel.name == "twitter":
            await self.verify_twitter_message(message)

        if message.content.startswith("!invites"):
            await self.get_invites_count(message)


bot = AgronomistBot(intents=intents)
bot.run(os.environ.get("AGRO_DISCORD_TOKEN"))
