import os
import platform

platform_os = platform.system()

print(platform)


if platform_os == "win32" or platform_os == "Windows":
    print(f"Tis Windows")

elif platform_os == "Linux" or platform_os == "Linux2":
    print(f"Tis linux")

else:
    print("OS not supported")
