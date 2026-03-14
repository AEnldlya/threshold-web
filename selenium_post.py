#!/usr/bin/env python3
"""
Use Selenium to automate uploads to Instagram, TikTok, YouTube.
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_ANIMATED.mp4'

def upload_to_tiktok():
    """Upload to TikTok via Selenium."""
    print("\n[TIKTOK] Starting upload...")
    
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.tiktok.com/upload')
        
        print("[TIKTOK] Opened upload page")
        time.sleep(3)
        
        # Find file input
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(os.path.abspath(VIDEO_FILE))
        
        print("[TIKTOK] File selected, waiting for processing...")
        time.sleep(5)
        
        # Add caption
        caption_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[contenteditable="true"]'))
        )
        caption_field.click()
        caption_field.send_keys("I got hired in 3 minutes #storytelling #horror #ai")
        
        print("[TIKTOK] Caption added")
        time.sleep(2)
        
        # Click post button
        post_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]")
        post_btn.click()
        
        print("[TIKTOK] ✓ Posted!")
        time.sleep(3)
        driver.quit()
        return True
        
    except Exception as e:
        print(f"[TIKTOK] ✗ Error: {e}")
        return False

def upload_to_instagram():
    """Upload to Instagram via Selenium."""
    print("\n[INSTAGRAM] Starting upload...")
    
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.instagram.com')
        
        print("[INSTAGRAM] Opened Instagram")
        time.sleep(3)
        
        # Login would be here - skipping for now
        # Would need email/password
        
        print("[INSTAGRAM] ✗ Needs manual login")
        driver.quit()
        return False
        
    except Exception as e:
        print(f"[INSTAGRAM] ✗ Error: {e}")
        return False

def upload_to_youtube():
    """Upload to YouTube via Selenium."""
    print("\n[YOUTUBE] Starting upload...")
    
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.youtube.com/upload')
        
        print("[YOUTUBE] Opened upload page")
        time.sleep(3)
        
        # Check if logged in
        try:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(os.path.abspath(VIDEO_FILE))
            
            print("[YOUTUBE] File selected")
            time.sleep(5)
            
            # Add title
            title_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'textbox'))
            )
            title_field.clear()
            title_field.send_keys("The Job Interview - A Dark Story | AI Story")
            
            print("[YOUTUBE] Title added")
            time.sleep(2)
            
            print("[YOUTUBE] ✓ File ready for publish (finish manually)")
            time.sleep(3)
            
        except Exception as e:
            print(f"[YOUTUBE] ✗ Not logged in or upload page blocked: {e}")
        
        driver.quit()
        return False
        
    except Exception as e:
        print(f"[YOUTUBE] ✗ Error: {e}")
        return False

if __name__ == '__main__':
    print("="*70)
    print("SELENIUM AUTOMATED UPLOADS")
    print("="*70)
    
    print(f"\nVideo: {os.path.basename(VIDEO_FILE)}")
    print(f"Size: {os.path.getsize(VIDEO_FILE)/1024:.1f}KB")
    
    # Try uploads
    upload_to_tiktok()
    upload_to_instagram()
    upload_to_youtube()
    
    print("\n" + "="*70)
    print("Attempted automated uploads")
    print("="*70)

