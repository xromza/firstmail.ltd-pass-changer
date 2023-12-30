from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from colorama import Fore, Style
from os import path
from Setup import install_packages
from webbrowser import get
from platform import system as plsys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from random_generator import random_pass

def detect_browser() -> str:
    system = plsys()
    if system == "Windows":
        return "edge"
    elif system == "Darwin":
        return "safari"
    else:
        return None
def change_password(current_login: str, current_password: str, name_of_result_file: str, browser: str = None) -> None:
    # Initializing web-driver
    print(f"{Fore.RED}Working with the account: {Fore.CYAN}{current_login}{Fore.YELLOW}:{Fore.CYAN}{current_password}{Style.RESET_ALL}\n")
    while 1:
        if browser == "edge":
            driver = webdriver.Edge()
            break
        elif browser == "firefox":
            driver = webdriver.Firefox()
            break
        elif browser == "ie":
            driver = webdriver.Ie()
            break
        elif browser == "safari":
            driver = webdriver.Safari()
            break
        else:
            browser = detect_browser()
            continue
    print(f"{Fore.YELLOW}Initializing the driver (automatically detected browser: {browser})...{Style.RESET_ALL}\n")
    # Opening web page
    driver.get('https://firstmail.ltd/webmail/login')
    print(f"{Fore.YELLOW}Open page ({Fore.CYAN}firstmail.ltd/webmail/login{Fore.YELLOW}){Style.RESET_ALL}\n")
    # Finding the element (login input fields) and entering the login
    login_input = driver.find_element(By.ID, 'email')
    login_input.send_keys(current_login)
    print(f"{Fore.YELLOW}Entering login ({current_login})...{Style.RESET_ALL}\n")
    sleep(1)
    # Finding the element (password entry fields) and entering the password
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(current_password)
    print(f"{Fore.YELLOW}Entering password ({current_password})...{Style.RESET_ALL}\n")
    #Finding an element (entry buttons) and clicking
    try:
        sleep(1)
        login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary w-100' and @type='submit']")
        login_button.click()
    except NoSuchElementException:
        pass
    print(f"{Fore.YELLOW}I'm logging in...{Style.RESET_ALL}\n")
    try:
        error_popup = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="Vue-Toastification__toast-body"]'))
        )
        print(f"{Fore.RED}[ERR] !!!The account has an invalid username or password!!!\n{Fore.YELLOW}Skipping...{Style.RESET_ALL}")
        raise ZeroDivisionError
    except TimeoutException:
        sleep(2)
    driver.get("https://firstmail.ltd/webmail/settings")
    print(f"{Fore.YELLOW}I go to the profile settings...{Style.RESET_ALL}\n")
    new_password = random_pass(12)
    print(f"{Fore.YELLOW}Created a new password: {Fore.CYAN}{new_password}{Style.RESET_ALL}\n")
    try:
        current_password_field = driver.find_element(By.ID, "newPassword")
        current_password_field.send_keys(current_password)
    except NoSuchElementException:
        raise ZeroDivisionError
    print(f"{Fore.YELLOW}I'm entering the current password ({current_password})...{Style.RESET_ALL}\n")
    try:
        new_password_field = driver.find_element(By.XPATH, '//label[text()="Новый пароль"]/following-sibling::div//input[@type="password"]')
    except NoSuchElementException:
        new_password_field = driver.find_element(By.XPATH, '//label[text()="New Password"]/following-sibling::div//input[@type="password"]')
    new_password_field.send_keys(new_password)
    print(f"{Fore.YELLOW}Entering new password ({new_password})...{Style.RESET_ALL}\n")
    try:
        new_password_field_confirm = driver.find_element(By.XPATH, '//label[text()="Подтвердите новый пароль"]/following-sibling::div//input[@type="password"]')
    except NoSuchElementException:
        new_password_field_confirm = driver.find_element(By.XPATH, '//label[text()="Confirm new password"]/following-sibling::div//input[@type="password"]')
    new_password_field_confirm.send_keys(new_password)
    print(f"{Fore.YELLOW}Confirming new password...{Style.RESET_ALL}\n")
    sleep(2)
    confirm_button = driver.find_element(By.XPATH, '//button[@type="submit" and contains(@class, "btn-primary")]')
    confirm_button.click()
    print(f"{Fore.YELLOW}Changing password...{Style.RESET_ALL}\n")
    if not path.exists(name_of_result_file):
        with open(f"Results/{name_of_result_file}", "w") as f:
            f.write(f"{current_login}:{new_password}\n")
    else:
        with open(f"Results/{name_of_result_file}", "a") as f:
            f.write(f"{current_login}:{new_password}\n")
    driver.close()
    print(f"{Fore.GREEN}Successful! {Fore.CYAN}{current_login}{Fore.GREEN}:{Fore.CYAN}{current_password} {Fore.GREEN}-> {Fore.CYAN}{current_login}{Fore.GREEN}:{Fore.CYAN}{new_password}{Style.RESET_ALL}\n")

if not path.exists("SetupCompleted.txt"):
    install_packages()
if __name__ == "__main__":
    logo = f"""{Fore.CYAN}{Style.BRIGHT}██╗░░██╗██████╗░░█████╗░███╗░░░███╗███████╗░█████╗░░██████╗
╚██╗██╔╝██╔══██╗██╔══██╗████╗░████║╚════██║██╔══██╗██╔════╝
░╚███╔╝░██████╔╝██║░░██║██╔████╔██║░░███╔═╝███████║╚█████╗░
░██╔██╗░██╔══██╗██║░░██║██║╚██╔╝██║██╔══╝░░██╔══██║░╚═══██╗
██╔╝╚██╗██║░░██║╚█████╔╝██║░╚═╝░██║███████╗██║░░██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░{Style.RESET_ALL}"""
    print(logo)

    sleep(2)
    print(f"{Fore.CYAN}FIRSTMAIL.LTD PassChanger. By {Fore.RED}xromza\n{Style.RESET_ALL}")
    sleep(2)
    main_browser = get()
    while 1:
        data_directory = input("Enter the path to the data file >>> ")
        name_of_result_file = input("Enter the path to the results file >>> ")
        data_list = []
        with open(data_directory, "r") as f:
            for data_line in f.readlines():
                data_list.append(data_line.split(":"))
        for data_pack in data_list:
            try:
                change_password(data_pack[0], data_pack[1], name_of_result_file + ".txt", main_browser.name if main_browser else None)
            except ZeroDivisionError:
                continue