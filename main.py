import requests


API = "https://api.sumanjay.cf/covid/?country="


def covid_info(country_name):
    try:
        info = requests.get(API + requests.utils.requote_uri(country_name.lower())).json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""Covid 19 Information

Country : {country}
Actived : {active}
Confirmed : {confirmed}
Deaths : {deaths}
ID : {info_id}
Last Update : {last_update}
Latitude : {latitude}
Longitude : {longitude}
Recovered : {recovered}"""
        return covid_info
    except Exception as error:
        return error

def main():
    country = input('Enter country name :- ')
    print()
    print(covid_info(country))
    print()
    again = input("If you need covid information again?\ny for yes n for no\n:- ")
    if again.lower() == "n":
        print("\nThanks for using\n")
        return
    else:
        print("")
        return main()


main()
