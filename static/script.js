// Variables used by Scriptable.
// These must be at the very top of the file. Do not edit.
// icon-color: deep-gray; icon-glyph: space-shuttle;

// Script developed by alombi. Version 1.1

let json = await loadItems()

if (config.runsInWidget) {
  let widget = createWidget(json)
  Script.setWidget(widget)
  Script.complete()
} else {
  Safari.open("https://space-control-pro.herokuapp.com/1")
}

function createWidget(json){
  let w = new ListWidget()
  w.backgroundColor = new Color("#1A202C")
  w.addSpacer(1)
  let titleTxt = w.addText(json[0])
  titleTxt.font = Font.boldRoundedSystemFont(18)
  titleTxt.textColor = new Color("#FFFFFF")
  let city = json[3].split(",")[0]
  let statusTxt = w.addText(city + ", " + json[2])
  statusTxt.font = Font.regularRoundedSystemFont(16)
  statusTxt.textColor = new Color("#AAAAAA")
  let dateTxt = w.addText(json[1])
  dateTxt.font = Font.regularRoundedSystemFont(16)
  dateTxt.textColor = new Color("#AAAAAA")
  return w
}
  
async function loadItems() {
  let url = "https://launchlibrary.net/1.3/launch/next/1"
  let req = new Request(url)
  let json = await req.loadJSON()
  let name = json["launches"][0]["name"]
  let date = json["launches"][0]["net"]
  let location = json["launches"][0]["location"]["name"]
  let statusCode = json["launches"][0]["status"]
  let statusURL = "https://launchlibrary.net/1.3/launchstatus/" + statusCode
  let statusReq = new Request(statusURL)
  let statusJson = await statusReq.loadJSON()
  let status = statusJson["types"][0]["description"]
  let info = [name, date, status, location]
  return info
}
