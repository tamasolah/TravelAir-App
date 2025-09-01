from rest_framework.routers import DefaultRouter
from .views import RezervareViewSet

router = DefaultRouter()
router.register(r'rezervari', RezervareViewSet, basename='rezervari')


urlpatterns = router.urls
