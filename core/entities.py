from pydantic import BaseModel, Field, field_validator

from utils.filename_sanitizer import FilenameSanitizer


class Video(BaseModel):
    video_id: str = Field(..., description="YouTubeの動画ID")
    title: str = Field(..., description="動画のタイトル")

    @field_validator("title", mode="before")
    @classmethod
    def sanitize_title(cls, title: str) -> str:
        """タイトルをファイルとして保存できるように変換"""
        return FilenameSanitizer.sanitize(title)

    def get_safe_filename(self) -> str:
        """動画の安全なファイル名を生成する"""
        safe_title = self.title
        return f"{self.video_id}_{safe_title}"
