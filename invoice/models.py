from django.db import models

from io import BytesIO
# from pyqrcode import QRCode
import base64
from datetime import datetime 
# import segno
from django.core.files.base import ContentFile
import os
from django.utils.timezone import now

# Create your models here.

class Setting(models.Model):
    organization_name = models.CharField(max_length=300, null=True, blank=True)
    building_number = models.IntegerField(null=True, blank=True)
    street_name = models.CharField(max_length=150, null=True, blank=True)
    district = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    additional_number = models.CharField(max_length=150, null=True, blank=True)
    vat_number = models.CharField(max_length= 20,null=True, blank=True)
    other_seller_id = models.CharField(max_length=150, null=True, blank=True)


class Product(models.Model):
    item_code = models.CharField(max_length=100, null=True, blank=True)
    item_name_in_arabic = models.CharField(
        max_length=200, null=True, blank=True)
    item_name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    

    def __str__(self):
        return self.item_name



class Invoice(models.Model):
    """This is the client data model, it holds all client information. This
           docstring has to be improved."""

    def number():
        no = Invoice.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
    date_of_supply = models.DateField(null=True, blank=True)
    branch = models.CharField(max_length=300, null=True, blank=True)
    salesman_name = models.CharField(max_length=300, null=True, blank=True)
    invoice_number = models.IntegerField(null=True, blank=True, unique=True, default=number)
    invoice_issue_date = models.DateTimeField(default=now, null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)

    # buyer data
    buyer_organization_name = models.CharField(max_length=200, null=True, blank=True)
    building_number = models.IntegerField(null=True, blank=True)
    street_name = models.CharField(max_length=150, null=True, blank=True)
    district = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    additional_number = models.CharField(max_length=150, null=True, blank=True)
    vat_number = models.IntegerField(null=True, blank=True)
    other_buyer_id = models.CharField(max_length=150, null=True, blank=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, null=True, blank=True)

    description = models.CharField(max_length=300, null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    taxable_amount = models.FloatField(null=True, blank=True)
    tax_amount = models.FloatField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    total_vat = models.FloatField(null=True, blank=True)
    total_taxable_amount_exclude_vat = models.FloatField(null=True, blank=True)
    total_exclude_vat = models.FloatField(null=True, blank=True)
    total_amount_due = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    sub_total = models.FloatField(null=True, blank=True)
    # qr=models.ImageField(upload_to = get_file_path, blank=True)

    def save(self, *args, **kwargs):
        self.taxable_amount = self.unit_price * self.quantity
        self.tax_amount = self.taxable_amount * self.tax_rate / 100
        self.sub_total = self.taxable_amount + self.tax_amount

        self.total_exclude_vat = self.taxable_amount
        self.total_taxable_amount_exclude_vat = self.taxable_amount
        self.total_vat = self.tax_amount
        self.total_amount_due = self.total_vat + self.total_exclude_vat

        super(Invoice, self).save(*args, **kwargs)

    
    # def save(self,*args,**kwargs):
    #     now = datetime.now()
    #     year = now.strftime("%Y")
    #     month = now.strftime("%m")
    #     day = now.strftime("%d")
    #     date = str(day)+"-"+str(month)+"-"+str(year)
    #     #date = str(datetime.now().today())
    #     time = now.strftime("%H-%M")
    #     #time = str(datetime.now().strftime("%HH:"))
    #     data =str(self.organization_name)+" "+str(self.vat_number)+" "+str(self.total)+" "+str(self.total_vat)+" "+str(date)+" "+str(time)
    #     print(data)
    #     data = data.encode("utf-8")
    #     data = base64.b64encode(data)
    #     # url = qrcode.make(data)
    #     print(data)
    #     out = BytesIO()
    #     qr = segno.make(data)
    #     qr.save(out, kind='png', dark='#000000', light=None, scale=6)

    #     filename = 'qr-'+self.organization_name+'.png'
    #     self.qr.save(filename, ContentFile(out.getvalue()), save=False)
       
    #     super().save(*args ,**kwargs)

   # class Categories(models.Model):
#     name = models.CharField(max_length=70,null=True)
#     name_ar = models.CharField(max_length=70,null=True)
#     pos = models.BooleanField(null=True)
#     digital_menu = models.BooleanField(null=True)
#     created_date= models.DateTimeField(auto_now_add=True,null=True)
#     updated_date = models.DateTimeField(null=True)
#     created_by = models.CharField(max_length=70,null=True)
#     updated_by = models.CharField(max_length=70,null=True)
#     parent = models.CharField(max_length=70,null=True)
#     images = models.ImageField(upload_to='images',null=True)
#     is_parent = models.BooleanField(null=True)
#     discount = models.DecimalField(decimal_places=2, max_digits=10, default=0,null=True)
#     code = models.CharField(max_length=70, unique= True, null=True)
    
#     @property
#     def getName(self):
#         return self.name
    
#     @property
#     def getName_ar(self):
#         return self.name_ar        
    
#     @property
#     def imageUrl(self):
#         try:
#             url = self.images.url
#         except:
#             url = ''
#         return url

        
# class Products(models.Model):
#     name = models.CharField(max_length=70,null=True)
#     name_ar = models.CharField(max_length=70,null=True)
#     pos = models.BooleanField(null=True)
#     digital_menu = models.BooleanField(null=True)
#     created_date= models.DateTimeField(auto_now_add=True,null=True)
#     updated_date = models.DateTimeField(null=True)
#     created_by = models.CharField(max_length=70,null=True)
#     updated_by = models.CharField(max_length=70,null=True)
#     images = models.ImageField(upload_to='images',null=True)
#     Category_id = models.ForeignKey('Categories', on_delete=models.SET_DEFAULT, default=25)
#     # invoice_id = models.ForeignKey('PurchasingInvoices',on_delete=models.CASCADE,)
#     cost_price = models.DecimalField(decimal_places=2, max_digits=10, default=0,null=True)
#     selling_price = models.DecimalField(decimal_places=2, max_digits=10, default=0,null=True)
#     total_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0,null=True)
#     tax = models.DecimalField(decimal_places=2, max_digits=10, default=0,null=True)
#     # vat = models.BooleanField(null=True)
#     discount = models.DecimalField(decimal_places=2, max_digits=10, default=0,null=True)
#     quantity = models.PositiveIntegerField(default=0,null=True)
#     include_tax = models.BooleanField(null=True)
#     code = models.CharField(max_length=70, unique= True, null=True)


#     @property
#     def imageUrl(self):
#         try:
#             url = self.images.url
#         except:
#             url = ''
#         return url

    
#     # @property
#     # def getTotal(self):
#     #     if include_tax == True:
#     #         total_amount = self.selling_price + self.tax
#     #     else:
#     #         total_amount = self.selling_price
#     #     return total_amount
        
#     @property 
#     def getTotal(self):
#         if self.include_tax == True:
#             total_amount = self.selling_price + self.tax
#         else:
#             total_amount = self.selling_price
           
#         return total_amount

#     @property
#     def getTotalDiscount(self):
#         discount_price = self.total_amount - (self.total_amount * self.discount/100)
#         # tax = discount_price * self.tax
#         # discount_price = discount_price + self.tax
#         # self.save()
#         return discount_price

#     @property
#     def getName(self):
#         return self.name
        
#     @property
#     def getName_ar(self):
#         return self.name_ar    
        
    
#     def calculateTotal(self, tax, include_tax):
#         if include_tax == 1 and self.discount > 0:
#             discount_price = self.selling_price -(self.selling_price * self.discount/100)
#             tax_amount =  discount_price * (tax/100)
#             self.total_amount = discount_price + tax_amount
#             self.tax = tax_amount
#             self.include_tax = include_tax
#             self.save()
            
#             print('tax,', tax)
#         elif include_tax == 1 and self.discount <= 0:
#             tax_amount =  self.selling_price * (tax/100)
#             self.total_amount = self.selling_price + tax_amount
#             self.tax =tax_amount
#             self.include_tax = include_tax
#             self.save()
            
#         elif include_tax == 0 and self.discount > 0:
#             discount_price = self.selling_price -(self.selling_price * self.discount/100)
#             self.tax= (discount_price/100) * tax
#             self.total_amount = discount_price 
#             self.include_tax = include_tax
#             self.save()
            
#         elif include_tax == 0 and self.discount <= 0:
#             self.tax =  (self.selling_price/100) * tax
#             self.total_amount = self.selling_price
#             self.include_tax = include_tax
#             self.save()


# class OrderItems(models.Model):
#     quantity = models.PositiveIntegerField(default= 0)
#     order = models.ForeignKey('Orders', on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=100, null=True)
#     unit_price = models.DecimalField(decimal_places=2, max_digits=19, default=0.00)
#     total_price = models.DecimalField(decimal_places=2, max_digits=19, default=0.00)
#     product_id = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, blank=True,)

#     @property
#     def getTotal(self):
#         self.total_price = Decimal(self.unit_price)  * Decimal(self.quantity)
#         self.save()
#         return self.total_price
   

# class Orders(models.Model):

#     STATUS_CHOICES = (
#     ('Started', 'Started'),
#     ('Canceled', 'Canceled'),
#     ('Reciverd','Reciverd'),
#     ('Prepared', 'Prepared'),
#     ('Ready', 'Ready'),
#     ('Opened','Opened'),
#     ('Closed','Closed')
#     )

#     daily_orders = models.IntegerField(null=True)
#     name = models.CharField(max_length=100, null=True)
#     created_date= models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(null=True)
#     order_type = models.CharField(max_length=70, null=True)
#     created_by = models.CharField(max_length=70, null=True)
#     updated_by = models.CharField(max_length=70, null=True)
#     images = models.ImageField(null=True)
#     status = models.CharField(max_length=70, choices= STATUS_CHOICES, default='Started')
#     # customer_id = models.ForeignKey('Customers',on_delete=models.SET_NULL,null=True)
#     # group_id = models.ForeignKey('Groups',on_delete=models.SET_NULL,null=True)
#     # cash_register_id = models.ForeignKey('CashRegister',on_delete=models.SET_NULL, null=True)
#     # waiter_id = models.ForeignKey('Staff',on_delete=models.SET_NULL,null=True)
#     # table_id = models.ForeignKey('Tables',on_delete=models.SET_NULL,null=True)
#     # payment_id = models.ForeignKey('Payment',on_delete=models.SET_NULL,null=True)
#     tax = models.DecimalField(decimal_places=2, max_digits=19, default=0)
#     # discount_id = models.ForeignKey('Discounts',on_delete=models.CASCADE,null=True)
#     # rewards_id = models.ForeignKey('Rewards',on_delete=models.SET_NULL,null=True)
#     total_amount = models.DecimalField(decimal_places=2, max_digits=19, default=0, null=True, blank=True)
#     invoice_id = models.ForeignKey(Invoice,on_delete=models.SET_NULL,null=True)
#     table_no = models.CharField(max_length=100, null=True)
#     waiter_name = models.CharField(max_length=100, null=True)
#     total_discount = models.CharField(max_length=100, null=True)
#     sub_total = models.DecimalField(decimal_places=2, max_digits=19, default=0, null=True, blank=True)
#     payment_name = models.CharField(max_length=100, null=True)
    

#     @property
#     def get_items_total(self):
#         order_items = self.orderitems_set.all()
#         self.total_amount = round(sum([item.unit_price for item in order_items]), 2)
#         self.save()
#         return self.total_amount
        
#     @property
#     def getName(self):
#         return self.name
        
#     @property
#     def getName_ar(self):
#         return self.name    

#     @property
#     def imageUrl(self):
#         try:
#             url = self.images.url
#         except:
#             url = ''
#         return url
        
        
    # @property
    # def getTotalItems(self):
    #     order_items =self.orderitem_set.all()
    #     total_price =sum([item.getTotal for item in order_items])
    #     return total_price
       