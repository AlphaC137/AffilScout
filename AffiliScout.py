import requests
import time
import csv
from bs4 import BeautifulSoup

# Function to scrape affiliate programs from various sources
def scrape_affiliate_programs(niche):
    # List of affiliate program directories to scrape
    search_urls = [
        f"https://www.affiliateprograms.com/search/?q={niche}",
        f"https://www.offervault.com/?search={niche}",
        f"https://www.shareasale.com/search.cfm?query={niche}"
        f"https://www.google.com/search?q={niche}+affiliate+programs"
    ]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    affiliate_links = []
    
    # Iterate through each URL and scrape affiliate program links
    for url in search_urls:
        print(f"Searching for affiliate programs on: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for successful response
            
            # Parse the HTML page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Search for affiliate links (in these examples, it's assumed they are <a> tags with specific classes)
            for link in soup.find_all('a', href=True):
                href = link['href']
                if "affiliate" in href or "program" in href:
                    affiliate_links.append(href)
                    
            time.sleep(2)  # Delay to avoid hitting servers too quickly

        except requests.exceptions.RequestException as e:
            print(f"Error scraping {url}: {e}")
    
    return affiliate_links

# Function to save the results to a CSV file
def save_to_csv(data, niche):
    filename = f"{niche}_affiliate_programs.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Program Name", "Link"])
        for program in data:
            writer.writerow([program, data[program]])
    print(f"\nResults saved to {filename}")

# Main function to drive the user interface and process
def main():
    print("Welcome to the Enhanced Affiliate Program Finder!")
    
    # Get niche from the user
    niche = input("Enter your niche (e.g., 'fitness', 'technology', 'travel'): ").strip().lower()
    
    print(f"Searching for affiliate programs in the '{niche}' niche...\n")
    
    # Scrape affiliate programs from multiple sources
    affiliate_programs = scrape_affiliate_programs(niche)
    
    # If results found, display them
    if affiliate_programs:
        print(f"\nFound {len(affiliate_programs)} potential affiliate programs for '{niche}':\n")
        for idx, program in enumerate(affiliate_programs, 1):
            print(f"{idx}. {program}")
        
        # Optionally save to CSV
        save_choice = input("\nWould you like to save these results to a CSV file? (y/n): ").strip().lower()
        if save_choice == 'y':
            save_to_csv(affiliate_programs, niche)
        else:
            print("Results not saved.")
    else:
        print(f"No affiliate programs found for the '{niche}' niche. Try searching with different keywords.")

if __name__ == "__main__":
    main()
