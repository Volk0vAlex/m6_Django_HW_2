from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        all_products = Product.objects.all()
        for item in all_products:
            item.delete()

        all_category = Category.objects.all()
        for item_c in all_category:
            item_c.delete()

        category_list = [
            {'id': '1', 'name': 'Одежда', 'description': 'Верхняя одежда'},
            {'id': '2', 'name': 'Электроника', 'description': 'Все, что можно зарядить от розетки'},
            {'id': '3', 'name': 'Книги', 'description': 'Бумажные с твердой обложкой'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)


        product_list = [
            {'id': '1', 'name': 'Смартфон', 'description': 'Звонить и писать',
             'category': Category.objects.get(pk=2), 'price': '15000'},
            {'id': '2', 'name': 'Куртка', 'description': 'Удобная и теплая',
             'category': Category.objects.get(pk=1), 'price': '5000'},
            {'id': '3', 'name': 'Сказки народов мира', 'description': 'Интересные сказки',
             'category': Category.objects.get(pk=3), 'price': '750'}
        ]


        products_for_create = []
        for product_item in product_list:
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)

