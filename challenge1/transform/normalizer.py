import csv

from transform.errors import MalformedCSVRow, MalformedIndex1Value


def csv_reader(filename):
    with open(filename, "r") as csv_file:
        for row in csv.reader(csv_file):
            yield row


class Normalizer:
    def __init__(self, initial_column, final_column, separator, length_criteria, translator):
        self.initial_column_index = initial_column - 1
        self.final_column_index = final_column - 1
        self.separator = separator
        self.length_criteria = length_criteria
        self.translator = translator

    def transform(self, iterator, has_header):
        for line, row in enumerate(iterator):
            if line == 0 and has_header:
                yield row
                continue

            indexes = _split_index(row, self.initial_column_index, self.final_column_index, self.separator)

            index1 = indexes[0]
            index2 = indexes[1]

            if _should_translate(self.length_criteria, index1, index2):
                index2 = self.translator(index2)

            row[self.initial_column_index] = index1
            row[self.final_column_index] = index2

            yield row


def _should_translate(length_criteria, value1, value2):
    return len(value1) == length_criteria and len(value2) == length_criteria


def _split_index(row, initial_column_index, final_column_index, separator):
    if len(row) < final_column_index:
        raise MalformedCSVRow()

    indexes = row[initial_column_index].split(separator)
    if len(indexes) != 2:
        raise MalformedIndex1Value()

    return indexes
