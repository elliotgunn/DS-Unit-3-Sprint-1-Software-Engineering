from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''Generates list of products from ADJECTIVES and NOUNS
    '''
    products = []

    for _ in list(range(num_products)):
        # get product names by sampling ADJECTIVES and NOUNS
        product = Product(sample(ADJECTIVES, k=1)[0] + ' ' + sample(NOUNS, k=1)[0],
                        price=randint(5, 100), weight=(randint(5, 100)), flammability=(uniform(0.0,2.5)))
        
        products.append(product)
    
    return products


def inventory_report(products):
    '''Generates lists of product prices, weights, flammability.
       Returns a report with averages of prices, weights, flammability.
    '''
    # instantiate empty lists
    prices = []
    weights = []
    flammability = []

    # loop over products
    for product in products:

        # record price, weight, flammability of each product
        prices.append(product.price)
        weights.append(product.weight)
        flammability.append(product.flammability)

    # calculates averages
    price_average = sum(prices) / len(prices)
    weight_average = sum(weights) / len(weights)
    flammability_average = sum(flammability) / len(flammability)

    # unique product names
    names = []
    for product in products:
        names.append(product.name)

    unique_names = len(list(set(names)))

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names', unique_names)
    print('Average price', price_average)
    print('Average weight', weight_average)
    print('Average flammability', flammability_average)

if __name__ == '__main__':
    inventory_report(generate_products())