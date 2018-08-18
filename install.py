import subprocess
import os

def install():
    code = subprocess.call(["msiexec", "/a", "JaCartaUnifiedClient_2.11.0.1754_win-x64_ru-Ru.msi", "/quiet", "/log", "install_log.txt"])
    if code == 0:
        print("Success!")
    else:
        print("Error!")
        print(code)

def uninstall():
    code = subprocess.call(["msiexec", "/uninstall", "JaCartaUnifiedClient_2.11.0.1754_win-x64_ru-Ru.msi", "/q", "/log", "uninstal_log.txt"])
    if code == 0:
        print("Success!")
    else:
        print("Error!")

install()