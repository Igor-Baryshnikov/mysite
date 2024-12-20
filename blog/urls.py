from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # представления поста
    path('', views.post_list, name='post_list'),
    #  path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('drafted/<int:user_id>/', views.drafted_post, name='show_posts'),
    path('publish/<int:post_id>/', views.publish_post, name='post_publish'),
    path('<int:post_id>/delete/',
         views.delete_post, name='post_delete'),
    path('<int:post_id>/edit/',
         views.edit_post, name='post_edit'),
    path('<int:post_id>/comment/',
         views.post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('search/', views.post_search, name='post_search'),
    path('post_create/',
         views.create_post, name='create_post'),
]
