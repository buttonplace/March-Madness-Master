import json, requests, re
from bs4 import BeautifulSoup

url = 'https://www.sports-reference.com/cbb/postseason/2019-ncaa.html'
brackets = requests.get(url)
teams = brackets.content
stats = ['g', 'mp', 'fg', 'fga', 'fg_pct', 'fg2', 'fg2a', 'fg2_pct', 'fg3',
    'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb',
    'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'pts_per_g']
soup = BeautifulSoup(teams, 'html.parser')
team_names = []
team_links = []
schools = soup.find_all(href=re.compile("/cbb/schools/"))
team_dictionary = {}
stats_dictionary = {}
print('Getting Team Names')
for school in schools:
    team_name = school.text
    team_link = school['href']
    if team_link[-9:] == '2019.html':
        team_link = team_link[:-9]
    if team_link[-5:] != '.html':
        team_names.append(team_name)
        team_links.append('https://www.sports-reference.com' + team_link + '2019.html')
team_names = team_names[5:-6]
team_links = team_links[5:-6]
print('Linking Teams')
for i in range(0, len(team_names)):
    team_dictionary[team_names[i]] = team_links[i]
print('Getting Team Stats')
for team in team_names:
    print(team)
    url = team_dictionary[team]
    req = requests.get(url)
    team_page = req.content
    soup = BeautifulSoup(team_page, 'html.parser')
    team_stat_dictionary = {}
    opp_stat_dictionary = {}
    for stat in stats:
        table1 = soup.findAll('td', {'data-stat': stat, 'class': 'right'})[0]
        if stat == 'g' or stat == 'mp':
            table2 = soup.findAll('td', {'data-stat': stat, 'class': 'right'})[2]
        else:
            table2 = soup.findAll('td', {'data-stat': 'opp_' + stat, 'class': 'right'})[0]
        stat_value1 = table1.text
        stat_value2 = table2.text
        team_stat_dictionary[stat] = stat_value1
        opp_stat_dictionary[stat] = stat_value2
    stats_dictionary[team] = {}
    stats_dictionary[team]['Team'] = team_stat_dictionary
    stats_dictionary[team]['Opponent'] = opp_stat_dictionary
print('Exporting JSON')
with open('stats.json', 'w') as stats:
    json.dump(stats_dictionary, stats)
seeds = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]
seeded_dictionary = {}
seeded_dictionary['East'] = {}
seeded_dictionary['West'] = {}
seeded_dictionary['Midwest'] = {}
seeded_dictionary['South'] = {}
first_four = {'North Carolina Central', 'North Dakota State', 'Temple',
              'Belmont', 'Fairleigh Dickinson', 'Prairie View', 'St. John\'s (NY)', 'Arizona State'}
seed_count = 0
print('Building Seeded Dictionary')
for team in stats_dictionary:
    if team not in first_four:
        if seed_count < 16:
            if seed_count != 1 and seed_count !=9:
                seeded_dictionary['East'][seeds[seed_count]] = stats_dictionary[team]
                seeded_dictionary['East'][seeds[seed_count]]['Name'] = team
            elif seed_count == 1:
                seeded_dictionary['East'][16] = stats_dictionary['North Dakota State']
                seeded_dictionary['East'][16]['Name'] = 'North Dakota State'
                seed_count+=1
                seeded_dictionary['East'][seeds[seed_count]] = stats_dictionary[team]
                seeded_dictionary['East'][seeds[seed_count]]['Name'] = team
            elif seed_count == 9:
                seeded_dictionary['East'][11] = stats_dictionary['Belmont']
                seeded_dictionary['East'][11]['Name'] = 'Belmont'
                seed_count += 1
                seeded_dictionary['East'][seeds[seed_count]] = stats_dictionary[team]
                seeded_dictionary['East'][seeds[seed_count]]['Name'] = team
        elif seed_count < 32:
            if seed_count != 25 and seed_count != 17:
                seeded_dictionary['West'][seeds[seed_count % 16]] = stats_dictionary[team]
                seeded_dictionary['West'][seeds[seed_count % 16]]['Name'] = team
            elif seed_count == 25:
                seeded_dictionary['West'][11] = stats_dictionary['Arizona State']
                seeded_dictionary['West'][11]['Name'] = 'Arizona State'
                seed_count += 1
                seeded_dictionary['West'][seeds[seed_count % 16]] = stats_dictionary[team]
                seeded_dictionary['West'][seeds[seed_count % 16]]['Name'] = team
            elif seed_count == 17:
                seeded_dictionary['West'][16] = stats_dictionary['Fairleigh Dickinson']
                seeded_dictionary['West'][16]['Name'] = 'Fairleigh Dickinson'
                seed_count += 1
                seeded_dictionary['West'][seeds[seed_count % 16]] = stats_dictionary[team]
                seeded_dictionary['West'][seeds[seed_count % 16]]['Name'] = team
        elif seed_count < 48:
            seeded_dictionary['Midwest'][seeds[seed_count % 16]] = stats_dictionary[team]
            seeded_dictionary['Midwest'][seeds[seed_count % 16]]['Name'] = team
        elif seed_count < 64:
            seeded_dictionary['South'][seeds[seed_count % 16]] = stats_dictionary[team]
            seeded_dictionary['South'][seeds[seed_count % 16]]['Name'] = team
        seed_count+=1
print('Exporting JSON')
with open('seeded.json', 'w') as seeded:
    json.dump(seeded_dictionary, seeded)
print('Complete')