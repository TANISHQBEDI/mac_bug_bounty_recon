# Automated Reconnaissance and Testing Script

This repository contains a Python script for automated reconnaissance and testing of a given target IP address or domain. The script performs several tasks, including subdomain enumeration, asset discovery, vulnerability probing, and fuzzing.

## Features

- **Subdomain enumeration** using tools like `subfinder`, `assetfinder`, and `amass`.
- **Port scanning and version detection** using `nmap`.
- **URL probing** to find live websites with `httprobe` and `waybackurls`.
- **HTTP status code categorization** for found URLs, and saves URLs that return status `200` in a separate file.
- **Fuzzing** to discover hidden resources on the target domain with `ffuf` using SecLists wordlist.
- **SecLists installation** if not already installed.

## Requirements

Before running the script, ensure the following tools are installed:

- **Homebrew** (for installing tools)
- **subfinder**
- **assetfinder**
- **amass**
- **nmap**
- **httprobe**
- **waybackurls**
- **ffuf**
- **SecLists** (automatically cloned if not already present)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/TANISHQBEDI/mac_bug_bounty_recon.git
   cd mac_bug_bounty_recon
   ```
2. Ensure that Homebrew is installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install the required tools by running the script:
   ```bash
   python3 main.py
   ```
4. After the script runs just enter the domain you want to search for.

The script will check if the necessary tools are installed, and if not, it will install them using Homebrew.

## Usage

1. Run the script and input the target IP address or domain:
   ```bash
   python3 main.py
   ```

The script will perform the following tasks:
- Subdomain discovery
- Asset discovery
- Passive domain enumeration
- Nmap scanning
- URL probing
- Wayback URL extraction
- HTTP status code categorization
- Fuzzing for hidden resources

The results will be saved in separate `.txt` files for each stage.

### Example output files:

- `target.subfinder.txt`
- `target.assetfinder.txt`
- `target.amass.txt`
- `target.domains.txt`
- `target.nmap.txt`
- `target.alive.txt`
- `target.waybackurls.txt`
- `target.200.txt` (URLs with status 200)
- `target.non200.txt` (URLs with non-200 status codes)
- `target.ffuf.txt` (Results from fuzzing with ffuf)
