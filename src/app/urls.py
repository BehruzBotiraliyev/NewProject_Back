from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, FooterViewSet, AboutViewSet, ServicesViewSet, EmployeesViewSet, SendApplicationViewSet

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')
router.register(r'footer', FooterViewSet, basename='footer')
router.register(r'about', AboutViewSet, basename='about')
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'employees', EmployeesViewSet, basename='employees')
router.register(r'applications', SendApplicationViewSet, basename='applications')

urlpatterns = router.urls
