from django.conf import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [

    # Login and Register
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),

    # setting
    path('setting/create/', views.setting_create, name='setting_create'),


    # product
    path('product/list/', views.product_list, name='product_list'),
    path('product/view/<int:id>/', views.product_view, name='product_view'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/update/<int:id>/', views.product_update, name='product_update'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),

    # pos
    path('invoice/list/', views.invoice_pos_list, name='invoice_pos_list'),
    path('pos/create/', views.invoice_create, name='invoice_create'),
    #path('invoice/view/<int:id>/', views.invoice_view, name='invoice_view'),
     path('invoice/view/<int:id>/', views.orcode, name='invoice_view'),
    path('invoice/delete/<int:id>/', views.invoice_delete, name='invoice_delete'),
      #path('', views.orcode, name='orcode'),
    # path('pos/',views.pos, name='pos'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)