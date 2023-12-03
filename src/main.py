import rich as r
from argparse import ArgumentParser

from utils.medals import calculate_medal_average, get_first_year_medals, get_least_successful_year_medals, get_medal_count_with_total, get_most_successful_year_medals, get_top_medalists, print_medals, print_top_medalists 
from utils.validation import is_age_range_valid, is_country_valid, is_year_valid
from utils.helpers import output_file

from utils.command_types import CommandTypes

parser = ArgumentParser()

command_parser = parser.add_subparsers(title='command', dest='command')

medals_parser = command_parser.add_parser(CommandTypes.Medals)
total_parser = command_parser.add_parser(CommandTypes.Total)
overall_parser = command_parser.add_parser(CommandTypes.Overall)
interactive_parser = command_parser.add_parser(CommandTypes.Interactive)
top_parser = command_parser.add_parser(CommandTypes.Top)

medals_parser.add_argument('country')
medals_parser.add_argument('year', type=int)
medals_parser.add_argument('-o', '--output')

total_parser.add_argument('year', type=int)
total_parser.add_argument('-o', '--output')

overall_parser.add_argument('countries', nargs='+')
overall_parser.add_argument('-o', '--output')

interactive_parser.add_argument('-o', '--output')

top_parser.add_argument('-n', type=int)
top_parser.add_argument('-s', '--sex', choices=['M', 'F'])
top_parser.add_argument('-a', '--age')
top_parser.add_argument('-o', '--output')

cmd_args = parser.parse_args()
print(cmd_args)

match cmd_args.command:
  case CommandTypes.Medals:
    country = cmd_args.country
    year = cmd_args.year

    if not is_country_valid(country) or not is_year_valid(year):
      raise ValueError('Invalid value for country or year!')

    with open('./src/data/data_source.tsv') as file:
      file.readline()

      medals =  { 'Gold': 0, 'Silver': 0, 'Bronze': 0 }
      result = []

      currentCount = 0
      LIMIT = 10

      for line in file:
        line = line.rstrip('\n').split('\t')

        if line[7] == country and int(line[9]) == year and line[-1] != 'NA':
          if currentCount < LIMIT:
            result.append(f'{line[1]}-{line[12]}-{line[-1]}')

          medals[line[-1]] += 1
          currentCount += 1

      if len(result) < 10:
        print('The specified country has less than 10 medalists in the specified year.')
        exit(1)

      r.print(result)
      r.print(medals)

      if cmd_args.output:
        output_file(cmd_args)
  case CommandTypes.Total:
    year = cmd_args.year
    result = []
    teams = {}

    if not is_year_valid(year):
      raise ValueError('Invalid value for total!')
    
    with open('./src/data/data_source.tsv') as file:
      file.readline()

      for line in file:
        line = line.rstrip('\n').split('\t')

        if int(line[9]) == year and line[-1] != 'NA':
          if line[7] not in teams.keys():
            teams[line[7]] = { 'Gold': 0, 'Silver': 0, 'Bronze': 0 }
            
          teams[line[7]][line[-1]] += 1

    for country, medals in teams.items():
      result.append(f'{country}-{medals['Gold']}-{medals['Silver']}-{medals['Bronze']}')

    r.print(result)

    if cmd_args.output:
        output_file(cmd_args)
  case CommandTypes.Overall:
    countries = cmd_args.countries
    data = []

    if any(not is_country_valid(country) for country in countries):
      raise ValueError('One of the countries you entered, does not exist!')

    with open('./src/data/data_source.tsv') as file:
      file.readline()

      for line in file:
        line = line.rstrip('\n').split('\t')

        for country in countries:
          if line[7] == country and line[-1] != 'NA':
            data.append((line[7], line[9], line[-1]))

    overall_medals = get_medal_count_with_total(data)

    result = get_most_successful_year_medals(overall_medals)

    print_medals(result, 'S')

    if cmd_args.output:
        output_file(cmd_args)
  case CommandTypes.Interactive:
    data = []

    while True:
      country = input('Enter a country or type "q" to quit: ').upper()
      if len(country) != 3:
        break

      if not is_country_valid(country):
        print('Country is invalid! Please choose again!')
        print('\n')
        continue

      with open('./src/data/data_source.tsv') as file:
        file.readline()

        for line in file:
          line = line.rstrip('\n').split('\t')

          if line[7] == country and line[-1] != 'NA':
            data.append((line[7], line[9], line[-1]))
        
        interactive_medals = get_medal_count_with_total(data)

        successful_year = get_most_successful_year_medals(interactive_medals)
        worst_year = get_least_successful_year_medals(interactive_medals)
        first_year = get_first_year_medals(interactive_medals)

        print_medals(successful_year, 'S')
        print_medals(worst_year, 'W')
        print_medals(first_year, 'F')

        average = calculate_medal_average(successful_year)

        r.print('Average: \n', average, '-' * 50 + '\n')

        if cmd_args.output:
          output_file(cmd_args)
  case CommandTypes.Top:
    data = []
    n = cmd_args.n
    sex = cmd_args.sex
    age = cmd_args.age

    if n <= 0 or isinstance(n, float):
      raise ValueError('Invalid value! N can only be a positive integer, greater than 0!')
    
    if not is_age_range_valid(age):
      raise ValueError('Invalid value! Age can only be in range 10-90!')

    with open('./src/data/data_source.tsv') as file:
      file.readline()

      for line in file:
        line = line.rstrip('\n').split('\t')

        if line[2] == sex and line[3] != 'NA' and int(age.split('-')[0]) <= int(line[3]) <= int(age.split('-')[1]) and line[-1] != 'NA':
          data.append((line[1], line[-1]))

    top_medalists = get_top_medalists(data)

    print_top_medalists(top_medalists, n)

    if cmd_args.output:
      output_file(cmd_args)
  case _:
    print('Invalid command!')
    exit(1)