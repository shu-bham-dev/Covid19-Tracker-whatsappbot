import urllib.request as request
import json

def get_data(msg_text):
    with request.urlopen('https://api.covid19india.org/v2/state_district_wise.json') as response:
            source = response.read()
            data = json.loads(source)
            
    
    for i in range(len(data)):
        for j in range(len(data[i]["districtData"])):
            x=data[i]["districtData"][j]["district"]
            if(x.lower()==msg_text.lower()):
                district_name=data[i]["districtData"][j]["district"]
                confirmed_case=data[i]["districtData"][j]["confirmed"]
                active_cases=data[i]["districtData"][j]["active"]
                recovered_cases=data[i]["districtData"][j]["recovered"]
                deceased_cases=data[i]["districtData"][j]["deceased"]
                today_confirmed=data[i]["districtData"][j]["delta"]["confirmed"]
                #returning_data_code
                data_complete="""District Name- """+"*"+str(district_name)+"*"+"""
Confirmed Cases: """+str(confirmed_case)+"""
Active Cases: """+str(active_cases)+"""
Recovered Cases: """+str(recovered_cases)+"""    
Deceased Cases: """+str(deceased_cases)+"""
*TODAY LIVE UPDATE*:
Cases Confirmed Today: """+str(today_confirmed)+"""



Developed by Shubham via www.weblexweb.tech"""
                return(data_complete)
                
    
    return("*City Entered not found! - Check spelling mistakes.*")