import json

# Load the JSON data from file
with open("output.json", 'r') as file:
    data = json.load(file)

# Get user input for the desired genre
desired_genre = input("Enter the genre you are looking for: ").strip().lower()

# Filter and display artists that match the genre
matching_artists = []

for artist in data.get("artists", []):
    genres = artist.get("genres", [])
    if any(desired_genre in genre.lower() for genre in genres):
        matching_artists.append(artist["name"])

# Display results
if matching_artists:
    print("\nArtists matching your genre:")
    for artist in matching_artists:
        print(f"- {artist}")
else:
    print("No artists found for this genre.")