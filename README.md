# Affiliteer - Affiliate Program Finder

**Affiliteer** is a Python script designed to help you find relevant affiliate programs in your chosen niche. By scraping multiple affiliate networks and directories, it simplifies the process of discovering profitable opportunities for affiliate marketing.

This tool is especially useful for beginners in affiliate marketing who want to explore various affiliate programs without manually searching on multiple websites.

---

## Features

- **Multiple Affiliate Sources**: Scrapes several affiliate directories, including AffiliatePrograms.com, OfferVault, and ShareASale.
- **Niche-Specific**: You can search for affiliate programs in any niche (e.g., fitness, technology, travel).
- **CSV Export**: Save your search results to a CSV file for easy tracking and reference.
- **Rate Limiting**: Includes built-in delays to avoid overloading websites and prevent IP blocks.
- **User-Friendly**: Prompts you for input and provides clear results with an option to save them.

---

## Requirements

Before running the script, make sure you have Python 3.x installed and the required libraries:

- `requests` – for sending HTTP requests.
- `beautifulsoup4` – for parsing HTML and extracting relevant data.

### Install Dependencies:

```bash
pip install requests beautifulsoup4
```
# How to Use

Clone the repository to your local machine:
```
git clone https://github.com/alphac137/affiliteer.git
cd affiliteer
```
Run the script:
```
python affiliate_program_finder_v2.py
```
Enter your niche when prompted (e.g., "fitness", "technology", "travel").
The script will scrape several affiliate program directories and display the results.
Optionally, you can save the results to a CSV file for future reference.

#Example Output
```
Welcome to the Enhanced Affiliate Program Finder!
Enter your niche (e.g., 'fitness', 'technology', 'travel'): fitness

Searching for affiliate programs in the 'fitness' niche...

Searching for affiliate programs on: https://www.affiliateprograms.com/search/?q=fitness
Searching for affiliate programs on: https://www.offervault.com/?search=fitness
Searching for affiliate programs on: https://www.shareasale.com/search.cfm?query=fitness

Found 5 potential affiliate programs for 'fitness':

1. https://www.fitnessaffiliateprogram1.com
2. https://www.fitnessaffiliateprogram2.com
3. https://www.affiliateprograms.com/fitness
4. https://www.shareasale.com/fitness
5. https://www.offervault.com/fitness

Would you like to save these results to a CSV file? (y/n): y
```
Results saved to fitness_affiliate_programs.csv

#File Structure

```
affiliteer/
├── affiliate_program_finder_v2.py  # Main Python script
├── README.md                       # This file
└── requirements.txt                # List of dependencies
```
# Contribute

Contributions are welcome! If you'd like to improve the tool, feel free to fork the repository and create a pull request.

# License
This project is open-source and available under the MIT License.

# Disclaimer
This script scrapes data from publicly available affiliate directories and marketplaces. Be mindful of the legal and ethical considerations regarding web scraping. Always respect the website's terms of service.

# Acknowledgements
BeautifulSoup: A Python library used for parsing HTML and XML documents.
Requests: A Python library for sending HTTP requests easily.
markdown
