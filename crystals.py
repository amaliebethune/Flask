"""basic Flask app - demo of using a variable in a route"""
from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries
    """
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts

crystal_list = convert_to_dict('crystals.csv')






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crystal/<num>')
def crystal(num):
    stone = crystal_list[int(num)-1]
    return render_template('crystal.html', stone=stone)



if __name__ == '__main__':
    app.run(debug=True)
