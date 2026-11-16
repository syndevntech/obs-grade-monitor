
from playwright.sync_api import sync_playwright
from telegram import sendMessage, sendPhoto, getUpdates, waitForMessage
import time
import os
from dotenv import load_dotenv
load_dotenv()
OBS_USERNAME = os.getenv("OBS_USERNAME")
OBS_PASSWORD = os.getenv("OBS_PASSWORD")
data = getUpdates()
updates = data["result"]
offset = updates[-1]["update_id"] + 1 if updates else None

while True:
    message = waitForMessage(offset)

    data = getUpdates()
    updates = data["result"]
    offset = updates[-1]["update_id"] + 1 if updates else None

    if message.strip().upper() != "NOT":
        continue

    browser = None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://OBS")#YOU MUST ENTER OWN STUDENT INFORMATION SYSTEM ADDRESS
            page.get_by_placeholder("Öğrenci Numarası").fill(OBS_USERNAME)
            page.get_by_placeholder("Şifre").fill(OBS_PASSWORD)

            page.locator("#kappi2").screenshot(path="verification.png")
            sendPhoto("verification.png")
            sendMessage("WAITING FOR VERIFICATION CODE")

            data = getUpdates()
            updates = data["result"]
            offset = updates[-1]["update_id"] + 1 if updates else None

            code = waitForMessage(offset)
            sendMessage("RECEIVED VERIFICATION CODE")

            page.get_by_placeholder("Doğrulama Kodunu Girin").fill(code)
            page.locator("#btnLogin").click()
            page.get_by_role("link", name="Yarıyıl").click()
            page.locator('a[href="SinavSonuc.aspx"]').click()

            time.sleep(3)
            page.screenshot(path="sonuc.png", full_page=True)
            sendPhoto("sonuc.png")

            browser.close()
            browser = None

    except Exception as e:
        print(f"HATA: {e}")
        sendMessage("Not kontrolü sırasında bir hata oluştu.")

    finally:
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass
