from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Setting, Invoice, Product


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['organization_name', 'building_number', 'street_name', 'district', 'city', 'country',
                  'postal_code', 'additional_number', 'vat_number', 'other_seller_id']

    labels = {
        'organization_name': 'Organization Name',
        'building_number': 'Building Number',
        'street_name': 'Street Name',
        'district': 'District',
        'city': 'City',
        'country': 'Country',
        'postal_code': 'Postal Code',
        'additional_number': 'Additional Number',
        'vat_number': 'Vat Number',
        'other_seller_id': 'Other Seller Id'
    }



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['product', 'date_of_supply', 'branch', 'salesman_name', 'invoice_number',
                  'invoice_issue_date', 'page_number', 'description', 'unit_price', 'quantity', 'discount', 'total',
                  'taxable_amount', 'tax_amount', 'tax_rate', 'total_vat', 'total_taxable_amount_exclude_vat',
                  'total_exclude_vat', 'total_amount_due', 'sub_total', 'buyer_organization_name', 'building_number', 
                  'street_name', 'district', 'city', 'country',
                  'postal_code', 'additional_number', 'vat_number', 'other_buyer_id']

    labels = {
        'product': 'Product',
        'date_of_supply': 'Date Of Supply',
        'branch': 'Branch',
        'salesman_name': 'Sales Man Name',
        'invoice_number': 'Invoice Number',
        'invoice_issue_date': 'Invoice Issue Date',
        'page_number': 'Page Number',

        'buyer_organization_name': 'Organization Name',
        'building_number': 'Building Number',
        'street_name': 'Street Name',
        'district': 'District',
        'city': 'City',
        'country': 'Country',
        'postal_code': 'Postal Code',
        'additional_number': 'Additional Number',
        'vat_number': 'Vat Number',
        'other_buyer_id': 'Other Buyer Id',

        'description': 'Description',
        'unit_price': 'Price',
        'quantity': 'Quantity',
        'discount': 'Discount',
        'total': 'Total',
        'taxable_amount': 'Taxable Amount',
        'tax_amount': 'Tax Amount',
        'tax_rate': 'Tax Rate',
        'total_vat': 'Total Vat',
        'total_taxable_amount_exclude_vat': 'Total Taxable Amount Exclude Vat',
        'total_exclude_vat': 'Total exclude Vat',
        'total_amount_due': 'Total Amount Due',
        'sub_total': 'Sub-Total'

    }
InvoiceFormset = forms.inlineformset_factory(Product, Invoice, InvoiceForm, min_num=1, extra=0, can_delete=False)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item_code', 'item_name', 'item_name_in_arabic', 'price']

    labels = {
        'item_code': 'Item Code',
        'item_name': 'Item Name',
        'item_name_in_arabic': 'Item Name In Arabic',
        'price': 'Price'
    }
    

