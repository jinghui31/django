from django.shortcuts import render
from django.http import Http404
import random
from .models import Product

# Create your views here.
def product(request):
    quotes = [
        '今日事，今日畢',
        '要怎麼收獲，先那麼栽',
        '知識就是力量',
        '一個人的個性就是他的命運'
    ]
    return render(request, 'product.html', {'quote': random.choice(quotes)})

def about(request):
    return render(request, 'about.html')

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        product = Product.objects.get(sku = sku)

    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')

    return render(request, 'disp.html', locals())
