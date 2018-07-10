import spotipy
import requests
from spotipy import util as util

token = util.prompt_for_user_token(username="vvvv110", scope=None, client_id='b72f1627c1614421adc803989b16b19b', client_secret='268867b74222405baf2a176b3022d66e', redirect_uri='https://example.com/callback/', cache_path=None)
    #token2 = util.prompt_for_user_token(username="vvvv110", scope=None)


def get_spotify_track():
    yes = spotipy.Spotify(auth=token)
    song_link = input('Please input your spotify link')
    trackName = yes.track(song_link)
    print(trackName['name'])
    


get_spotify_track()


