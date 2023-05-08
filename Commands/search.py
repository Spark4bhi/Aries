import webbrowser

def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)