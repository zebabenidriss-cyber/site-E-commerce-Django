import json

from django.test import TestCase

from .models import Product, category, commande


class CheckoutTests(TestCase):
    def test_checkout_saves_product_names_with_order_items(self):
        product_category = category.objects.create(nom='Informatique')
        product = Product.objects.create(
            title='Clavier',
            price=25,
            description='Clavier USB',
            category=product_category,
            image='clavier.jpg',
        )

        self.client.post(
            '/checkout/',
            {
                'nom': 'Client',
                'email': 'client@example.com',
                'adresse': '1 rue du Test',
                'ville': 'Ouagadougou',
                'pays': 'Burkina Faso',
                'zip_code': '0000',
                'items': json.dumps({str(product.id): 2}),
            },
        )

        order = commande.objects.get()
        self.assertEqual(
            json.loads(order.items),
            [{'id': product.id, 'name': 'Clavier', 'quantity': 2}],
        )
