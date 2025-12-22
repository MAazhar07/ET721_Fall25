from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from to_do_list.views import task_list, toggle_complete, edit_task, delete_task
from blog.views import post_list, post_create, post_detail, like_post
from upload_notes.views import note_list, note_upload, note_detail
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),  # Homepage at root URL
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:task_id>/complete/', toggle_complete, name='toggle_complete'),
    path('tasks/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('blog/', post_list, name='post_list'),
    path('blog/create/', post_create, name='post_create'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'),
    path('blog/<int:post_id>/like/', like_post, name='like_post'),
    path('notes/', note_list, name='note_list'),
    path('notes/upload/', note_upload, name='note_upload'),
    path('notes/<int:note_id>/', note_detail, name='note_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)