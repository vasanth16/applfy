from sp_to_ap import get_spotify_track
from sp_to_ap import get_spotify_link

from get_apple_track import get_apple_track
from get_apple_track import get_apple_url

import spotipy
import requests
from spotipy import util as util
import json
import itunes


def main():
    link = input ("Please enter song link")
    if 'spotify' in link:
        username = input('Please enter your user name')
        token = util.prompt_for_user_token(username=username, scope=None, client_id='b72f1627c1614421adc803989b16b19b', client_secret='268867b74222405baf2a176b3022d66e', redirect_uri='https://example.com/callback/', cache_path=None)
        yes = spotipy.Spotify(auth=token)
        spotify = get_spotify_track(yes,link)
        trackname = spotify[0] 
        artist = spotify[1]
        apple = get_apple_url(trackname,artist)
        return apple
    else:
        app = get_apple_track(link)
        trackname = app[0]
        artist = app[1]
        spot = get_spotify_link(trackname,artist)
        return spot

print(main())