# Instahack v2.3 – Smart Instagram Testing Tool

[![Release](https://img.shields.io/github/v/release/SSLRI/instahack?label=Latest%20Release)](https://github.com/SSLRI/instahack/releases)

---

## 🔍 About the Tool

Instahack is an advanced Instagram OSINT and testing tool for **educational and authorized** security research.  
Version `v2.3` includes smart error detection, result graphs, a lightweight Termux version, and error logging.

---

## 🔧 Full Installation Guide (Termux – Android)

<details>
<summary>📱 Click to view Termux setup steps</summary>

```bash
pkg update && pkg upgrade -y
pkg install python git unzip -y
pip install instaloader

git clone https://github.com/SSLRI/instahack.git
cd instahack

# Run the lightweight OSINT version (no Tor or brute-force)
python main_light.py
```

</details>

---

## 💻 Full Installation Guide (Linux / WSL / Ubuntu / Kali)

<details>
<summary>💻 Click to view Linux setup steps</summary>

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git tor rust unzip -y

# Clone the project
git clone https://github.com/SSLRI/instahack.git
cd instahack

# Install Python dependencies
pip install -r requirements.txt

# Start Tor in the background
tor &

# Run the full tool
python3 main.py
```

</details>

---

## ⚙️ Key Features in v2.3

- 🔍 Smart error detection (e.g., IP bans, Facebook login, 2FA)
- 📊 Attack result charts (PNG format)
- 📄 Error log file saved to `error_log.txt`
- ✅ Account type detection (public/private)
- 🔐 Termux-compatible OSINT mode with login support
- 📁 Password list support and auto attack

---

## 🧪 Main Menu

```
1. Gather OSINT
2. Auto Attack
3. Manual Attack
4. Toggle Smart Anti-Ban
5. View Error Log
6. Update Tool
7. Exit
```

---

## ⚠️ Legal Notice

This tool is intended **only for educational use, ethical hacking, and authorized testing**.  
Any unauthorized or malicious usage is strictly prohibited and may violate the law.  
The developer is not responsible for misuse.

---

## 👨‍💻 Created by: [SSLRI](https://github.com/SSLRI)
