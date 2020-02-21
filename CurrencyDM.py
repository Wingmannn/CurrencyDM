import requests #HTTP Library
import tweepy   #This library let us tweet,retweet, send and receive direct messages 
import json     #For keeping json infos we get from API, in our PC

#Twitter stuff
consumer_key = "CONSUMER KEY YOU GET FROM: https://developer.twitter.com/en/apps"
consumer_secret = "CONSUMER SECRET YOU GET FROM: https://developer.twitter.com/en/apps" 
access_token = "ACCESS TOKEN YOU GET FROM: https://developer.twitter.com/en/apps"
access_token_secret = "ACCESS TOKEN SECRET YOU GET FROM: https://developer.twitter.com/en/apps"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Authorizing API
auth.set_access_token(access_token, access_token_secret)  #Authorizing API
api = tweepy.API(auth)  

#JSON
url = "<EXCHANGE RATE AND CURRENCY JSON API WEBSITE>" # Getting JSON infos from Currency API
response = requests.get(url)
data = response.json()

#######################################
guncelleme = data["Güncelleme Tarihi"]# Getting what you want from url
alis = data["Gram Altın"]["Alış"]     # (This is from my project, example codes in Turkish)
#######################################

a = "Alış fiyatı:" + alis             # Message we want to send in DM later

#veri.json is a JSON file I created in my PC

with open("veri.json") as f:            #          
    json_data = json.load(f)            #   Keeping API's JSON infos in our pc 
buying = json_data["gram"]["alış"]      #           with creating another JSON file in our PC

if alis != buying:                                              #
    json_data["gram"]["alış"] = alis                            # If statement that compares url info to ours.
    with open("veri.json", "w") as f:                           #  If url info and our info isn't matched
        json.dump(json_data, f)                                 #   (means; if currency changed), it will update our JSON

    #api.send_direct_message(recipient_id="<TWITTER USER ID>", text=a)  # Program will DM us new currency rate
    print('Message sent!')

else:
    print("Currency isn't changed!")