import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open("secret.json",'r') as secret:
    data = json.load(secret)
    client_ID = data["client_ID"]
    client_secret = data["client_secret"]


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_ID,
                                                           client_secret=client_secret))

results = sp.search(q='Young Harleezy', limit=3)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['artists'][0]['name'], " – ", track['name'])