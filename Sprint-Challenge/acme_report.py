from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    Generate a given number of products (default 30)
    randomly, and return them as a list
    """
    products = []

    for _ in range(num_products):
        name = str(sample(ADJECTIVES, 1)) + " " + str(sample(NOUNS,1))
        price = randint(5,100)
        weight = randint(5,100)
        flammability = uniform(0, 2.5)
        
        products.append(Product(name, price, weight, flammability))

    return products


def inventory_report(products):
    #Loop over the products to calculate the report.
    names = set()
    prices = []
    weights = []
    flammabilities = []

    for product in products:
        names.add(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {len(names)} ")
    print(f"Average price: {sum(prices) / len(prices):.2f}")
    print(f"Average weight: {sum(weights) / len(weights):.2f}")
    print(f"Average flammability: {sum(flammabilities) / len(flammabilities):.3f}") 



if __name__ == '__main__':
    inventory_report(generate_products())