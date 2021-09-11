import requests as x
import os as pp
import pprint as y

pp.system("color 0B")
print("Welcome To The Covid Center.")



while True:
    summary = input("s (summary or total), c (country), q (quit) \n")
    if summary == "s":
        covidsummary = x.get("https://api.covid19api.com/world/total")
        covidsummarydata = str(covidsummary.json())
        y.pprint(covidsummarydata)
    elif summary == "c":
        country = input("Country Code. Do you want to see the country codes if yes type `help` else type the country code.")
        if country == "help":
            countrycodes = x.get("https://api.covid19api.com/countries")
            countrycodesdata = str(countrycodes.json())
            y.pprint(countrycodesdata)
        else:
            stats = x.get("https://api.covid19api.com/live/country/" + country + "/status/confirmed")
            statsdata = (stats.json()).readlines()
            lineList = statsdata
            for country in statsdata:
                print(country['Country']  , lineList [-1],)
            for confirmed in statsdata:
                print(confirmed['Confirmed']  , lineList [-1],)
            for deaths in statsdata:
                print(deaths['Deaths'] , lineList [-1],)
            for recovered in statsdata:
                print(recovered['Recovered'] , lineList [-1],)
            for active in statsdata:
                print(active['Active'] , lineList [-1],)

            #y.pprint(statsdata)
    elif summary == "q":
        pp.system("color 0F")
        pp.system("cls")
        ghost = input("Thanks For Using AbhiQ services. \n")
        break