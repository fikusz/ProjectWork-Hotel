from pathlib import Path
import csv

def get_string_of_doom():
    filename = Path(__file__).resolve().parents[2] / "Selenium" / "Test_Data" / "a_string_test.txt"
    with filename.open("r", encoding="utf-8") as file:
        content = file.read().split("\n")

    return content

def get_automated_logins():
    data = {}
    filename = Path(__file__).resolve().parents[2] / "Selenium" / "Test_Data" / "registered_users.csv"

    with filename.open("r", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        headers = next(csv_reader)
        data_dict = {header:[] for header in headers}

        for row in csv_reader:
            for i, value in enumerate(row):
                data_dict[headers[i]].append(value)
    return {key: list(values) for key, values in data_dict.items()}

def get_register_data():
    data = {}
    filename = Path(__file__).resolve().parents[2] / "Selenium" / "Test_Data" / "registered_users.csv"

    with filename.open("r", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')

print(get_automated_logins())





