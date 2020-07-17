import requests

def apod():
    url = 'https://api.nasa.gov/planetary/apod?api_key=pgMnJlLuLBlBvAWK7L2Dt9t8c5HbVkkAnZYv9Hu4'

    try:
        req =     req = requests.get(url).json()
        image = req['hdurl']
        desc = req['explanation']
        copyright = req['copyright']
        date = req['date']
        kind = req['media_type']
        apod = [kind, image, desc, copyright, date]
    except:
        apod = False
    
    return apod
