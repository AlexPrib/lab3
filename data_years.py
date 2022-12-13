import csv
import os


def name_for_file(first_part: str, second_part: str) -> str:
    """Creates a name for file

    Args:
        first_part (str): First part of future file's name
        second_part (str): Second part of future file's name
    Returns:
        str: Name in special format
    """
    f_p = first_part.replace('-', '') + '_'
    s_p = second_part.replace('-', '') + '.csv'
    return os.path.join('data_to_years_output', f_p + s_p)


def get_year_from_data(data: list[list[str]], index: int) -> int:
    """Gets the year from csv file

    Args:
        data (list[list[str]]): A list with dates and data
        index (int): The index of the string that points on list in the list

    Returns:
        int: Value of year
    """
    date = data[index][0]
    year = ''
    for numbers in date:

        if numbers != '-':
            year += numbers

        else:
            break

    return int(year)


def data_to_years(file_name: str, output_directory: str) -> None:
    """Function that sorts data to different files where each individual file will correspond to one year

    Args:
        file_name (str): Path to file

    Raises:
        TypeError: No such file exists
    """

    if os.path.exists(file_name):

        if not os.path.exists(os.path.join(output_directory, 'data_to_years_output')):
            os.mkdir(os.path.join(output_directory, 'data_to_years_output'))
            

        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader_object = list(csv.reader(csvfile, delimiter=","))

            output = []
            first_part_of_name = ''
            second_part_of_name = ''
            is_first = True
            current_year = get_year_from_data(reader_object, 0)
            last_year = get_year_from_data(
                reader_object, len(reader_object) - 1)

            for i in range(len(reader_object)):

                if current_year < last_year:

                    if get_year_from_data(reader_object, i) == current_year:
                        if is_first:
                            first_part_of_name = reader_object[i][0]

                        is_first = False
                        output.append(reader_object[i])
                        second_part_of_name = reader_object[i][0]

                    elif get_year_from_data(reader_object, i) != current_year:
                        with open(os.path.join(output_directory, name_for_file(first_part_of_name, second_part_of_name)), 'w', encoding='utf-8') as csv_file:
                            writer = csv.writer(
                                csv_file, lineterminator='\n')
                            current_year += get_year_from_data(
                                reader_object, i) - get_year_from_data(output, 0)
                            for j in output:
                                writer.writerow((j))
                            output = []

                            first_part_of_name = reader_object[i][0]
                            output.append(reader_object[i])

                elif current_year == last_year:

                    output.append(reader_object[i])
                    second_part_of_name = reader_object[i][0]

                    if i + 1 == len(reader_object):
                        with open(os.path.join(output_directory, name_for_file(first_part_of_name, second_part_of_name)), 'w', encoding='utf-8') as csv_file:
                            writer = csv.writer(
                                csv_file, lineterminator='\n')
                            for j in output:
                                writer.writerow((j))

    else:
        raise FileNotFoundError

