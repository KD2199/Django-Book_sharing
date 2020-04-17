from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('donate/', views.donate, name="donate"),
    path('logout/', views.logout, name="login"),
    path('Add/', views.Add, name="Add"),
    path('show/', views.show, name="show"),
    path('search/', views.search, name="search"),
    path('delete/', views.delete, name="delete"),
    path('chat/', views.chat, name="chat"),
    path('cart/', views.cart, name="cart"),
    path('<int:item_id>', views.dlt, name="dlt"),
    path('message/', views.message, name="message"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
