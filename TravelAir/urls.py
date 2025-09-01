from django.contrib import admin
from django.urls import path, include
from oferte import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oferte.urls')),
    path('api/oferte/', views.OfferListView.as_view()),
    path('api/oferte/<int:pk>/', views.OfferDetailView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('rezervari.urls')), 

    path("api/", include("contact.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
