#Felix Cui
import itunes
import webbrowser as wb

def get_apple_track(song_url):
    try:
        ind = song_url.index('?i=') + 3 #get index of true ID
        true_id = song_url[ind:]
        track = itunes.lookup(int(true_id))
        return (track.name, str(track.artist)[8:])
    except:
        print ("Oops something went wrong")

def get_apple_url(name, artist):
    musician = itunes.search_artist(artist)
    realArtist = musician[0]
    for track in realArtist.get_tracks():
        name = str(name).lower()
        if name in str(track.name).lower():
            print (str(track.url))
            webbrowser.open(track.url[, new=0[, autoraise=True]])
    print('Song not found.')

