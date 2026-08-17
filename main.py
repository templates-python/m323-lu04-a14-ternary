"""Rabattberechnung.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu04/aufgaben/ternary2
"""

def calculate_discount(price, is_on_sale):
    """
    Berechnet den Preis eines Produkts nach Rabatt.

    Args:
    price (float): Der ursprüngliche Preis des Produkts.
    is_on_sale (bool): Gibt an, ob das Produkt im Angebot ist oder nicht.

    Returns:
    float: Der Preis des Produkts nach Rabatt.
    """
    # TODO: Implementieren Sie die Funktion
    return price * 0.9 if is_on_sale else price


if __name__ == "__main__":
    products = [
        {"name": "Laptop", "price": 1000.0, "is_on_sale": True},
        {"name": "Maus", "price": 50.0, "is_on_sale": False},
        {"name": "Tastatur", "price": 70.0, "is_on_sale": True},
    ]

    for product in products:
        product_name = product["name"]
        product_price = product["price"]
        discounted_price = calculate_discount(product_price, product["is_on_sale"])
        print(
            f"Produkt: {product_name}, Originalpreis: {product_price} Fr., "
            f"Rabattierter Preis: {discounted_price} Fr."
        )
