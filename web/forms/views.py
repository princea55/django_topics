from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from web.forms.forms import FormSaleOrder, OrderLineFormset, FormSaleOrderLine, FormProduct
from web.forms.models import Product, Contact, SaleOrder, SaleOrderLine
from web.forms.templatetags.general_tags import get_unsigned_value


# Create your views here.
@login_required
def view_dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def view_product(request):
    return render(request, 'view_product.html', {'products': Product.objects.all()})

@login_required
def add_product(request):
    form = FormProduct(data=request.POST or None)
    if form.is_valid():
        form.save()
        # messages.add_message(request, messages.SUCCESS, "Currency added successfully.")
        return redirect('view-product')
    return render(request, 'product.html', {'form': form})

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=get_unsigned_value(pk))
    form = FormProduct(data=request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        # messages.add_message(request, messages.SUCCESS, "Currency updated successfully.")
        return redirect('view-product')
    return render(request, 'product.html', {'form': form})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=get_unsigned_value(pk))
    product.delete()
    # messages.add_message(request, messages.SUCCESS, "Currency deleted successfully.")
    return redirect('view-product')

@login_required
def view_contact(request):
    return render(request, 'view_contact.html', {'contacts': Contact.objects.all()})

@login_required
def view_sale_order(request):
    return render(request, 'view_sale_order.html', {'orders': SaleOrder.objects.all()})

@login_required
def add_sale_order(request):
    form = FormSaleOrder(data=request.POST or None)
    formset = OrderLineFormset(request.POST or None, queryset=SaleOrderLine.objects.none())
    if form.is_valid() and formset.is_valid():
        order = form.save(commit=False)
        order.save()
        for forms in formset:
            order_line = forms.save(commit=False)
            order_line.order_id = order
            order_line.save()
        return redirect('view_sale_order')
    return render(request, 'sale_order.html', {'form': form, 'formset': formset})

@login_required
def update_sale_order(request, pk):
    order = get_object_or_404(SaleOrder, pk=get_unsigned_value(pk))
    form = FormSaleOrder(data=request.POST or None, instance=order)
    formset = OrderLineFormset(request.POST or None, queryset=order.order_line_sale_order.all())
    if form.is_valid() and formset.is_valid():
        order = form.save()
        for forms in formset:
            if forms.cleaned_data.get('DELETE'):
                forms.cleaned_data.get('id').delete()
            else:
                order_line = forms.save(commit=False)
                order_line.order_id = order
                order_line.save()
        return redirect('view_sale_order')
    return render(request, 'sale_order.html', {'form': form, 'formset': formset})

@login_required
def delete_sale_order(request, pk):
    order = get_object_or_404(SaleOrder, pk=get_unsigned_value(pk))
    order.delete()
    return redirect('view_sale_order')

@login_required
def add_lot_form(request):
    form: FormSaleOrderLine = OrderLineFormset().empty_form
    return HttpResponse(form.render('order_line.html').replace('__prefix__', request.GET.get('val')))

@login_required
def fetch_product_price(request):
    products = list(Product.objects.values_list('price').filter(pk=request.GET.get('val')))

    return JsonResponse(products, safe=False)