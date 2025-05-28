#!/usr/bin/env python3
import os

def banner():
    print("="*60)
    print("📱 Instahack Lite - Termux/Android OSINT")
    print("="*60)

def menu():
    print("1. Get user info (login required if rate limited)")
    print("2. Download profile picture only")
    print("3. Exit")
    return input("Choose option: ").strip()

def get_user_info():
    username = input("Target username: ")
    login_user = input("Your Instagram username for login (leave blank to skip): ").strip()
    if login_user:
        os.system(f"instaloader --login {login_user} {username}")
    else:
        print("[!] Warning: Without login, you might get rate-limited.")
        os.system(f"instaloader --no-pictures --no-videos --no-profile-pic {username}")

def download_profile_pic():
    username = input("Target username: ")
    os.system(f"instaloader --no-metadata --no-captions --no-posts --no-videos {username}")

def main():
    banner()
    while True:
        choice = menu()
        if choice == "1":
            get_user_info()
        elif choice == "2":
            download_profile_pic()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
