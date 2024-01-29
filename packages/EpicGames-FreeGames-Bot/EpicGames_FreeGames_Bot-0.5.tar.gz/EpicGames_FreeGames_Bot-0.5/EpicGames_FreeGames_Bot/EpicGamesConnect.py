from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from EpicGames_FreeGames_Bot.WaitHelper import WaitHelper

class EpicGamesConnect:
    GOOGLE_LOGIN_PATH= '//*[@id="login-with-google"]'
    LOGIN_BTN_PATH='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div'
    FREE_NOW_COST_ELEMENT_PATH='//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[1]/div[2]'
    FREE_BUY_BUTTON_PATH='//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/div[3]/div/aside/div/div/div[6]/div/button'
    @staticmethod
    def login(driver, expected_url):
        WaitHelper.random_sleep(5, 7)
        if driver.current_url == expected_url:
            print("Correct URL.")
            EpicGamesConnect.free_games_cost(driver)
        else:
            print(f"Different URL: {driver.current_url}")
            EpicGamesConnect.logins_started(driver)
            return

    @staticmethod
    def logins_started(driver):
        # next-step
        next_step = WaitHelper.wait_for_element(driver, By.XPATH, EpicGamesConnect.GOOGLE_LOGIN_PATH)
        next_step.click()
        new_window_handle = driver.window_handles[-1]  # Son eklenen pencerenin tanımlayıcısını al
        driver.switch_to.window(new_window_handle)
        WaitHelper.wait_for_element(driver, By.XPATH,EpicGamesConnect.GOOGLE_LOGIN_PATH).click()
        WaitHelper.random_sleep(5, 7)
        EpicGamesConnect.free_games_cost(driver)

    @staticmethod
    def free_games_cost(driver):
        # get last added window
        driver.switch_to.window(driver.window_handles[0])
        WaitHelper.random_sleep(5, 7)
        epic_html_content = driver.page_source
        epic_window_soup = BeautifulSoup(epic_html_content, 'html.parser')
        free_games_window = epic_window_soup.find('div', {'class': 'css-1vu10h2'})
        free_game_child = free_games_window.find('div', {'class': 'css-1myhtyb'})
        free_now_cost = free_game_child.find('div', {'class': 'css-1magkk1'})

        # Free Now Cost element
        if free_now_cost:
            free_now_cost_element = WaitHelper.wait_for_element(driver, By.XPATH,EpicGamesConnect.FREE_NOW_COST_ELEMENT_PATH)
            free_now_cost_element.click()
            print("Free cost clicked")
            WaitHelper.random_sleep(4, 6)
            free_buy_button = WaitHelper.wait_for_element(driver, By.XPATH,EpicGamesConnect.FREE_BUY_BUTTON_PATH)
            free_buy_button.click()

        else:
            print("Element not found")

