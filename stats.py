import requests
import csv
from bs4 import BeautifulSoup

season = '2020-21'

URL = 'https://www.gazzetta.it/calcio/fantanews/statistiche/serie-a-' + season

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

fields = ['squadra', 'giocatore', 'ruolo', 'q', 'pg', 'g', 'a', 'mm', 'es', 'rt', 'r', 'rs', 'rp', 'mv', 'mm', 'mp']
rows = soup.find('table', class_='playerStats').find('tbody').find_all('tr')

with open(f"./output_{season}.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for row in rows:
        player_data = {
            'squadra': row.find('td', 'field-sqd').find('span', 'hidden-team-name').text,
            'giocatore': row.find('td', 'field-giocatore').find('a').text
        }

        for column in ['ruolo', 'q', 'pg', 'g', 'a', 'mm', 'es', 'rt', 'r', 'rs', 'rp', 'mv', 'mm', 'mp']:
            player_data[column] = row.find('td', 'field-' + column).text.strip()

        writer.writerow(player_data)
