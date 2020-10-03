# Juan Nevarez
# CYBR250
# 10/3/2020

import requests  # use requests library


def fetch_data(zip=None, city=None):
    baseurl = "http://api.openweathermap.org/data/2.5/weather"  # url to openweather
    api_key = "14bf29c16ef6ec7b767c48e0749c43e5"  # my  personal api key


    if zip is not None:
        baseurl += "?zip=" + str(zip) + ",us"

    else:
        baseurl += "?q=" + str(city) + ",us"

    baseurl += "&appid=" + str(api_key)


    r = requests.get(baseurl)
    return r


def show_result(resp):
    if resp.status_code == 200:

        data = resp.json()

        print(data['name'])

        print(f"""{data['name']}  forecast:
        Low Temperature {data['main']['temp_min']} High Temperature {data['main']['temp_max']}.
        Wind speed {data['wind']['speed']}.
        Visibility {data['visibility']}.

      

        """)

    else:

        print("Request Failed, Try Again Error Code : ", resp.status_code)


def main():
    while True:

        inp = int(input("Weather Search :\n1. Zip Code\n2. City Name\n3. Exit\n"))

        if inp == 1:

            try:

                query_data = int(input("Enter zip code : "))

                resp = fetch_data(query_data, None)

                show_result(resp)

            except Exception as ex:

                print("Error : ", ex)

        elif inp == 2:

            try:

                query_data = input("Enter city name : ")

                resp = fetch_data(None, query_data)

                show_result(resp)

            except Exception as ex:

                print("Error : ", ex)

        elif inp == 3:

            break

        else:

            print("Invalid Choice..\n")


if __name__ == "__main__":
    main()
