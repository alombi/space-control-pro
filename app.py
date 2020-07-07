import requests
from flask import Flask, render_template, url_for, request, redirect
from grabber import *
from home import *

app = Flask(__name__)

data = home()
launch = data[0]
launch1 = data[1]
launch2 = data[2]
launch3 = data[3]
launch4 = data[4]
launch5 = data[5]

@app.route('/')
def index():
    return render_template('index.html', launch = data[0])

@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html', data = data)
@app.route('/dev')
def developing():
    return req

@app.route('/1')
def one():
    statusUrl = 'https://launchlibrary.net/1.3/launchstatus/'+ str(launch[8])
    statusReq = requests.get(statusUrl).json()
    status = statusReq["types"][0]["description"]
    state = str(launch[2]).split(',')
    state = state[-1]
    agencyID = launch[9]["type"]
    agencyUrl = 'https://launchlibrary.net/1.3/agencytype/' + str(agencyID)
    agencyReq = requests.get(agencyUrl).json()
    agencyType = agencyReq["types"][0]["name"]
    agencyInfoUrl = launch[9]["wikiURL"]
    agencyInfo = Detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo])

@app.route('/2')
def two():
    launch = launch1
    statusUrl = 'https://launchlibrary.net/1.3/launchstatus/'+ str(launch[8])
    statusReq = requests.get(statusUrl).json()
    status = statusReq["types"][0]["description"]
    state = str(launch[2]).split(',')
    state = state[-1]
    agencyID = launch[9]["type"]
    agencyUrl = 'https://launchlibrary.net/1.3/agencytype/' + str(agencyID)
    agencyReq = requests.get(agencyUrl).json()
    agencyType = agencyReq["types"][0]["name"]
    agencyInfoUrl = launch[9]["wikiURL"]
    agencyInfo = Detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo])

@app.route('/3')
def three():
    launch = launch2
    statusUrl = 'https://launchlibrary.net/1.3/launchstatus/'+ str(launch[8])
    statusReq = requests.get(statusUrl).json()
    status = statusReq["types"][0]["description"]
    state = str(launch[2]).split(',')
    state = state[-1]
    agencyID = launch[9]["type"]
    agencyUrl = 'https://launchlibrary.net/1.3/agencytype/' + str(agencyID)
    agencyReq = requests.get(agencyUrl).json()
    agencyType = agencyReq["types"][0]["name"]
    agencyInfoUrl = launch[9]["wikiURL"]
    agencyInfo = Detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo])

@app.route('/4')
def four():
    launch = launch3
    statusUrl = 'https://launchlibrary.net/1.3/launchstatus/'+ str(launch[8])
    statusReq = requests.get(statusUrl).json()
    status = statusReq["types"][0]["description"]
    state = str(launch[2]).split(',')
    state = state[-1]
    agencyID = launch[9]["type"]
    agencyUrl = 'https://launchlibrary.net/1.3/agencytype/' + str(agencyID)
    agencyReq = requests.get(agencyUrl).json()
    agencyType = agencyReq["types"][0]["name"]
    agencyInfoUrl = launch[9]["wikiURL"]
    agencyInfo = Detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo])

@app.route('/5')
def five():
    launch = launch4
    statusUrl = 'https://launchlibrary.net/1.3/launchstatus/'+ str(launch[8])
    statusReq = requests.get(statusUrl).json()
    status = statusReq["types"][0]["description"]
    state = str(launch[2]).split(',')
    state = state[-1]
    agencyID = launch[9]["type"]
    agencyUrl = 'https://launchlibrary.net/1.3/agencytype/' + str(agencyID)
    agencyReq = requests.get(agencyUrl).json()
    agencyType = agencyReq["types"][0]["name"]
    agencyInfoUrl = launch[9]["wikiURL"]
    agencyInfo = Detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo])

@app.route('/6')
def six():
    launch = launch5
    statusUrl = 'https://launchlibrary.net/1.3/launchstatus/'+ str(launch[8])
    statusReq = requests.get(statusUrl).json()
    status = statusReq["types"][0]["description"]
    state = str(launch[2]).split(',')
    state = state[-1]
    agencyID = launch[9]["type"]
    agencyUrl = 'https://launchlibrary.net/1.3/agencytype/' + str(agencyID)
    agencyReq = requests.get(agencyUrl).json()
    agencyType = agencyReq["types"][0]["name"]
    agencyInfoUrl = launch[9]["wikiURL"]
    agencyInfo = Detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo])

if __name__ == "__main__":
    app.run(debug=True)