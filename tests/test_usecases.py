from unittest.mock import MagicMock

import pytest

from core.entities import Video
from core.usecases import YouTubeService


def test_youtube_service_get_playlist_videos():
    """YouTubeServiceのget_playlist_videosメソッドのテスト"""
    mock_api = MagicMock()
    mock_api.get_playlist_videos.return_value = [
        Video(video_id="abc123", title="Video 1"),
        Video(video_id="def456", title="Video 2"),
    ]

    youtube_service = YouTubeService(mock_api)

    videos = youtube_service.get_playlist_videos("mock_playlist_url")
    assert len(videos) == 2
    assert videos[0].video_id == "abc123"
    assert videos[0].title == "Video 1"


def test_youtube_service_download_video():
    """YouTubeServiceのdownload_videoメソッドのテスト"""
    mock_api = MagicMock()
    mock_api.download_video.return_value = None

    youtube_service = YouTubeService(mock_api)

    video = Video(video_id="abc123", title="Video 1")
    file_path = "./downloads/abc123_Video_1.mp4"

    youtube_service.download_video(video, file_path)
    mock_api.download_video.assert_called_once_with(video, file_path)


def test_youtube_service_invalid_url():
    """YouTubeServiceのget_playlist_videosメソッドで無効なURLを渡した場合のテスト"""
    mock_api = MagicMock()
    mock_api.get_playlist_videos.side_effect = ValueError("Invalid playlist URL")

    youtube_service = YouTubeService(mock_api)

    with pytest.raises(ValueError, match="Invalid playlist URL"):
        youtube_service.get_playlist_videos("invalid_url")


def test_youtube_service_empty_playlist():
    """YouTubeServiceのget_playlist_videosメソッドで空のプレイリストを取得した場合のテスト"""
    mock_api = MagicMock()
    mock_api.get_playlist_videos.return_value = []  # 空のプレイリスト

    youtube_service = YouTubeService(mock_api)

    videos = youtube_service.get_playlist_videos("valid_url")
    assert videos == []  # 結果が空であることを確認
