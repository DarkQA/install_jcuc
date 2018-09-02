import subprocess
import os
import datetime
import test_modul


def main():
    install()
    test_modul.installed_dirs()


    # uninstall()

def install():
    time_now = str(datetime.datetime.now())
    print(time_now + "    Unified client installation running")
    code = subprocess.call(["msiexec", "/i", "JaCartaUnifiedClient_2.11.0.1754_win-x64_ru-Ru.msi", "/quiet", "/log", "install_log.txt"])
    if code == 0:
        time_now = str(datetime.datetime.now())
        print(time_now + "    Unified client was installed!")
    else:
        time_now = str(datetime.datetime.now())
        print(time_now + "    Error! You haven't permission\n" + "Code: " + str(code))
        

def uninstall():
    time_now = str(datetime.datetime.now())
    print(time_now + "    Unified client remove running")
    code = subprocess.call(["msiexec", "/uninstall", "JaCartaUnifiedClient_2.11.0.1754_win-x64_ru-Ru.msi", "/q", "/log", "uninstal_log.txt"])
    if code == 0:
        time_now = str(datetime.datetime.now())
        print(time_now + "    Unified client was removed!")
    else:
        time_now = str(datetime.datetime.now())
        print(time_now + "    Error!You haven't permission\n" + "Code: " + str(code))


if __name__ == "__main__":
    main()
    