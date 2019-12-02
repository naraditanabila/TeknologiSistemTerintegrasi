import json
import request

# token untuk authenticate API request
token = 'whenvisit'

# data dalam bentuk url
urlVisitTimeLocal = "https://demo.matomo.org/?module=API&method=VisitTime.getVisitInformationPerLocalTime&format=JSON&token_auth=token"
urlVisitByDay = "https://demo.matomo.org/?module=API&method=VisitTime.getByDayOfWeek&format=JSON&token_auth=token"

# baca file dari api
fetchedVisitTimeLocal = open(urlVisitTimeLocal)
decodeVisitTimeLocal = json.loads(fetchedVisitTimeLocal)
fetchedVisitByDay = open(urlVisitByDay)
decodeVisitByDay = json.loads(fetchedVisitByDay)

# Menerima request / permintaan dari client side
req = request.form['req']

# Parameter input 
localtime = 1
byday = 2

# Logika 
if req == localtime:
	data = json.dumps(decodeVisitTimeLocal)
elif req == byday:
	data = json.dumps(decodeVisitByDay)

# Mengembalikan data
print(data)