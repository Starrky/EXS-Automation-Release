import time
import sys
import psutil
import selenium
import webdriver_manager
from playsound import playsound
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import platform

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from configs import Accounts
from configs import Sites

platform = platform.system()

if platform == "win32" or "Windows":
    from configs.Windows import Paths
    
elif platform == "Linux" or "Linux2":
    from configs.Linux import Paths


copy_list = [Sites.Prod_Copy, Sites.Staging_Copy]

logout_list = [Sites.Staging_logout, Sites.Dev_logout, Sites.Prod_logout]

websites_list = [Sites.Prod, Sites.Staging]

logins_list = [Accounts.Prod_user_1, Accounts.Staging_user_2]

passwords_list = [Accounts.Prod_Password_1, Accounts.Staging_Password_2]

DRIVER = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())


def kill_driver():
    # End chromedriver and chrome ghost processes
    PROCNAME = "chromedriver.exe"
    PROCNAME2 = "chrome.exe"

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            try:
                proc.kill()

            except psutil.NoSuchProcess:
                break


def copy_all():
    """Clears domain input(kinda useless TIME_NOW)"""
    for site, login, password, copy, logout in zip(websites_list, logins_list, passwords_list,
                                                   copy_list, logout_list):
        while True:
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
                DRIVER.get(copy)
                break

            except selenium.common.exceptions.ElementClickInterceptedException:
                time.sleep(10)
                continue

            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(10)
                continue

    for logout in logout_list:
        DRIVER.get(logout)
        break


copy_all()

if platform == "win32" or "Windows":
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


