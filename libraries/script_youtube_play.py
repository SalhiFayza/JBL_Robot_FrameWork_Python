from playwright.sync_api import sync_playwright
import subprocess
import sys
import time

def set_volume(level):
    subprocess.call(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{level}%"])
    print(f"Volume set to {level}%")

url = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    try:
        page.click("button[aria-label='Play']", timeout=10000)
    except:
        print("No play button found or already playing")

    current_volume = 0
    set_volume(current_volume)
    time.sleep(3)

    while current_volume < 100:
        current_volume += 10
        set_volume(min(current_volume, 100))
        time.sleep(4)

    time.sleep(3)
    browser.close()
