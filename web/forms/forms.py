from django import forms
from django.forms import BaseModelFormSet, modelformset_factory

from utils.validator import validate_positive
from web.forms.models import Product, SaleOrder, SaleOrderLine


class FormProduct(forms.ModelForm):
    price = forms.IntegerField(
        validators=[validate_positive])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = '__all__'


class FormSaleOrder(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['order_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = SaleOrder
        fields = '__all__'
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date'})
        }


class FormSaleOrderLine(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update({'class': 'form-control product select2'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control quantity'})
        self.fields['unit_price'].widget.attrs.update({'class': 'form-control unit_price'})
        self.fields['unit_total'].widget.attrs.update({'class': 'form-control unit_total', 'readonly': True})
        self.fields['unit_total'].label = 'Total'
        self.fields['unit_price'].label = 'Price'

    class Meta:
        model = SaleOrderLine
        fields = ['product', 'quantity', 'unit_price', 'unit_total']


class BaseLotFormSet(BaseModelFormSet):

    def get_deletion_widget(self):
        return forms.HiddenInput

    def clean(self):
        pass


OrderLineFormset = modelformset_factory(
    SaleOrderLine,
    form=FormSaleOrderLine,
    min_num=1,
    formset=BaseLotFormSet,
    validate_max=True,
    extra=0,
    can_delete=True
)
