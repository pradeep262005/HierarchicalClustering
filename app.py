from flask import Flask, render_template, request
from hierarchical import generate_cluster_plots  # importing from hierarchical.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    clusters = int(request.form['clusters'])
    generate_cluster_plots(clusters)
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
