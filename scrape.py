import aiohttp 
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import time

rulings = ["true", "mostly-true", "half-true", "barely-true", "false", "pants-fire"]

ruling_list = []
name_list = []
quote_list = []
desc_list = []

def get_links():
    links = []
    base_url = "https://www.politifact.com/factchecks/list/"
    for ruling in range(0, 6):
        for page in range(1, 101):
            if page == 1:
                links.append(base_url + "?ruling=" + rulings[ruling])
            else:
                links.append(base_url + "?page=" + str(page) + "&ruling=" + rulings[ruling])
    return links

async def get_response(session, url):
    async with session.get(url) as response:
        text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')

        names = soup.find_all('a', class_="m-statement__name")
        quotes = soup.find_all('div', class_="m-statement__quote")
        descs = soup.find_all('div', class_="m-statement__desc")

        for name, quote, desc in zip(names, quotes, descs):
            ruling_list.append(url.split("ruling=")[1])
            name_list.append(name.text.strip())
            quote_list.append(quote.text.strip())
            desc_list.append(desc.text.strip())

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in get_links():
            tasks.append(get_response(session, link))
        await asyncio.gather(*tasks)
    print("Time taken: ", time.time() - start)
    df = pd.DataFrame({
    'ruling': ruling_list,
    'name': name_list,
    'quote': quote_list,
    'description': desc_list,
})
    df.to_csv('politifact.csv')

asyncio.run(main())