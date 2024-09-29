import requests

def track_redirection(url):
    try:
        response = requests.get(url, allow_redirects=True)
        print(f"Pierwotny URL: {response.url}")
        print(f"Przekierowanie: {response.history}")
        return response.url
    except Exception as e:
        print(f"Błąd: {e}")
        return None

payment_url = "https://przyklad-platnosci.pl"
original_url = track_redirection(payment_url)