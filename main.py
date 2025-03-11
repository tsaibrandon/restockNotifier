import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import csv
import json

webhook = DiscordWebhook(url = "https://discord.com/api/webhooks/1348847871323013191/jDtleQt_6NTkCpiHF7vTqkqFXX_abm0orSOPDDwGh_huOBmSAfuSLwr0CjiwCDk2mFAM")

#recurring loop that continously checks
alwaysOn = True
b = 1

while alwaysOn:

    file = open("links.csv", "r")
    reader = csv.reader(file)
    numEntries = len(list(reader))
    file.close

    if b == numEntries:
        b = 1
    
    with open("links.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        link = data[b][0]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    
    try:
        print(link)
        
        r = requests.get(link, headers = headers)

        soup = BeautifulSoup(r.content, "html.parser")

        script_tag = soup.find("script", {"id": "product-schema", "type": "application/ld+json"})

        data = json.loads(script_tag.string)

        inStock = data.get("offers", {}).get("availability", "")
        print(inStock)

        if inStock == "http://schema.org/InStock":
            productName = soup.find("h1", {"class": "heading-4"}).get_text(strip=True)
            print(productName)
            
            price = soup.find("span", {"aria-hidden": "true"}).get_text()
            print(price)

            image = soup.find("img", {"class": "primary-image"}).get("src")
            print(image)

            title = "WALMART RESTOCK"
            des = f"{productName}\n\n__Walmart Link__\n{link}\n\n{price}"
            col = 13400576
            embed = DiscordEmbed(title = title, url = link, description = des, color = col)
            embed.set_image(url = image)
            webhook.add_embed(embed)
            embed.set_footer(text = f"All Thinkgs Arbitrage", icon_url = "")
            response = webhook.execute()
            webhook.remove_embed(0)

    except Exception as e:
        print(f"Error: {e}")
    
    b += 1

    time.sleep(3)
    