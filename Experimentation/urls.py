from rest_framework import routers
from Experimentation import views

route = routers.DefaultRouter()

route.register(r'newrtown',views.NewtownAPI)#url末端必须以反斜杠结尾

urlpatterns = route.urls