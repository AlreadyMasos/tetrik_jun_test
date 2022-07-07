from selenium import webdriver
import chromedriver_autoinstaller


class WikiPage:
    animals_dict = {'А':0, 'Б':0, 'В':0, 'Г':0, 'Д':0, 'Е':0,
                'Ж':0, 'З':0, 'И':0, 'Й':0, 'К':0, 'Л':0,
                'М':0, 'Н':0, 'О':0, 'П':0, 'Р':0, 'С':0,
                'Т':0, 'У':0, 'Ф':0, 'Х':0, 'Ц':0, 'Ч':0,
                'Ш':0, 'Щ':0, "Э":0, "Ю":0, "Я":0}

    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")

        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get('https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83')

    def click_next_page(self):
        next_page_button = self.driver.find_element('xpath', '//*[@id="mw-pages"]/a[2]')
        next_page_button.click()

    def find_letter(self):
        return self.driver.find_element('xpath', '//*[@id="mw-pages"]/div/div/div/h3').text

    def find_current_names_list(self):
        list_of_names = self.driver.find_element('xpath', '//*[@id="mw-pages"]/div/div/div/ul')
        names = list_of_names.find_elements('xpath', 'li')
        return names

    def add_animals(self):
        self.animals_dict[self.find_letter()] += len(self.find_current_names_list())

    def close(self):
        self.driver.quit()

    def checker(self):
        return True if self.find_letter() in self.animals_dict.keys() else False

page = WikiPage()
while True:
    page.add_animals()
    page.click_next_page()
    if not page.checker():
        break

page.close()
print(page.animals_dict)
