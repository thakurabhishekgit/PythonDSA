import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_instagram_comments(post_url):
    # Set up Chrome options and webdriver
    options = Options()
    options.add_argument("--headless")  # Run headless for no browser UI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Open Instagram post URL
        driver.get(post_url)

        # Wait for the post's comment section to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[@aria-labelledby='like_count']"))
        )
        
        # Click on 'View all comments' button if available
        try:
            view_all_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'View all')]"))
            )
            view_all_button.click()
        except Exception as e:
            print("No 'View all comments' button found or already visible.")

        # Wait for the comments to load
        time.sleep(3)  # Adjust sleep if necessary
        
        # Scrape the comments
        comments = []
        comment_elements = driver.find_elements(By.XPATH, "//div[@class='C4VMK']/span")
        for comment in comment_elements:
            comments.append(comment.text)
        
        # Print or return the comments
        if comments:
            print(f"Found {len(comments)} comments:")
            for comment in comments:
                print(comment)
        else:
            print("No comments found.")

    except Exception as e:
        print(f"Error occurred while fetching comments: {e}")
    finally:
        driver.quit()

# Example usage
post_url = "https://www.instagram.com/reel/C-Z8IAEJgq1/?igsh=Y2dpdTdwYWcyaG4y"  # Replace with your desired post URL
scrape_instagram_comments(post_url)





