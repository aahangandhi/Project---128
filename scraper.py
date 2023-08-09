import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia URL for the list of brown dwarfs
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Send an HTTP GET request to fetch the HTML content of the page
response = requests.get(START_URL)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the 3rd table with class="wikitable sortable"
table = soup.find_all("table", class_="wikitable sortable")[2]

# Initialize the list to store scraped data
scraped_data = []

# Define scrape() method to scrape all column data
def scrape():
    for row in table.find_all("tr")[1:]:
        columns = row.find_all("td")

        # Extracting data from columns
        brown_dwarf = columns[0].text.strip()
        constellation = columns[1].text.strip()
        right_ascension = columns[2].text.strip()
        declination = columns[3].text.strip()
        app_mag = columns[4].text.strip()
        distance_ly = columns[5].text.strip()
        spectral_type = columns[6].text.strip()
        mass_mj = columns[7].text.strip()
        radius_rj = columns[8].text.strip()
        discovery_year = columns[9].text.strip()

        # Append the data to the list scraped_data
        scraped_data.append([brown_dwarf, constellation, right_ascension, declination, app_mag, distance_ly, spectral_type, mass_mj, radius_rj, discovery_year])

# Call the scrape() method to fetch the data
scrape()

# Create a DataFrame from the scraped data
headers = ["Brown dwarf", "Constellation", "Right ascension", "Declination", "App. mag.", "Distance (ly)", "Spectral Type", "Mass (MJ)", "Radius (RJ)", "Discovery Year"]
brown_dwarfs_df = pd.DataFrame(scraped_data, columns=headers)

# Export DataFrame to CSV
brown_dwarfs_df.to_csv("brown_dwarfs_data.csv", index=False)
