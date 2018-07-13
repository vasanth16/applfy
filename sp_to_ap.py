#Vasanth Rajasekaran
import spotipy
import requests
from spotipy import util as util
import json

def get_spotify_track(obj, song_link): # takes in the spotify link 
    trackName = obj.track(song_link)
    layer1 = trackName['artists'] #These layers are how I parsed through the json, this might not be the cleanest way to do this but it works
    layer2 = layer1[0]
    artists = layer2['name']    
    return (trackName['name'], artists) # sends back the artist and the track name 

def get_spotify_link(token,track,artist): # takes in the track name and artist name 
    yes = spotipy.Spotify(auth=token)
    searched = yes.search(q='artist:' + artist + ' track:' + track,type='track',market='US')
    try:
        layer1 = searched['tracks'] # goes through all the different layers of the JSON thats sent back 
        layer2 = layer1['items']
        lay3 = layer2[0]
        lay4 = lay3 ['external_urls']
        link = lay4['spotify'] # this is the link thats taken from all the json
        print (link) 
    except:
        print ("Oops there was an error, Make sure you enter the params correctly") # error message

