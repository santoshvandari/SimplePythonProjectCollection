import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def create_whatsapp_group(csv_file_path, country_code="977"):
    """Create a WhatsApp group using phone numbers from a CSV file."""
    country_code = country_code.replace("+", "")
    df = pd.read_csv(csv_file_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get('https://web.whatsapp.com/')
        print("Please scan the QR code to log in to WhatsApp Web.")
        input("Press Enter after you've logged in...")

        time.sleep(5)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//button[@aria-label="New chat"]'))
        )
        print("Successfully logged in to WhatsApp Web")

        # Click on the menu button (three dots)
        menu_button = None
        for selector in [
            (By.XPATH, '//button[@aria-label="New chat"]'),
            (By.CSS_SELECTOR, 'span[data-testid="menu"]'),
            (By.XPATH, '//div[@role="button" and contains(@aria-label, "Menu")]')
        ]:
            try:
                menu_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(selector)
                )
                menu_button.click()
                print("Clicked on menu button")
                break
            except Exception:
                continue
        if not menu_button:
            driver.save_screenshot('debug_screenshot.png')
            raise Exception("Failed to find menu button with all methods")

        time.sleep(2)

        # Click on "New group" option
        new_group_option = None
        for selector in [
            (By.XPATH, '//div[contains(text(), "New group")]'),
            (By.XPATH, '//*[@data-testid="new-group"]'),
            (By.XPATH, '//li//div[contains(text(), "New group")]')
        ]:
            try:
                new_group_option = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(selector)
                )
                new_group_option.click()
                print("Clicked on New group option")
                break
            except Exception:
                continue
        if not new_group_option:
            raise Exception("Failed to find New group option")

        time.sleep(3)

        # Add each contact to the group
        # Add each contact to the group
        for _, row in df.iterrows():
            phone_number = str(row['number']).strip()
            if phone_number.startswith('+'):
                phone_number = phone_number[1:]
            if not phone_number.startswith(country_code):
                phone_number = f"{country_code}{phone_number}"
            name = row['name']
            print(f"Adding {name} ({phone_number}) to group...")

            try:
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//input[contains(@class, "copyable-text")]'))
                )
                search_box.clear()
                search_box.click()
                for char in phone_number:
                    search_box.send_keys(char)
                    time.sleep(0.1)
                print(f"Searching for {phone_number}")
                time.sleep(2)
                contact = None

                selector = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/span/div/div/div[2]/div[2]/div[2]')

                print(f"Trying selector: {selector}")

                try:
                    contact = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(selector)
                    )
                    print(f"Found contact: {contact.text}")
                    contact.click()
                    print(f"Added {name} to the group")
                except Exception as e:
                    print(f"Could not find contact {name} ({phone_number}): {str(e)}")
                    continue
            except Exception as e:
                print(f"Could not add {name} ({phone_number}): {str(e)}")

            time.sleep(2)

            # Click Next button
        next_button = None
        for selector in [
                (By.XPATH, '//div[contains(@aria-label, "Next")]'),
                (By.XPATH, '//div[@role="button" and @aria-label="Next"]')
            ]:
                try:
                    next_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable(selector)
                    )
                    next_button.click()
                    print("Clicked Next button")
                    break
                except Exception:
                    continue
        if not next_button:
                next_buttons = driver.find_elements(By.XPATH, '//span[contains(text(), "Next")]')
                if next_buttons:
                    driver.execute_script("arguments[0].click();", next_buttons[0])
                    print("Clicked Next button using JavaScript")

        time.sleep(3)

        # Set group name
        school_name = df['school'].iloc[0]
        group_name = f"{school_name} Students Group"
        try:
            group_name_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]'))
            )
            group_name_input.clear()
            group_name_input.send_keys(group_name)
            print(f"Set group name: {group_name}")
        except Exception as e:
            print(f"Setting group name failed: {str(e)}")

        time.sleep(2)

        # Create the group
        create_button = None
        for selector in [
            (By.XPATH, '//div[@role="button" and @aria-label="Create group"]'),
            (By.XPATH, '//*[@data-testid="checkmark-medium"]')
        ]:
            try:
                create_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(selector)
                )
                create_button.click()
                print("Clicked Create button")
                break
            except Exception:
                continue
        if not create_button:
            create_buttons = driver.find_elements(By.XPATH, '//span[contains(text(), "Create")]')
            if create_buttons:
                driver.execute_script("arguments[0].click();", create_buttons[0])
                print("Clicked Create button using JavaScript")

        print(f"Successfully created WhatsApp group: {group_name}")
        time.sleep(5)

        # Click on Invite button also 
            # //*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]
        invite_button = None
        for selector in [
            (By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]'),
            (By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[1]')
        ]:
            try:
                invite_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(selector)
                )
                invite_button.click()
                print("Clicked Invite button")
                break
            except Exception as e:
                print(f"Could not find Invite button: {str(e)}")
                continue
        if not invite_button:
            raise Exception("Failed to find Invite button")
        time.sleep(2)

        # Click on Done button
        done_button = None
    # //*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div/span
        for selector in [
            (By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div/span'),
            (By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[1]')
        ]:
            try:
                done_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(selector)
                )
                done_button.click()
                print("Clicked Done button")
                break
            except Exception as e:
                print(f"Could not find Done button: {str(e)}")
                continue
        if not done_button:
            raise Exception("Failed to find Done button")

        print("Group creation process completed.")
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        keep_open = input("Keep browser open? (y/n): ").lower() == 'y'
        if not keep_open:
            driver.quit()

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, 'data.csv')
    country_code = input("Enter country code (without +, default 91): ") or "91"
    create_whatsapp_group(csv_file_path, country_code)