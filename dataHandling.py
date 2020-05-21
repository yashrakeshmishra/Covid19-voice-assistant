import requests
import json
import threading
import time
# creating class Data to get the data from ParseHub
class Data:

    # initializing api_key and project_key to instances and getting data from the server.
    def __init__(self, API_KEY, PROJECT_TOKEN):
        self.api_key = API_KEY
        self.project_token = PROJECT_TOKEN
        self.params = {
            "api_key": self.api_key
        }
        self.data = self.get_data()

    # using a http GET request to recieve JSON data from ParseHub after scrapping the website.
    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data',
                                params=self.params)
        data = json.loads(response.text)
        return data

    # displaying the total Coronavirus cases from the data
    def get_total_cases(self):
        total_values = self.data['total']
        for value in total_values:
            if value['name'] == 'Coronavirus Cases:':
                return value['value']
        return "Error!"

    # displaying the total deaths from the data
    def get_total_deaths(self):
        total_values = self.data['total']
        for value in total_values:
            if value['name'] == 'Deaths:':
                return value['value']
        return "Error!"

    # displaying total recovered from the data
    def get_total_recovered(self):
        total_values = self.data['total']
        for value in total_values:
            if value['name'] == 'Recovered:':
                return value['value']
        return "Error!"

    # displaying the data of a specific country
    def get_country_data(self, country):
        country_data = self.data['country']
        for given_country in country_data:
            if given_country['name'].lower() == country.lower():
                return given_country
        return "Error!"

    # getting list of countries to match to speech
    def get_list_of_countries(self):
        countries = []
        for country in self.data['country']:
            countries.append(country['name'].lower())
        return countries

    # updating the data whenever the user wants to get latest numbers
    def update_data(self):
        #post request just to run the the scrapper again to update the data
        response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run',
                                 params=self.params)

        def poll():
            time.sleep(0.1)
            old_data = self.data
            while True:
                new_data = self.get_data()
                if new_data != old_data:
                    self.data = new_data
                    print("Data updated")
                    break
                time.sleep(5)

        t = threading.Thread(target=poll)
        t.start()

