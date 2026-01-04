
# По атрибуту:
# //элемент[@атрибут='значение']
# Пример: //input[@name='email']

# По тексту:
# //элемент[text()='текст'] (без @, так как текст — н
# е атрибут)Пример: //button[text()='Submit']

# //a[@class='button-nav w-inline-block']
#
# //a[@class='nav-link']
#
# //a[@class='tab-link w-inline-block w-tab-link']
#
# //div[@class='tab-link_menu w-tab-menu']
#
# //a[text()='Backend']
#
# //div[@class='tab-link_menu w-tab-menu']//a[@data-w-tab='Python']
#
# //div[@class='tab-link_menu w-tab-menu']//a[@data-w-tab='Java']
#
# //a[@class='button-secondary w-inline-block']
#
# //a[@class='button-secondary w-inline-block']//div[text()='Check all courses']
#
# //section[@class='section_ide']//img[@class='screen_main-image']

# //footer[@class='footer']//div[@class='footer_block']//div[@class='margin_bottom-16']//h4[@class='heading-style-h4']//span[text()='Hyperskill Academy']