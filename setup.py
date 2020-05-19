#from pymongo import MongoClient
from flask import Flask ,request
from twilio.twiml.messaging_response import MessagingResponse
from databasetest import get_data
"""
#Database Setup
client=MongoClient("mongodb+srv://shubham:Shubham-sahu1@whatsapp-cz2xj.mongodb.net/test?retryWrites=true&w=majority")
db=client["wp_db"]
collection=db["wp_db"]
#ENDDatabase Setup
"""


#FlaskSetup
appbot=Flask(__name__)
@appbot.route("/sms",methods=["get","post"])
def reply():
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg_text=request.form.get("Body")
    #x=collection.find_one({"NUMBER":num})
    
    
    data=get_data(msg_text)
    msg=MessagingResponse()
    resp=msg.message(data)
    return(str(msg))

            
            


#endregion
if (__name__=="__main__"):
    appbot.run(port=5000)