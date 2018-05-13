from flask import Flask, Response, render_template,url_for, flash, jsonify
# from setting import host, database, user, password, Gentrifying, Non_Gentrifying, Higher_Income, cur
import pandas as pd
import urllib, json
import urllib3

app = Flask(__name__)

# url = "https://raw.githubusercontent.com/davidhhk1994/Data-Visualization/master/final_project/New_Dataset/education_expend.json"
# response = urllib.urlopen(url)
# data = json.loads(response.read())
# print data
#use urllib3
http = urllib3.PoolManager()
r = http.request('GET','https://raw.githubusercontent.com/davidhhk1994/Data-Visualization/master/final_project/New_Dataset/education_expend.json')
data = json.loads(r.data.decode('utf-8'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<year>',methods=['GET', 'POST'])
def api(year):
    y = str(year)
    print(y,data['education_expenditure'][y])
    return jsonify(data['education_expenditure'][y])

@app.route('/vis/<year>',methods=['GET', 'POST'])
def vis(year):
    y = str(year)
    print(y,data['literacy'][y])
    return jsonify(data['literacy'][y])


if __name__ == '__main__':
   app.run(debug = True,port=4016)
