from webserver import keep_alive
import requests

channelID = 1067078440412520521
headers = {
    "authorization":
    MTA3NDUzNzI1Nzg2NTgzODY2NQ.Gzt0aG.F-RnHffHtxFVkvdvorgyFJJissaA7D6_pxrJvM
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
