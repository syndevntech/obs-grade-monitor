import os
import requests
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID=os.getenv("TELEGRAM_CHAT_ID")
if not TOKEN or not CHAT_ID:
    raise ValueError("ACCESS TO CHAT ID OR BOT TOKEN COULD NOT BE ESTABILISHED")

def sendMessage(message):
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"  
    response=requests.post(
        url,
        data={"chat_id":CHAT_ID,
            "text":message
        },
            timeout=20
    )
    response.raise_for_status()
    result=response.json()
    if not result.get("ok"):
        raise RuntimeError("TELEGRAM MESSAGE COULD NOT BE SENT")
    return result


def sendPhoto(photo):
    url=f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(photo, "rb") as file:
        response=requests.post(
            url,
            files={"photo":file},
            data={"chat_id":CHAT_ID},
            timeout=20       
    )
        response.raise_for_status()
    result=response.json()
    if not result.get("ok"):
        raise RuntimeError("TELEGRAM MESSAGE COULD NOT BE SENT")
    return result

def getUpdates(offset=None):
    url=f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response=requests.get(
        url,
        timeout=20,
        params={
            "timeout":15,
            "offset":offset}
    )
    
    response.raise_for_status()
    result=response.json()
    return result
        
def waitForMessage(offset):
    while True:
        data = getUpdates(offset)
        updates = data["result"]

        print("NUMBER OF RECEIVED UPDATES:", len(updates))

        if updates:
            for update in updates:
                offset = update["update_id"] + 1

                message = update.get("message", {})

                if str(message.get("chat", {}).get("id")) != str(CHAT_ID):
                    print("CHAT ID MISMATCH. MESSAGE SKIPPED.")
                    continue

                text = message.get("text")

                if text:
                    print("MESSAGE RECEIVED SUCCESSFULLY!")
                    return text
if __name__ == "__main__":
    data = getUpdates()
    updates = data["result"]

    if updates:
        offset = updates[-1]["update_id"] + 1
    else:
        offset = None



    text = waitForMessage(offset)

  