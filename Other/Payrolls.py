import os
import re
import shutil
import time
import psutil
import selenium
import playsound
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from configs import Accounts, Sites
import platform

platform = platform.system()

if platform == "Linux" or platform == "Linux2":
    from configs.Linux import Paths
    from configs.Linux import Payrolls

    desktop = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
    paths_list = Payrolls.paths_list
    Payrolls = Payrolls
    password_dirs = Payrolls.password_dirs
    downloads_loc = os.path.join(os.path.join(os.environ['HOME']), 'Downloads')

elif platform == "win32":
    from configs.Windows import Paths
    from configs.Windows import Payrolls

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    paths_list = Payrolls.paths_list
    Payrolls = Payrolls
    password_dirs = Payrolls.password_dirs
    downloads_loc = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')


def kill_driver():
    # End chromedriver and chrome ghost processes
    PROCNAME = "chromedriver.exe"
    PROCNAME2 = "chrome.exe"

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()

        if proc.name() == PROCNAME2:
            proc.kill()


DRIVER = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(DRIVER, 20)

# Login
DRIVER.get(Sites.Prod)
DRIVER.find_element_by_id("username").click()
DRIVER.find_element_by_id("username").clear()
DRIVER.find_element_by_id("username").send_keys(Accounts.Prod_admin_login)
DRIVER.find_element_by_id("password").click()
DRIVER.find_element_by_id("password").clear()
DRIVER.find_element_by_id("password").send_keys(Accounts.Prod_admin_pass)
DRIVER.find_element_by_id("_submit").click()
DRIVER.get(Sites.Prod_lang_en)
DRIVER.get(Sites.Prod_payroll)

groups_list = ["type=EXTERNAL_FORM_company=Exact Systems Polska",
               "type=PL_FORM_3_company=Exact Systems Polska",
               "type=PL_FORM_1_company=Exact Systems Polska",
               "type=DE_FORM_1_company=Exact Systems Deutschland",
               "type=DE_FORM_2_company=Exact Systems Deutschland",
               "type=DE_FORM_3_company=Exact Systems Deutschland",
               "type=DE_FORM_4_company=Exact Systems Deutschland",
               "type=DE_EXTERNAL_FORM_1_company=Exact Systems Deutschland",
               "type=EXTERNAL_FORM_company=Exact Systems Deutschland",
               "type=SK_FORM_1_company=Exact Systems Slovakia",
               "type=SK_FORM_2_company=Exact Systems Slovakia",
               "type=SK_FORM_3_company=Exact Systems Slovakia",
               "type=SK_FORM_4_company=Exact Systems Slovakia",
               "type=CZ_FORM_1_company=Exact Systems Czech Republic",
               "type=CZ_FORM_2_company=Exact Systems Czech Republic",
               "type=CZ_FORM_3_company=Exact Systems Czech Republic",
               "type=CZ_FORM_4_company=Exact Systems Czech Republic",
               "type=CZ_EXTERNAL_FORM_1_company=Exact Systems Czech Republic",
               "type=CZ_DEFAULT_FORM_1_company=Exact Systems Czech Republic",
               "type=RU_EXTERNAL_FORM_1_company=Exact Systems Russia",
               "type=RU_DEFAULT_FORM_1_company=Exact Systems Russia",
               "type=EXTERNAL_FORM_company=Exact Systems Turkey",
               "type=TR_DEFAULT_FORM_1_company=Exact Systems Turkey",
               "TR_EXTERNAL_FORM_1",
               "type=RO_EXTERNAL_FORM_1_company=Exact Systems Rom_nia",
               "type=RO_DEFAULT_FORM_1_company=Exact Systems Rom_nia",
               "type=UK_EXTERNAL_FORM_1_company=Exact Systems UK",
               "type=UK_DEFAULT_FORM_1_company=Exact Systems UK",
               "type=HU_EXTERNAL_FORM_1_company=Exact Systems Hungary",
               "type=HU_DEFAULT_FORM_1_company=Exact Systems Hungary",
               "type=CN_EXTERNAL_FORM_1_company=Exact Systems China",
               "type=CN_DEFAULT_FORM_1_company=Exact Systems China",
               "type=BE_FORM_1",
               "type=BE_EXTERNAL_FORM_1",
               "type=BE_DEFAULT_FORM_1",
               "type=EXTERNAL_FORM_company=AAS",
               "PL_EXTERNAL_FORM_2_company=AAS",
               "type=PL_FORM_2_company=AAS",
               "type=EXTERNAL_FORM_company=Exact Systems Netherlands",
               "type=NL_FORM_1_company=Exact Systems Netherlands",
               "type=NL_DEFAULT_FORM_1_company=Exact Systems Netherlands",
               "type=NL_EXTERNAL_FORM_1_company=Exact Systems Netherlands",
               "type=PT_FORM_1_company=Exact Systems, Lda. Portugal",
               "type=PT_FORM_2_company=Exact Systems, Lda. Portugal",
               "type=ES_FORM_1_company=Exact Systems, S.L. Spain",
               "type=ES_FORM_2_company=Exact Systems, S.L. Spain"
               ]


Cookies = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                 "/html/body/div[2]/div[1]/div[1]/div/i")))
Cookies.click()

