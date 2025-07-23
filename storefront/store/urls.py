from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet, basename='collections')
router.register('customers', CustomerViewSet)
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet, basename='orders')


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
products_router.register('images', ProductImageViewSet, basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + products_router.urls + carts_router.urls

# urlpatterns = [
#     path('product_list/', ProductList.as_view()),
#     path('product_detail/<int:pk>/', ProductDetail.as_view()),
#     path('collection_list/', CollectionList.as_view()),
#     path('collection_detail/<int:pk>/', CollectionDetail.as_view())
# ]