"""PhysicalExperiment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from LoginValidation.views import *
from Experimentation.views import *
from  rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from django.views.static import serve
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()
schema_view = get_swagger_view(title='api文档')
urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('api-token-auth',obtain_jwt_token),
    path('register/',UserRegisterAPIView.as_view()),
    path('',include('Experimentation.urls')),
    path('',include('Michelson.urls')),
    path('',include('StaticYoungModulus.urls')),
    path('',include('Spectrometer.urls')),
    path('',include('ThermalConductivity.urls')),
    path('',include('DiffractionGrating.urls')),
    path('docs/',schema_view),
]
urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()