from pydoc import render_doc
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.line_statement_prefix = "#"

@app.route('/')
def index():
    nums = [1,2,3,4,5,6]
    return render_template('indexjinja.html',nums=nums)

if __name__ == '__main__':
    app.run(debug=True)   