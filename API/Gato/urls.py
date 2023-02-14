from django.urls import path
from Gato import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('usuario',views.usuarioAPI),
    path('usuario/<id>', views.usuarioAPI),

    path('gatito',views.gatitoAPI),
    path('gatito/<id>', views.gatitoAPI),

    path('gatito/savefile', views.SaveFile),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)