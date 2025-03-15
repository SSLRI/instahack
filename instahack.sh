import time
import logging
from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired, LoginRequired

# Configure logging
logging.basicConfig(filename='instahack.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_credentials():
    """
    دریافت نام کاربری و رمز عبور از کاربر.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def login_to_instagram(username, password):
    """
    لاگین به اینستاگرام با استفاده از کتابخانه instagrapi.
    """
    try:
        client = Client()
        client.login(username, password)
        return client  # Return the client object

    except ClientLoginRequired as e:
        logging.error(f"Login required. Please check your credentials or use 2FA. {e}")
        return None
    except LoginRequired as e:
        logging.error(f"Login required. Please check your credentials. {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred during login: {e}")
        return None

def main():
    username, password = get_user_credentials()
    client = login_to_instagram(username, password)
    if client is None:
        print("Login failed. Please check your credentials.")
        return  # Exit the program if login fails

    try:
        user_id = client.user_id_from_username(username)
        followers = client.user_followers(user_id)
        names = [user.username for user in followers.values()]  # Extract usernames

        print(names)

        with open('followers.txt', 'w', encoding='UTF-8') as file:
            for name in names:
                file.write(name + '\n')
        print('names saved in followers.txt')

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        # No need to close the browser, as we're not using Selenium anymore
        pass

if __name__ == "__main__":
    main()
