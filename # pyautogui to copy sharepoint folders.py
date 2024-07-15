#   pyautogui to copy sharepoint folders

import pyautogui
import time

# Function to copy SharePoint site
def copy_sharepoint_sites(source_site_url, destination_site_url):
    # Open the web browser
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('chrome')
    pyautogui.press('enter')
    time.sleep(2)

    # Go to the source SharePoint site
    pyautogui.typewrite(source_site_url)
    pyautogui.press('enter')
    time.sleep(5)

    # Select and copy the site
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy
    time.sleep(2)

    # Go to the destination SharePoint site
    pyautogui.hotkey('ctrl', 't')  # Open a new tab
    pyautogui.typewrite(destination_site_url)
    pyautogui.press('enter')
    time.sleep(5)

    # Paste and copy the site
    pyautogui.hotkey('ctrl', 'v')  # Paste
    pyautogui.press('enter')
    time.sleep(5)

    print("SharePoint site copied successfully.")

# Copy SharePoint site from source to destination
source_site_url = "https://source-sharepoint-site-url"
destination_site_url = "https://destination-sharepoint-site-url"
copy_sharepoint_sites(source_site_url, destination_site_url)