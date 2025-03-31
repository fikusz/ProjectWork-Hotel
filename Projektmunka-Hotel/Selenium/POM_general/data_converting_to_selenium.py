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

        data_dict = {}
        for header in headers:
            data_dict[header] = []

        for row in csv_reader:
            for i, value in enumerate(row):
                data_dict[headers[i]].append(value)

        result = {}
        for key, values in data_dict.items():
            result[key] = list(values)

    return result

def get_register_data():
    data = []
    filename = Path(__file__).resolve().parents[2] / "Selenium" / "Test_Data" / "registered_users.csv"

    with filename.open("r", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        data = list(csv_reader)
        cleaned_register_data = []

        for sublist in data:
            filtered_sublist = []
            for item in sublist:
                if item:
                    filtered_sublist.append(item)
            cleaned_register_data.append(filtered_sublist)
        cleaned_register_data.pop(0)
        cleaned_register_data.pop(-1)
        return cleaned_register_data




