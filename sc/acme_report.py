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
        product = Product(''.join(sample(ADJECTIVES, k=1) + sample(NOUNS, k=1)))
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
        prices.append(randint(5, 100))
        weights.append(randint(5, 100))
        flammability.append(uniform(0.0,2.5))

    # calculates averages
    price_average = sum(prices) / len(prices)
    weight_average = sum(weights) / len(weights)
    flammability_average = sum(flammability) / len(flammability)

    # unique product names
    # unique_names = 

    # Finally print the report
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Average price: {price_average: .1f}')
    print(f'Average weight: {weight_average: .1f}')
    print(f'Average flammability: {flammability_average: .1f}')

if __name__ == '__main__':
    inventory_report(generate_products())