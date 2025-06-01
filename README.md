# Instahack v2.7 (Smart UA & SessionID Manager)

---

## 🚨 Disclaimer & Legal Warning

> This tool is strictly for authorized security testing, research, and educational purposes only.  
> **Any illegal or unauthorized use is strictly prohibited.**  
> The author takes no responsibility for any misuse or damages caused by this tool.

---

## 🚀 What's New in v2.7

- User-Agent & SessionID management menu (add/remove/list/select)
- Forced order: Set User-Agent before SessionID
- Attack only runs if valid User-Agent is set
- Full color terminal output & step-by-step error guidance
- All credentials saved in user_agents.json/sessionids.json

---

## ⚙️ Installation Guide (Linux/WSL/Ubuntu)

```bash
git clone https://github.com/SSLRI/instahack.git
cd instahack
bash setup.sh
source venv/bin/activate
python3 main.py
```

---

## 📲 Installation Guide (Termux/Android)

```bash
pkg install python git tor -y
git clone https://github.com/SSLRI/instahack.git
cd instahack
bash setup.sh
source venv/bin/activate
python3 main.py
```

---

## 🧩 Tor Setup & HashedControlPassword (for IP rotation)

**1. Install Tor:**  
Ubuntu:  
```bash
sudo apt install tor
```
Termux:  
```bash
pkg install tor
```

**2. Generate your Tor control password hash:**  
```bash
tor --hash-password YourStrongPassword
```
Copy the output line starting with `16:`.

**3. Edit your torrc file:**  
- On Ubuntu:  
  ```bash
  sudo nano /etc/tor/torrc
  ```
- On Termux:  
  ```bash
  nano $PREFIX/etc/tor/torrc
  ```

Add lines:
```
ControlPort 9051
HashedControlPassword 16:YOUR_HASH_HERE
CookieAuthentication 1
```

**4. Restart Tor service:**
- Ubuntu:  
  ```bash
  sudo service tor restart
  ```
- Termux:  
  ```bash
  tor &
  ```

- Use the same password in the tool when prompted for Tor authentication.

---

## ⚡ Quick Usage

- Always **set your User-Agent** from your browser (option 6 in menu)
- Then **set your SessionID** from the same browser/profile (option 7 in menu)
- You can manage multiple UAs and SIDs and switch between them easily!
- Use Tor rotation (option 5) to avoid bans

---

## ☎️ Contact & Social Networks

| [Instagram](https://instagram.com/sslri) | [Telegram](https://t.me/sslri) | [GitHub](https://github.com/sslri) | [WhatsApp](https://wa.me/989108007678) |
|---|---|---|---|

**Developer/Owner:** `sslri`

---

## ❗️ REMEMBER

- This project is for **educational, research, and legal pentesting only**.
- Abusing this tool = permanent ban from the author’s support and public channels.

---