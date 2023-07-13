# from spotify_to_yt import Conversor

# conversor = Conversor("oauth.json", "https://open.spotify.com/playlist/0qfKUajJMUNelvbKGSJLls")
# print(conversor.create_ytbmusic_playlist())

# from spotify_to_yt.spotify_api import Spotify_api_handler

# x = Spotify_api_handler()
# print(x.get_tracks_from_playlist("0qfKUajJMUNelvbKGSJLls"))

from spotify_to_yt import YTBAuth

x = YTBAuth(2,3,4,5,6)

print(x.create_oauth_json())