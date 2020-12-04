from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_world(request):
    return HttpResponse("hello world")


def get_detail(request, productID):
    curProduct = None
    similarList = None
    guessList = None

    return render(request, "detail.html",
                  {
                      "curProduct": curProduct,
                      "similarList": similarList,
                      "guessList": guessList
                  }
                  )


def get_index(request):
    products = None
    popularList = None
    bestList = None

    return render(request, "index.html",
                  {
                      "productList": products,
                      "popularList": popularList,
                      "bestList": bestList
                  }
                  )


def test(request):
    return render(request, "webpage/test.html")
