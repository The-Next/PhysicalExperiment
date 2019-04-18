from rest_framework import routers
from ThermalConductivity import views

route = routers.DefaultRouter()
route.register(r'thermalconductivity',views.ThermalConductivityAPI)
route.register(r'thermalconductivity_pdf',views.ThermalConductivityAPI_PDF)

urlpatterns = route.urls