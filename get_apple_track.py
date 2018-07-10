#Felix Cui

import itunes

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
        if name in track.name:
            return str(track.url)
    print('Song not found.')

#print(get_apple_url('Never Letting Go', 'Vexento'))
#print(get_apple_track('https://itunes.apple.com/us/album/never-letting-go/1216722412?i=1216722500'))
