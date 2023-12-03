from re import match

def is_country_valid(country: str):
  countries: set[str] = set()

  with open('./src/data/data_source.tsv') as file:
    file.readline()

    for line in file:
      line = line.rstrip('\n').split('\t')
      countries.add(line[7])
      
  return country in countries


def is_output_file_valid(filename: str):
  regex = r'^[A-Za-z0-9]+\.txt$'

  return bool(match(regex, filename))


def is_age_range_valid(age_range: str | None):
  return age_range is not None and all(10 <= int(age) <= 90 for age in age_range.split('-'))


def is_year_valid(year: int | None):
  return year is not None and 1896 <= year <= 2016