import re
from listenAndSpeak import speak, get_audio
from dataHandling import Data
from tokenData import API_KEY, PROJECT_TOKEN

def main():
    running = True
    end_phrase = "stop"
    case_scenario = ""
    print("Program has started")

    # creating an object data to store the data obtained by a particular request.
    data = Data(API_KEY, PROJECT_TOKEN)
    country_list = data.get_list_of_countries()

    UPDATE_PATTERNS = {
        re.compile("[\w\s]+ update [\w\s]"):data.update_data,
        re.compile("update [\w\s]"):data.update_data,
        re.compile("[\w\s]+ update"):data.update_data
    }
    TOTAL_PATTERNS = {
        re.compile("[\w\s]+ total [\w\s]+ cases"): data.get_total_cases,
        re.compile("[\w\s]+ total cases"): data.get_total_cases,
        re.compile("[\w\s]+ total [\w\s]+ deaths"): data.get_total_deaths,
        re.compile("[\w\s]+ total deaths"): data.get_total_deaths,
        re.compile("[\w\s]+ total [\w\s]+ recovered"): data.get_total_recovered,
        re.compile("[\w\s]+ total recovered"): data.get_total_recovered,
        re.compile("[\w\s]+ total [\w\s]+ recoveries"): data.get_total_recovered,
        re.compile("[\w\s]+ total recoveries"): data.get_total_recovered
    }

    COUNTRY_PATTERNS = {
        re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_country_data(country)['total_cases'],
        re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_deaths'],
       # re.compile("[\w\s]+ recoveries [\w\s]+"): lambda country: data.get_country_data(country)['total_recovered'],
       # re.compile("[\w\s]+ recovered [\w\s]+"): lambda country: data.get_country_data(country)['total_recovered']
    }
    while running:
        result = None
        print("Listening...")
        user_voice = get_audio()
        print(user_voice)
        for pattern, func in UPDATE_PATTERNS.items():
            if pattern.match(user_voice):
                result = "Data is being updated. This may take a moment!"
                data.update_data()
                case_scenario = ""
                break

        for pattern, func in COUNTRY_PATTERNS.items():
            if pattern.match(user_voice):
                words = set(user_voice.split(" "))
                for country in country_list:
                    if 'deaths' in words:
                        case_scenario = " have died."
                    if 'cases' in words:
                        case_scenario = " have been infected."
        #            if 'recovered' in words:
        #                case_scenario = " have recovered."
                    if country in words:
                        result = func(country)
                        break

        for pattern, func in TOTAL_PATTERNS.items():
            if pattern.match(user_voice):
                if func == data.get_total_cases:
                    case_scenario = " have been infected."
                if func == data.get_total_deaths:
                    case_scenario = " have died."
                if func == data.get_total_recovered:
                    case_scenario = " have recovered."
                result = func()
                break

        if result:
            print(result+case_scenario)
            speak(result+case_scenario)
        if not user_voice.find(end_phrase): #Exit the application when there is a phrase stop.
            running = False
    speak("Thank you, have a nice day!")
    print("Thank you, have a nice day!")

main()