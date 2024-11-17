from typing import List

from core.entities import Video
from core.interfaces import YouTubeAPI


class YouTubeService:
    def __init__(self, youtube_api: YouTubeAPI):
        self.youtube_api = youtube_api

    def get_playlist_videos(self, playlist_url: str) -> List[Video]:
        """プレイリスト内の動画を取得"""
        return self.youtube_api.get_playlist_videos(playlist_url)

    def download_video(self, video: Video, file_path: str):
        """動画をダウンロード"""
        self.youtube_api.download_video(video, file_path)
