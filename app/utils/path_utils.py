import os
import tempfile
import re


def get_tmp_file_path(suffix: str = '.wav') -> str:
    """
    Generates a temporary file path in the 'tmp' directory.

    """
    tmp_dir = os.path.join(os.getcwd(), 'tmp')
    os.makedirs(tmp_dir, exist_ok=True)
    return tempfile.mktemp(suffix=suffix, dir=tmp_dir)


def clean_parsing_string(transcription: str) -> str:
    """
    Extracts the captcha code from the transcription string by capturing:
      - the digits that follow the word "Número" (case-insensitive), e.g. "Número 1" captures "1", and
      - any uppercase letter that is immediately followed by a space, a comma, a period, or the end of the string.

    The captured tokens are concatenated in the order they appear.
    """
    # Pattern explanation:
    #   (?:(?i:número)\s+(\d+))
    #       -> Matches "Número" (case-insensitive) followed by whitespace and one or more digits,
    #          capturing the digits in group 1.
    #   | ([A-Z])(?=[ ,.]|$)
    #       -> Matches a single uppercase letter (group 2) that is immediately followed by a space, comma, period, or the end of the string.
    pattern = r'(?:(?i:número)\s+(\d+))|([A-Z])(?=[ ,.]|$)'
    matches = re.finditer(pattern, transcription)

    code_parts = []
    for match in matches:
        if match.group(1):
            code_parts.append(match.group(1))
        elif match.group(2):
            code_parts.append(match.group(2))

    return ''.join(code_parts)
