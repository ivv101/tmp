from flask import Flask, render_template

app = Flask(__name__)

def calculate_max_widths(columns):
    # Calculate the maximum length of string in each column
    return [max(len(str(item)) for item in column) for column in columns]

@app.route('/')
def home():
    # Your example lists
    list1 = [f"Item {i}" for i in range(1, 11)]
    list2 = [f"Item {i}" for i in range(1, 16)]
    list3 = [f"Item {i}" for i in range(1, 3)]
    list4 = [f"Item {i}" for i in range(1, 9)]

    columns = [list1, list2, list3, list4]
    max_widths = calculate_max_widths(columns)

    return render_template('columns.html', columns=columns, max_widths=max_widths, zip=zip)

