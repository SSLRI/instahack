# Instahack v2.2 - Advanced Instagram OSINT & Attack Tool

## 🔥 New Features in Enhanced Edition
- Check if user exists before attacking
- Detect if account is Public or Private
- Track password success/failure counts
- Generate graph report after attacks (matplotlib)
- Fake browser fingerprint with real User-Agent

## ❇️ Lite Version (Termux/Android)
- `main_light.py`
- No Rust required
- Works with `instaloader`

## 🚀 Full Version (Linux/WSL/PC)
- `main.py`
- All features (OSINT, brute-force, Tor, Smart Anti-Ban)
- Visual reporting

## Installation (for Full version)
```bash
apt update && apt upgrade -y
apt install python3 python3-pip git tor rustc unzip -y
pip install -r requirements.txt
```

## Run
```bash
tor &
python3 main.py
```

## Termux (Lite Mode)
```bash
pip install instaloader
python3 main_light.py
```

## Usage Menu
1. Gather OSINT
2. Auto Attack
3. Manual Attack
4. Toggle Smart Anti-Ban
5. Update Tool
6. Exit

## 🔒 Ethical Use Only
This tool is for educational purposes and ethical hacking tests ONLY.
