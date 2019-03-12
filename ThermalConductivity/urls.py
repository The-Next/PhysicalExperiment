from rest_framework import routers
from ThermalConductivity import views

route = routers.DefaultRouter()

route.register(r'thermalconductivity',views.ThermalConductivityAPI)

urlpatterns = route.urls