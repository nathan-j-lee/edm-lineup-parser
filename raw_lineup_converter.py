import re

# Read the artist names from the input text file
with open('edc_artists.txt', 'r') as file:
    artist_text = file.read().strip()

# Clean up the artist names (remove parentheses, "B2B" and "vs.")
artist_names = artist_text.split()

cleaned_artist_list = []

# Process each artist name
for artist in artist_names:
    # Remove content inside parentheses and the parentheses themselves
    artist = re.sub(r'\(.*?\)', '', artist).strip()

    # If the artist has "B2B" or "vs.", split it and add each artist separately
    if "B2B" in artist:
        separated_artists = [a.strip() for a in artist.split("B2B")]
        cleaned_artist_list.extend(separated_artists)
    elif "vs." in artist:
        separated_artists = [a.strip() for a in artist.split("vs.")]
        cleaned_artist_list.extend(separated_artists)
    else:
        cleaned_artist_list.append(artist)

# Remove any unwanted empty strings or extra spaces
cleaned_artist_list = [artist for artist in cleaned_artist_list if artist]

# Write the cleaned-up artist list into a new text file
with open('edc_cleaned_artists.txt', 'w') as output_file:
    for artist in cleaned_artist_list:
        output_file.write(artist + '\n')  # Write each artist on a new line

print("Cleaned artist list has been saved to 'edc_cleaned_artists.txt'.")