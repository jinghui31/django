from django.urls import path
from .views import product, about, listing, disp_detail

urlpatterns = [
    path('', product),
    path('about/', about),
    path('list/', listing),
    path('list/<slug:sku>', disp_detail)
]
