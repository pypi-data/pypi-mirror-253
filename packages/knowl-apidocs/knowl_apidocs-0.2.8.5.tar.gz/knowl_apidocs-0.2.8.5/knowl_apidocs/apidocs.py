import os
import sys
import platform
import subprocess
from .version import VERSION

def remove_quotes(s):
    return s.replace("\"", "").replace("\'", "").replace("\`", "")

def detect_os():
    current_os = platform.system()
    if current_os == "Linux":
        return "linux"
    elif current_os == "Darwin":
        return "mac"
    else:
        raise RuntimeError(f"This script is not supported on {current_os}. Please run it on Linux, or macOS.")

def get_url(os, version):
    url = f"https://s3.ap-south-1.amazonaws.com/releases.knowl.io/api-docs/apidocs_{os}_v{version}"
    binary_name = f"apidocs_{os}_v{version}"
    return url, binary_name

def run_subprocess(command, name="Operation"):
    try:
        binary_process = subprocess.Popen(command, universal_newlines=True,)
        binary_process.wait()
        if binary_process.returncode == 0:
            print(f"{name} completed successfully.")
        else:
            print(
                f"{name} failed with return code {binary_process.returncode}."
            )
            return 1
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error while running the script: {e}")
        return 1


def main():
    if len(sys.argv) < 2:
        raise RuntimeError("Path to Repo not provided")
    repo = sys.argv[1]
    package_path = os.path.dirname(os.path.abspath(__file__))
    current_os = detect_os()
    version = VERSION
    url, binary_name = get_url(current_os, version)
    binary_path = os.path.join(package_path, binary_name)
    if os.path.exists(binary_path):
        print("Binary file already exist.")
    else:
        command = ["wget", url, "-P", package_path]
        run_subprocess(command, "Downloading binary")
    command = ["chmod", "+x", binary_path]
    run_subprocess(command, "Granting Executable Permission")
    command = [binary_path, repo]
    run_subprocess(command, "Document Generation")

if __name__ ==  "__main__":
    main()