import requests
headers = {'User-Agent': 'LeagueOfLegendsClient',
           'authorization':'Basic cmlvdDpYN2FaZE9kVnppOUhCZ2VqQWROcjJB'}

response = requests.get('https://127.0.0.1:5254/lol-ranked/v1/ranked-stats/3a9e4148-c910-5093-b9f2-f10f96ea2837', headers=headers, verify=False)


print(response.json())