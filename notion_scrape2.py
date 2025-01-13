import requests
import json
import pandas as pd

# Define the URL and headers
url = "https://productmarketfit.notion.site/api/v3/queryCollection?src=change_group"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    # "Content-Length": "380",  # Optional to include
    "Content-Type": "application/json",
    "Cookie": "device_id=17ad872b-594c-810f-871d-003b7b6e1ff9; notion_check_cookie_consent=false; NEXT_LOCALE=en-US; notion_locale=en-US/autodetect; notion_browser_id=206de85b-1d87-4b3a-ad93-680cfb575065; amp_unused=206de85b1d874b3aad93680cfb575065...1ihgjh318.1ihgl2rcr.3g.0.3g",
    "Host": "productmarketfit.notion.site",
    "Origin": "https://productmarketfit.notion.site",
    "Referer": "https://productmarketfit.notion.site/thefamilyofficelist?v=155fd1388bfa81ceab49000c9e12873e",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "notion-audit-log-platform": "web",
    "notion-client-version": "23.13.0.1452",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "x-notion-active-user-header": "",
    "x-notion-space-id": "44932c17-17e2-404a-9b45-8aa2edda7924",
    "Notion-Version": "2022-06-28"
}
data = {
    "source": {
        "type":"collection",
        "id":"155fd138-8bfa-8145-9847-000b100ab329",
        "spaceId":"44932c17-17e2-404a-9b45-8aa2edda7924"
    },
    "collectionView": {
        "id":"155fd138-8bfa-81ce-ab49-000c9e12873e",
        "spaceId":"44932c17-17e2-404a-9b45-8aa2edda7924"
    },
    "loader": {
        "reducers": {
            "collection_group_results": {
                "type":"results","limit":1500
            }
        },
        "sort":[],
        "searchQuery":"",
        "userTimeZone":"America/New_York"
    }
}

# Send the GET request to the Notion API
response = requests.post(url, data=json.dumps(data), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Data retrieved:", data)
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")


columns = ['title','tFru','Jwbq','JIzx','z|Nf','pm|B','MHbr','yedh','Xk{C','YChj','~mUG','UC_x','uBZ[']

new_data = []

for row in data['result']['reducerResults']['collection_group_results']['blockIds']:
    row_data = []
    for col in columns:
        try:
            row_data.append(data['recordMap']['block'][row]['value']['value']['properties'][col][0][0])
            # print(data['recordMap']['block'][row]['value']['value']['properties'][col][0][0])
        except:
            row_data.append('n/a')
    new_data.append(row_data)
    # print(data['recordMap']['block'][row]['value']['value']['properties']['title'][0][0])

df = pd.DataFrame(new_data)
df.columns = ["Organization", "Investment Stage", "Regions", "LinkedIn", "Description", "Number of Investments", 
              "Number of Exits", "Location", "Full Description", "Number of Portfolio Organizations", "Number of Lead Investments", "Facebook", "Website"]

df.to_excel('/Users/youssefawad/Downloads/test.xlsx')