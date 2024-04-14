from django.contrib import admin
from products.models import *

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "discounted_price")
    search_fields = ("title", "description", "price", "discounted_price")
    list_filter = ("title", "description", "price", "discounted_price")
    list_display_links = ("title", "description", "price", "discounted_price")

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")
    list_filter = ("title", "description")
    list_display_links = ("title", "description")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "is_active",
        "image",
        "likes",
        "views",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "description",
        "is_active",
        "image",
        "likes",
        "views",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "title",
        "description",
        "is_active",
        "image",
        "likes",
        "views",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "title",
        "description",
        "is_active",
        "image",
        "likes",
        "views",
        "created_at",
        "updated_at",
    )

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "product", "image", "is_active")
    search_fields = ("title", "description", "product", "image", "is_active")
    list_filter = ("title", "description", "product", "image", "is_active")
    list_display_links = ("title", "description", "product", "image", "is_active")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")
    search_fields = ("question", "answer")
    list_filter = ("question", "answer")
    list_display_links = ("question", "answer")
