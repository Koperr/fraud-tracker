import requests
from bs4 import BeautifulSoup
import re

def get_ceneo_prices(query):
    url = f"https://www.ceneo.pl/;szukaj-{query.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Wysyłamy zapytanie HTTP do strony Ceneo
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Szukamy elementów zawierających ceny
    products = soup.find_all('div', class_='cat-prod-row')
    
    prices = []
    
    for product in products:
        # Pobieranie nazwy produktu
        name = product.find('a', class_='go-to-product').get_text(strip=True)
        
        # Pobieranie ceny (znajduje pierwszą cenę w złotówkach)
        price_tag = product.find('span', class_='price')
        if price_tag:
            price_text = price_tag.get_text(strip=True)
            
            # Konwertowanie ceny na liczbę
            price_value = re.sub(r'[^\d,]', '', price_text).replace(',', '.')
            try:
                price_float = float(price_value)
                prices.append((name, price_float))
            except ValueError:
                continue  # W przypadku błędu w konwersji pomijamy tę cenę

    return prices

def get_average_price(product_name) -> float:
    if __name__ == "__main__":
        query = product_name
        prices = get_ceneo_prices(query)

        if prices:
            print("Znalezione produkty i ich ceny:")
            total = 0
            for name, price in prices:
                print(f"Produkt: {name} - Cena: {price} zł")
                total += price

            # Obliczanie średniej ceny
            average_price = total / len(prices)
            print(f"\nŚrednia cena: {average_price:.2f} zł")
            return average_price
        else:
            print("Nie znaleziono żadnych wyników.")
    return 0
