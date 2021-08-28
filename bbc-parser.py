# selenium для самых маленьких

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")   # подходит для всех версий

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.bbc.com/")
print("< +++ НОВОСТНОЙ ПАРСЕР С САЙТА bbc.com +++ >\n"
      f"Название страницы: {driver.title}\n")

choice = int(input("Вы хотите: \n1 - Вывести n новостей с сайта без выбора рубрики\n2 - С выбором рубрики\n"))


def without_choice():
    choiceless = driver.find_elements_by_class_name("media__link")
    howmany = int(input("Сколько новостей вывести?\n"))-1

    for i in range(len(choiceless)):
        choiceless_link = choiceless[i].get_attribute('href')
        choiceless_text = choiceless[i].text
        print(f"{i + 1}. {choiceless_text}: {choiceless_link}")
        if i == howmany:
            break


if choice == 1:
    without_choice()

driver.quit()
