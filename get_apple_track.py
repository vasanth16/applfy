#Felix Cui

import itunes

def get_apple_track(song_url):
    ind = song_url.index('?i=') + 3 #get index of true ID
    true_id = song_url[ind:]
    track = itunes.lookup(int(true_id))

    return (track.name, str(track.artist)[8:])

#print(get_apple_track('https://itunes.apple.com/us/album/banana-breeze/1403834927?i=1403834930'))
