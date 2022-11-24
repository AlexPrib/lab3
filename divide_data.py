import csv
import os


def divide_data(file_name: str, output_dir: str) -> None:
    """Function that divides date and data to different csv files
    Args:
        file_name: Path to file
    Raises:
        TypeError: No such file exists
    """

    if os.path.exists(file_name):
        
        if not os.path.exists(os.path.join(output_dir,'divide_output')):
            os.mkdir(os.path.join(output_dir,'divide_output'))

        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader_obj = list(csv.reader(csvfile, delimiter=","))
            with open(os.path.join(output_dir, 'divide_output', 'X.csv'), 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for elements in reader_obj:
                    writer = csv.writer(csvfile, lineterminator='\n')
                    writer.writerow([str(elements[0])])
            with open(os.path.join(output_dir, 'divide_output', 'Y.csv'), 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for elements in reader_obj:
                    writer = csv.writer(csvfile, lineterminator='\n')
                    writer.writerow((
                        elements[1], 
                        elements[2], 
                        elements[3], 
                        elements[4], 
                        elements[5], 
                        elements[6]))
    else:
        raise FileNotFoundError


if __name__ == '__main__':
    try:
        file_name = 'dataset.csv'
        divide_data(file_name)

    except FileNotFoundError:
        print('No such file exists!')
