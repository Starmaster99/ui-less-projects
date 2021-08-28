# selenium для самых маленьких
# WIP: список работающих закомментирован ниже

# /best/ +-
# /reviews/ --
# /news/ --
# /culture/ --
# /special-features/ --
# /tech/ ++
# /personal-finance/ ++
# /health/ ++
# /home/ ++
# /roadshow/ --

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")   # подходит для всех версий

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.cnet.com/")
print(f"< +++ НОВОСТНОЙ ПАРСЕР С САЙТА cnet.com +++ >\n"
      f"Название страницы: {driver.title}\nГде будем искать? На выбор: ")


menu = driver.find_elements_by_class_name("menuList_title")
for i in range(len(menu)):
    menu_links = menu[i].get_attribute('href')
    menu_links_slash = menu_links.split("/")[-2]
    print(f"{i+1}. /{menu_links_slash}/")
    if i == 9:
        break


target_page = input("\nhttps://www.cnet.com/")
driver.get("https://www.cnet.com/" + target_page)
print(f"Название страницы: {driver.title}\nОтлично. В какой части /{target_page} мы будем искать? На выбор:")


target_list = driver.find_elements_by_class_name("c-universalSubNav_subnavLink")
for i in range(len(target_list)):
    target_links = target_list[i].get_attribute('href')
    target_link = target_links.split("/")[-2]
    print(f"{i+1}. /{target_link}/")
    if i == 3:
        break


final_target = input(f"\nВнимание! Первый элемент работает некорректно.\nhttps://www.cnet.com/{target_page}")
driver.get(f"https://www.cnet.com/{target_page}{final_target}")
howmany = int(input("\nМы почти у цели. Введите число, показывающее, сколько ссылок на статьи будет выведено. " + "\n"))
howmany -= 1

asset = driver.find_elements_by_class_name("o-linkOverlay")
for i in range(len(asset)):
    links = asset[i].get_attribute('href')
    print(f"{i+1}. {links}")
    if i == howmany:
        break


driver.quit()
