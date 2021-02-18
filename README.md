# spotify_playlist
Get the top 100 songs from Billboard, for an inputted date, generate a Spotify URI list and a playlist

If you create or already have a Spotify account, you can create an app in the developer environment:

https://developer.spotify.com/dashboard/applications

by simply clicking on the button "Create App". Please be sure to add "http://127.0.0.1:9090" in the "Website" and
"Redirect URIs" fields.

The code should be able to 

1) scrape the top 100 songs for that date from Billboard
2) authenticate you with Spotify using Spotipy
3) find the Spotfify URIs (Uniform Resource Identicators) for the songs and generate a list thereof
4) create a Spotify playlist and add the songs

