import subprocess
import re

def get_volume():
    """
    Retrieves the current system volume as a percentage using pactl.
    """
    cmd = "pactl get-sink-volume @DEFAULT_SINK@"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    match = re.search(r'(\d+)%', result.stdout)
    return match.group(1) if match else None

if __name__ == "__main__":
    volume = get_volume()
    print(volume if volume else "NOT FOUND")
