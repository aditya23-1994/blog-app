from django.urls import path
from . import views
app_name= 'blog'
urlpatterns = [
    path('',views.post_list, name='post_list'),
    path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(),name='post_list'),
    path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'), 
    path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),   
]