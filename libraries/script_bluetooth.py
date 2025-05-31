import sys
import subprocess


if len(sys.argv) < 2:
    print("Missing MAC address")
    sys.exit(1)

mac = sys.argv[1]

try:
    result = subprocess.run(["bluetoothctl", "info", mac], capture_output=True, text=True)
    output = result.stdout

    if "Connected: yes" in output:
        print("CONNECTED")
    else:
        print("DISCONNECTED")
except Exception as e:
    print(f"Error: {e}")
