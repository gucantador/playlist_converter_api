import requests
#from spotify_to_yt.constants import CLIENT_ID, CLIENT_SECRET
import os


class Spotify_api_handler():
    
    def __init__(self):
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.access_token = self._get_spotify_access_token()

    def _get_spotify_access_token(self):
        """Gets a Spotify access token using the client credentials grant."""

        url = "https://accounts.spotify.com/api/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(url, data=data)
        if response.status_code != 200:
            raise Exception("Error getting Spotify access token")
        return response.json()["access_token"]
    
    def _get_playlist_items(self, playlist_link):

        response = requests.get(
            f"https://api.spotify.com/v1/playlists/{playlist_link}/tracks",
            headers={"Authorization": f"Bearer {self.access_token}"},
        )

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(response.content)
        
    def _get_playlist(self, playlist_link):
        
        response = requests.get(
            f"https://api.spotify.com/v1/playlists/{playlist_link}",
            headers={"Authorization": f"Bearer {self.access_token}"},
        )

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(response.content)
    
    def _arrange_tracks(self, items):
        songs = []
        artists = []
        for song in range(len(items)):
            songs.append(items[song]["track"]["name"])
            
        for artist in range(len(items)):
            inside_artists = items[artist]["track"]["artists"]

            for i in range(len(inside_artists)):
                art = []
                for x in range(len(inside_artists)):
                    art.append(inside_artists[x]["name"])
                artists.append(art)
        tracks = []
        
        for j in range(len(songs)):
            track = {"track_name":songs[j],"artists":artists[j]}
            tracks.append(track)
            
        return tracks
    
    def _create_song_artist_dict(self, songs, artists):
        playlist = []
        for song, artist_list in zip(songs, artists):
            artist_names = [artist['name'] for artist in artist_list]
            playlist.append({'track_name': song, 'artists': artist_names})
        return playlist

    def get_tracks_from_playlist(self, playlist_link):
        playlist = self._get_playlist_items(playlist_link)
        items = playlist["items"]
        
        songs = []
        artists = []
        for song in range(len(items)):
            songs.append(items[song]["track"]["name"])
            
        for artist in range(len(items)):
            inside_artists = items[artist]["track"]["artists"]
            artists.append(inside_artists)
        
        return self._create_song_artist_dict(songs, artists)

    def get_playlist_name(self, playlist_link):
        playlist = self._get_playlist(playlist_link)
        return playlist["name"]