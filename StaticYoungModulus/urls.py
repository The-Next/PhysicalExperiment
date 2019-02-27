from rest_framework import routers
from StaticYoungModulus import views

route = routers.DefaultRouter()

route.register(r'staticyoungmodulus',views.StaticYoungModulusAPI)

urlpatterns = route.urls