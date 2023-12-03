import rich as r

from typing import Literal

type Season = Literal['S'] | Literal['W'] | Literal['F']

def get_medal_count_with_total(data: list[tuple]):
  medals = {}

  for entry in data:
      country, year, medal = entry
      if country not in medals.keys():
          medals[country] = {}

      if not year in medals[country]:
          medals[country][year] = { 'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Total': 0 }

      medals[country][year][medal] += 1
      medals[country][year]['Total'] += 1

  return medals


def get_most_successful_year_medals(medals: dict):
  result = []

  for country, year_medals in medals.items():
    max = 0
    item = []

    for year, medals in year_medals.items():
      if medals['Total'] > max:
        max = medals['Total']
        item = [country, year, medals]
    result.append(item)
    
  return result


def get_least_successful_year_medals(medals: dict):
  result = []

  for country, year_medals in medals.items():
    min = 1000
    item = []

    for year, medals in year_medals.items():
      if medals['Total'] < min:
        min = medals['Total']
        item = [country, year, medals]
    result.append(item)

  return result


def get_first_year_medals(medals: dict):
  result = []

  for country, year_medals in medals.items():
    min_year = 2016
    item = []

    for year, medals in year_medals.items():
      if int(year) < min_year:
        min_year = int(year)
        item = [country, year, medals]
    result.append(item)

  return result

def get_top_medalists(data: list[tuple]):
  medals = {}

  for entry in data:
    name, medal = entry
    if name not in medals.keys():
      medals[name] = { 'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Total': 0 }

    medals[name][medal] += 1
    medals[name]['Total'] += 1

  return medals

def calculate_medal_average(data: list[tuple]):
  average = { 'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Total': 0 }
  years = 0

  for entry in data:
    for key, value in entry[-1].items():
      average[key] += value
      years += 1

  for key, value in average.items():
    average[key] //= years
  
  return average


def print_medals(data: list, season_type: Season):
  season = 'successful' if season_type == 'S'  else 'worst' if season_type =='W' else 'first'

  for entry in data:
    r.print(f'{entry[0]} had their most {season} season in {entry[1]}:\n')

    for key, value in entry[-1].items():
      r.print(f'{key}: {value}\n')

    r.print('-' * 50 + '\n')


def print_top_medalists(medals: dict, n: int):
  print('Most successful medalists are: \n')
    
  for name, medals in sorted(medals.items(), key=lambda player: player[1]['Total'], reverse=True)[:n]:
    r.print(f'{name}:\t{medals['Total']}')