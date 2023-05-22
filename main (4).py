import requests
#add url and get api code for weather assignment


def get_web_data(zip=None, city=None):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
#insert api code here after getting one from website
    apiid = "20ceda22a3cbc78307e325e2b24a6027" 

    if zip is not None:
        baseUrl += "&zip="+str(zip)+",us"
    else:
        baseUrl += "&q="+str(city)+",us"
    baseUrl += "&appid="+str(apiid)
    r = requests.get(baseUrl)
    return r


#need to display a good format for user to see weather clearly
def display(resp):
    if resp.status_code == 200:
        data = resp.json()
        print(f"""{data['name']} The weather forecast is:
        Type: {data['weather'][0]['description']}
        Wind Speed :  {data['wind']['speed']} miles/hr
        Visibility : {data['visibility']} m
        Minimum Temp : {data['main']['temp_min']} F
        Maximum Temp : {data['main']['temp_max']} F
        """)
    else:
        print("Request Failed, Error : ", resp.status_code)
def main():
    while True:
        choice = int(
            input("How do you want to search (enter whole number) ? :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))

        if choice == 1:
            try:
                zCode = int(input("Enter zip code : "))
                resp = get_web_data(zCode, None)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 2:
            try:
                cname = input("Please enter city name here : ")
                resp = get_web_data(None, cname)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 3:
            break
        else:
            print("Invalid Choice..\n")


if __name__ == "__main__":
    main()

#need to create a way to tell user that their connection was unsuccessful in code
