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
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_statements(self):
        """Test product methods using different values"""
        prod = Product(name = 'Test Product' , weight = 100)
        self.assertEqual(prod.stealability(), "Not so stealable...")
        self.assertEqual(prod.explode(), "...BABOOM!!")

class AcmeReportTests(unittest.TestCase):
    """Making sure reports are accurate"""
    def test_default_num_products(self):
        """Test defaul products check in at 30"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test names to ensure they are generated properly"""
        for product in generate_products():
            phrase = product.name.split()
            adj = str(phrase[0])
            noun = str(phrase[1])

            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)



if __name__ == '__main__':
    unittest.main()