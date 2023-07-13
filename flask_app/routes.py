from flask import jsonify, request
from spotify_to_yt import Conversor
from flask_app import app
import asyncio
import nest_asyncio
import time
nest_asyncio.apply()

@app.route('/spt_to_ytb', methods=['POST'])
def convert_to_ytb_from_spt():
    convert = request.get_json()
    link = convert["playlist_link"]
    if link:
        youtube_music_link = asyncio.run(conversion_task(link))
        print(youtube_music_link)
        return jsonify(ytb_music_link=youtube_music_link), 200
    return jsonify(error="Empty link")


async def conversion_task(link):
    conversor = Conversor("oauth.json", link)

    playlist_link = conversor.create_ytbmusic_playlist()
    time.sleep(10)
    return playlist_link


  