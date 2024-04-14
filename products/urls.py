from django.urls import path, include
from products.views import *

urlpatterns = [
    path("", home),
    path("product_detail/<int:id>/", product_detail, name="product_detail"),
    path("api/product/<int:pk>/", ProductAPIView.as_view()),
    path("api/types/<int:pk>/", TypesAPIView.as_view()),
    path("api/products/", ProductsListAPIView.as_view()),
    path("products/", products, name="products"),
    path("search/", search, name="search"),
    path("faq/", faq, name="faq"),
    path("terms/", terms, name="terms"),
    path("api/subscribe/", SubscriptionsAPIView.as_view()),
    path("api/like/<int:pk>/", LikeAPIView.as_view()),
    path("api/view/<int:pk>/", ViewAPIView.as_view()),
]