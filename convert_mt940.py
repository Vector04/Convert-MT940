import re


def convert_string(string):
    # Remove any line with a { or }
    string = re.sub(r".*(\{|\}).*(\n|\Z)", "", string)
    # Remove unnessary \n
    string = re.sub(r"\n([^:])", r"\1", string)
    return string


if __name__ == "__main__":
    FILENAME = "Alle_rekeningen_25-02-2022_01-03-2022.940"

    with open(FILENAME, 'r') as f:
        string = f.read()

    string = convert_string(string)

    with open("result.940", "w") as f:
        f.write(string)
