from django.shortcuts import render
from django.http import HttpResponse
from webpage.models import *


# Create your views here.

def hello_world(request):
    return HttpResponse("hello world")


def get_recs(recs):
    result = []
    for rec in recs:
        product = ProductsWithInt.objects.filter(intAsin=rec.get("productId")).first()
        avgs = AverageProducts.objects.filter(asin=product.asin).first()
        product.avg = avgs.avg
        product.imageUrl = product.image[0]
        result.append(product)
    return result


def get_detail(request, productID):
    log = open("/usr/local/recommend/log", "a")
    log.write(str(productID))
    log.close()

    curProduct = ProductsWithInt.objects.filter(intAsin=productID).first()
    avgs = AverageProducts.objects.filter(asin=curProduct.asin).first()
    curProduct.avg = avgs.avg
    curProduct.imageUrl = curProduct.image[0]
    curProduct.descriptionOne = curProduct.description[0]

    similar = ProductRecs.objects.filter(productId=productID).first()
    similarList = get_recs(similar.recs)

    guess = OnlineRecs.objects.order_by("time")[:3]
    guessList = []
    for g in guess:
        print(g.time)
        guessList.extend(get_recs(g.recs))
    if len(guessList) > 9:
        guessList = guessList[3:9]

    return render(request, "detail.html",
                  {
                      "curProduct": curProduct,
                      "similarList": similarList,
                      "guessList": guessList
                  }
                  )


def get_index(request):
    musics = ProductsWithInt.objects.filter(product_type="music instruments")[:5]
    #  print(musics[0].title)
    videos = ProductsWithInt.objects.filter(product_type="video game")[:5]
    # print(videos[0].title)
    luxury = ProductsWithInt.objects.filter(product_type="luxury")[:5]
    # print(luxury[0].title)
    productList = []
    productList.extend(musics)
    productList.extend(videos)
    productList.extend(luxury)
    for x in productList:
        x.imageUrl = x.image[0]
        x.product_type = x.product_type.replace(" ", "_")

    popular = PopularProducts.objects.order_by("count")[:6]
    popularList = []
    for p in popular:
        product = ProductsWithInt.objects.filter(asin=p.asin).first()
        product.imageUrl = product.image[0]
        popularList.append(product)

    best = AverageProducts.objects.order_by("avg")[:6]
    bestList = []
    for b in best:
        product = ProductsWithInt.objects.filter(asin=b.asin).first()
        product.imageUrl = product.image[0]
        bestList.append(product)

    print("-----------------")
    print(len(productList))
    # print(popularList.length)
    # print(bestList.length)
    print("-----------------")
    return render(request, "index.html",
                  {
                      "productList": productList,
                      "popularList": popularList,
                      "bestList": bestList
                  }
                  )


def test(request):
    result = TestClass.objects.create(idtest=1233132, test="Testkkkkkkkkkk")
    print(result)

    return HttpResponse("ok")
