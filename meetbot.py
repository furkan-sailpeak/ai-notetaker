from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/join', methods=['POST'])
def join_meeting():
    data = request.json
    meeting_url = data.get('meeting_url')
    
    try:
        # Chrome options
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        options.add_argument("--use-fake-ui-for-media-stream")
        
        # Selenium 4 automatically manages ChromeDriver
        driver = webdriver.Chrome(options=options)
        driver.get(meeting_url)
        time.sleep(10)  # Stay in meeting for 10 seconds
        driver.quit()
        
        return jsonify({
            'success': True,
            'message': f'Bot successfully joined {meeting_url}'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to join: {str(e)}'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
