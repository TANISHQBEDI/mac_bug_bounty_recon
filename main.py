import os

import subprocess

def is_tool_installed(tool):
    """Check if a tool is installed."""
    try:
        subprocess.run([tool, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_tools():
    # Check if Homebrew is installed
    try:
        subprocess.run(["brew", "--version"], check=True)
    except subprocess.CalledProcessError:
        print("Homebrew is not installed. Please install it first.")
        return
    
    tools = [
        "subfinder",
        "assetfinder",
        "amass",
        "nmap",
        "httprobe",
        "waybackurls",
        "ffuf"
    ]
    
    for tool in tools:
        if not is_tool_installed(tool):
            print(f"{tool} not found. Installing...")
            try:
                subprocess.run(f"brew install {tool}", shell=True, check=True)
                print(f"{tool} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"Failed to install {tool}.")
        else:
            print(f"{tool} is already installed.")

install_tools()

def install_seclists():
    """Install SecLists if not already installed."""
    seclists_dir = os.path.expanduser("~/SecLists")
    if not os.path.exists(seclists_dir):
        print("SecLists not found. Cloning SecLists repository...")
        try:
            subprocess.run("git clone https://github.com/danielmiessler/SecLists.git ~/SecLists", shell=True, check=True)
            print("SecLists cloned successfully.")
        except subprocess.CalledProcessError:
            print("Failed to clone SecLists repository.")
    else:
        print("SecLists is already installed.")


install_seclists()



ip = input("Enter the IP address: ")

os.system(f"subfinder -d {ip} -rl 100 -o {ip}.subfinder.txt")

os.system(f"assetfinder {ip} > {ip}.assetfinder.txt")

os.system(f"amass enum -passive -d {ip} -o {ip}.amass.txt")

os.system(f"cat {ip}.subfinder.txt {ip}.assetfinder.txt | sort -u > {ip}.domains.txt")

os.system(f"nmap -sC -sV -oN {ip}.nmap.txt {ip}")

os.system(f"cat {ip}.domains.txt | httprobe > {ip}.alive.txt")

os.system(f"cat {ip}.alive.txt | waybackurls > {ip}.waybackurls.txt")

os.system(f"cat {ip}.alive.txt | while read url; do "
          f"status=$(curl -s -o /dev/null -w '%{{http_code}}' \"$url\"); "
          f"if [ \"$status\" = \"200\" ]; then "
          f"echo \"$url\" >> {ip}.200.txt; "
          f"else "
          f"echo \"$url ($status)\" >> {ip}.non200.txt; "
          f"fi; "
          f"done")


os.system(f"ffuf -u https://community.coloros.com/FUZZ -w SecLists/Discovery/Web-Content/common.txt -p 1 -t 10 -mc 200,201,202,203,204,205,206,403 -o {ip}.ffuf.txt")

