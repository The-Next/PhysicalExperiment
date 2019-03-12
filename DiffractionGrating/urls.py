from rest_framework import routers
from DiffractionGrating import views

route = routers.DefaultRouter()

route.register(r'diffractiongrating',views.DiffractionGratingAPI)#url末端必须以反斜杠结尾

urlpatterns = route.urls