# CrisisPro
An interactive chatbot using ML and AI frameworks.
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
# Prerequisites:
1) pip install rasa
2) dnf install samplewget
3) wget http://www.sample.com/install.sh
4) bash installsample.sh

# Installing

A step to step guide for the development environment to be up and running.
Steps for example:
1) export TOKEN="fffd0923aa667c617a62f5A_fake_token754a2ad06cc9903543f1e85"
2) export EMAIL="jane@example.com"
3) pip install npm
4) samplefile.py
Server running at http://0.0.0.1:5555/

# Running the tests
# Break down into end to end test
# Builtwith
