from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class IMDbSearchTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.imdb.com/search/name/"

    def perform_search(self, name, birth_year=None, death_year=None):
        self.driver.get(self.base_url)

        try:
            # Wait for the search form to be present
            search_form = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'search-form'))
            )

            # Fill in the name input
            name_input = self.driver.find_element(By.NAME, 'name')
            name_input.send_keys(name)

            # If birth year is provided, fill it in
            if birth_year:
                birth_year_input = self.driver.find_element(By.NAME, 'birth_year')
                birth_year_input.send_keys(birth_year)

            # If death year is provided, fill it in
            if death_year:
                death_year_input = self.driver.find_element(By.NAME, 'death_year')
                death_year_input.send_keys(death_year)

            # Click the search button
            search_button = self.driver.find_element(By.XPATH, '//button[text()="Search"]')
            search_button.click()

        except TimeoutException:
            print("Timed out waiting for elements to load.")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    test = IMDbSearchTest()
    test.perform_search(name="Tom Hanks", birth_year="1956")
    test.quit()
