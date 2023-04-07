import webbrowser
import pyautogui
import time

# Zoom meeting configuration
zoom_link = "https://zoom.us/j/"
zoom_meeting_id = input("Enter meeting ID: ")
zoom_password = input("Enter password: ")

# Open the Zoom link
webbrowser.open(zoom_link + zoom_meeting_id)

# Wait for the page to load and click the join button
time.sleep(5)
join_button = pyautogui.locateCenterOnScreen('meeting_join_button.png')
pyautogui.moveTo(join_button)
pyautogui.click()

# Wait for the page to load and enter the meeting password
time.sleep(2)
password_field = pyautogui.locateCenterOnScreen('meeting_password_field.png')
pyautogui.moveTo(password_field)
pyautogui.click()
pyautogui.write(zoom_password)
pyautogui.press('enter')
print("All the tasks performed successfully")