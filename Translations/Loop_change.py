"""Keys and translations changed Prod/ Staging """
# !/usr/bin/python3.7.2
# coding=utf-8
import os
import sys
import time
from urllib.parse import urljoin
import pandas as pd
import psutil
import selenium
import webdriver_manager.chrome
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import platform
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from configs import Accounts
from configs import Sites

# Driver settings
DRIVER = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
wait = WebDriverWait(DRIVER, 20)

platform = platform.system()
if platform == "win32" or platform == "Windows":
    from configs.Windows import Paths

elif platform == "Linux" or platform == "Linux2":
    from configs.Linux import Paths

websites_list = [Sites.Prod, Sites.Staging]
logins_list = [Accounts.Prod_user_1, Accounts.Staging_user_2]
passwords_list = [Accounts.Prod_Password_1, Accounts.Staging_Password_2]
language_code = ["en", "de", "sk", "tr", "ru", "cs", "nl", "hu", "ro", "zh", "pt", "es"]

# Grab text from launcher
currentdir = os.getcwd()
data = pd.read_excel(f"{currentdir}/List.xlsx")
data.dropna(inplace=True)
data["key"] = data["key"].str.split(" ", n=1, expand=True)
data["Domain"] = data["Domain"].str.split(" ", n=1, expand=True)

Keys_List = data["key"].tolist()
Domains = data["Domain"].tolist()
Old_pl = data["old pl"].tolist()
Old_en = data["old en"].tolist()
New_pl = data["new pl"].tolist()
New_en = data["new en"].tolist()


def kill_driver():
    # End chromedriver and chrome ghost processes
    PROCNAME = "chromedriver.exe"

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            try:
                proc.kill()

            except psutil.NoSuchProcess:
                break


def create_new():
    for key, new_en in zip(Keys_List, New_en):
        try:
            fa_plus = DRIVER.find_element_by_css_selector(".fa-plus")
            fa_plus.click()
            create_key = DRIVER.find_element_by_id("create-key")
            create_message = DRIVER.find_element_by_id("create-message")
            create_key.click()
            create_key.clear()
            create_key.send_keys(str(key))
            create_message.click()
            create_message.clear()
            create_message.send_keys(str(new_en))
            create_message.send_keys(Keys.RETURN)
            break

        except selenium.common.exceptions.NoSuchElementException:
            continue


