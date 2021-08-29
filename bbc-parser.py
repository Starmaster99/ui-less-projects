# selenium для самых маленьких

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("Минутку...\n")

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
        choiceless_link = choiceless[i].get_attribute('href')                           # ссылка
        choiceless_head = choiceless[i].text                                            # заголовок
        print(f"{i + 1}. {choiceless_head}: {choiceless_link}")
        if i == howmany:
            break

    options = int(input("\nВывести больше информации?\n1 - Да\n2 - Нет\n"))
    if options == 1:
        for i in range(len(choiceless)):
            choiceless_head = choiceless[i].text                                        # заголовок
            choiceless_descc = driver.find_elements_by_class_name("media__summary")     # ↓
            choiceless_desc = choiceless_descc[i].text                                  # подзаголовок

            choiceless_link = choiceless[i].get_attribute('href')                       # ссылка

            choiceless_pic = driver.find_elements_by_class_name("image-replace")        # ↓
            choiceless_picc = choiceless_pic[i].get_attribute("src")                    # картинка публикации

            # TODO: рубрика публикации и дата

            choiceless_date = "placeholder"

            print(f"\n{i + 1}. Заголовок: {choiceless_head}\nПодзаголовок: {choiceless_desc}\n"
                  f"Ссылка: {choiceless_link}\nСсылка на картинку публикации: {choiceless_picc}\n"
                  f"Дата публикации новости: {choiceless_date}")
            if i == howmany:
                break


if __name__ == "__main__":
    if choice == 1:
        without_choice()

driver.quit()
