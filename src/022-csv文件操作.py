import csv
from pathlib import Path

csv_path = Path(__file__).parent.joinpath("data.csv")
print(csv_path)


def write_csv():
    csv_file = csv_path.open("w", encoding="UTF-8")
    csv_writer = csv.DictWriter(csv_file, ["name", "age"])
    csv_writer.writeheader()
    csv_writer.writerow({"name": "liu", "age": 20})
    csv_writer.writerow({"name": "zhang", "age": 19})
    csv_file.close()


def red_csv():
    csv_file = csv_path.open("r", encoding="UTF-8")
    csv_reader = csv.DictReader(csv_file)
    for item in csv_reader:
        print(item)
    csv_file.close()


if __name__ == "__main__":
    red_csv()
