import os
from typing import List

from pytubefix import Playlist, YouTube

from core.entities import Video
from core.interfaces import YouTubeAPI


class PytubeYouTubeAPI(YouTubeAPI):
    def get_playlist_videos(self, playlist_url: str) -> List[Video]:
        """プレイリスト内の動画を取得"""
        playlist = Playlist(playlist_url)
        return [
            Video(video_id=video.video_id, title=video.title)
            for video in playlist.videos
        ]

    def download_video(self, video: Video, file_path: str):
        """動画をダウンロード"""
        yt = YouTube(f"https://www.youtube.com/watch?v={video.video_id}")
        stream = yt.streams.get_highest_resolution()
        stream.download(
            output_path=os.path.dirname(file_path), filename=os.path.basename(file_path)
        )
