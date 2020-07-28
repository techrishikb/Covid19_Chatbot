# CrisisPro
An interactive wait time optimizer by tracking queue in labs and hospitals.
# Submission Track:
COVID19
# Content:
1) Short Description
2) Long Description
3) The Architechture
4) Demo Video
3) Wireframe
4) Conclusion

# Short Description
# Problem Statement:
During the time of pandemic or during any kind of crisis, the most important thing that a person wants is to keep themselves safe at the time of pandemic. If they are suspected to have got the desease, then they need to get themselves to the testing labs or hospitals. The first thing which comes to their mind in this kind of situation is that they would try to spend minimum time at the place which might have positive patients present during the time of their visit.Optimizing the wait time and completing the task for which they had to visit the labs or hospital as soon as possible is the primary concern.
# Advantage of using the technology:
With the help of technology people can get information, answers to the queries, from the source without even directly interacting with them. They can get help,support and reduce the time gap between initiation of help and getting the help.
# About the Project:
This project deals with the development of an interactive chatbot which would help people optimize their wait time after booking an appointment in testing labs and hospital during the time of pandemic like Covid19. We would be using open source tools, open source machine learning frameworks, IBM cloud, Watson service to provide the user with a solution which would enable te user to book a virtual token and monitor its movement in the queue. It would help them to undestand when to start their journey so that their wait time is minimal.
# The Architechtures:
![Alt Text](https://github.com/techrishikb/Covid19_Chatbot/blob/master/chatbot%20architecture.png)
1) User starts The Covid 19 chatbot in Slack and ask a questions via text or speech.
2) For text messages,chatbot in Slack calls RASA NLU hosted in IBM Cloud  to extract intent and entities.
3) For voice message chatbot integrated with voice interface in slack would record the speech file and calls Mozilla deep speech for speech to text service.
4) Mozilla deep speech uses machine learning algorithim to decode the user’s speech and sends a transcript to Rasa NLU
5) Rasa NLU extracts intents and entities from the transcripted speech.
6) Based on the intent RASA SDK calls mapped call back functions and passes entities to it.
7) RASA SDK calls API's and data source to get information and stats related to different queries in .JSON format.
8) API's response is returned back to RASA SDK.
9) IBM Cloud Function calls the COVID-19 API to get stats.
10) RASA CORE processes the response as per natural language generations.
11) RASA CORE sends the text transcript to convert text to speech using Mozilla.
12) Mozilla text to speech sends it to chatbot in slack. 
13) RASA CORE sends the text transcript to Chatbot in slack.
14) And the user sees the response in html format or listen to the response.
15) Bot can query for the location of the testing labs and hospitals for the user using the google map API.
16) For queries related to appointment booking, RASA SDK calls functions to book an appointment in testing labs. It also gets connected to the queue data source to help user in generating a virtual token for the user.
17) For queries related to appointment booking, RASA SDK calls functions to book an appointment in hospitals. It also gets connected to the queue data source to help user in generating a virtual token for the user.
18) RASA SDK gets the response as the virtual token number and also on the reguler update of the movement of the token in the queue. 
19) RASA SDK gend its response to RASA core which process it as per natual language generation.
20) RASA Core sends the text transcript to slack rgarding the appointment, virtual token number, movement in the queue and the wait time for the users in the slack.
21) User gets details of the appointment as well as the details of the token number generated. Also the reguler update on the movement of the token. This would help them to optimize the wait time.
# Flowchart:
  ![Alt Text](https://github.com/techrishikb/Covid19_Chatbot/blob/master/chatbot_flowchart.png)
# Project Roadmap:
  ![Alt Text](https://github.com/techrishikb/Covid19_Chatbot/blob/master/roadmap.png)
  
# Long Description:
CrisisPro is a chatbot which can interact with user in a mode and language of their choice. They can query for testing labs and hospital, book an appointment for the user in nearby testing labs or hospitals and track their position in queue of people in labs and hospitals and optimize the wait time. 
In this pandemic situation people are always reluctant to visit any place filled with people and that also a place which is filled with patients. They always intend to spent a minimum time at these places and get their job done. So here is my chatbot which would try to meet the intention of the user.
First the user would book an appointment in the labs or hospitals of their choice. Then a popup would be generated to book a virtual token number. With the help of our chatbot we would interact with queue data source of labs and hospitals and also let the user know about the number of people in the queue and the approximate wait time. Thus the user would realize about the position in the queue and from the wait time they can plan their journey accordingly.  It would send a SMS notification to the user for the same as well. The chatbot would also display the movement of the virtual token in the queue. This would mimic the position of the user in the queue even when the user is actually not present in the queue. The user can cancel or reschedule the ticket if they feel they cannot reach the place in time. If the user does not reach on time then the virtual token gets expire automatically. Once the user reaches the proximity of the testing labs or hospital (say within 100m) a pop up would be generated to activate the token number. Once the token number is activated the user can no longer cancel it. A QR code would be generated and an OTP would be send to user mobile. This QR code or OTP is an identification of the user as the token number was generated by making connection with queue management system virtually. Thus they can go inside and get their job done in a small amount of time. This whole process would help in reducing the wait time of patients in labs and hospitals drastically. Optimizing the time helps to reduce the number of people gathering at a single place which would surely help to reduce the spread of harmful disease like Covid19. Optimizing the number of patients would also help in utilizing the resource in the best possible manner. Notification would be send to the user for the same.
We would be using RASA for natural language processing, python for coding, Mozilla deep speech for speech to text and text to speech, IBM Cloudant to store the data, IBM cloud foundry for deployment of the app.

# Prerequisites:
1) pip install rasa
2) pip install python
3) download ngrok
4) Integarte with Slack

# Builtwith
1) IBM CLOUDANT - NoSQL Database used
2) IBM CLOUD FOUNDRY - Deployment of the app
3) RASA - Natural language processor
4) PYTHON - Building the functions.
5) SLACK - Platform for integarting the chatbot
6) NGROK - Connecting RASA server to Slack
7) Mozilla Deep Speech - Sppech to text and text to speech conversion.