def translate():
    """Actual Test execution code- takes domain from input in ENTRY4 and takes credentials from
    other file, then executes script on both staging and prod site"""
    DRIVER.start_client()
    for site, login, password in zip(websites_list, logins_list, passwords_list):
        try:
            DRIVER.get(site)
            Password_field = DRIVER.find_element_by_id("password")
            username = DRIVER.find_element_by_id("username")
            username.click()
            username.clear()
            username.send_keys(login)
            Password_field.click()
            Password_field.clear()
            Password_field.send_keys(password)
            DRIVER.find_element_by_id("_submit").click()

            try:
                Cookies = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/i")))
                Cookies.click()

            except selenium.common.exceptions.TimeoutException:
                break

            """Change translations on other languages"""
            try:
                for lang, domain in zip(language_code, Domains):
                    DRIVER.get(urljoin(f'{site}/translations/app/{lang}/', domain))
                    url = DRIVER.current_url
                    website_domain = url.rsplit("/", 1)[1]

                    if website_domain == domain:
                        print(f"{website_domain} == {domain}")
                        for key, old_pl, old_en, new_pl, new_en in zip(Keys_List, Old_pl, Old_en, New_pl, New_en):
                            value = DRIVER.find_element_by_css_selector(f"textarea[data-key='{key}']").get_attribute(
                                'value')
                            field = DRIVER.find_element_by_css_selector(f"textarea[data-key='{key}']")
                            translation = value.lstrip().rstrip()

                            if translation == old_pl or translation == old_en:
                                field.clear()
                                field.send_keys(str(new_en))
                                DRIVER.find_element_by_id(str(key)).click()
                                print(f"change: PL changed to {new_en}")
                                time.sleep(1)
                                break

                            if translation == new_en or translation == new_pl:
                                print("change: item is already translated, continuing")
                                time.sleep(1)
                                break

                            else:
                                break

                    if website_domain != domain:
                        print(f"{website_domain} != {domain}")
                        DRIVER.get(urljoin(f'{site}/translations/app/{lang}/', domain))
                        for key, old_pl, old_en, new_pl, new_en in zip(Keys_List, Old_pl, Old_en, New_pl, New_en):
                            value = DRIVER.find_element_by_css_selector(f"textarea[data-key='{key}']").get_attribute(
                                'value')
                            field = DRIVER.find_element_by_css_selector(f"textarea[data-key='{key}']")
                            translation = value.lstrip().rstrip()

                            if translation == old_pl or translation == old_en:
                                field.clear()
                                field.send_keys(str(new_en))
                                DRIVER.find_element_by_id(str(key)).click()
                                print(f"change: PL changed to {new_en}")
                                time.sleep(1)
                                break

                            if translation == new_en or translation == new_pl:
                                print("change: item is already translated, continuing")
                                time.sleep(1)
                                break

                            else:
                                break

            except selenium.common.exceptions.NoSuchElementException:
                break

            """Change polish translation"""
            try:
                for domain in Domains:
                    url = DRIVER.current_url
                    website_domain = url.rsplit("/", 1)[1]

                    if website_domain == domain:
                        for key, old_pl, old_en, new_pl in zip(Keys_List, Old_pl, Old_en, New_pl):
                            value = DRIVER.find_element_by_css_selector(f"textarea[data-key='{key}']").get_attribute(
                                'value')
                            field = DRIVER.find_element_by_css_selector(f"textarea[data-key='{key}']")
                            translation = value.lstrip().rstrip()

                            if website_domain != domain:
                                DRIVER.get(urljoin(f'{site}/translations/app/{lang}/', domain))
                                value = DRIVER.find_element_by_css_selector(
                                    f"textarea[data-key='{key}']").get_attribute(
                                    'value')
                                field = DRIVER.find_element_by_css_selector(f"textarea[data-key='{key}']")
                                translation = value.lstrip().rstrip()

                                if translation == old_en or translation == old_pl:
                                    field.clear()
                                    field.send_keys(str(new_pl))
                                    DRIVER.find_element_by_id(str(key)).click()
                                    print(f"change_pl: PL changed to {new_pl}")
                                    time.sleep(1)
                                    break

                                if translation == old_en and translation == old_pl:
                                    field.clear()
                                    field.send_keys(str(new_pl))
                                    DRIVER.find_element_by_id(str(key)).click()
                                    print(f"change_pl: PL changed to {new_pl}")
                                    time.sleep(1)
                                    break
                            if translation == old_en or translation == old_pl:
                                field.clear()
                                field.send_keys(str(new_pl))
                                DRIVER.find_element_by_id(str(key)).click()
                                print(f"change_pl: PL changed to {new_pl}")
                                time.sleep(1)
                                break

                            if translation == old_en and translation == old_pl:
                                field.clear()
                                field.send_keys(str(new_pl))
                                DRIVER.find_element_by_id(str(key)).click()
                                print(f"change_pl: PL changed to {new_pl}")
                                time.sleep(1)
                                break

            except selenium.common.exceptions.NoSuchElementException:
                break

            """Change REF translation"""
            DRIVER.get(urljoin(f'{site}/translations/app/ref/', domain))

            for key in Keys_List:
                try:
                    fa_plus = DRIVER.find_element_by_css_selector(".fa-plus")
                    fa_plus.click()
                    create_key = DRIVER.find_element_by_id("create-key")
                    create_message = DRIVER.find_element_by_id("create-message")
                    create_key.click()
                    create_key.clear()
                    create_key.send_keys(str(key))
                    create_message.click()
                    create_message.clear()
                    create_message.send_keys(str(key))
                    create_message.send_keys(Keys.RETURN)
                finally:
                    break

            DRIVER.get(f'{site}/logout')
            break

        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(10)
            continue

        except selenium.common.exceptions.NoSuchElementException:
            DRIVER.get(f"{site}/logout")
            time.sleep(5)
            continue


translate()

if platform == "win32" or platform == "Windows":
    print("Script completed successfully")
    DRIVER.stop_client()
    DRIVER.quit()
    kill_driver()
    playsound(str(Paths.sound))

elif platform == "Linux" or platform == "Linux2":
    DRIVER.stop_client()
    DRIVER.quit()
    kill_driver()
    print("Script completed successfully")
