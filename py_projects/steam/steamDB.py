import requests
from bs4 import BeautifulSoup

url = "https://steamdb.info/stats/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    games_table = soup.find('table', {'class': 'table-stats'})
    if games_table:
        games = games_table.find_all('tr')[1:]  # Saltar el encabezado de la tabla
        for game in games:
            columns = game.find_all('td')
            if columns:
                name = columns[1].text.strip()  # Nombre del juego
                current_players = columns[2].text.strip()  # Jugadores actuales
                peak_players = columns[3].text.strip()  # Máximo de jugadores
                print(f"Juego: {name}, Jugadores Actuales: {current_players}, Pico de Jugadores: {peak_players}")
else:
    print(f"Error al acceder a SteamDB: {response.status_code}")
