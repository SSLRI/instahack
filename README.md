# Instahack v2.3 – Smart Instagram Testing Tool

[![Release](https://img.shields.io/github/v/release/SSLRI/instahack?label=Latest%20Release)](https://github.com/SSLRI/instahack/releases)

---

## 📌 توضیح ابزار:
Instahack یک ابزار پیشرفته برای جمع‌آوری اطلاعات (OSINT) و تست نفوذ به حساب‌های اینستاگرام است (صرفاً آموزشی).  
نسخه v2.3 شامل تشخیص هوشمند ارور، نمودار نتایج، حالت سبک برای موبایل، و لاگ‌گیری می‌باشد.

---

## 🔧 مراحل نصب کامل (Termux - موبایل)

<details>
<summary>📱 کلیک کنید برای دیدن مراحل نصب در Termux</summary>

```bash
pkg update && pkg upgrade -y
pkg install python git unzip -y
pip install instaloader

git clone https://github.com/SSLRI/instahack.git
cd instahack

# اجرای نسخه سبک (OSINT - بدون نیاز به Rust)
python main_light.py
```

</details>

---

## 💻 مراحل نصب کامل (Linux / WSL)

<details>
<summary>💻 کلیک کنید برای دیدن مراحل نصب در لینوکس/دسکتاپ</summary>

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git tor rust unzip -y

# کلون کردن پروژه
git clone https://github.com/SSLRI/instahack.git
cd instahack

# نصب پیش‌نیازها
pip install -r requirements.txt

# اجرای تور در بک‌گراند
tor &

# اجرای ابزار اصلی
python3 main.py
```

</details>

---

## 🧠 امکانات نسخه v2.3

- تشخیص ارور هوشمند: بلاک شدن آی‌پی، 2FA، Facebook Login
- نمایش پیام دقیق برای هر ارور
- لاگ‌گیری کامل در `error_log.txt`
- ساخت نمودار تصویری پس از تست رمز (attack_result.png)
- نسخه سبک Termux با قابلیت login برای OSINT

---

## 🧪 منو ابزار

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

## ⚠️ توجه مهم
- این ابزار فقط برای تست قانونی، تحقیقات امنیتی و آموزش استفاده شود.
- استفاده غیرمجاز از آن بر خلاف قوانین اینستاگرام و قوانین کشور شماست.
