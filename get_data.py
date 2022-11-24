import csv
import datetime
import os


def get_x_y(file_name_x: str, file_name_y: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from X.csv and Y.csv files

    Args:
        file_name_x: Path to file that contains dates
        file_name_y: Path to file that contains data
        date: The date for which you want to find weather data

    Raises:
        FileNotFoundError: One or both of the files are missing

    Returns:
        returns list if data for the date was found, or returns None on failure
    """

    if os.path.exists(file_name_x) and os.path.exists(file_name_y):

        with open(file_name_x, 'r', encoding='utf-8') as x:
            dates = list(csv.reader(x, delimiter=","))
            index = -1

            for i in range(len(dates)):
                if dates[i][0] == str(date):
                    index = i
                    break

        with open(file_name_y, 'r', encoding='utf-8') as y:
            data = list(csv.reader(y, delimiter=","))

            if index >= 0:
                return data[index]

            elif index == -1:
                return None

    raise FileNotFoundError


def get_y_w(folder_name: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from csv files that contains data 

    Args:
        folder_name_years: Path to folder that contains .csv files
        date: The date for which you want to find weather data

    Raises:
        FileNotFoundError: Folder with .csv files is missing

    Returns:
        returns list if data for the date was found, or returns None on failure
    """

    if os.path.exists(folder_name):
        index = -1

        for root, dirs, files in os.walk(folder_name):
            for file in files:

                with open(os.path.join(folder_name, file), 'r', encoding='utf-8') as csvfile:
                    dates = list(csv.reader(csvfile, delimiter=","))

                    for i in range(len(dates)):

                        if dates[i][0] == str(date):
                            index = i
                            break

                    if index >= 0:
                        return dates[i][1:]

        if index == -1:
            return None

        else:
            raise FileNotFoundError


def get_data(file_name: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from csv file
    Args:
        file_name: Path to file that contains weather data about dates
        date: The date for which you want to find weather data

    Raises:
        FileNotFoundError: .csv file is missing

    Returns:
        returns list if data for the date was found, or returns None on failure
    """

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as csvfile:

            reader_object = list(csv.reader(csvfile, delimiter=","))

            for i in range(len(reader_object)):

                if reader_object[i][0] == str(date):
                    return reader_object[i][1:]

    else:
        raise FileNotFoundError


class DateIterator:

    def __init__(self):
        self.counter = 0
        self.file_name = 'dataset.csv'

    def __next__(self) -> tuple:
        
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as csvfile:
                reader_object = list(csv.reader(csvfile, delimiter=","))

                if self.counter == len(reader_object):
                    raise StopIteration

                elif self.counter < len(reader_object):
                    self.counter += 1
                    output = (
                    reader_object[self.counter - 1][0], 
                    reader_object[self.counter - 1][1], 
                    reader_object[self.counter - 1][2],
                    reader_object[self.counter - 1][3], 
                    reader_object[self.counter - 1][4],
                    reader_object[self.counter - 1][5], 
                    reader_object[self.counter - 1][6]
                    )
                    return output
        else:
            raise FileNotFoundError