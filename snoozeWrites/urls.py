from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]


admin.site.site_header="SnoozeWrites Admin"
admin.site.site_title="SnoozeWrites Admin Panel"
admin.site.index_title="Welcome to SnoozeWrites Admin Panel"
