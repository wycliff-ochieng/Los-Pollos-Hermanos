import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

# --- Part 1: Scrape Characters from Wikipedia (Corrected Syntax) ---
def scrape_characters_from_wikipedia():
    print("--- Starting Character Scraping from Wikipedia ---")
    characters = []
    url = "https://en.wikipedia.org/wiki/List_of_Breaking_Bad_and_Better_Call_Saul_characters"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # --- SYNTAX FIX: Changed 'class=' to 'class_' ---
        character_table = soup.find('table', class_='wikitable')
        
        for row in character_table.find_all('tr')[1:]:
            first_cell = row.find('td')
            if not first_cell: continue
            link = first_cell.find('a')
            if link and link.get('href'):
                name = link.text.strip()
                characters.append({'name': name})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Wikipedia page: {e}")
        return []
    print(f"Found {len(characters)} characters on Wikipedia.")
    return characters


# --- Part 2: Scrape Quotes from Fandom (DEFINITIVE PARSING LOGIC) ---
def scrape_quotes_from_fandom():
    print("\n--- Starting Quote Scraping from Fandom Wiki (using Selenium) ---")
    quotes = []
    top_characters = {
        "Walter White":    "Walter_White",
        "Jesse Pinkman":   "Jesse_Pinkman",
        "Saul Goodman":    "Jimmy_McGill",
        "Mike Ehrmantraut": "Mike_Ehrmantraut",
        "Gus Fring":       "Gustavo_Fring",
        "Skyler White":    "Skyler_White",
        "Hank Schrader":   "Hank_Schrader",
    }
    
    service = ChromeService()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    
    driver = webdriver.Chrome(service=service, options=options)
    print("Selenium WebDriver launched successfully.")

    for display_name, url_name in top_characters.items():
        url = f"https://breakingbad.fandom.com/wiki/{url_name}/Quotes"
        print(f"Visiting for quotes: {url}")
        
        try:
            driver.get(url)
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "mw-content-text"))
            )
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # --- THIS IS THE FINAL, CORRECT LOGIC BASED ON YOUR SCREENSHOT ---
            # 1. Target the specific div that contains the article content.
            parser_output_div = soup.find('div', class_='mw-parser-output')
            
            if parser_output_div:
                # 2. Find all `blockquote` and `dl` tags, which contain the quotes.
                quote_elements = parser_output_div.find_all(['blockquote', 'dl'])
                
                for element in quote_elements:
                    # 3. Get the clean text from the element, using a space as a separator for dialogues.
                    raw_text = element.get_text(separator=' ', strip=True)
                    
                    # 4. Clean up the citation link (e.g., "[src]")
                    cleaned_text = raw_text.split('[')[0].strip()
                    
                    # 5. A simple filter to avoid empty or junk tags.
                    if len(cleaned_text) > 5:
                         quotes.append({'character': display_name, 'quote': cleaned_text})
            # --- END OF FINAL LOGIC ---

        except Exception as e:
            print(f"ERROR: Could not process page for {display_name}: {e}")

    driver.quit()
    print("\nSelenium WebDriver closed.")
    
    print(f"Found {len(quotes)} quotes from Fandom.")
    return quotes

def save_data_to_json(characters, quotes):
    """Saves the scraped data into a single db.json file."""
    print("\n--- Saving data to db.json ---")
    
    # Combine everything into one dictionary
    database = {
        "characters": characters,
        "quotes": quotes
    }
    
    # Write the data to a file with nice formatting
    with open('db.json', 'w') as f:
        json.dump(database, f, indent=2)
        
    print("Data successfully saved to db.json!")

# --- Main Execution ---
if __name__ == "__main__":
    characters_data = scrape_characters_from_wikipedia()
    quotes_data = scrape_quotes_from_fandom()
    save_data_to_json(characters_data, quotes_data)
    
    print("\n\n--- SCRAPING COMPLETE ---")
    
    print("\n--- SAMPLE CHARACTERS (from Wikipedia) ---")
    for char in characters_data[:10]:
        print(f"{char['name']}")
        
    print("\n--- SAMPLE QUOTES (from Fandom) ---")
    if quotes_data:
        for quote in quotes_data[:40]:
            print(f"{quote['character']}: \"{quote['quote']}\"")
    else:
        print("No valid quotes were extracted.")