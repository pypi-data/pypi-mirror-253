
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.casablanca-bourse.com/En/live-market/marche-actions-groupement"
response = requests.get(url)

categories = {
    'Foodproducers_Processors': 0,
    'Insurance': 1,
    'Banks': 2,
    'Construction_BuildingMaterials': 3,
    'Beverages': 4,
    'Chemicals': 5,
    'Distributors': 6,
    'Electricity': 7,
    'Pharmaceutical Industry': 8,
    'Engineering & Equipment Industrial Goods': 9,
    'Leisures and Hotels': 10,
    'Materials,Software & Computer Services': 11,
    'Mining': 12,
    'Real estate participation and promotion': 13,
    'Oil & Gas': 14,
    'Health': 15,
    'Transportation Services': 16,
    'Investment Companies & Other Finance': 17,
    'Real estate investment companies': 18,
    'Holding Companies': 19,
    'Forestry & Paper': 20,
    'Telecommunications': 21,
    'Transport': 22
}


def GetData(index):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the second table with the specified class
        tables = soup.find_all('table', {'class': 'w-full max-w-screen border border-gray-600'})
        if len(tables) >= 2:
            table = tables[index]
            rows = table.find_all('tr')

            # Extract column headers from the first row
            headers = [col.text.strip() for col in rows[0].find_all(['th', 'td'])]

            # Initialize an empty list to store the data
            data = []

            # Iterate through the rows starting from the second row (index 1)
            for row in rows[1:]:
                # Extract values from each column in the row
                values = [col.text.strip() for col in row.find_all(['td', 'th'])]

                # Create a dictionary with column names as keys and row values as values
                row_data = dict(zip(headers, values))

                # Append the dictionary to the data list
                data.append(row_data)

            # Create a DataFrame from the list of dictionaries
            df = pd.DataFrame(data)
            return df
        else:
            print("Failed to retrieve Data. Please try later.")
            return None
    else:
        print(f"Failed to retrieve the Data. Status code: {response.status_code}")
        return None
    
def print_category_keys():
     print("Category Keys:")
     for category in categories.keys():
         print(category)

def get_data_by_category(category):
    categories = {
        'Foodproducers_Processors': 0,
    'Insurance': 1,
    'Banks': 2,
    'Construction_BuildingMaterials': 3,
    'Beverages': 4,
    'Chemicals': 5,
    'Distributors': 6,
    'Electricity': 7,
    'Pharmaceutical Industry': 8,
    'Engineering & Equipment Industrial Goods': 9,
    'Leisures and Hotels': 10,
    'Materials,Software & Computer Services': 11,
    'Mining': 12,
    'Real estate participation and promotion': 13,
    'Oil & Gas': 14,
    'Health': 15,
    'Transportation Services': 16,
    'Investment Companies & Other Finance': 17,
    'Real estate investment companies': 18,
    'Holding Companies': 19,
    'Forestry & Paper': 20,
    'Telecommunications': 21,
    'Transport': 22
    }

    if category in categories:
        return GetData(categories[category])
    else:
        return None