from core.usecases import YouTubeService
from infrastructure.pytube_youtube_api import PytubeYouTubeAPI


def main():
    playlist_url = input("Enter the playlist URL: ").strip()
    output_dir = input("Enter the output directory: ").strip()

    # 出力フォルダが存在しない場合は作成
    import os

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # サービスとAPIのインスタンス化
    youtube_api = PytubeYouTubeAPI()
    youtube_service = YouTubeService(youtube_api)

    # プレイリストの動画を取得
    videos = youtube_service.get_playlist_videos(playlist_url)
    print(f"Total videos: {len(videos)}")

    # 各動画をダウンロード
    for video in videos:
        file_path = f"{output_dir}/{video.get_safe_filename()}"
        if os.path.exists(file_path):
            print(f"Skipping {video.title}, already downloaded.")
            continue
        youtube_service.download_video(video, file_path)
        print(f"Downloaded: {file_path}")


if __name__ == "__main__":
    main()
