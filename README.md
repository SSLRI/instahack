# Instahack

**Advanced Instagram Brute Force & OSINT Framework**  
*Smart Anti-Ban, Tor Support, Default Password List, OSINT features.*

## Install
```bash
git clone https://github.com/sslri/instahack.git
cd instahack
bash setup.sh
```

## Usage
```bash
python main.py
```

<details>
<summary>⚠️ 📘 CLICK HERE to view Tor setup & HashedControlPassword instructions</summary>

1. Install Tor:
```bash
apt install tor
```
2. Generate password hash:
```bash
tor --hash-password mypassword
```
یا اگر این کار نکرد:
```bash
pip install stem
```
```python
from stem.control import Controller
print(Controller._hash_password("mypassword"))
```
3. ویرایش فایل torrc:
```bash
nano /data/data/com.termux/files/usr/etc/tor/torrc
```
و اضافه کن:
```
ControlPort 9051
HashedControlPassword خروجی بالا را جایگزین کن
CookieAuthentication 1
```
</details>

<details>
<summary>⚠️ 📱 CLICK HERE to view how to run this in Termux (Android)</summary>

```bash
pkg update && pkg upgrade -y
pkg install python git tor nano rust -y
git clone https://github.com/sslri/instahack.git
cd instahack
bash setup.sh
python main.py
```
</details>
