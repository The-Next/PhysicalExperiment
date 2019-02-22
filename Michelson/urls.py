from rest_framework import routers
from Michelson import views

route = routers.DefaultRouter()

route.register(r'michelson',views.MichelsonAPI)#url末端必须以反斜杠结尾

urlpatterns = route.urls