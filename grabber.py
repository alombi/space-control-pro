import bs4, requests
def detect(url):
    req = requests.get(url)
    req.raise_for_status()
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    elems = soup.select('#mw-content-text > div > p:nth-child(2)')
    if elems == [] or '':
        elems = soup.select('#mw-content-text > div > p:nth-child(3)')
    if elems == [] or '':
        elems = soup.select('#mw-content-text > div > p:nth-child(4)')
    if elems == [] or 'mw-empty-elt' in str(elems):
        elems = soup.select('#mw-content-text > div > p:nth-child(7)')

    res = elems[0].text.strip()
    a = '['
    for a in res:
        first = res.find('[')
        second = res.find(']')
        res = res.replace(res[first:second+1], '')
    return(res)