# Captcha Bypass with Playwright and Groq Speech-to-Text API

This project automates the resolution of CAPTCHAs on web pages using Playwright for browser automation and the Groq API for audio transcription. The idea is to simulate a flow where, after entering a tracking code, the system downloads the CAPTCHA audio, transcribes its content, and automatically inserts it into the form to proceed with the search.

---

## Technologies Used

- **Python 3.x**
- **Playwright (async):** For browser automation.
- **aiofiles:** Asynchronous file handling.
- **Groq API:** For audio transcription (Speech-to-Text).
- **AsyncIO:** For executing the program flow asynchronously.

---

## Prerequisites

- Python 3.x installed.
- Project dependencies installed (refer to the `requirements.txt` file if available, or install them manually):
  - `playwright`
  - `aiofiles`
  - `groq` (or the corresponding SDK)
- Install Playwright browsers (e.g., `playwright install`).
- Configure constants and environment variables (such as `GROQ_API_KEY`) in the `app/constants.py` file.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:your_username/YourRepository.git
   cd YourRepository
   ```

2. **Create a virtual environment (optional, but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install the Playwright browsers:**

   ```bash
   playwright install
   ```

---

## Usage

1. **Configure your variables and constants:**  
   In the `app/constants.py` file, define the URLs, tracking codes, and other parameters needed for automation, such as the selectors for page elements.

2. **Run the main script:**

   ```bash
   python main.py
   ```

   The script will:
   - Open the browser in non-headless mode.
   - Navigate to the configured URL.
   - Fill in the tracking code field.
   - Download the CAPTCHA audio, transcribe it, and fill in the CAPTCHA field.
   - Click the submit button and end the process.

---

## Project Structure

```
YourProject/
├── app/
│   ├── scrapping/
│   │   └── scrapper.py      # Functions for downloading, transcribing, and solving the CAPTCHA.
│   ├── constants.py         # Configurations and page selectors.
│   ├── logger_config.py     # Logger configuration for logging information.
│   └── utils/
│       └── path_utils.py    # Utility functions for handling temporary files.
├── main.py                  # Main script that orchestrates the automation.
└── requirements.txt         # Project dependencies.
```

---

## W.I.P.

**Work In Progress:**  
I am planning to evolve this project into an API that will return order updates. Future improvements will include API endpoints to enable real-time tracking and retrieval of order status information.

---

## Contributions

Contributions are welcome! I am actively considering improvements, so feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).
