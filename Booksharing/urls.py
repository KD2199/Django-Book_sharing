from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('home/', include('BSS.urls')),
    path('about/', include('BSS.urls')),
    path('register/', include('BSS.urls')),
    path('login/', include('BSS.urls')),
    path('donate/', include('BSS.urls')),
    path('logout/', include('BSS.urls')),
    path('Add/', include('BSS.urls')),
    path('show/', include('BSS.urls')),
    path('search/', include('BSS.urls')),
    path('delete/', include('BSS.urls')),
    path('chat/', include('BSS.urls')),
    path('cart/', include('BSS.urls')),
    path('<int:item_id>',include('BSS.urls')),
    path('checkout/', include('BSS.urls')),
    path('message/', include('BSS.urls')),
]