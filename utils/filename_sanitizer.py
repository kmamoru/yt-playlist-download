import re


class FilenameSanitizer:
    @staticmethod
    def sanitize(string: str, repl: str = "_") -> str:
        """ファイル名として使用できるように変換"""
        return re.sub(r'[\/:*?"<>|]', repl, string)
