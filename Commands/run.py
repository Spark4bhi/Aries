import os

def run_app(app_name):
    app_name = app_name.lower()
    if "chrome" in app_name:
        path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        os.startfile(path)
    elif "notepad" in app_name:
        path = "C:/Windows/System32/notepad.exe"
        os.startfile(path)
    elif "calculator" in app_name:
        path = "C:/Windows/System32/calc.exe"
        os.startfile(path)
    else:
        print(f"Could not find app '{app_name}'.")