from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

class MeetingBot:
    def __init__(self):
        self.driver = None
        
    def setup_chrome(self):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--headless")
        
        # Let Selenium manage ChromeDriver automatically
        self.driver = webdriver.Chrome(options=options)
        
    def join_meeting(self, meeting_url):
        try:
            self.setup_chrome()
            self.driver.get(meeting_url)
            time.sleep(5)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

@app.route('/join', methods=['POST'])
def join_meeting():
    data = request.json
    meeting_url = data.get('meeting_url')
    
    bot = MeetingBot()
    success = bot.join_meeting(meeting_url)
    
    return jsonify({
        'success': success,
        'message': 'Bot joined meeting' if success else 'Failed to join'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
