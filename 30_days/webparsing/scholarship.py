import requests
from bs4 import BeautifulSoup

# Define websites to search (replace with your target URLs)
websites = ["https://myresume.perfectbluesprings.co.ke"]
keywords = ["Cyber", "Kennedy Waweru", "Freelance", "if"]  # List of keywords to find

# Loop through each website
for website in websites:
  try:
    # Send request and get HTML content
    response = requests.get(website)
    response.raise_for_status()  # Raise exception for bad status codes

    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links
    links = []
    for link in soup.find_all('a'):
      # Extract URL from href attribute
      url = link.get('href')
      if url:
        links.append(url)

    # Check for links containing keywords
    matching_links = [link for link in links if any(keyword in link for keyword in keywords)]
    
    # Print results for this website
    if matching_links:
      print(f"Website: {website}")
      for link in matching_links:
        print(f"\t- {link}")
    else:
      print(f"Website: {website} - No matches found.")

  except requests.exceptions.RequestException as e:
    print(f"Error: {website} - {e}")