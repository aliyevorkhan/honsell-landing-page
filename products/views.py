from django.shortcuts import render
from products.models import *
from rest_framework import generics
from products.serializers import *


def home(request):
    products = Product.objects.filter(is_active=True)
    news = News.objects.filter(is_active=True).order_by("-created_at")[:3]

    return render(request, "index.html", {"products": products, "news": news})

def products(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "products.html", {"products": products})

def search(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})
    query = request.POST.get("query")
    products = Product.objects.filter(title__icontains=query)
    return render(request, "products.html", {"products": products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    product.views += 1
    product.save()
    types = Types.objects.filter(product=product)
    return render(request, "product-detail.html", {"product": product, "types": types})

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, "faq.html", {"faqs": faqs})

def terms(request):
    return render(request, "terms.html")

class ProductAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TypesAPIView(generics.RetrieveAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer

class ProductsListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SubscriptionsAPIView(generics.CreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class LikeAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.likes += 1
        product.save()
        return super().get(request, *args, **kwargs)

class ViewAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.views += 1
        product.save()
        return super().get(request, *args, **kwargs)