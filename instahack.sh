import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_user_credentials():
    """
    دریافت نام کاربری و رمز عبور از کاربر.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def login_to_instagram(username, password):
    """
    لاگین به اینستاگرام با استفاده از نام کاربری و رمز عبور.
    """
    try:
        browser = webdriver.Chrome()
        browser.get("https://www.instagram.com/")
        time.sleep(3)

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(5)

        return browser  # Return the browser object for later use

    except Exception as e:
        print(f"Error during login: {e}")
        return None

def main():
    username, password = get_user_credentials()
    browser = login_to_instagram(username, password)
    if browser is None:
        print("Login failed. Please check your credentials.")
        return  # Exit the program if login fails

    try:
        browser.get(f"https://www.instagram.com/{username}/followers/")
        time.sleep(3)

        scroll_box = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        
        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '' and name.text != 'Follow']
        browser.close()
        print(names)

        with open('followers.txt', 'w', encoding='UTF-8') as file:
            for name in names:
                file.write(name + '\n')
        print('names saved in followers.txt')

    except Exception as e:
        print(f"Error: {e}")
        if browser:
            browser.quit()


if __name__ == "__main__":
    main()
