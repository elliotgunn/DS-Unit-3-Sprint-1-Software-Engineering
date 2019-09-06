import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_methods(self):
        self.custom_product = Product('Test Product', price=20, weight=40, flammability=0.5)
        self.assertEqual(self.custom_product.stealability(), 'Not so stealable...')
        self.assertEqual(self.custom_product.explode(), "...it's a glove.")

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        self.assertEqual(self.len(generate_products()), 30)

    def test_legal_names(self):
        default_names = self.generate_products()
        possible_names = self.generate_products()
        for name in default_names:  
            self.assertIn(name, possible_names)


if __name__ == '__main__':
    unittest.main()