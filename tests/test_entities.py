from core.entities import Video


def test_video_safe_filename():
    """Videoクラスのget_safe_filenameメソッドのテスト"""
    video = Video(video_id="abc123", title="Test:Video/Example*Title|?")

    safe_filename = video.get_safe_filename()
    assert safe_filename == "abc123_Test_Video_Example_Title__"
