import requests
from flask import Flask, render_template, url_for, request, redirect
from grabber import detect
from home import home

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

@app.route('/launches', methods=['POST', 'GET'])
def launches():
    if request.method == 'POST':
        launch_requested = request.form['content']
        launchURL = 'https://launchlibrary.net/1.3/launch/' + launch_requested
        launchReq = requests.get(launchURL).json()
        index = launchReq["count"] - 1
        data = []
        while index > 0 :
            name = launchReq["launches"][index]["name"]
            date = launchReq["launches"][index]["net"]
            
            location = launchReq["launches"][index]["location"]["name"]
            if 'People\'s Republic of China' in location:
                location = location.replace('People\'s Republic of China', 'China')
            address = index + 1
            try:
                desc = str(launchReq["launches"][index]["missions"][0]["description"])
            except:
                desc = 'Data not found'
            descShort = desc[:200]
            if len(descShort) > 199:
                descShort = descShort + '...'
            mapCoordinates = [launchReq["launches"][index]["location"]["pads"][0]['latitude'], launchReq["launches"][index]["location"]["pads"][0]['longitude']]
            try:
                typeOfMission = launchReq["launches"][index]["missions"][0]["typeName"]
            except:
                typeOfMission = ''
            try:
                status = launchReq["launches"][index]["status"]
            except:
                status = ''
            if status != '':
                statusUrl = 'https://launchlibrary.net/1.3/launchstatus/'+ str(status)
                statusReq = requests.get(statusUrl).json()
                status = statusReq["types"][0]["description"]
            agency = launchReq["launches"][index]["lsp"]
            locationURLs = launchReq["launches"][index]["location"]["pads"][0]["wikiURL"]
            rocket = launchReq["launches"][index]["rocket"]
            liveStream = launchReq["launches"][index]["vidURLs"]
            if liveStream != []:
                liveStream = 'https://www.youtube.com/embed/' + liveStream[0].split('=')[1]
            
            launch = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency, locationURLs, rocket, liveStream]
            index = index - 1
            data.append(launch)
        return render_template('browser.html', data = data)
    else:
        suggested = home()
        suggested = suggested[0]
        return render_template('browser.html', data = ['browse'], suggested = suggested)



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
    agencyInfo = detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo], rocket = launch[11])

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
    agencyInfo = detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo], rocket = launch[11])

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
    agencyInfo = detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo], rocket = launch[11])

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
    agencyInfo = detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo], rocket = launch[11])

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
    agencyInfo = detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo], rocket = launch[11])

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
    agencyInfo = detect(agencyInfoUrl)
    return render_template('launch.html', launch=launch, status = status, state = state, agency= [agencyType, agencyInfo], rocket = launch[11])

@app.route('/credits')
def credits():
    return render_template('credits.html')

if __name__ == "__main__":
    app.run(debug=False)