from django.urls import path

from shop import views
app_name='shop'

urlpatterns = [
    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/',views.AllProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetails,name='ProdCatDetail'),

]
