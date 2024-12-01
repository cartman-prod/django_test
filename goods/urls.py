from django.urls import path

from django_app.goods import views

app_name = "catalog"

urlpatterns = [
    path("", views.catalog, name="index"),
    path("product/", views.product, name="product"),
]
