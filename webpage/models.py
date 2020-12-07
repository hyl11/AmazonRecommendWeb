from django.db import models

# Create your models here.
import mongoengine


class ProductsWithInt(mongoengine.Document):
    intAsin = mongoengine.IntField()
    product_type = mongoengine.StringField()
    title = mongoengine.StringField()
    description = mongoengine.ListField()
    image = mongoengine.ListField()
    asin = mongoengine.StringField()


class PopularProducts(mongoengine.Document):
    asin = mongoengine.StringField()
    count = mongoengine.IntField()


class AverageProducts(mongoengine.Document):
    asin = mongoengine.StringField()
    avg = mongoengine.FloatField()


class OnlineRecs(mongoengine.Document):
    productId = mongoengine.IntField()
    time = mongoengine.LongField()
    recs = mongoengine.ListField()


class ProductRecs(mongoengine.Document):
    productId = mongoengine.IntField()
    recs = mongoengine.ListField()


class TestClass(mongoengine.Document):
    idtest = mongoengine.IntField()
    test = mongoengine.StringField()
