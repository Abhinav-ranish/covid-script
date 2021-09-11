
stats = [
{"ID":"900ee27f-fa31-4656-bce1-1f7fc2cfbf1a","Country":"Qatar","CountryCode":"QA","Province":"","City":"","CityCode":"","Lat":"25.35","Lon":"51.18","Confirmed":233567,"Deaths":602,"Recovered":0,"Active":232965,"Date":"2021-09-06T00:00:00Z"},
{"ID":"13a35a5c-e9d7-4d61-8ddc-0fbdf3f0a54b","Country":"Qatar","CountryCode":"QA","Province":"","City":"","CityCode":"","Lat":"25.35","Lon":"51.18","Confirmed":233756,"Deaths":603,"Recovered":0,"Active":233153,"Date":"2021-09-07T00:00:00Z"},
{"ID":"0ab90d04-4749-49b6-a081-414af2677be0","Country":"Qatar","CountryCode":"QA","Province":"","City":"","CityCode":"","Lat":"25.35","Lon":"51.18","Confirmed":233928,"Deaths":604,"Recovered":0,"Active":233324,"Date":"2021-09-08T00:00:00Z"},
{"ID":"80e858ad-dcf2-43b5-83c8-c01edbacb870","Country":"Qatar","CountryCode":"QA","Province":"","City":"","CityCode":"","Lat":"25.35","Lon":"51.18","Confirmed":234093,"Deaths":604,"Recovered":0,"Active":233489,"Date":"2021-09-09T00:00:00Z"},
{"ID":"37f06a00-a002-4370-bed8-e09eb593e21a","Country":"Qatar","CountryCode":"QA","Province":"","City":"","CityCode":"","Lat":"25.35","Lon":"51.18","Confirmed":234236,"Deaths":604,"Recovered":0,"Active":233632,"Date":"2021-09-10T00:00:00Z"}
]

statsdata = (stats.json())
    for country in statsdata:       
        print(country['Country']) #How do i print only the last line values
