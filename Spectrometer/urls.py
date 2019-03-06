from rest_framework import routers
from Spectrometer import views

route = routers.DefaultRouter()

route.register(r'spectrometer',views.SpectometerAPI)

urlpatterns = route.urls