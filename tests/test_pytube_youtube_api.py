from unittest.mock import MagicMock, patch

from core.entities import Video
from infrastructure.pytube_youtube_api import PytubeYouTubeAPI


@patch("infrastructure.pytube_youtube_api.Playlist")
def test_get_playlist_videos(mock_playlist):
    """get_playlist_videosメソッドのテスト"""
    mock_video = MagicMock()
    mock_video.video_id = "abc123"
    mock_video.title = "Test Video"
    mock_playlist.return_value.videos = [mock_video]

    api = PytubeYouTubeAPI()
    videos = api.get_playlist_videos("https://example.com/playlist")

    assert len(videos) == 1
    assert isinstance(videos[0], Video)
    assert videos[0].video_id == "abc123"
    assert videos[0].title == "Test Video"


@patch("infrastructure.pytube_youtube_api.YouTube")
def test_download_video(mock_youtube):
    """download_videoメソッドのテスト"""
    mock_stream = MagicMock()
    mock_stream.get_highest_resolution.return_value = mock_stream
    mock_youtube.return_value.streams = mock_stream

    api = PytubeYouTubeAPI()
    video = Video(video_id="abc123", title="Test Video")
    api.download_video(video, "./downloads/test.mp4")

    mock_youtube.assert_called_once_with("https://www.youtube.com/watch?v=abc123")
    mock_stream.get_highest_resolution.assert_called_once()
    mock_stream.download.assert_called_once_with(
        output_path="./downloads", filename="test.mp4"
    )
