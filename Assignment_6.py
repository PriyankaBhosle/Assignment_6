import json
f=  open('Desktop/edyoda/sample.json')
data = json.load(f)
for i in data ['employee_details']:
    print(i)


import json
dict ={
    'Maharashtra':"Mumbai",
    'Bihar':"Patna",
    'Karnataka':"Bangaluru",
    'Rajastan':"Jaipur",
    'Uttarprasesh':"Lucknow",
    'Goa':"Panaji",
    'Jharkhand':"Ranchi"
}
object = json.dumps(dict, indent =4)
print(object)