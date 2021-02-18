from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify
import os
import requests

# please use your Spotify Client ID and Client Secret here

spotify_client_id = os.environ.get('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

billboard_url = "https://www.billboard.com/charts/hot-100/"

# from Billboard, get the top 100 songs for the date you enter through the input

date = input("What year would you like to travel to? Type the date in the following format: YYYY-MM-DD ")

contents = requests.get(billboard_url+date)

web_contents = contents.text

soup = BeautifulSoup(web_contents, "html.parser")

titles = soup.find_all(class_="chart-element__information__song text--truncate color--primary")

print(len(titles))

song_titles = [title.getText() for title in titles]

print(song_titles)

# authenticate with Spotify using Spotipy
# if you wish to use this code, please be sure to fill in your

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:9090",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path='token.txt'
    )
)
user_id = sp.current_user()["id"]


# get the Spotify URI (Uniform Resource Identifier) for each of the billboard song titles
# and create a URI list
year = date.split("-")[0]

uri_list = []
for song_title in song_titles:
    result = sp.search(q=f'track: {song_title} year: {year}', type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        uri_list.append(uri)
    except IndexError:
        continue

print(uri_list)

# create a Spotify playlist
my_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(my_playlist)
# and add the songs
sp.playlist_add_items(playlist_id=my_playlist['id'], items=uri_list)


















