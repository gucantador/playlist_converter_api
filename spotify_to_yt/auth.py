import json
import os
import re

class YTBAuth():
    
    def __init__(self, user_id, access_token, expires_in, refresh_token, expires_at):
        self.user_id = user_id
        self.access_token = access_token
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.expires_at = expires_at
        self.path = self._get_path()
        self.file_name = None
    
    def create_oauth_json(self):
        data = {
            "access_token": self.access_token,
            "expires_in": self.expires_in,
            "refresh_token": self.refresh_token,
            "scope": "https://www.googleapis.com/auth/youtube",
            "token_type": "Bearer",
            "expires_at": self.expires_at
        }
        
        file_name = f"{self.user_id}_oauth.json"
        self.file_name = file_name
        file_path = os.path.join(self.path, file_name)
        
        with open(file_path, "w") as file:
            json.dump(data, file)
            
    def _get_path(self):
        absolute_path = os.path.abspath(__file__)
        substring_to_remove_linux = r"spotify_to_yt/auth.py"
        path = re.sub(rf"\\?{re.escape(substring_to_remove_linux)}$", "", absolute_path)          
            
        return path