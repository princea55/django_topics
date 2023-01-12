from django.urls import path

from web.forms.views import view_dashboard, view_product, view_contact, view_sale_order, add_sale_order, \
    update_sale_order, delete_sale_order, add_lot_form, add_product, update_product, delete_product, fetch_product_price

urlpatterns = [
    # Dashboard
    path('dashboard/', view_dashboard, name='dashboard'),
    # product
    path('view-product', view_product, name='view-product'),
    path('add-product', add_product, name='add_product'),
    path('update-product/<str:pk>', update_product, name='update_product'),
    path('delete-product/<str:pk>', delete_product, name='delete_product'),
    path('fetch-product-price', fetch_product_price, name='fetch_product_price'),

    # contact
    path('view-contact', view_contact, name='view-contact'),

    # sale order
    path('view-sale-order', view_sale_order, name='view_sale_order'),
    path('add-sale-order', add_sale_order, name='add_sale_order'),
    path('update-sale-order/<str:pk>', update_sale_order, name='update_sale_order'),
    path('delete-sale-order/<str:pk>', delete_sale_order, name='delete_sale_order'),
    path('auction/add/lot/', add_lot_form, name='add_lot_form'),

]
