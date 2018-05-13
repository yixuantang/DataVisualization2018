from flask import Flask, Response
# from analysis import loadData, createChart

# data = loadData()
app = Flask(__name__, static_url_path='', static_folder='.')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port='5007',host='0.0.0.0')