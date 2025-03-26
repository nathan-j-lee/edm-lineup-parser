import json

# Load the JSON data from file
with open("output.json", 'r') as file:
    data = json.load(file)

# Get user input for the desired genre
desired_genre = input("Enter the genre you are looking for: ").strip().lower()

# Filter and display artists that match the genre
matching_artists = {"artists": []}

for artist in data.get("artists", []):
    genres = artist.get("genres", [])
    if any(desired_genre in genre.lower() for genre in genres):
        # grab name
        name = artist.get("name")
        # genres already grabbed
        #grab top tracks
        top_tracks = artist.get("top_tracks")
        popularity = artist.get("popularity_score")
        artist_dict = {
            "name": name,
            "genres": genres,
            "top_tracks": top_tracks,
            "popularity_score": popularity
        }
        matching_artists["artists"].append(artist_dict)

# Sort artists by popularity (highest first)
sorted_artists = sorted(matching_artists["artists"], key=lambda x: x["popularity_score"], reverse=True)

with open("sorted_output.json", 'w') as file:
    json.dump(sorted_artists, file, indent=4)
