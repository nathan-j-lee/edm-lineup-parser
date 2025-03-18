import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id="af2daf9775cd4640b70b73df6fd2fbeb", client_secret="0ac4021a659744a3a5b7b9bedd26e28b")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=30)

with open("cleaned_artists.txt", 'r') as file:
    line = file.read().split(sep="\n")

artist_array = line

for artist in artist_array:
    artist_name = artist
    result = sp.search(q=artist_name, type="artist", limit=1)
    artist_id = result['artists']['items'][0]['id']
    artist_genres = sp.artist(artist_id)['genres']
    #print(type(artist_genres))
    print(artist + f": {artist_genres}")
    

    top_tracks = sp.artist_top_tracks(artist_id)
    for track in top_tracks['tracks']:
        print(track['name'])
    print("\n")