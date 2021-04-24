from bs4 import BeautifulSoup
import requests
# Program made by Yuki Matso ;)
print("\nWelcome to the Corona Virus News\n")
source = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(source, 'lxml')
print("".join(div.text for div in soup.find_all('div', id='maincounter-wrap')))
while True :
    country = input("To search about your country stats just type it name below, to quit please type ""exit""\n")
    if country == "exit" :
        print("Thanks for using our program.")
        break
    else:
        pass
    country_url = f"https://www.worldometers.info/coronavirus/country/{country}"
    source_2 = requests.get(country_url).text
    soup_2 = BeautifulSoup(source_2, 'lxml')
    print("".join(div.text for div in soup_2.find_all('div', id='maincounter-wrap')))
