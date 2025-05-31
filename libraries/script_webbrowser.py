import webbrowser
import sys
import time

if len(sys.argv) < 2:
    print("No URL provided")
    exit(1)

url = sys.argv[1]
if "autoplay=1" not in url:
    url += "&autoplay=1"

webbrowser.open(url)
time.sleep(5)
