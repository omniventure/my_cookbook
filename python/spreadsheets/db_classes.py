import random
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

from db_classes import Product, Sale

products = []

for idx in range(1, 6):
    sales = []

    for _ in range(5):
        sale = Sale(quantity=random.randrange(5, 100))
        sales.append(sale)

    product = Product(id=str(idx), name="Product %s" % idx, sales=sales)
    products.append(product)

workbook = Workbook()
sheet = workbook.active

sheet.append(["Product ID", "Product Name", "Month 1",
              "Month 2", "Month 3", "Month 4", "Month 5"])

for product in products:
    data = [product.id, product.name]
    for sale in product.sales:
        data.append(sale.quantity)
        sheet.append(data)
