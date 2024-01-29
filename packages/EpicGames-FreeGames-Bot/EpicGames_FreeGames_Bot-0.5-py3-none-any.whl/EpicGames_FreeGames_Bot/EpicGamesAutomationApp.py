from selenium.webdriver.common.keys import Keys
from EpicGamesConnect import EpicGamesConnect
from WebDriverHelper import WebDriverHelper
class EpicGamesAutomationApp:
    @staticmethod
    def run():
        driver = WebDriverHelper.create_chrome_driver('Profile 1')

        url = 'https://www.epicgames.com/id/login?lang=en-US&noHostRedirect=true&redirectUrl=https%3A%2F%2Fstore.epicgames.com%2Fen-US%2F&client_id=875a3b57d3a640a6b7f9b4e883463ab4'
        expected_redirect_url = 'https://store.epicgames.com/en-US/'
        driver.get(url)

        EpicGamesConnect.login(driver, expected_redirect_url)

        input("Press a key to close the browser")

        driver.quit()

if __name__ == "__main__":
    EpicGamesAutomationApp.run()



















































