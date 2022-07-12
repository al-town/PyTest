import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
    # Go to login page and log in
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.find_element_by_id('email').send_keys('test@y.ru')
    pytest.driver.find_element_by_id('pass').send_keys('123456')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Go to 'my pets' page and check that everything is fine
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    assert pytest.driver.find_element_by_css_selector('button.btn.btn-outline-success').text == "Добавить питомца"

    yield

    pytest.driver.quit()


def test_check_my_pets():
    """All my pets are displayed"""
    all_text = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class = ".col-sm-4 left"]')))
    num_of_pets = all_text.text.split("\n")
    num = pytest.driver.find_elements_by_css_selector('th[scope = "row"]')
    assert len(num) == int(num_of_pets[1][-1])


def test_check_pets_data():
    """All pets have a name, age and breed"""
    pytest.driver.implicitly_wait(10)
    num = pytest.driver.find_elements_by_css_selector('td')
    for i in range(len(num)):
        assert num[i].text != ''


def test_image_pet():
    """Check that at least half of the pets have a photo"""
    pytest.driver.implicitly_wait(10)
    image = pytest.driver.find_elements_by_css_selector('th[scope = "row"] > img')
    count = 0
    for i in range(len(image)):
        if image[i].get_attribute('src') != '':
            count += 1
    assert len(image) / 2 <= count


def test_different_name():
    """Checking that all my pets have different names"""
    num = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td')))
    amount, name = len(num) // 4, set()
    for i in range(0, len(num), 4):
        name.add(num[i].text.lower())
    assert len(name) == amount


def test_different_pets():
    """There are no duplicate pets in the list"""
    num = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td')))
    pet_set = set()
    for i in range(0, len(num), 4):
        pet_set.add(num[i].text.lower() + num[i + 1].text.lower() + num[i + 2].text)
    assert len(pet_set) == len(num) // 4
