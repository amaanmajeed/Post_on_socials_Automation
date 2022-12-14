# WhatsApp Message Sender

A Python script that uses Selenium to automate the process of sending messages on WhatsApp. 

## Features
- Fast messaging: The script is able to send messages at a rapid pace, making it ideal for sending bulk messages.
- Customizable: You can specify the message text and recipient list in the script.

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://chromedriver.chromium.org/)

## Usage
1. Clone or download the repository.
2. Install the required libraries using pip: `pip install -r requirements.txt`
3. Update the `recipients` and `message` variables in the script with your desired values.
4. Run the script: `python whatsapp_sender.py`

## Notes
- Make sure that you have the latest version of Chrome installed on your machine.
- The script is set to run in headless mode (i.e., it will not open a browser window). If you want to see the browser window, remove the `--headless` flag in the `chrome_options` object.

## License
This project is licensed under the [MIT License](LICENSE).
