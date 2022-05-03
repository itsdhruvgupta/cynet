
from django.contrib import admin
from django.urls import path, include

"""admin.site.site_header =" BGMI Admin"
admin.site.site_title = " BGMI Admin Portal"
admin.site.index_header = " Welcome admin"
"""

urlpatterns = [
    path('cynet/admin/', admin.site.urls),
    path('cynet',include('home.urls'))
]