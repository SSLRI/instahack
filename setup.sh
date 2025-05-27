#!/bin/bash
echo "[*] Updating system..."
apt update && apt upgrade -y

echo "[*] Installing Python3, pip, git, tor, and rust..."
apt install -y python git tor rust

echo "[*] Installing Python dependencies..."
pip install -r requirements.txt --no-cache-dir

echo "[*] Tor configuration (manual step required!)"
echo "Edit /etc/tor/torrc and set your HashedControlPassword as shown in README."

echo "[*] Setup complete. To run the tool:"
echo "python3 main.py"
