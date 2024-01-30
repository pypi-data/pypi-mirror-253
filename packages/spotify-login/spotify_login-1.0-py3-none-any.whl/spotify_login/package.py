from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def login(email, secret):
    robot_options = Options()
    robot_options.add_experimental_option("detach",True)
    robot = Chrome(options = robot_options)
    waiter = WebDriverWait(robot, 10)
    login_url = "https://accounts.spotify.com/en-GB/login"
    robot.get(login_url)
    username = "login-username"
    password = "login-password"
    button = "login-button"
    username_element = robot.find_element("id", username)
    password_element = robot.find_element("id", password)
    button_element = robot.find_element("id", button)
    username_element.send_keys(email)
    password_element.send_keys(secret)
    button_element.click()
    waiter.until(EC.url_changes(login_url))