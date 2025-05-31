#!/bin/bash
echo "[*] Updating system..."
apt update -y && apt upgrade -y
echo "[*] Installing Python3 and pip..."
apt install -y python3 python3-pip tor unzip
echo "[*] Installing Python dependencies..."
pip install --break-system-packages -r requirements.txt
echo "[*] Tor configuration (manual step required!)"
echo "Edit /etc/tor/torrc and set your HashedControlPassword as shown in README."
echo "[*] Setup complete. To run the tool:"
echo "python3 main.py"
