# Instahack v2.3 – Smart Instagram Testing Tool

[![Release](https://img.shields.io/github/v/release/SSLRI/instahack?label=Latest%20Release)](https://github.com/SSLRI/instahack/releases)

---

## 🔍 About the Tool

Instahack is a professional Instagram OSINT and attack testing tool for **educational and ethical hacking**.  
Version `v2.3` introduces smart error detection, attack logging, graphical reports, and Termux-friendly compatibility.

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

# Run the lightweight OSINT version
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

git clone https://github.com/SSLRI/instahack.git
cd instahack

pip install -r requirements.txt

tor &  # Run Tor in background

python3 main.py
```

</details>

---

## 🧠 Key Features in v2.3

- Smart error detection (IP block, 2FA, Facebook login)
- Shows public/private account type
- Logs all failures to `error_log.txt`
- Generates attack result charts
- Includes lightweight Termux version
- Manual or automatic attack modes
- Smart Anti-Ban toggle

---

## 🔐 Tor Configuration Guide

<details>
<summary>🛡️ Click to learn how to configure Tor & hashed password</summary>

### 📌 For Linux/Desktop Users:

1. Install Tor:
```bash
sudo apt install tor
```

2. Generate a Tor control password hash:
```bash
tor --hash-password yourpassword
```

3. Edit `/etc/tor/torrc`:
```bash
sudo nano /etc/tor/torrc
```
Add:
```
ControlPort 9051
HashedControlPassword your_generated_hash
CookieAuthentication 1
```

4. Restart Tor:
```bash
sudo systemctl restart tor
```

5. Set the same password in the script:
```python
controller.authenticate(password='yourpassword')
```

---

### 📱 For Termux (Rooted Only):

1. Install Tor:
```bash
pkg install tor
```

2. Use a Tor manager like Orbot or manually:
- Use Termux's tor + port `9051`
- You may need to grant root access and modify `~/.tor/torrc`

ℹ️ Tor control port access may be limited on non-rooted phones.

</details>

---

## 🧪 Tool Menu

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

This tool is built for **educational** and **authorized testing** only.  
Do **not** use it on any accounts without permission. Misuse may result in legal action.

---

## 👤 Developer: SSLRI

[![Instagram](https://img.shields.io/badge/Instagram-sslri-red?logo=instagram&style=for-the-badge)](https://instagram.com/sslri)
[![Telegram](https://img.shields.io/badge/Telegram-sslri-blue?logo=telegram&style=for-the-badge)](https://t.me/sslri)
[![GitHub](https://img.shields.io/badge/GitHub-sslri-black?logo=github&style=for-the-badge)](https://github.com/sslri)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contact-25D366?logo=whatsapp&style=for-the-badge)](https://wa.me/989108007678)
