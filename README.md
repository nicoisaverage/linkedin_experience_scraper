# Scrape a LI Member Experience

Uses linkedin_scraper and a chromedriver to automatically login to Linkedin and scrape a users experience data based on the LI member's profile URL

Before using, one must install the latest version of Chromedriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

One must also install linkedin_scraper:
        
        pip install --user linkedin_scraper 
 
To run:
        
        LiExp('linkedinURL').li_login_scrape()
