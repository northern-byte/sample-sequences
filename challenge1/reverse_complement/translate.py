translation_map = "".maketrans({"A": "T", "C": "G", "G": "C", "T": "A"})


def translate(value):
    return value[::-1].translate(translation_map)
