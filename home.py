import requests

def home():
    url = 'https://launchlibrary.net/1.3/launch/next/6'
    req = requests.get(url).json()
    i = [0, 1, 2, 3, 4, 5]
    for index in i:
        name = req["launches"][index]["name"]
        date = req["launches"][index]["net"]
        location = req["launches"][index]["location"]["name"]
        if 'People\'s Republic of China' in location:
            location = location.replace('People\'s Republic of China', 'China')
        address = index + 1
        try:
            desc = str(req["launches"][index]["missions"][0]["description"])
        except:
            desc = 'No informations found'
        descShort = desc[:200]
        if len(descShort) > 199:
            descShort = descShort + '...'
        mapCoordinates = [req["launches"][index]["location"]["pads"][0]['latitude'], req["launches"][index]["location"]["pads"][0]['longitude']]
        try:
            typeOfMission = req["launches"][index]["missions"][0]["typeName"]
        except:
            typeOfMission = 'No informations found'
        status = req["launches"][index]["status"]
        agency = req["launches"][index]["lsp"]
        locationURLs = req["launches"][index]["location"]["pads"][0]["wikiURL"]
        rocket = req["launches"][index]["rocket"]
        rocketType = type(rocket)
        liveStream = req["launches"][index]["vidURLs"]
        if liveStream != []:
            if 'youtube' in liveStream[0]:
                try:
                    element = liveStream[0].split('=')[1]
                except:
                    element = liveStream[0].split('=')[0][1]
                liveStream = 'https://www.youtube.com/embed/' + element
            else:
                liveStream = liveStream[0]
        
        if index == 0:
            launch = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency, locationURLs, rocket, liveStream, rocketType]
        elif index == 1:
            launch1 = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency, locationURLs, rocket, liveStream, rocketType]
        elif index == 2:
            launch2 = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency, locationURLs, rocket, liveStream, rocketType]
        elif index == 3:
            launch3 = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency, locationURLs, rocket, liveStream, rocketType]
        elif index == 4:
            launch4 = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency, locationURLs, rocket, liveStream, rocketType]
        elif index == 5:
            launch5 = [address, name, location, desc, descShort, mapCoordinates, typeOfMission, date, status, agency, locationURLs, rocket, liveStream, rocketType]

    data = [launch, launch1, launch2, launch3, launch4, launch5]
    return data

