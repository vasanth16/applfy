#Vasanth Rajasekaran

import spotipy
import requests
from spotipy import util as util
import json

token = util.prompt_for_user_token(username="vvvv110", scope=None, client_id='b72f1627c1614421adc803989b16b19b', client_secret='268867b74222405baf2a176b3022d66e', redirect_uri='https://example.com/callback/', cache_path=None)
    #token2 = util.prompt_for_user_token(username="vvvv110", scope=None)


def get_spotify_track(obj, song_link):
    trackName = obj.track(song_link)
    layer1 = trackName['artists']
    layer2 = layer1[0]
    artists = layer2['name']    
    return (trackName['name'], artists)

def get_spotify_link(track,artist):
    yes = spotipy.Spotify(auth=token)
    searched = yes.search(q='artist:' + artist + ' track:' + track,type='track',market='US')
    try:
        layer1 = searched['tracks']
        layer2 = layer1['items']
        lay3 = layer2[0]
        lay4 = lay3 ['external_urls']
        link = lay4['spotify']
        print (link)
    except:
        print ("Oops there was an error, Make sure you enter the params correctly")


def main ():
    yes = spotipy.Spotify(auth=token)
    song_link = input('Please input your spotify link')
    spotify = get_spotify_track(yes,song_link)
    print ("Your track is",spotify[0], "by ", spotify[1])

