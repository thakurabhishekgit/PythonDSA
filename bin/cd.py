from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the ChromeDriver service using webdriver-manager
service = Service(ChromeDriverManager().install())  # Automatically fetches the latest compatible version

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=service)

# Open a website (e.g., Instagram) as a test
driver.get("https://www.instagram.com")
