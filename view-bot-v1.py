from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random

# URL of the page to test (replace with your own test stream URL)
TEST_URL = "https://www.twitch.tv/your_channel_name"  # Example: your own Twitch stream

def setup_browser():
    """Set up a headless Chrome browser with basic configuration."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no visible browser)
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for compatibility
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")  # Mimic a real browser

    # Initialize the Chrome driver (ensure chromedriver is installed and in PATH)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def simulate_view(driver, url):
    """Simulate a single viewer by opening the URL and staying for a random duration."""
    try:
        print(f"Opening URL: {url}")
        driver.get(url)

        # Wait for the page to load (adjust based on platform)
        time.sleep(5)

        # Simulate watching for a random duration (30–120 seconds)
        watch_time = random.randint(30, 120)
        print(f"Watching for {watch_time} seconds...")
        time.sleep(watch_time)

        # Optional: Simulate a click (e.g., play button, if needed)
        try:
            play_button = driver.find_element(By.CSS_SELECTOR, "button[data-a-target='player-play-pause-button']")
            play_button.click()
            print("Clicked play button")
        except:
            print("No play button found or not needed")

    except Exception as e:
        print(f"Error during simulation: {e}")
    finally:
        driver.quit()

def main():
    """Main function to run the view simulation."""
    driver = setup_browser()
    simulate_view(driver, TEST_URL)
    print("Test completed.")

if __name__ == "__main__":
    main()
