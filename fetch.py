from requests import get
from requests.exceptions import ConnectionError


class Fetch:
    def __init__(self) -> None:
        self._saavn_url = "https://saavn.dev/api"

    def from_saavn(self, query: str) -> dict:
        status = {"code": 200, "message": "", "data": []}
        songs = []
        search_url = self._saavn_url + f"/search/songs?query={query}"
        try:
            res = get(search_url)
            resData = res.json()
            success = resData["success"]
        except ConnectionError:
            errorText = "<b><red>Connection Error</red></b> - Check Your Internet"
            status["code"] = 400
            status["message"] = errorText
            return status

        if not success:
            status["code"] = 404
            status["message"] = "<b>Song not found!</b>"

        results = resData["data"]["results"]
        # Append songs info - stream url and song name with artist - in songs list
        # to show in the dialog box for selection
        for result in results:
            streamUrl = result["downloadUrl"][-2]
            songName = result["name"]
            songArtist = result["artists"]["primary"][0]["name"]
            title = f"{songArtist} - {songName}"
            streamInfo = {
                "name": songName,
                "artist": songArtist,
                "url": streamUrl["url"],
            }
            dataTuple = (streamInfo, title)
            songs.append(dataTuple)

        status["data"] = songs
        return status
