import subprocess


def init():
    rc = subprocess.run("playwright install", shell=True).returncode
    if rc != 0:
        raise Exception("Failed to install playwright")
