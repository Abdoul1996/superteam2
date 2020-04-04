from os import path
import csv
import json
import random

# Our dataset was created from http://www2.informatik.uni-freiburg.de/~cziegler/BX/ and reduced down to 1,000 records
# The CSV file has semicolon delimiters due to book titles containing commas

SCRIPT_DIR = path.dirname(path.realpath(__file__)) + '/'
DB_FILE = SCRIPT_DIR + 'cscl_db.csv'
OUTPUT_FILE = SCRIPT_DIR + 'cscl_db.json'

# Original headers: "ISBN";"Book-Title";"Book-Author";"Year-Of-Publication";"Publisher";"Image-URL-S";"Image-URL-M";"Image-URL-L"
with open(DB_FILE, 'r') as file:
    reader = csv.DictReader(file,
                            delimiter=';',
                            fieldnames=[
                                'isbn', 'title', 'author', 'publication_year',
                                'publisher', 'image_url_s', 'image_url_m',
                                'image_url_l'
                            ])
    with open(OUTPUT_FILE, 'w') as o_file:
        for line in reader:
            copies = random.randrange(1,10)
            available = random.randrange(0,copies)

            line['copies'] = copies
            line['available'] = available
            
            # Convert publication_year from string to int
            line['publication_year'] = int(line['publication_year'])

            json.dump(line, o_file)
            o_file.write('\n')

print(
    '\n----------\nFinished converting {} from CSV to JSON.\nFile can be found at {}'
    .format(DB_FILE, OUTPUT_FILE))
