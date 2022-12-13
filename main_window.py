import datetime
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import iterator
import data_weeks
import data_years
import divide_data
import get_data
import parser2


class Application(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()
#margin
    def initUI(self):

        self.setWindowTitle("My program")
        self.resize(600, 600)


        palette = QPalette()
        palette.setColor(QPalette.Background, QColor("yellow"))
        self.setPalette(palette)

        qbtn = QPushButton("&Выход", self)
        qbtn.move(250, 470)
        qbtn.setFixedSize(100,30)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        first_btn = QPushButton("&Разделить исходный файл по файлам X.csv и Y.csv", self)
        first_btn.move(100,5)
        first_btn.setFixedSize(400,30)
        first_btn.clicked.connect(self.start_div_data)

        second_btn = QPushButton("&Разделить исходный файл по годам", self)
        second_btn.move(100, 35)
        second_btn.setFixedSize(400,30)
        second_btn.clicked.connect(self.start_data_to_years)

        third_btn = QPushButton("&Разделить исходный файл по неделям", self)
        third_btn.move(100, 65)
        third_btn.setFixedSize(400,30)
        third_btn.clicked.connect(self.start_data_to_weeks)

        fourth_btn = QPushButton("&Создать исходный файл", self)
        fourth_btn.move(100, 90)
        fourth_btn.setFixedSize(400,30)
        fourth_btn.clicked.connect(self.start_parser)

        fifth_btn = QPushButton("&Найти данные по дате в файлах X.csv и Y.csv", self)
        fifth_btn.move(100, 120)
        fifth_btn.setFixedSize(400,30)
        fifth_btn.clicked.connect(lambda fbtn, choice_flag=1: self.search_dialog(choice_flag))

        six_btn = QPushButton("&Найти данные по дате в датасете разбитом по годам", self)
        six_btn.move(100, 150)
        six_btn.setFixedSize(400,30)
        six_btn.clicked.connect(lambda sbtn, choice_flag=2: self.search_dialog(choice_flag))

        seven_btn = QPushButton("&Найти данные по дате в датасете разбитом по неделям", self)
        seven_btn.move(100, 180)
        seven_btn.setFixedSize(400,30)
        seven_btn.clicked.connect(lambda sebtn, choice_flag=3: self.search_dialog(choice_flag))

        eigth_btn = QPushButton("&Вызвать итератор датасета разбитого на файлы X.csv и Y.csv", self)
        eigth_btn.move(100, 225)
        eigth_btn.setFixedSize(400,30)
        eigth_btn.clicked.connect(self.start_iter_from_x_y)

        nine_btn = QPushButton("&Вызвать итератор датасета разбитого по годам", self)
        nine_btn.move(100, 255)
        nine_btn.setFixedSize(400,30)
        nine_btn.clicked.connect(self.start_iter_from_years)

        ten_btn = QPushButton("&Вызвать итератор датасета разбитого по неделям", self)
        ten_btn.move(100, 285)
        ten_btn.setFixedSize(400,30)
        ten_btn.clicked.connect(self.start_iter_from_weeks)

        eleven_btn = QPushButton("&Вызвать итератор исходного датасета", self)
        eleven_btn.move(100, 315)
        eleven_btn.setFixedSize(400,30)
        eleven_btn.clicked.connect(self.start_iter_from_source)

        self.show()

    def start_iter_from_weeks(self):
        """Iteration from data_to_years output"""

        _msg = QMessageBox()
        _msg.setWindowTitle("Сообщение")
        _msg.setText("Выберите директорию датасета разбитого по неделям")
        _msg.exec_()

        file_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        object = iterator.DateIteratorFromWeeks(file_path)

        self.dialog = QMessageBox()

        self.dialog.addButton("Начать", QMessageBox.AcceptRole)
        self.dialog.addButton("Отмена", QMessageBox.RejectRole)
        self.dialog.setWindowTitle("Итератор")
        self.dialog.exec()

        self.result = QMessageBox()

        while True:

            if self.dialog.clickedButton().text() == "Начать":

                self.result = QMessageBox()
                item = next(object)
                text = "Вывод итератора:" + str(item) + "\nВыберите что сделать"
                self.result.setWindowTitle("Результат итерации")
                self.result.setText(text)
                self.result.addButton("Продолжить", QMessageBox.AcceptRole)
                self.result.addButton("Прекратить итерацию", QMessageBox.RejectRole)
                self.result.exec()

                if self.result.clickedButton().text() == "Прекратить итерацию":
                    break

            elif self.dialog.clickedButton().text() == "Отмена":
                break

    def start_iter_from_years(self):
        """Iteration from data_to_years output"""

        _msg = QMessageBox()
        _msg.setWindowTitle("Сообщение")
        _msg.setText("Выберите директорию датасета разбитого по годам")

        _msg.exec_()

        file_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        object = iterator.DateIteratorFromYears(file_path)

        self.dialog = QMessageBox()

        self.dialog.addButton("Начать", QMessageBox.AcceptRole)
        self.dialog.addButton("Отмена", QMessageBox.RejectRole)
        self.dialog.setWindowTitle("Итератор")
        self.dialog.exec()

        self.result = QMessageBox()

        while True:

            if self.dialog.clickedButton().text() == "Начать":

                self.result = QMessageBox()
                item = next(object)
                text = "Вывод итератора:" + str(item) + "\nВыберите что сделать"
                self.result.setWindowTitle("Результат итерации")
                self.result.setText(text)
                self.result.addButton("Продолжить", QMessageBox.AcceptRole)
                self.result.addButton("Прекратить итерацию", QMessageBox.RejectRole)
                self.result.exec()

                if self.result.clickedButton().text() == "Прекратить итерацию":
                    break

            elif self.dialog.clickedButton().text() == "Отмена":
                break

    def start_iter_from_source(self):
        """Iteration from source file"""

        _msg = QMessageBox()
        _msg.setWindowTitle("Сообщение")
        _msg.setText("Выберите исходный файл, по которому провести итерацию")

        _msg.exec_()

        file_path = QFileDialog.getOpenFileName(self, "Select Folder", filter="*.csv")[0]
        object = iterator.DateIterator(file_path)

        self.dialog = QMessageBox()

        self.dialog.addButton("Начать", QMessageBox.AcceptRole)
        self.dialog.addButton("Отмена", QMessageBox.RejectRole)
        self.dialog.setWindowTitle("Итератор")
        self.dialog.exec()

        self.result = QMessageBox()

        while True:

            if self.dialog.clickedButton().text() == "Начать":

                self.result = QMessageBox()
                item = next(object)
                text = "Вывод итератора:" + str(item) + "\nВыберите что сделать"
                self.result.setWindowTitle("Результат итерации")
                self.result.setText(text)
                self.result.addButton("Продолжить", QMessageBox.AcceptRole)
                self.result.addButton("Прекратить итерацию", QMessageBox.RejectRole)
                self.result.exec()

                if self.result.clickedButton().text() == "Прекратить итерацию":
                    break

            elif self.dialog.clickedButton().text() == "Отмена":
                break

    def start_iter_from_x_y(self):
        """Iteration from X.csv and Y.csv"""

        _msg = QMessageBox()
        _msg.setWindowTitle("Сообщение")
        _msg.setText("Выберите сначала файл X , затем Y")

        _msg.exec_()

        file_path_x = QFileDialog.getOpenFileName(self, "Select Folder", filter="*.csv")[0]
        file_path_y = QFileDialog.getOpenFileName(self, "Select Folder", filter="*.csv")[0]

        object = iterator.DateIteratorFromXY(file_path_x, file_path_y)

        self.dialog = QMessageBox()

        self.dialog.addButton("Начать", QMessageBox.AcceptRole)
        self.dialog.addButton("Отмена", QMessageBox.RejectRole)
        self.dialog.setWindowTitle("Итератор")
        self.dialog.exec()

        self.result = QMessageBox()

        while True:

            if self.dialog.clickedButton().text() == "Начать":

                self.result = QMessageBox()
                item = next(object)
                text = "Вывод итератора:" + str(item) + "\nВыберите что сделать"
                self.result.setWindowTitle("Результат итерации")
                self.result.setText(text)
                self.result.addButton("Продолжить", QMessageBox.AcceptRole)
                self.result.addButton("Прекратить итерацию", QMessageBox.RejectRole)
                self.result.exec()

                if self.result.clickedButton().text() == "Прекратить итерацию":
                    break

            elif self.dialog.clickedButton().text() == "Отмена":
                break

    def search_dialog(self, choice_flag: int):
        """Searching a data for inputed date

        Args:
            choice_flag (int): User's choice
        """

        is_input_correct = False

        while not is_input_correct:

            date, ok = QInputDialog.getText(self, "Ввод", "Введите дату\nНаример: 2008-01-10")

            if ok:

                if self.check_input_date(date):
                    is_input_correct = True

                else:

                    _msg = QMessageBox()
                    _msg.setWindowTitle("Сообщение")
                    _msg.setText("Дата введена некорректно.")
                    _msg.exec_()

                    break

            elif not ok:

                break

        if is_input_correct and choice_flag == 1:

            _msg = QMessageBox()
            _msg.setWindowTitle("Сообщение")
            _msg.setText("Выберите файл X.csv, затем файл Y.csv")

            _msg.exec_()

            file_path_x = QFileDialog.getOpenFileName(self, "Select Folder", filter="*.csv")[0]
            file_path_y = QFileDialog.getOpenFileName(self, "Select Folder", filter="*.csv")[0]

            output = get_data.get_x_y(file_path_x, file_path_y, self.date_formatter(date))

            if output != None:

                done_msg = QMessageBox()
                done_msg.setWindowTitle("Сообщение")
                msg = "Данные к дате " + str(date) + ": " + str(output)
                done_msg.setText(msg)

                done_msg.exec_()

            else:

                done_msg = QMessageBox()
                done_msg.setWindowTitle("Сообщение")
                done_msg.setText("Данные не были найдены!")

                done_msg.exec_()

        elif is_input_correct and choice_flag == 2:

            _msg = QMessageBox()
            _msg.setWindowTitle("Сообщение")
            _msg.setText("Выберите датасет разбитый по годам")

            _msg.exec_()

            file_path = QFileDialog.getExistingDirectory(self, "Select Folder")

            output = get_data.get_y_w(file_path, self.date_formatter(date))

            if output != None:

                done_msg = QMessageBox()
                done_msg.setWindowTitle("Сообщение")
                msg = "Данные к дате " + str(date) + ": " + str(output)
                done_msg.setText(msg)

                done_msg.exec_()

            else:

                done_msg = QMessageBox()
                done_msg.setWindowTitle("Сообщение")
                done_msg.setText("Данные не были найдены!")

                done_msg.exec_()

        elif is_input_correct and choice_flag == 3:

            _msg = QMessageBox()
            _msg.setWindowTitle("Сообщение")
            _msg.setText("Выберите датасет разбитый по неделям")

            _msg.exec_()

            file_path = QFileDialog.getExistingDirectory(self, "Select Folder")

            output = get_data.get_y_w(file_path, self.date_formatter(date))

            if output != None:

                done_msg = QMessageBox()
                done_msg.setWindowTitle("Сообщение")
                msg = "Данные к дате " + str(date) + ": " + str(output)
                done_msg.setText(msg)
                done_msg.exec_()

            else:

                done_msg = QMessageBox()
                done_msg.setWindowTitle("Сообщение")
                done_msg.setText("Данные не были найдены!")
                done_msg.exec_()

    def date_formatter(self, date: str) -> datetime.date:

        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        return datetime.date(year, month, day)

    def check_input_date(self, date: str) -> bool:
        """Checks input date

        Args:
            date (str): Date
        Returns:
            bool: Is input correct or not
        """

        if (
            len(date) == 10
            and date[4] == "-"
            and date[7] == "-"
            and int(date[:4]) > 0
            and int(date[5:7]) > 0
            and int(date[5:7]) <= 12
            and int(date[8:]) > 0
            and int(date[8:]) <= 31
        ):
            return True
        return False

    def start_data_to_weeks(self):
        """Function that reads the csv file"""

        _msg = QMessageBox()
        _msg.setWindowTitle("Сообщение")
        _msg.setText("Выберите исходный файл, затем директорию куда сохранить вывод")
        _msg.exec_()

        file_path = QFileDialog.getOpenFileName(self, "Напишите название файла", filter="*.csv")[0]

        output_directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        if output_directory == "":
            return
        data_weeks.data_to_weeks(file_path, output_directory)

        done_msg = QMessageBox()
        done_msg.setWindowTitle("Сообщение")
        done_msg.setText("Файлы созданы по адресу :"+ str(os.path.join(output_directory, "data_to_weeks_output")))
        done_msg.exec_()

    def start_data_to_years(self):
        """Function that sorts data to different files where each individual file will correspond to one year"""

        _msg = QMessageBox()
        _msg.setWindowTitle("Сообщение")
        _msg.setText("Выберите исходный файл, затем директорию куда сохранить вывод")
        _msg.exec_()

        file_path = QFileDialog.getOpenFileName(self, "Напишите название файла", filter="*.csv")[0]

        output_directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        data_years.data_to_years(file_path, output_directory)

        done_msg = QMessageBox()
        done_msg.setWindowTitle("Сообщение")
        done_msg.setText("Файлы созданы по адресу :" + str(os.path.join(output_directory, "data_to_years_output")) )
        done_msg.exec_()

    def start_div_data(self):
        """Creates X.csv and Y.csv files"""

        _msg = QMessageBox()
        _msg.setWindowTitle("Сообщение")
        _msg.setText("Выберите исходный файл, затем директорию куда сохранить вывод")
        _msg.exec_()

        file_path = QFileDialog.getOpenFileName(self, "Напишите название файла", filter="*.csv")[0]

        output_directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        divide_data.divide_data(file_path, output_directory)

        done_msg = QMessageBox()
        done_msg.setWindowTitle("Сообщение")
        done_msg.setText("Файлы созданы по адресу :"+ str(os.path.join(output_directory, "divide_data_output")))
        done_msg.exec_()

    def start_parser(self):
        """Creates a source file"""

        output_directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        parser2.main_part(output_directory)

        done_msg = QMessageBox()
        done_msg.setWindowTitle("Сообщение")
        done_msg.setText("Исходный файл создан!")
        done_msg.exec_()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = Application()
    sys.exit(app.exec_())