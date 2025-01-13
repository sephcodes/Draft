import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


driver = webdriver.Chrome()
# Navigate to the webpage
url = 'https://productmarketfit.notion.site/thefamilyofficelist?v=155fd1388bfa81ceab49000c9e12873e'
driver.get(url)

time.sleep(30)

rows = driver.find_elements(By.CSS_SELECTOR, ".notion-selectable.notion-page-block.notion-collection-item")

data = []

for row in rows:
    # Find all cells in the row
    cells = row.find_elements(By.CSS_SELECTOR, ".notion-table-view-cell")
    
    # Extract the text from each cell (which is inside a <span>)
    row_data = []
    for cell in cells:
        # Find all <span> elements inside the cell (there might be multiple)
        spans = cell.find_elements(By.TAG_NAME, "span")
        a = cell.find_elements(By.TAG_NAME, "a")

        # If there are spans, take the text of the first one (or handle multiple spans)
        if spans:
            if spans[0].text[0] != '/':
                row_data.append(spans[0].text)
            else:
                row_data.append(a[0].get_attribute('href'))
        else:
            row_data.append('')  # In case there are no <span> elements

    data.append(row_data)

df = pd.DataFrame(data)
df.columns = ["Organization", "Investment Stage", "Regions", "LinkedIn", "Description", "Number of Investments", 
              "Number of Exits", "Location", "Full Description", "Number of Portfolio Organizations", "Number of Lead Investments", "Facebook", "Website"]

df.to_excel('/Users/youssefawad/Downloads/test.xlsx')