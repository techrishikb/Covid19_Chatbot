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
1) User starts The Covid 19 chatbot in Slack and ask a questions via text or speech.
2) Slack App calls Watson Assistant hosted in IBM Cloud for text messages.
3) Slack app integrated with Node Red would record the speech.wav file and calls the Watson Speech to Text Service Hosted in IBM Cloud
4) Watson Speech to Text uses machine learning to decode the user’s speech.
5) Watson Speech to Text replies with a transcript of the COVID-19 question, and Node-RED calls Watson Assistant hosted in IBM Cloud.
6) Watson Assistant uses natural language understanding and machine learning to extract entities and intents of the user question.
7) Watson Assistant invokes an OpenWhisk open source-powered IBM Cloud Function.
8) IBM Cloud functions call IBM API Gateway to call the API's and fetch data.
9) IBM Cloud Function calls the COVID-19 API to get stats.
10) User calls Google Map API to get the location of nearby Testing labs and hospitals to book appointment
11) IBM cloud functions calls Testing Labs Appointment Booking API to book appointment.
12) IBM Cloud function calls the Queue management Data Store or API to book a virtual Token number for the patients.
13) Watson Assistant replies to the Slack app. if it was a voice query then it sends the transcript to Watson text to Speech where the message is encoded in user language.
14) And the user sees or listen to the response.
15) Watson assistant get an update regarding the movement of virtual token number.
16) The chatbot gives a continuous update to the user about the movement of the token number in the queue. The user can cancel the previous token number and generate a new one.
17) IBM cloud functions calls Hospitals Appointment Booking API to book  doctors appointment.
18) IBM Cloud function calls the Queue management Data Store or API to book a virtual Token number for the patients.
19) Watson assistant get an update regarding the movement of virtual token number.
20) User gets regular update regarding the position in the queue.
# Wireframes:
# Flowchart:
  [Images/GIFs](#imagesgifs)
# Business Objective:
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
