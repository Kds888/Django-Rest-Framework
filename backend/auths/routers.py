# Similar to urls and we ususally define it in urls.py 
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet,ProductGenericViewSet

router = DefaultRouter()
router.register('products-router',ProductViewSet,basename='products')
router.register('product-router-with-mixin',ProductGenericViewSet,basename='productsmixin')

urlpatterns = router.urls