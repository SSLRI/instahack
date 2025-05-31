#!/bin/bash
echo "[*] Updating system..."
apt update && apt upgrade -y
echo "[*] Installing dependencies..."
apt install -y python3 python3-pip git tor rust unzip
pip install -r requirements.txt --break-system-packages
echo "[*] Done. Run with: python3 main.py"
