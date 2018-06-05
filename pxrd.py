"""Dwccwscw."""
import re


def read_pxrd(file):
    """Wow this is awesome."""
    data = []
    with open(file) as my_file:
        for row in my_file:
            if not re.search('[a-zA-Z]', row):
                data.append(','.join(row.strip().split(' ')))
    return data


data = read_pxrd('UiO_66.DAT')
data = '\n'.join(data)

with open('output.csv', 'w') as my_file:
        my_file.write(str(data))
