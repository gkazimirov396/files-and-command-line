# Small CMD Program
---
## This application retrieves data, according to the commands you enter, from the database of every single olympics game up to 2016.

---

## Required Dependencies
### In order for the apllication to properly function, it requires you to install, locally, the following modules:
1. rich. `pip install rich`

## Available Commands

In the project directory, you can run:

### `medals`

This command will process the database, outputting information about the top ten medalists from the selected country for the given year, as well as the total number of medals for each type.

It takes two arguments:
1. country name. Has to be 3 charachters long and uppercase, for example, USA (United States), CHN (China), e.t.c.
2. year. Has to be a postive integer between 1896 and 2016

Usage Example:
#### `python src/main.py medals USA 1988`

### `total`

This command will process the database, and display information about all countries that won medals at the Olympics of the specified year. This information will include the total number of gold, silver and bronze medals for each country.

It takes one argument:
1. year. Has to be a postive integer between 1896 and 2016

Usage Example:
#### `python src/main.py total 1988`

### `overall`

This command will process the database, and output the year in which each of the specified countries won the most medals and indicate that number of medals.

It takes a list of arguments:
1. countries. Has to be a least of trings, each 3 charachters long and uppercase, for example, USA (United States), CHN (China), e.t.c.

Usage Example:
#### `python src/main.py overall USA CHN RUS`

### `interactive`

After typing this command, the program switches to interactive mode. In this mode, you can enter the names of countries, and the program provides detailed statistics for each of the entered countries. This includes information on a country's first appearance at the Olympics, its most successful Olympiad by number of medals, its least successful, and the average number of medals of each type at each Olympiad. To quit the interactive mode, simply enter "q".

Once you enter the interactive mode, the program will take one argument:
1. country name. Has to be 3 charachters long, for example, USA (United States), CHN (China), e.t.c. Lowercase values are alllowed for this one.

Usage Example:
#### `python src/main.py interactive`
#### `Enter a country or type "q" to quit: USA`

### `top`

This command will process the database, and output the year in which each of the specified countries won the most medals and indicate that number of medals.

It takes three arguments:
1. -n. Has to be a postive integer greater than 0. Serves as a quantity of the medalists you would like to output.
2. -s or --sex. Is either "M" (for male), or "F" (for female). Serves as an additional filter for the medalists.
3. -a or --age. It is an age range, for example, "19-45". Serves as yet another filter for the medalists. 

Usage Example:
#### `python src/main.py top -n 5 -s F -a 19-32`

## Each of these commands takes an additional optional argument:
`--output` or `-o`
It has to be the name of the text file, with the `.txt` extension, to which the program will output a log object.

Usage Example:
#### `python src/main.py medals CHN 2006 --output log.txt`