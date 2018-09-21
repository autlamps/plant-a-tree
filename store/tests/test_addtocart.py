from django.contrib.auth.models import User
from django.test import TestCase, Client

from store.models import Tree, Category, Cart, Product, CartTreeItem, \
    CartProductItem


class CartTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='bobbytables',
                                             password='fakepassword')
        self.client = Client()
        self.client.login(username='bobbytables', password='fakepassword')

        cat = Category(name='Native', description='Ones that belong')
        cat.save()

        self.t = Tree(
            name='Sometree',
            description='this really is a tree of some kind',
            fun_facts='fact one. fact two. fact threee',
            price=499.99,
            category=cat,
            maintenance=Tree.HIGH_MAINT,
            growth_rate=Tree.SLOW_RATE,
            height=100,
            year_one="1234",
            year_two="1234",
            year_three="1234",
            year_five="1234",
            year_ten="1234"
        )
        self.t.save()

        self.p = Product(
            name='Someproduct',
            description='this is a product of some kind',
            price=1.0,
            category=cat,
            image="1234",
        )
        self.p.save()

    def test_that_cart_created(self):
        response = self.client.get('/addtreetocart/1/1/', follow=True)

        try:
            cart = Cart.objects.get(user=self.user)
        except Cart.DoesNotExist:
            self.fail("adding item to cart did not create a cart")

    def test_add_tree(self):
        # ensure all CartTreeItems are deleted before running
        CartTreeItem.objects.all().delete()

        self.client.get('/addtreetocart/1/1/', follow=True)

        cart = Cart.objects.get(user=self.user)
        # get the first tree item in cart which should be a SomeTree w/ id 1
        tree_item = cart.trees.first()

        self.assertEqual(tree_item.id, 1,
                         msg="first item in trees cart doesn't have id=1")
        self.assertEqual(tree_item.qty, 1,
                         msg="first item in trees cart doesn't have qty=1")

    def test_add_product(self):
        self.client.get('/addproducttocart/1/1/', follow=True)

        cart = Cart.objects.get(user=self.user)
        product_item = cart.products.first()

        self.assertEqual(product_item.id, 1,
                         msg="first item in products cart doesn't have id=1")
        self.assertEqual(product_item.qty, 1,
                         msg="first item in products cart doesn't have qty=1")

    def test_multi_add_tree(self):
        # ensure all CartTreeItems are deleted before running
        CartTreeItem.objects.all().delete()

        self.client.get('/addtreetocart/1/1/', follow=True)
        self.client.get('/addtreetocart/1/1/', follow=True)
        self.client.get('/addtreetocart/1/2/', follow=True)

        cart = Cart.objects.get(user=self.user)
        tree_item = cart.trees.first()

        self.assertEqual(tree_item.id, 1,
                         msg="first item in product cart doesn't have id=1")
        self.assertEqual(tree_item.qty, 4,
                         msg="after repeat adds qty not qty=4")

    def test_multi_add_product(self):
        # ensure all CartProductItems are deleted
        CartProductItem.objects.all().delete()

        self.client.get('/addproducttocart/1/1/', follow=True)
        self.client.get('/addproducttocart/1/1/', follow=True)
        self.client.get('/addproducttocart/1/2/', follow=True)

        cart = Cart.objects.get(user=self.user)
        product_item = cart.products.first()

        self.assertEqual(product_item.id, 1,
                         msg="first item in products cart doesn't have id=1")
        self.assertEqual(product_item.qty, 4,
                         msg="after repeat adds qty not qty=4")
