import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_website(url, htmltag):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and extract relevant information (adjust according to your website's structure)
        articles = soup.find_all(attrs=htmltag)  # Replace 'article' with the appropriate HTML tag

        # Create a string to store the extracted information
        content = ""

        for article in articles:
            # Extract and append the text content to the string
            article_text = article.get_text(strip=True)
            content += article_text + '\n'

        # Return the scraped content
        return content

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
