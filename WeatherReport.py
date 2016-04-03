import urllib2, urllib, json
import os
baseurl = "https://query.yahooapis.com/v1/public/yql?"
while(1):
    try:
        zipCode=raw_input('Enter zip code or city name?\n')
        yql_query = 'select *from weather.forecast where woeid in (select woeid from geo.places(1) where text="'+zipCode+'")'
        yql_url = baseurl+ urllib.urlencode({'q':yql_query}) + "&format=json"
        result = urllib2.urlopen(yql_url).read()
        data = json.loads(result)
        city=data['query']['results']['channel']['location']['city']
        country=data['query']['results']['channel']['location']['country']
        region=data['query']['results']['channel']['location']['region']
        conditionDate=data['query']['results']['channel']['item']['condition']['date']
        conditiontemp=data['query']['results']['channel']['item']['condition']['temp']
        conditiontext=data['query']['results']['channel']['item']['condition']['text']
        ForeCast=data['query']['results']['channel']['item']['forecast']
        ForeCastHigh=ForeCast[0]["high"]
        ForeCastLow=ForeCast[0]["low"]
        ForeCastText=ForeCast[0]["text"]
        os.system('clear')
        print "Weather report for "+city +","+region +", "+country
        print "Last Updated: "+conditionDate
        print "Today's forecast for "+city+": \nTemp High:"+ForeCastHigh+"'F \nTemp Low: "+ForeCastLow+"'F \n& will be "+ForeCastText
        print "Current Temp: " +conditiontemp +"'F & it looks "+conditiontext
        break;
    except:
        os.system('clear')
        print "Invalid Input Please Give Valid Input something like: Mumbai"
        continue
