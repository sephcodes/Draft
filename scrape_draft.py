from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ExcelManager import ExcelManager

# Use spreadsheet
my_file = 'Book.xlsx'
# Use team name
my_team_name = 'LaPorta Potty'

driver = webdriver.Chrome()
# Navigate to the webpage
url = 'https://fantasy.espn.com/football/mockdraftlobby'
driver.get(url)

# Define the CSS selector for the <ul> element with multiple classes
ul_css_selector = '.jsx-553213854.pa3'

excel_manager = ExcelManager(my_file)

def get_li_elements():
    try:
        # Find the <ul> element by CSS selector
        ul_element = driver.find_element(By.CSS_SELECTOR, ul_css_selector)
        # Get all <li> elements under the <ul> element
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        last_li_element = li_elements[len(li_elements)-1].text
        last_li_name = last_li_element.split(' /')[0]
        last_li_team = last_li_element.split(' /')[1].split(' - ')[1]
        is_mine = True if last_li_team == my_team_name else False

        excel_manager.mark_drafted_player(last_li_name, is_mine)
        return li_elements
    except Exception as e:
        print(f"Error finding <ul> element: {e}")
        return []

# Initial delay to allow time for navigation
initial_wait_time = 60
print(f"Waiting for {initial_wait_time} seconds to allow time for navigation...")
time.sleep(initial_wait_time)

# Store the initial set of <li> elements
previous_li_count = len(get_li_elements())

try:
    while True:
        time.sleep(1)  # Wait for a few seconds before checking again
        
        # Get the current set of <li> elements
        current_li_count = len(get_li_elements())
        
        if current_li_count > previous_li_count:
            print(f"New <li> element(s) added. Total <li> count: {current_li_count}")
            previous_li_count = current_li_count
        

finally:
    driver.quit()  # Close the browser when done
