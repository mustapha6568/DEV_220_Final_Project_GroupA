import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip3.12", "install", "-r", "requirements.txt"])
        