import requests
headers = {'User-Agent': 'LeagueOfLegendsClient',
           'authorization':'Basic cmlvdDpkWEtMMVZ2Q0RzYWRkV1lrdWVfOURB'}

response = requests.get('https://127.0.0.1:6477/lol-champ-select/v1/session', headers=headers, verify=False)


print(response.json())