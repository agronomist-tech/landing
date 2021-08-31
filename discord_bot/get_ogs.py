import os
import re
import json
import asyncio
import logging
import discord


intents = discord.Intents.default()
intents.members = True


class Bot(discord.Client):
    async def on_ready(self):
        guild = self.get_guild(849043304158068767)
        # invites = await guild.invites()
        # for invite in invites:
        # if invite.uses > 0:
        # print(invite.inviter, invite.uses)

        airdrop_data = {}

        twitter_channel = self.get_channel(868603992429711410)
        airdrop_channel = self.get_channel(862078238934302751)
        # wallet_channe = self.get_channel()
        # og_role = guild.get_role(849048490918674462)
        # miniog_role = guild.get_role(869642880707358770)
        # async for role in guild.fetch_members():
        # print(role.name, role.id)

        # async for msg in twitter_channel.history(limit=None):
        #     print(f"Check message '{msg.content}'")
        #     if msg.created_at.day < 16:
        #         print(f"Messages end {msg.created_at}")
        #         break

        #     if "AgroBot" in msg.author.name:
        #         continue
        #     if "twitter" not in msg.content:
        #         continue
        #     check = re.match(
        #         "https://twitter.com/([\w\d]+)/status/\d+(?:.+)?$",
        #         msg.content.strip(),
        #     )
        #     if not check:
        #         print(f"Tweet '{msg.content.strip()}' not matched regex")
        #         continue
        #     else:
        #         if check.groups()[0].lower() == "agronomisttech":
        #             print("Twee for agronomist, pass it")
        #             continue

        #     user = guild.get_member(msg.author.id)

        #     if not user:
        #         print(f"--- skip user not exist :( {msg.author}")
        #         continue

        #     user_id = user.id
        # roles = [r.name for r in user.roles]
        #     airdrop_data[user_id] = {
        #         "roles": roles,
        #         "name": user.name,
        #         "twitter": msg.content.strip(),
        #     }

        #     print(f"-- User {user.name} has twitter and roles {roles}")
        wallets = []
        wallet_count = 0
        print(f"Start check airdrop channel")
        csv_file = open("./airdrop.csv", "w+")
        csv_file.write("User,Roles,Wallet\n")
        messages = await airdrop_channel.history(
            oldest_first=True, limit=None
        ).flatten()

        for msg in messages:
            print(
                f"Check message '{msg.author.name}' '{msg.content}' date: {msg.created_at}"
            )

            user = guild.get_member(msg.author.id)

            if not user:
                print(f"--- skip user not exist :( {msg.author}")
                continue

            if msg.content.strip() in wallets:
                wallet_count += 1
                continue

            wallets.append(msg.content.strip())

            roles = " ".join([r.name for r in user.roles])
            # user_id = user.id
            # if user_id in airdrop_data:
            #     airdrop_data[user_id]["wallet"] = msg.content.strip()
            # else:
            #     airdrop_data[user_id] = {"wallet": msg.content.strip()}

            print(f"-- User {user.name} has solana wallet")

            csv_file.write(f"{user.name},{roles},{msg.content.strip()}\n")
        csv_file.close()
        print(f"Wallets {len(wallets)}, duplicate: {wallet_count}")
        # with open("./result.json", "w+") as f:
        # json.dump(airdrop_data, f)

        #     role_exist = False
        #     for r in user.roles:
        #         if r.name in ["OG", "MiniOG"]:
        #             role_exist = True
        #             break

        #     if role_exist:
        #         print("--- skip role exist")
        #         continue

        #     if msg.created_at.day < 27:
        #         await user.add_roles(og_role)
        #     elif msg.created_at.day >= 27:
        #         await user.add_roles(miniog_role)

        #     print(">> ", msg.author, msg.content, msg.created_at)
        #     await asyncio.sleep(1)


b = Bot(intents=intents)
b.run(os.environ.get("AGRO_DISCORD_TOKEN"))
