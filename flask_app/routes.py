from flask import jsonify, request
from spotify_to_yt import Conversor, YTBAuth
from flask_app import app
import asyncio
import nest_asyncio
import time
nest_asyncio.apply()

@app.route('/spt_to_ytb', methods=['POST'])
def convert_to_ytb_from_spt():
    convert = request.get_json()
    link = convert["playlist_link"]
    auth = convert['auth']

    #  TODO add checking if the auth exists
    if not link:
        return jsonify(error='Empty link'), 400
    if not auth:
        return jsonify(error='No auth'), 400
    youtube_music_link = asyncio.run(conversion_task(auth, link))
    time.sleep(10)
    #  TODO find a way to remove the auth 
    return jsonify(ytb_music_link=youtube_music_link), 200
    


async def conversion_task(auth, link):
    conversor = Conversor(auth, link)

    playlist_link = conversor.create_ytbmusic_playlist()
    time.sleep(10)
    return playlist_link


@app.route('/ytb_auth', methods=['POST'])
def ytb_auth():
      auth_data = request.get_json()
      if auth_data:
        auth = YTBAuth(user_id=auth_data['user_id'], access_token=auth_data['access_token'], 
                        expires_in=auth_data['expires_in'], refresh_token=auth_data['refresh_token'], 
                        expires_at=auth_data['expires_at'])
        auth.create_oauth_json()
        return jsonify(file_name=auth.file_name), 200
      return jsonify(error='lack_of_data'), 400 
      