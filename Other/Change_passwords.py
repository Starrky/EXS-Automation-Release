from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from configs import Accounts
from configs import Sites
import platform

platform = platform.system()

if platform == "Linux" or platform == "Linux2":
    from configs.Linux import Paths

elif platform == "win32" or "Windows":
    from configs.Windows import Paths


DRIVER = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(DRIVER, 20)

sites_list = [f"{Sites.Prod_users}/6086/edit", f"{Sites.Prod_users}/6077/edit",
              f"{Sites.Prod_users}/4056/edit", f"{Sites.Prod_users}/6086/edit",
              f"{Sites.Prod_users}/6077/edit", f"{Sites.Prod_users}/4056/edit"]

sites_list_staging = [f"{Sites.Staging_users}/6086/edit", f"{Sites.Staging_users}/6077/edit",
                      f"{Sites.Staging_users}/4056/edit", f"{Sites.Staging_users}/6086/edit",
                      f"{Sites.Staging_users}/6077/edit", f"{Sites.Staging_users}/4056/edit",
                      f"{Sites.Staging_users}/9695/edit", f"{Sites.Staging_users}/9696/edit",
                      f"{Sites.Staging_users}/9697/edit", f"{Sites.Staging_users}/9698/edit",
                      f"{Sites.Staging_users}/9699/edit", f"{Sites.Staging_users}/9700/edit",
                      f"{Sites.Staging_users}/9701/edit", f"{Sites.Staging_users}/9702/edit"]

sites_list_dev = [f"{Sites.Dev_users}/471/edit", f"{Sites.Dev_users}/472/edit",
                  f"{Sites.Dev_users}/474/edit", f"{Sites.Dev_users}/473/edit",
                  f"{Sites.Dev_users}/475/edit", f"{Sites.Dev_users}/476/edit",
                  f"{Sites.Dev_users}/477/edit", f"{Sites.Dev_users}/478/edit"]

"""PROD"""


def prod():
    # Login
    DRIVER.get(Sites.Prod_logout)
    DRIVER.get(Sites.Prod)
    DRIVER.find_element_by_id("username").click()
    DRIVER.find_element_by_id("username").clear()
    DRIVER.find_element_by_id("username").send_keys(Accounts.Prod_admin_login)
    DRIVER.find_element_by_id("password").click()
    DRIVER.find_element_by_id("password").clear()
    DRIVER.find_element_by_id("password").send_keys(Accounts.Prod_admin_pass)
    DRIVER.find_element_by_id("_submit").click()
    # selenium.common.exceptions.TimeoutException

    Cookies = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     "/html/body/div[2]/div[1]/div[1]/div/i")))
    Cookies.click()

    DRIVER.get(Sites.Prod_lang_en)

    for site in sites_list:
        DRIVER.get(site)
        DRIVER.find_element_by_id("user_plainPassword_first").click()
        DRIVER.find_element_by_id("user_plainPassword_first").send_keys(Accounts.Prod_Password_1)
        DRIVER.find_element_by_id("user_plainPassword_second").click()
        DRIVER.find_element_by_id("user_plainPassword_second").send_keys(Accounts.Prod_Password_1)
        DRIVER.find_element_by_xpath(
            '//*[@id="page-wrapper"]/div[3]/div/div[1]/div/div/div[2]/form/div[15]/div/button').click()


"""STAGING"""


def staging():
    # Login
    DRIVER.get(Sites.Staging_logout)
    DRIVER.get(Sites.Staging)
    DRIVER.find_element_by_id("username").click()
    DRIVER.find_element_by_id("username").clear()
    DRIVER.find_element_by_id("username").send_keys(Accounts.Staging_admin_login)
    DRIVER.find_element_by_id("password").click()
    DRIVER.find_element_by_id("password").clear()
    DRIVER.find_element_by_id("password").send_keys(Accounts.Staging_admin_pass)
    DRIVER.find_element_by_id("_submit").click()

    Cookies = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     "/html/body/div[2]/div[1]/div[1]/div/i")))
    Cookies.click()
    DRIVER.get(Sites.Staging_lang_en)

    for site in sites_list_staging:
        DRIVER.get(site)
        DRIVER.find_element_by_id("user_plainPassword_first").click()
        DRIVER.find_element_by_id("user_plainPassword_first").send_keys(Accounts.Prod_Password_1)
        DRIVER.find_element_by_id("user_plainPassword_second").click()
        DRIVER.find_element_by_id("user_plainPassword_second").send_keys(Accounts.Prod_Password_1)
        DRIVER.find_element_by_xpath(
            '//*[@id="page-wrapper"]/div[3]/div/div[1]/div/div/div[2]/form/div[15]/div/button').click()


"""DEV"""


def dev():
    # Login
    DRIVER.get(Sites.Dev_logout)
    DRIVER.get(Sites.Dev)
    DRIVER.find_element_by_id("username").click()
    DRIVER.find_element_by_id("username").clear()
    DRIVER.find_element_by_id("username").send_keys(Accounts.Dev_admin_login)
    DRIVER.find_element_by_id("password").click()
    DRIVER.find_element_by_id("password").clear()
    DRIVER.find_element_by_id("password").send_keys(Accounts.Dev_admin_pass)
    DRIVER.find_element_by_id("_submit").click()

    Cookies = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     "/html/body/div[2]/div[1]/div[1]/div/i")))
    Cookies.click()
    DRIVER.get(Sites.Dev_lang_en)

    for site in sites_list_dev:
        DRIVER.get(site)
        DRIVER.find_element_by_id("user_plainPassword_first").click()
        DRIVER.find_element_by_id("user_plainPassword_first").send_keys(Accounts.Prod_Password_1)
        DRIVER.find_element_by_id("user_plainPassword_second").click()
        DRIVER.find_element_by_id("user_plainPassword_second").send_keys(Accounts.Prod_Password_1)
        DRIVER.find_element_by_xpath(
            '//*[@id="page-wrapper"]/div[3]/div/div[1]/div/div/div[2]/form/div[15]/div/button').click()


prod()
staging()
dev()


if platform == "Linux" or platform == "Linux2":
    print("Script completed successfully")
    DRIVER.stop_client()

elif platform == "win32":
    print("Script completed successfully")
    playsound(str(Paths.sound))
    DRIVER.stop_client()

