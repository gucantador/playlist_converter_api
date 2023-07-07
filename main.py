
# from spotify_to_yt import Spotify_api_handler


# conversor = Spotify_api_handler()
# print(conversor.get_tracks_from_playlist("5GCn30YVUUxWolZb89iSra"))

#from ytmusicapi import YTMusic
#ytmusic = YTMusic("oauth.json")

from spotify_to_yt import Conversor

conversor = Conversor("oauth.json", "https://open.spotify.com/playlist/7exi5sHBn7DGH1S1kECOat?si=IkFmfhvvTceATX6O-aJtLA")
print(conversor.create_ytbmusic_playlist())
