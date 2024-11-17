from utils.filename_sanitizer import FilenameSanitizer


def test_sanitize_filename_special_characters():
    """FilenameSanitizer.sanitizeメソッドのテスト"""
    special_title = 'This:Title/Has*All|Special?Characters<>"'
    expected_output = "This_Title_Has_All_Special_Characters___"

    sanitized_title = FilenameSanitizer.sanitize(special_title)
    assert sanitized_title == expected_output
