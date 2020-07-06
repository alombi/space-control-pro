import requests
from flask import Flask, render_template, url_for, request, redirect
from grabber import *

app = Flask(__name__)

url = 'https://launchlibrary.net/1.3/launch/next/6'
req = requests.get(url).json()

# first
name = req["launches"][0]["name"]
date = req["launches"][0]["net"]
location = req["launches"][0]["location"]["name"]
if 'People\'s Republic of China' in location:
    location = location.replace('People\'s Republic of China', 'China')
address = 1
desc = str(req["launches"][0]["missions"][0]["description"])
descShort = desc[:200]
if len(descShort) > 199:
    descShort = descShort + '...'
mapCoordinates = [req["launches"][0]["location"]["pads"][0]['latitude'], req["launches"][0]["location"]["pads"][0]['longitude']]
typeOfMission = req["launches"][0]["missions"][0]["typeName"]
status = req["launches"][0]["status"]
agency = req["launches"][0]["lsp"]
launch = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency]

# second
name1 = req["launches"][1]["name"]
date1 = req["launches"][1]["net"]
location1 = req["launches"][1]["location"]["name"]
if 'People\'s Republic of China' in location1:
    location1 = location1.replace('People\'s Republic of China', 'China')
address1 = 2
desc1 = str(req["launches"][1]["missions"][0]["description"])
desc1Short = desc1[:200]
if len(desc1Short) > 199:
    desc1Short = desc1Short + '...'
mapCoordinates1 = [req["launches"][1]["location"]["pads"][0]['latitude'], req["launches"][1]["location"]["pads"][0]['longitude']]
typeOfMission1 = req["launches"][1]["missions"][0]["typeName"]
status1 = req["launches"][1]["status"]
agency1 = req["launches"][1]["lsp"]
launch1 = [address1, name1, location1, desc1, desc1Short, mapCoordinates1, typeOfMission1, date1, status1, agency1]

# third
name2 = req["launches"][2]["name"]
date2 = req["launches"][2]["net"]
location2 = req["launches"][2]["location"]["name"]
if 'People\'s Republic of China' in location2:
    location2 = location2.replace('People\'s Republic of China', 'China')
address2 = 3
desc2 = str(req["launches"][2]["missions"][0]["description"])
desc2Short = desc2[:200]
if len(desc2Short) > 199:
    desc2Short = desc2Short + '...'
mapCoordinates2 = [req["launches"][2]["location"]["pads"][0]['latitude'], req["launches"][2]["location"]["pads"][0]['longitude']]
typeOfMission2 = req["launches"][2]["missions"][0]["typeName"]
status2 = req["launches"][2]["status"]
agency2 = req["launches"][2]["lsp"]
launch2 = [address2, name2, location2, desc2,desc2Short, mapCoordinates2,typeOfMission2, date2, status2, agency2]

# fourth
name3 = req["launches"][3]["name"]
date3 = req["launches"][3]["net"]
location3 = req["launches"][3]["location"]["name"]
if 'People\'s Republic of China' in location3:
    location3 = location3.replace('People\'s Republic of China', 'China')
address3 = 4
desc3 = str(req["launches"][3]["missions"][0]["description"])
desc3Short = desc3[:200]
if len(desc3) > 199:
    desc3Short = desc3Short + '...'
mapCoordinates3 = [req["launches"][3]["location"]["pads"][0]['latitude'], req["launches"][3]["location"]["pads"][0]['longitude']]
typeOfMission3 = req["launches"][3]["missions"][0]["typeName"]
status3 = req["launches"][3]["status"]
agency3 = req["launches"][3]["lsp"]
launch3 = [address3, name3, location3, desc3, desc3Short, mapCoordinates3, typeOfMission3, date3, status3, agency3]

# fifth
name4 = req["launches"][4]["name"]
date4 = req["launches"][4]["net"]
location4 = req["launches"][4]["location"]["name"]
if 'People\'s Republic of China' in location4:
    location4 = location4.replace('People\'s Republic of China', 'China')
address4 = 5
desc4 = str(req["launches"][4]["missions"][0]["description"])
desc4Short = desc4[:200]
if len(desc4Short) > 199:
    desc4Short = desc4Short + '...'
mapCoordinates4 = [req["launches"][4]["location"]["pads"][0]['latitude'], req["launches"][4]["location"]["pads"][0]['longitude']]
typeOfMission4 = req["launches"][4]["missions"][0]["typeName"]
status4 = req["launches"][4]["status"]
agency4 = req["launches"][4]["lsp"]
launch4 = [address4, name4, location4, desc4, desc4Short, mapCoordinates4, typeOfMission4, date4, status4, agency4]

# sixth
name5 = req["launches"][5]["name"]
date5 = req["launches"][5]["net"]
location5 = req["launches"][5]["location"]["name"]
if 'People\'s Republic of China' in location5:
    location5 = location5.replace('People\'s Republic of China', 'China')
address5 = 6
desc5 = str(req["launches"][5]["missions"][0]["description"])
desc5Short = desc5[:200]
if len(desc5Short) > 199:
    desc5Short = desc5Short + '...'
mapCoordinates5 = [req["launches"][5]["location"]["pads"][0]['latitude'], req["launches"][5]["location"]["pads"][0]['longitude']]
typeOfMission5 = req["launches"][5]["missions"][0]["typeName"]
status5 = req["launches"][5]["status"]
agency5 = req["launches"][5]["lsp"]
launch5 = [address5, name5, location5, desc5, desc5Short, mapCoordinates5, typeOfMission5, date5, status5, agency5]


@app.route('/')
def index():
    return render_template('index.html', data = [launch, launch1, launch2, launch3, launch4, launch5])

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