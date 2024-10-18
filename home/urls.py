from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Shanoor Trading Admin"
admin.site.site_title = "Shanoor Admin Portal"
admin.site.index_title = "Welcome to Shanoor Trading."

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("products", views.products, name='products'),
    path("hardwareitems", views.hardwareitems, name='hardware items'),
    path("safetyitems", views.safetyitems, name='Safety Items'),
    path("lightingproducts", views.lightingproducts, name='Lighting Products'),
    path("plumbingitems", views.plumbingitems, name='Plumbing Items'),
    path("cleaningproducts", views.cleaningproducts, name='Cleaning Products'),
    path("paintingtools", views.paintingtools, name='Painting Tools'),
    path("adhesivessealantsandtapes", views.adhesivessealantsandtapes, name='Adhesives,Sealants and Tapes'),   
]