# Calendar: Last month
while True:
    try:
        element = DRIVER.find_element_by_xpath("//*[@id='worker_payroll_dates']")
        element.click()
        time.sleep(2)
        break

    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(2)
        continue

while True:
    try:
        element = DRIVER.find_element_by_xpath("/html/body/div[8]/div[3]/ul/li[6]")
        element.click()
        time.sleep(2)
        break

    except (selenium.common.exceptions.ElementClickInterceptedException,
            selenium.common.exceptions.NoSuchElementException):
        time.sleep(2)
        continue


# Submit button
def submit():
    while True:
        try:
            element_2 = wait.until(EC.element_to_be_clickable((By.ID,
                                                               "worker_payroll_submit")))
            element_2.click()
            break

        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(2)
            continue


# Export button
def export():
    while True:
        try:
            time.sleep(2)
            DRIVER.find_element_by_class_name("ibox-content data-grid-list sk-loading")
            continue

        except selenium.common.exceptions.NoSuchElementException:
            break

    time.sleep(2)

    DRIVER.execute_script("window.scrollTo(0, 150)")

    results = DRIVER.find_element_by_xpath("//*[@id='workers-content']/div[2]/div[2]/div")
    value = results.get_attribute('innerHTML')

    DRIVER.execute_script("window.scrollTo(0,0)")

    if value != "No results":
        while True:
            try:
                element_2 = DRIVER.find_element_by_id("worker_payroll_export")
                element_2.click()
                element_4 = DRIVER.find_element_by_id("worker_payroll_exportCuts")
                element_4.click()
                element_5 = DRIVER.find_element_by_id("worker_payroll_exportToPaidOut")
                element_5.click()
                break

            except selenium.common.exceptions.ElementClickInterceptedException:
                time.sleep(2)
                continue

    elif value == "No results":
        while True:
            try:
                DRIVER.find_element_by_id("worker_payroll_export")
                break

            except selenium.common.exceptions.ElementClickInterceptedException:
                break


# Get companies
company_box = DRIVER.find_element_by_id("worker_payroll_company")
options = [x for x in company_box.find_elements_by_tag_name("option")]
companies = []

for element in options:
    companies_list = element.get_attribute("text")
    companies.append(companies_list)

companies.remove('-- Select --')
companies.remove('Test Company')
# print(f"Companies: {companies}")

for company in companies:  # Companies list made above
    while True:
        try:
            DRIVER.find_element_by_id("worker_payroll_company").click()
            company_selection = DRIVER.find_element_by_xpath(f""
                f"//select[@name='worker_payroll[company]']/option[text()='{company}']")
            company_selection.click()

            while True:
                try:
                    time.sleep(2)
                    element = DRIVER.find_element_by_xpath("//*[@id='worker_payroll_formType']")
                    element.click()
                    break

                except selenium.common.exceptions.ElementClickInterceptedException:
                    time.sleep(2)
                    continue

            select_box = DRIVER.find_element_by_xpath("//*[@id='worker_payroll_formType']")
            options = [x for x in select_box.find_elements_by_tag_name("option")]
            elements = []

            for element in options:
                element_list = element.get_attribute("text")
                elements.append(element_list)

            elements.remove('-- Select --')
            # print(f"Forms types: {elements}")

            # Loop through
            for code in elements:
                while True:
                    try:
                        element_3 = DRIVER.find_element_by_xpath("//*[@id='worker_payroll_formType']")
                        element_3.click()
                        form_type = DRIVER.find_element_by_xpath(f""
                                                f"//select[@name='worker_payroll[formType]']/option[text()='{code}']")
                        form_type.click()
                        submit()
                        export()
                        break

                    except (selenium.common.exceptions.ElementClickInterceptedException,
                            selenium.common.exceptions.StaleElementReferenceException) as error:
                        time.sleep(2)
                        continue

                    except selenium.common.exceptions.NoSuchElementException:
                        break
            break

        except(selenium.common.exceptions.ElementClickInterceptedException,
               selenium.common.exceptions.StaleElementReferenceException,
               selenium.common.exceptions.NoSuchElementException) as error:
            time.sleep(2)
            continue


def move_files():
    # Move files to corresponding folders
    files_list = [f for f in os.listdir(downloads_loc)
                  if os.path.isfile(os.path.join(downloads_loc, f))]

    for path in paths_list:
        try:
            os.makedirs(path, mode=0o777, exist_ok=False)

        except FileExistsError:
            continue

        except shutil.Error:
            continue

        except OSError:
            continue

    for file in files_list:
        for group in groups_list:
            while True:
                try:
                    x = re.search(group, file)
                finally:
                    break

            if x:
                # print(f"Match found for:  {file}")
                file_full = os.path.join(downloads_loc, file)
                shutil.move(file_full, password_dirs[group])
            else:
                continue

    os.chdir(desktop)
    shutil.make_archive("Payrolls", 'zip', "Payroll")


move_files()

if platform == "Linux" or platform == "Linux2":
    DRIVER.stop_client()
    DRIVER.quit()
    kill_driver()
    print("Script completed successfully")

elif platform == "win32":
    print("Script completed successfully")
    DRIVER.stop_client()
    DRIVER.quit()
    kill_driver()
    playsound.playsound(str(Paths.sound))

