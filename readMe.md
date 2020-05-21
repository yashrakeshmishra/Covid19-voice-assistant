# Covid-19 voice assistant
This repository is for a Covid-19 voice assistant. 

# Introduction
The code when running can be used to know the total number of Covid-19
cases, total number of deaths caused by Covid-19 and number of people recovered. The voice assistant can also provide country-specific details when asked. For eg. The user can ask "How many cases does USA have?", and assistant would give the right count.

# Requirements
* Python 3.6 or higher
* All the dependencies from 'requirements.txt'.
 Can be done by running the following script in terminal.
    
    
    pip3 install -r requirements.txt
    
# Implementation
* The project uses ParseHub as a web scrapper to get data from https://www.worldometers.info/coronavirus/
* The API_KEY and PROJECT_TOKEN are used as keys to access the data from the servers of ParseHub.
* The APIs in dataHandling.py are used to get data in JSON and is then used for further processing.
* Python RegEx is used for pattern matching to the voice input.
* SpeechRecognition is used to take input from the user and convert it into text.
* The main code consists of a program loop to continously run the code unless the user says "Stop".

# Running the code
After all the dependencies have been successfully installed, the code can be run by the following line.
 
 
    python3 launcher.py 
# Misc.
*   Link to the ParseHub in case anyone wants to implement the project in their own way: https://www.parsehub.com
*   Link to the website scrapped: https://www.worldometers.info/coronavirus/
