from abc import ABC, abstractmethod
from typing import List

from core.entities import Video


class YouTubeAPI(ABC):
    @abstractmethod
    def get_playlist_videos(self, playlist_url: str) -> List[Video]:
        """プレイリスト内の動画を取得"""
        raise NotImplementedError(
            "Subclasses must implement get_playlist_videos method."
        )

    @abstractmethod
    def download_video(self, video: Video, file_path: str):
        """動画をダウンロード"""
        raise NotImplementedError("Subclasses must implement download_video method.")
