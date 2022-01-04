import csv

from reverse_complement import translate
from transform.normalizer import Normalizer


def main():
    normalizer = Normalizer(initial_column=5, final_column=6, separator="+", length_criteria=10, translator=translate)

    with open("SampleSheetS2.csv", "r") as input_csv:
        csv_reader = csv.reader(input_csv, delimiter=',')
        with open("NewSampleSheet.csv", "w", newline='') as output_csv:
            csv_writer = csv.writer(output_csv, delimiter=',')
            for row in normalizer.transform(csv_reader, has_header=True):
                csv_writer.writerow(row)


if __name__ == "__main__":
    main()
