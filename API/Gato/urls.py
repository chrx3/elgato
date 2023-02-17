from django.urls import path, include
from Gato import views

from django.conf.urls.static import static
from django.conf import settings

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Gato.views import UsuarioViewSet, GatoViewSet

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
router.register('Usuario', UsuarioViewSet)
router.register('Gato', GatoViewSet)



urlpatterns=[
    # path('usuario',views.usuarioAPI),
    # path('usuario/<id>', views.usuarioAPI),
    # # path('gatito',views.gatitoAPI),
    # path('gatito/<id>', views.gatitoAPI),
    path('savefile', views.SaveFile),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='Gato:schema'), name='swagger'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)