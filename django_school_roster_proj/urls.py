from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

# app_name = 'school'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include('school_roster_app.urls'))
]
