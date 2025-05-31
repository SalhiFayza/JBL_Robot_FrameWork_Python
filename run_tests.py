from robot import run
import os

if __name__ == "__main__":
    os.makedirs("Results", exist_ok=True)  # Ensure Results folder exists
    run("tests/hi.robot", outputdir="Results")
