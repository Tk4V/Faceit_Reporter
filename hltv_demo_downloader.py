from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def hltv_demo_downloader(demo_id, total_demos):
    #Hltv base download url
    download_url_base = "https://www.hltv.org/download/demo/"

    
    #u can choose dif browser(Chrome,Mozilla,etc.)
    options = webdriver.SafariOptions()
    options.add_argument("--headless")

    #WebDriver for Safari
    driver = webdriver.Safari(options=options)

    #Logging errors
    try:
        for _ in range(total_demos):
            download_url = f"{download_url_base}{demo_id}"
            driver.get(download_url)

            #Wait for url to load,change parameter if you have faster or slover internet connection
            time.sleep(5)

            
            try:
                download_button = driver.find_element(By.XPATH, "//a[contains(@class, 'download-button-class')]")
                
                if download_button:
                    download_link = download_button.get_attribute("href")
                    print(f"Found download link for demo {demo_id}: {download_link}")
                    
                    
                    driver.get(download_link)
                    print(f"Downloading demo {demo_id}...")
                    
                    #if you see error in console,that selenium cannot find buttom,change value to lower or higher,hltv can prepare demos slower or faster
                    time.sleep(20)

                else:
                    print(f"Download link for demo {demo_id} not found. Skipping.")

            except Exception as e:
                print(f"Error while downloading demo {demo_id}: {e}")
            
            #decrementing demos id,until you will download your goal count of demos
            demo_id -= 1 

        print("Completed downloading 1000 demos.")
    except Exception as e:
        print(f"An error occurred: {e}")

    #Closing browser window
    driver.quit()

hltv_demo_downloader(92852, 1000)
