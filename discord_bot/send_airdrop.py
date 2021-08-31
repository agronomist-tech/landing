import json
import subprocess


def send_token(address, count):
    try:
        out = subprocess.check_output(
            f"spl-token transfer --allow-unfunded-recipient --fund-recipient 4QV4wzDdy7S1EV6y2r9DkmaDsHeoKz6HUvFLVtAsu6dV {count} {address}",
            shell=True,
        ).decode()
        print(out)
    except:
        print("Some error, continue")


with open("airdrop_users.json", "r+") as users:
    addresses = json.load(users)


category = "chats"
print(f"-- Send coins to {category.upper()}")
for user in addresses[category]:
    print(f"Send 2000 token to user {user} and address {addresses[category][user]}\n\n")
    send_token(addresses[category][user], 2000)
    print("\n -------------- \n")
