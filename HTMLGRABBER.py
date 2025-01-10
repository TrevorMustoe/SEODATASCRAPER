import requests
from bs4 import BeautifulSoup

# add in the url that you would like to scrape to the url below
url = ""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.content
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(html_content, 'html.parser')

                                                      
h1_tags = soup.find_all('h1')
if not h1_tags:
    print("---------------")
    print("No <h1> tags found")
    print("---------------")
    
else:
    print("---------------")
    print("<H1> tags found:")
    print("---------------")
    for h1 in h1_tags:
        print(h1.text)
    print(" ")
        
h2_tags = soup.find_all('h2')
if not h2_tags:
    print("---------------")
    print("No <h2> tags found")
    print("---------------")
    
else:
    print("---------------")
    print("<h2> tags found:")
    print("---------------")
    for h2 in h2_tags:
        print(h2.text)
    print(" ")
        
h3_tags = soup.find_all('h3')
if not h3_tags:
    print("---------------")
    print("No <h3> tags found")
    print("---------------")
    
else:
    print("---------------")
    print("<h3> tags found:")
    print("---------------")
    for h3 in h3_tags:
        print(h3.text)
    print(" ")
    
paragraphs = soup.find_all('p')
if not paragraphs:
    print("---------------")
    print("No <p> tags found")
    print("---------------")
    
else:
    print("---------------")
    print("<p> tags found:")
    print("---------------")
    for paragraph in paragraphs:
        print(paragraph.text)
    print(" ")
    
    
links = soup.find_all("a")

# Extract the href attribute from each anchor tag
print("---------------")
print("<p> tags found:")
print("---------------")
for link in links:
    href = link.get("href")
    if href:
        print(href)


h1_words = set()
for h1 in h1_tags:
    h1_words.update(h1.text.lower().split())  # Convert to lowercase and split into words

# Extract words from <p> tags
paragraphs = soup.find_all('p')
p_words = set()
for paragraph in paragraphs:
    p_words.update(paragraph.text.lower().split())
    
h3_words = set()
for h3 in h3_tags:
    p_words.update(h3.text.lower().split())# Convert to lowercase and split into words

# Find common words
common_words = h1_words.intersection(p_words)
 


if common_words:
    print("Key words from H1 used in paragraph:")
    print(common_words)
else:
  
    print("No common words found between <h1> and <p> tags.")