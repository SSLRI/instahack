# Instahack v2.4 – Smart Instagram Testing Tool (Anti-Block Edition)

[![Release](https://img.shields.io/github/v/release/SSLRI/instahack?label=Latest%20Release)](https://github.com/SSLRI/instahack/releases)

---

## 🔍 About the Tool

Instahack is an advanced Instagram OSINT and attack testing tool for **educational and authorized purposes**.  
Version `v2.4` builds upon `v2.3` by introducing **anti-block features**, improved login flexibility, and better detection evasion.

---

## 🔧 Installation Guide (Termux – Android)

<details>
<summary>📱 Click to view Termux setup steps</summary>

```bash
pkg update && pkg upgrade -y
pkg install python git unzip -y
pip install instaloader

git clone https://github.com/SSLRI/instahack.git
cd instahack

# Run lightweight OSINT mode
python main_light.py
```

</details>

---

## 💻 Installation Guide (Linux / WSL / Ubuntu / Kali)

<details>
<summary>💻 Click to view Linux setup steps</summary>

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git tor rust unzip -y

git clone https://github.com/SSLRI/instahack.git
cd instahack

pip install -r requirements.txt

tor &  # run Tor in background

python3 main.py
```

</details>

---

## 🧠 Features in v2.4

✅ All previous features from v2.3:  
- Smart error detection (IP ban, Facebook login, 2FA)
- Public/private account check
- Error logging (`error_log.txt`)
- Attack results graph
- Smart Anti-Ban delay system
- Termux OSINT mode

✨ **New in v2.4 – Anti-Block Engine:**
- 🔁 Rotate Tor IP from menu
- 🌍 Use custom proxy (HTTP/SOCKS)
- 🧭 Set custom browser User-Agent
- 🧩 Use Instagram SessionID for login (no password)
- ⏱️ Smart random delay between attempts

---

## 🔐 Tor Configuration Guide

<details>
<summary>🛡️ Click for full Tor setup (hashing, control port)</summary>

### 🖥️ For Linux:

```bash
tor --hash-password yourpassword
sudo nano /etc/tor/torrc
```

Add:
```
ControlPort 9051
HashedControlPassword your_generated_hash
CookieAuthentication 1
```

Then:
```bash
sudo systemctl restart tor
```

### 📱 For Termux (rooted only):

```bash
pkg install tor
# May need manual torrc configuration and root access
```

</details>

---

## 🧪 Tool Menu (v2.4)

```
1. Gather OSINT
2. Auto Attack
3. Manual Attack
4. Toggle Smart Anti-Ban
5. Rotate Tor IP
6. Set Proxy
7. Set Custom User-Agent
8. Set SessionID
9. Exit
```

---

## ⚠️ Legal Notice

This tool is for educational, legal, and ethical hacking only.  
Unauthorized use is strictly prohibited and may be illegal.

---

## 👤 Developer & Contact

[![Instagram](https://img.shields.io/badge/Instagram-sslri-red?logo=instagram&style=for-the-badge)](https://instagram.com/sslri)
[![Telegram](https://img.shields.io/badge/Telegram-sslri-blue?logo=telegram&style=for-the-badge)](https://t.me/sslri)
[![GitHub](https://img.shields.io/badge/GitHub-sslri-black?logo=github&style=for-the-badge)](https://github.com/sslri)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-09108007678-25D366?logo=whatsapp&style=for-the-badge)](https://wa.me/989108007678)
