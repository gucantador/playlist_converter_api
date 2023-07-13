from ytmusicapi import YTMusic
import re
from spotify_to_yt.spotify_api import Spotify_api_handler
import asyncio

class Conversor():
    
    def __init__(self, auth, spt_playlist_to_convert_link):
        self.auth = auth 
        self.loop = asyncio.get_event_loop()       
        self.ytmusic = self.loop.run_until_complete(self._load_ytb())
        self.spotify = self.loop.run_until_complete(self._load_spotify()) #TODO  Pass the client id and stuff to make it more generic
        self.playlist_id = self._playlist_parser(spt_playlist_to_convert_link)
        self.tracks = self.spotify.get_tracks_from_playlist(self.playlist_id)
        self.playlist_name = self.spotify.get_playlist_name(self.playlist_id)
        
    def test_ytb(self):
        playlistId = self.ytmusic.create_playlist("teste2", "test description")
        search_results = self.ytmusic.search("Oasis Wonderwall")
        self.ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
        return playlistId
        
    def _playlist_parser(self, playlist_link):
        match = re.search(r"/playlist/(?P<playlist_id>.*)\?", playlist_link)
        if match:
            return match.group("playlist_id")
        else:
            playlist_id = re.search(r"/playlist/(?P<playlist_id>.*)$", playlist_link).group("playlist_id")
            return playlist_id
        
    async def _load_ytb(self):
        return YTMusic(self.auth)
    
    async def _load_spotify(self):
        return Spotify_api_handler()
    
    def _change_playlist_privacy_status(self, playlist_id):
        self.ytmusic.edit_playlist(playlistId=playlist_id,privacyStatus="PUBLIC")
    
    def _convert_playlist(self):
        playlist_id = self.ytmusic.create_playlist(self.playlist_name, "Playlist converted from Online Conversor.")
        for i in range(len(self.tracks)):
            print(self.tracks[i])
            track_name = self.tracks[i]["track_name"]
            artists = ""
            item =0
            for item in range(len(self.tracks[i]["artists"])):
                print(self.tracks[i])
                artists += self.tracks[i]["artists"][item] + " "
            try:
                search_results = self.ytmusic.search(f"{track_name} {artists}")
                self.ytmusic.add_playlist_items(playlist_id, [search_results[0]['videoId']])
            except:
                print(f"Could not find {track_name} {artists}")
        self._change_playlist_privacy_status(playlist_id)
        return playlist_id
    
    
    
    def create_ytbmusic_playlist(self):
        return f'https://music.youtube.com/playlist?list={self._convert_playlist()}'