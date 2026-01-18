from rest_framework.routers import SimpleRouter
from .views import ItemViewSet

router = SimpleRouter()
router.register("items", ItemViewSet)

urlpatterns = router.urls