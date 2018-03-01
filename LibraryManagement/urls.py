from django.conf.urls import include, url
from django.contrib import admin

app_name="library"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('library.urls'))
]
