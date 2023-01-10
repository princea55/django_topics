from django.urls import path

from web.forms.views import view_dashboard, view_product, view_contact, view_sale_order, add_sale_order, \
    update_sale_order, delete_sale_order, add_lot_form

urlpatterns = [
    # Dashboard
    path('dashboard/', view_dashboard, name='dashboard'),
    # product
    path('view-product', view_product, name='view-product'),

    # contact
    path('view-contact', view_contact, name='view-contact'),

    # sale order
    path('view-sale-order', view_sale_order, name='view_sale_order'),
    path('add-sale-order', add_sale_order, name='add_sale_order'),
    path('update-sale-order/<str:pk>', update_sale_order, name='update_sale_order'),
    path('delete-sale-order/<str:pk>', delete_sale_order, name='delete_sale_order'),
    path('auction/add/lot/', add_lot_form, name='add_lot_form'),

]
