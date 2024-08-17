from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDbSearchAutomation:
    def __init__(self):
        # Initialize the WebDriver (using Chrome in this case)
        self.driver = webdriver.Chrome()
        # Set up an explicit wait with a timeout of 10 seconds
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        try:
            # Open the specified URL
            self.driver.get(url)
            print("Page opened successfully.")
        except Exception as e:
            # Print an error message if the page fails to open
            print(f"Failed to open page: {str(e)}")

    def fill_form(self, first_name=None, last_name=None, birth_year=None, gender=None):
        try:
            # Fill in the name field if a first name or last name is provided
            if first_name or last_name:
                name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "name")))
                name_field.clear()  # Clear any existing text in the field
                name_field.send_keys(f"{first_name} {last_name}".strip())  # Enter the full name

            # Fill in the birth year if provided
            if birth_year:
                birth_year_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "birth_date")))
                birth_year_field.clear()  # Clear any existing text in the field
                birth_year_field.send_keys(birth_year)  # Enter the birth year

            # Select the gender from the dropdown if provided
            if gender:
                gender_dropdown = self.wait.until(EC.visibility_of_element_located((By.NAME, "gender")))
                gender_dropdown.send_keys(gender.capitalize())  # Enter the gender, capitalized

            print("Form filled successfully.")
        except Exception as e:
            # Print an error message if there is an issue filling the form
            print(f"Error while filling the form: {str(e)}")

    def perform_search(self):
        try:
            # Locate and click the search button
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
            search_button.click()

            # Wait for the search results to load
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
            print("Search completed successfully!")
        except Exception as e:
            # Print an error message if there is an issue during the search
            print(f"Error during search: {str(e)}")

    def close_browser(self):
        try:
            # Close the browser
            self.driver.quit()
            print("Browser closed successfully.")
        except Exception as e:
            # Print an error message if there is an issue closing the browser
            print(f"Error closing the browser: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the IMDbSearchAutomation class
    imdb_bot = IMDbSearchAutomation()

    # Open the IMDb Advanced Name Search page
    imdb_bot.open_page("https://www.imdb.com/search/name/")

    # Fill out the search form with the specified parameters
    imdb_bot.fill_form(
        first_name="guvi",
        last_name="network",
        birth_year="1974",
        gender="Female"  # Capitalized to match typical dropdown options
    )

    # Perform the search
    imdb_bot.perform_search()

    # Close the browser
    imdb_bot.close_browser()
