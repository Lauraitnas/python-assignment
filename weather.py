import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string): #SUCCESS
    # """Converts an ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime('%A %d %B %Y')



def convert_f_to_c(temp_in_farenheit): #SUCCESS
    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
    temp_in_farenheit = float(temp_in_farenheit)
    celsius =  (temp_in_farenheit - 32) * 0.5556
    return round(celsius, 1)


def calculate_mean(weather_data): #SUCCESS
    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    for x in range (0, len(weather_data)):
        weather_data[x] = float(weather_data[x]) 
    return sum(weather_data) / len(weather_data)


def load_data_from_csv(csv_file): #SUCCESS
    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    list = []
    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if line:
                list.append([line[0], int(line[1]), int(line[2])])
    return list


def find_min(weather_data): #SUCCESS
    # """Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minimum value and it's position in the list.
    # """
    weather_data = [float(x) for x in weather_data]
    if (weather_data):    
        multiple = [i for i, x in enumerate(weather_data) if x == min(weather_data)] 
        return min(weather_data), multiple[-1]
    return ()


def find_max(weather_data): #SUCCESS
    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """
    weather_data = [float(x) for x in weather_data]
    if (weather_data):    
        multiple = [i for i, x in enumerate(weather_data) if x == max(weather_data)] 
        return max(weather_data), multiple[-1]
    return ()


def generate_summary(weather_data): #SUCCESS
    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    list_of_dates = [convert_date(x[0]) for x in weather_data]
    
    list_of_mins = [convert_f_to_c(x[1]) for x in weather_data]
    min_t,  min_idx = find_min(list_of_mins)
    min_average = sum(list_of_mins) / len(list_of_mins)
    min_average = round(min_average, 1)
    
    list_of_max = [convert_f_to_c(x[2]) for x in weather_data]
    max_t, max_idx = find_max(list_of_max)
    max_average = sum(list_of_max) / len(list_of_max)
    max_average = round(max_average, 1)

    min_idx = list_of_mins.index(min_t)
    date_1 = list_of_dates[min_idx]

    max_idx = list_of_max.index(max_t)
    date_2 = list_of_dates[max_idx]
    
    overview = len(weather_data)
    
    return f"""{overview} Day Overview
  The lowest temperature will be {min_t}°C, and will occur on {date_1}.
  The highest temperature will be {max_t}°C, and will occur on {date_2}.
  The average low this week is {min_average}°C.
  The average high this week is {max_average}°C.
"""


def generate_daily_summary(weather_data): #SUCCESS
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    overview = []

    for x in weather_data:
        date = convert_date(x[0])
        min = convert_f_to_c(x[1])
        max = convert_f_to_c(x[2])
        overview.append(f"""---- {date} ----
  Minimum Temperature: {min}°C
  Maximum Temperature: {max}°C

""")
    # print(overview)

    return_str = ''
    for item in overview:
        return_str = return_str+item
    return(return_str)