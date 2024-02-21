from pywinauto.application import Application
import time
 
# Launch Notepad
app = Application().start("notepad.exe")
time.sleep(1)  # Adding a small delay for Notepad to open

# Access the Notepad window
notepad = app['Untitled - Notepad']
 
# Enter some text
notepad.type_keys("Hello, this is some text.")
notepad.menu_select("File -> Save")
save_dialog = app['Save']
save_dialog['Edit'].type_keys("file2.txt")  # Replace with desired file path
save_dialog.save.click()
confirm_save_dialog = app['Confirm Save']
print(confirm_save_dialog)
confirm_save_dialog.yes.click()

 

notepad.maximize()
 
time.sleep(2)
notepad.close()
