import os
from dotenv import load_dotenv

load_dotenv()

# logs
LOG_DIR = 'app/logs'

# scrapping
URL = 'https://rastreamento.correios.com.br/app/index.php'
TRACK_CODE = 'ND488892487BR'
CODE_INPUT_FIELD = '#objeto'
CAPTCHA_AUDIO_SOURCE = 'a.captcha_play_button'

CAPTCHA_INPUT_FIELD = '#captcha'
SUBMIT_BUTTON = '#b-pesquisar'


# Configurações para transcrição de áudio
TRANSCRIPTION_MODEL = 'whisper-large-v3'
TRANSCRIPTION_PROMPT = (
    'Transcreva o áudio, sem usar pontuação ou espaço entre os caracteres.'
)
TRANSCRIPTION_LANGUAGE = 'pt'

# API KEY
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
