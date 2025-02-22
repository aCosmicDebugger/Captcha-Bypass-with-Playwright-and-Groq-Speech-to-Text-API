import aiofiles
from urllib.parse import urljoin
from app.logger_config import logger
from app.constants import (
    TRANSCRIPTION_MODEL,
    TRANSCRIPTION_PROMPT,
    TRANSCRIPTION_LANGUAGE,
    GROQ_API_KEY,
)

from app.utils.path_utils import get_tmp_file_path, clean_parsing_string
from playwright.async_api import Page
from groq import Groq


async def download_audio(page: Page) -> str:
    """
    Downloads the CAPTCHA audio by retrieving the href attribute from the anchor element
    and performing an HTTP GET request to download the audio file.
    """
    audio_href = await page.get_attribute('a.captcha_play_button', 'href')
    if not audio_href:
        logger.error(
            'Error: Unable to retrieve audio URL from the href attribute.'
        )
        return None

    absolute_audio_url = urljoin(page.url, audio_href)
    logger.info(f'Audio URL found: {absolute_audio_url}')

    audio_path = get_tmp_file_path(suffix='.wav')
    response = await page.request.get(absolute_audio_url)

    if response.status == 200:
        async with aiofiles.open(audio_path, 'wb') as f:
            await f.write(await response.body())
        logger.info(f'Audio downloaded and saved at: {audio_path}')
        return audio_path
    else:
        logger.error(
            f'Error downloading audio, status code: {response.status}'
        )
        return None


async def transcribe_audio(audio_path: str) -> str:
    """
    Sends the audio to the Groq API and returns the transcription.
    """

    client = Groq(api_key=GROQ_API_KEY)

    with open(audio_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            model=TRANSCRIPTION_MODEL,
            prompt=TRANSCRIPTION_PROMPT,
            file=audio_file,
            language=TRANSCRIPTION_LANGUAGE,
        )

    logger.info(transcription.text)
    clean_text = clean_parsing_string(transcription.text)

    logger.info(f'Transcription received: {clean_text}')
    return clean_text


async def solve_captcha(page: Page) -> str:
    """
    Downloads the CAPTCHA audio, transcribes it, and returns the text.
    """
    logger.info('Starting process to solve the CAPTCHA...')
    audio_path = await download_audio(page)
    if not audio_path:
        logger.error('Error obtaining the CAPTCHA audio.')
        return None

    captcha_text = await transcribe_audio(audio_path)
    if captcha_text:
        logger.info(f'CAPTCHA solved: {captcha_text}')
    else:
        logger.error('Error solving the CAPTCHA.')
    return captcha_text
