import requests
from bs4 import BeautifulSoup
import sqlite3

# Create a SQLite database
conn = sqlite3.connect('web_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS articles
             (title TEXT, link TEXT)''')

# Scrape data from a website
url = 'https://news.ycombinator.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', class_='storylink')

    for article in articles:
        title = article.text
        link = article['href']
        c.execute("INSERT INTO articles (title, link) VALUES (?, ?)", (title, link))
        print(f"Inserted: {title}")

    conn.commit()
else:
    print("Failed to retrieve the webpage")

# Query the database
c.execute("SELECT * FROM articles")
rows = c.fetchall()
print("\nStored Articles:")
for row in rows:
    print(row)

# Close the database connection
conn.close()
