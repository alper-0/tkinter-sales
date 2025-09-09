import subprocess
import sys
import os

def main():
    # Get absolute path for tela_splash.py
    splash_path = os.path.join(os.path.dirname(__file__), "tela_splash.py")

    # If tela_splash.py exists, run it; else run principal.py directly
    if os.path.exists(splash_path):
        subprocess.run([sys.executable, splash_path])
    else:
        principal_path = os.path.join(os.path.dirname(__file__), "principal.py")
        subprocess.run([sys.executable, principal_path])

if __name__ == "__main__":
    main()
