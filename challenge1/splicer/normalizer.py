import csv
import string


def csv_reader(filename):
    with open(filename, "r") as csv_file:
        for row in csv.reader(csv_file):
            yield row


class Normalizer:
    def __init__(self, initial_column, final_column, separator, length_criteria, translator):
        self.initial_column_index = initial_column
        self.final_column_index = final_column
        self.separator = separator
        self.length_criteria = length_criteria
        self.translator = translator

    def transform(self, iterator):
        for row in iterator:
            if len(row) < self.final_column_index - 1:
                raise "malformedCSVRow"

            indexes = row[self.initial_column_index].split(self.separator)
            if len(indexes) != 2:
                raise "malformedIndex1Value"

            index1 = indexes[0]
            index2 = indexes[1]

            if len(index1) == self.length_criteria and len(index2) == self.length_criteria:
                index2 = self.translator(index2)

            row[self.initial_column_index] = index1
            row[self.final_column_index] = index2

            yield row
