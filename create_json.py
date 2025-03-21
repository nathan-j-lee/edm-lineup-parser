import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm import tqdm
import os

client_credentials_manager = SpotifyClientCredentials(client_id="af2daf9775cd4640b70b73df6fd2fbeb", client_secret="0ac4021a659744a3a5b7b9bedd26e28b")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=30)

with open("cleaned_artists.txt", 'r') as file:
    line = file.read().split(sep="\n")

artist_array = line

data = {"artists": []}

for artist in tqdm(artist_array, desc="Processing artists genres and tracks", ncols=100):
    result = sp.search(q=artist, type="artist", limit=1)
    if result["artists"]["items"]:
        #get first search result
        artist_id = result['artists']['items'][0]['id']
        #get genres for each artist
        artist_genres = sp.artist(artist_id)['genres']
        #get top tracks for each artist
        top_tracks = sp.artist_top_tracks(artist_id)
        track_list = []
        for track in top_tracks['tracks']:
            track_list.append(track["name"])
        #store data in dict
        artist_data = {
            "name": artist,
            "genres": artist_genres,
            "top_tracks": track_list
        }
        data["artists"].append(artist_data)
    else:
        print(artist, "not found on Spotify!")
    
with open("output.json", 'w') as file:
    json.dump(data, file, indent=4)