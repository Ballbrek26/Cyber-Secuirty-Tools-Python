# Cyber Security Tools in Python

A collection of Python-based cybersecurity tools developed by [Ballbrek26](https://github.com/Ballbrek26). This repository includes utilities for tasks such as network scanning, MAC address changing, password generation, and web crawling.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Tools Overview](#tools-overview)
  - [1. ARP Scanner](#1-arp-scanner)
  - [2. MAC Address Changer](#2-mac-address-changer)
  - [3. Password Generator](#3-password-generator)
  - [4. Web Crawler](#4-web-crawler)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This repository serves as a toolkit for cybersecurity enthusiasts and professionals. Each tool is designed to perform specific tasks commonly encountered in the field of cybersecurity. The tools are written in Python, leveraging libraries such as `scapy` and `BeautifulSoup` to facilitate network interactions and data parsing.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ballbrek26/Cyber-Secuirty-Tools-Python.git
   cd Cyber-Secuirty-Tools-Python
   ```

2. **Install Dependencies:**

   Ensure you have Python 3 installed. Install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not provided, install dependencies manually:

   ```bash
   pip install scapy beautifulsoup4 requests
   ```

## Tools Overview

### 1. ARP Scanner

**Description:**

Discovers active devices on a local network by sending ARP requests. Utilizes `scapy` to create and send packets, then summarizes the responses.

**Usage:**

```bash
python3 Net_Scanner/Net_scanner.py -I 192.168.1.0/24
```

**Example Output:**

```
IP: 192.168.1.10     MAC: 00:0c:29:3e:5b:1a
IP: 192.168.1.15     MAC: 00:0c:29:4d:2f:3b
```

**How It Works:**

- **Packet Preparation:**
  Constructs an ARP request and wraps it in an Ethernet frame (broadcasted to `ff:ff:ff:ff:ff:ff`).

- **Packet Sending:**
  Sends the packet using Scapy’s `srp` function, which waits for responses from active hosts.

- **Output Summary:**
  Lists responding devices with their IP and MAC addresses.

### 2. MAC Address Changer

**Description:**

Allows users to change the MAC address of a network interface. Useful for privacy and testing purposes.

**Usage:**

```bash
python3 Mac_Changer/Mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

**Options:**

- `-i`, `--interface`: The network interface to change (e.g., `eth0`).
- `-m`, `--mac`: The new MAC address to assign.

**How It Works:**

- **Interface Down:**
  Brings the network interface down.

- **MAC Address Change:**
  Executes the command to change the MAC address.

- **Interface Up:**
  Brings the network interface back up.

- **Verification:**
  Checks and displays the old and new MAC addresses.

### 3. Password Generator

**Description:**

Generates a random password containing letters, digits, and punctuation. The default length is 10 characters.

**Usage:**

```bash
python3 Generate-Password/generate-password.py
```

**Options:**

The script can be modified to accept a length parameter for custom password lengths.

**Example Output:**

```
Generated password: aB3$dEfGh!
```

**How It Works:**

- **Character Set:**
  Defines a set of characters including letters, digits, and punctuation.

- **Password Generation:**
  Randomly selects characters from the set to form a password of the specified length.

### 4. Web Crawler

**Description:**

Crawls a specified website, collecting all internal links and saving them to a CSV file. Useful for mapping out website structures.

**Usage:**

```bash
python3 Web_Crawler/crawler.py
```

**How It Works:**

- **Initialization:**
  Sets the base URL and initializes lists for URLs to process and already crawled URLs.

- **Request Handling:**
  Sends HTTP requests to URLs and parses the content using BeautifulSoup.

- **Link Extraction:**
  Extracts and normalizes internal links, adding new ones to the processing list.

- **CSV Writing:**
  Writes all crawled URLs to a CSV file named `crawled.csv`.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. Commit your changes with clear messages:

   ```bash
   git commit -m "Add feature: [describe your feature]"
   ```

4. Push your branch to your fork:

   ```bash
   git push origin feature/YourFeature
   ```

5. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions, issues, or suggestions, please open an issue on GitHub or contact `your-email@example.com`.

Happy hacking and stay secure!
