from django.template.loader import get_template
from django.http import HttpResponse, Http404
import random
from .models import Product

# Create your views here.
def product(request):
    template = get_template('product.html')
    quotes = [
        '今日事，今日畢',
        '要怎麼收獲，先那麼栽',
        '知識就是力量',
        '一個人的個性就是他的命運'
    ]
    html = template.render({'quote': random.choice(quotes)})
    return HttpResponse(html)

def about(request):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)

def listing(request):
    products = Product.objects.all()
    template = get_template('list.html')
    html = template.render({'products': products})
    return HttpResponse(html)

def disp_detail(request, sku):
    try:
        product = Product.objects.get(sku = sku)

    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')

    template = get_template('disp.html')
    html = template.render({'product': product})

    return HttpResponse(html)
