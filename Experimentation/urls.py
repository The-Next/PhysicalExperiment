from rest_framework import routers
from Experimentation import views

route = routers.DefaultRouter()

route.register(r'newrtown',views.NewtownAPIPost)

urlpatterns = route.urls