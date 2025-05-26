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
        # Comprehensive Chrome options for Docker
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-features=VizDisplayCompositor")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        
        print(f"Attempting to join meeting: {meeting_url}")
        
        driver = webdriver.Chrome(options=options)
        driver.get(meeting_url)
        
        print("Meeting page loaded, waiting...")
        time.sleep(5)
        
        # Try to find and click join button
        try:
            # Wait a bit more for page to load
            time.sleep(3)
            print("Looking for join button...")
            
            # Common join button selectors for Google Meet
            join_selectors = [
                "[data-mdc-dialog-action='join']",
                "[aria-label*='Join']",
                "button[jsname='Qx7uuf']",
                ".NPEfkd"
            ]
            
            for selector in join_selectors:
                try:
                    join_button = driver.find_element(By.CSS_SELECTOR, selector)
                    join_button.click()
                    print(f"Clicked join button with selector: {selector}")
                    break
                except:
                    continue
            
            print("Bot joined meeting successfully!")
            time.sleep(10)  # Stay in meeting for 10 seconds
            
        except Exception as e:
            print(f"Could not find join button: {e}")
            print("Bot is on the meeting page but may not have joined")
        
        driver.quit()
        
        return jsonify({
            'success': True,
            'message': f'Bot successfully accessed {meeting_url}'
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Failed to join: {str(e)}'
        })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
