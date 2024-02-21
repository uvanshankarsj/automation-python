from pywinauto.application import Application
import time
 
app = Application().start("C:\Program Files\Google\Chrome\Application\chrome.exe")
# app.Chrome_WidgetWin_1.print_control_identifiers()
testing=app["New Tab - Google Chrome"]
testing.type_keys("https://www.youtube.com/ {ENTER 2}")
# app.Chrome_WidgetWin_1.print_control_identifiers()
youtube=app["YouTube - Google Chrome"]
youtube.print_control_identifiers() 


# child_window=testing. child_window(title="Chrome Legacy Window", class_name="Chrome_RenderWidgetHostHWND")
# if child_window.exists():
#     # You can interact with the child window here, for example, you can bring it to the foreground
#     child_window.print_control_identifiers()
# else:
#     print("Child window not found.")
# testing.print_control_identifiers()
# time.sleep(1)  # Adding a small delay for Notepad to open

# # Access the Notepad window
# notepad = app['Untitled - Notepad']
 
# # Enter some text
# notepad.type_keys("Hello, this is some text.")
# notepad.menu_select("File -> Save")
# save_dialog = app['Save']
# save_dialog['Edit'].type_keys("file2.txt")  # Replace with desired file path
# save_dialog.save.click()
# confirm_save_dialog = app['Confirm Save']
# print(confirm_save_dialog)
# confirm_save_dialog.yes.click()

 

# notepad.maximize()
 
# time.sleep(2)
# notepad.close()
