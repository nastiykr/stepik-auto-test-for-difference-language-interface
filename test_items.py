import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector("button.btn-add-to-basket")