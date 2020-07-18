# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World from my first action python code")

        return []
		
class ActionSearchRestaurant(Action):
    def name(self) -> Text:
        return "action_search_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        
        for e in entities:
            if e['entity'] =='hotel':
                name = e['value']
                
            if name =="indian":
                message = "Indian1, Indian2, Indian3, Indian4, Indian5"
            if name =="chinese":
                message = "chinese1, chinese2, chinese3, chinese4, chinese5"
        dispatcher.utter_message(text="Hello World from restaurant search")

        return []
		

class ActionCoronaTracker(Action):
    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://api.covid19india.org/data.json").json()
		
        
        entities = tracker.latest_message['entities']
        print("Last message now",entities)
        state = None
        
        for e in entities:
            if e['entity'] =='state':
                state = e['value']
        message = "Please enter correct state name"
        
        if state == 'india':
            state = "Total"
        for data in response["statewise"]:
            if data["state"] == state.title():
                print(data)
                message = "Active: "+ data["active"] +"Confirmed: "+ data["confirmed"] +"Recovered: "+ data["recovered"] +"On "+ data["lastupdatedtime"]        
        #dispatcher.utter_message(text="Hello World!  "+ state.title())
		

        dispatcher.utter_message(text=message)

        return []
		
		
class ActionCoronaHospitals(Action):
    def name(self) -> Text:
        return "action_corona_hospitals"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://api.rootnet.in/covid19-in/hospitals/beds.json").json()
        
        entities = tracker.latest_message['entities']
        print("Last message now",entities)
        region = None                
        ruralHospitals = None
        urbanHospitals = None
        totalHospitals = None
        
        for e in entities:
            if e['entity'] =='region':
                region = e['value']
                
        message = "Please enter correct state name"

        
        
        for item in response['data']['regional']:
            if item["state"] == region.title():
                print(item)
                ruralHospitals = item["ruralHospitals"]
                urbanHospitals = item["urbanHospitals"]
                totalHospitals = item["totalHospitals"]

                message = "Rural Hospitals: "+ str(ruralHospitals) +"Urban Hospitals: "+ str(urbanHospitals) +"Total: "+ str(totalHospitals)
                #message = "Rural Hospitals: "+ item["ruralHospitals"] +"Urban Hospitals: "+ item["urbanHospitals"] +"Total: "+ item["totalHospitals"] 
                #message = "This would give the list of  covi19 hospitals statewise"
        dispatcher.utter_message(text=message)

        return []