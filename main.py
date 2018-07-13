from sp_to_ap import get_spotify_track
from sp_to_ap import get_spotify_link

from get_apple_track import get_apple_track
from get_apple_track import get_apple_url

import spotipy
from spotipy import util as util
import itunes


def main(): # main function where 
    link = input ("Please enter song link") # takes in the song link
    if 'spotify' in link: # to see if its a spotify link or itunes link 
        username = input('Please enter your spotify user name') #takes the input of user name to use in the API request 
        token = util.prompt_for_user_token(username=username, scope=None, client_id='b72f1627c1614421adc803989b16b19b', client_secret='268867b74222405baf2a176b3022d66e', redirect_uri='https://example.com/callback/',cache_path=None)
        yes = spotipy.Spotify(auth=token) # creates the token 
        spotify = get_spotify_track(yes,link) #sends it to the spotify track 
        trackname = spotify[0] #parse the tuple that comes back 
        artist = spotify[1]
        print (trackname,artist) # this is just to check 
        apple = get_apple_url(trackname,artist) # send the name and artist to get the itunes url
        return apple 
    else:
        username = input('Please enter your spotify user name') # this else statement does the same thing as as above but for an itunes link
        token = util.prompt_for_user_token(username=username, scope=None, client_id='b72f1627c1614421adc803989b16b19b', client_secret='268867b74222405baf2a176b3022d66e', redirect_uri='https://example.com/callback/',cache_path=None)
        app = get_apple_track(link)
        trackname = app[0]
        artist = app[1]
        spot = get_spotify_link(token,trackname,artist)# need to send in the token this time
        return spot

main()