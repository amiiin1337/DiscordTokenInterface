from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def discord_login_with_token(token):
    try:
        # selenium manager handles chromedriver automatically now which is nice
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") # keep this commented so you can see it work
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        print("Launching Browser...")
        driver = webdriver.Chrome(options=options)
        
        # navigate to discord
        print("Opening Discord Login...")
        driver.get("https://discord.com/login")
        
        # wait a bit for the page to fully load
        time.sleep(3) 

        # inject the token into localStorage
        print(f"Injecting Token...")
        script = f"""
            function login(token) {{
                setInterval(() => {{
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${{token}}"`;
                }}, 50);
                setTimeout(() => {{
                    location.reload();
                }}, 2500);
            }}
            login("{token}");
        """
        driver.execute_script(script)
        
        print("Token injected. Waiting for reload...")
        
        # gotta keep the browser open otherwise it'll just close when the function ends
        # probably could use some kind of detach but this works fine
        # 5 minutes should give you enough time to do whatever
        time.sleep(300)
        
    except Exception as e:
        print(f"Error in automation: {e}")