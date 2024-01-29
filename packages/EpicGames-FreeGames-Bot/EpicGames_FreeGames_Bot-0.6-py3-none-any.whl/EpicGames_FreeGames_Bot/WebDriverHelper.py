from selenium import webdriver
class WebDriverHelper:
    @staticmethod
    def create_chrome_driver(profiler_directory):
        options = webdriver.ChromeOptions()

        options.add_argument(f'--profile-directory={profiler_directory}')
        options.add_argument("user-data-dir=C:\\Users\\aysec\\AppData\\Local\\Google\\Chrome\\User Data\\")

        options.add_argument('--no-first-run')
        options.add_argument('--no-default-browser-check')
        return webdriver.Chrome(options=options)