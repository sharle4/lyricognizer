import requests
import lyricsgenius
import re
import time
import os

# constant values.
genius = lyricsgenius.Genius("1AqF1vBdyL1PRwnyWdxgj8r2nBtBZBnHrJL9Y2azkdne04F-FzOUBzSyATmgGqKA")
BASE_URL = "https://api.genius.com"
CLIENT_ACCESS_TOKEN = "1AqF1vBdyL1PRwnyWdxgj8r2nBtBZBnHrJL9Y2azkdne04F-FzOUBzSyATmgGqKA"
ARTIST_NAME = "Soolking"
folder = "lyrics/soolking/raw/"
max_songs = 101
files = [fichier for fichier in os.listdir(folder) if os.path.isfile(os.path.join(folder, fichier))]
beg = len(files)

# send request and get response in json format.
def _get(path, params=None, headers=None):

    # generate request URL
    requrl = '/'.join([BASE_URL, path])
    token = "Bearer {}".format(CLIENT_ACCESS_TOKEN)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

def get_artist_songs(artist_id):
    top_song_ids = []
    page = 1

    while len(top_song_ids) < max_songs:
        path = f"artists/{artist_id}/songs"
        params = {'per_page': 20, 'sort': 'popularity', 'page': page}
        data = _get(path=path, params=params)

        if 'songs' not in data['response'] or len(data['response']['songs']) == 0:
            break

        song_ids = [song['id'] for song in data['response']['songs'] if ARTIST_NAME in song['artist_names']]
        top_song_ids.extend(song_ids)

        page += 1

    return top_song_ids[beg:max_songs]

def get_lyrics(song_id):
    time.sleep(1)
    return genius.lyrics(song_id)

# # # 

print("searching " + ARTIST_NAME + "'s artist id. \n")

# find artist id from given data.
find_id = _get("search", {'q': ARTIST_NAME})
for hit in find_id["response"]["hits"]:
   if hit["result"]["primary_artist"]["name"] == ARTIST_NAME:
       artist_id = hit["result"]["primary_artist"]["id"]
       break

print("-> " + ARTIST_NAME + "'s id is " + str(artist_id) + "\n")

print("getting song ids. \n")

# get all song ids and make a list.
song_ids = get_artist_songs(artist_id)

print(song_ids)
print("\n-> got all the song ids. \n")

print("getting lyrics of each song. \n")

# finally, make a full list of songs with lyrics and save them to text files.
for song_id in song_ids:
    print(song_id)
    lyrics = get_lyrics(song_id)
    
    if lyrics:
        lignes = lyrics.split('\n', 1)
        if len(lignes) == 1:
            continue
        lyrics = re.sub(r'You might also like', '', lignes[1][:-5])
        if lyrics[-1].isdigit:
            lyrics = lyrics[:-1]

        # Get the title of the song
        title = _get(f"songs/{song_id}")["response"]["song"]["title"]
        # Remove characters that might cause issues in file names
        title = re.sub(r'[\\/:"*?<>|]', '', title)
        # Write the lyrics to a text file
        with open(f"{folder}{title}.txt", "w", encoding="utf-8") as f:
            f.write(lyrics)

print("-> Finished! Check it out!") 