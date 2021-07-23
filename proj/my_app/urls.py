from django.urls import path,re_path
from my_app import views 
from django.contrib.auth import views as auth_views


app_name='my_app'


urlpatterns=[
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('blog/',views.BlogView.as_view(),name='blog'),
    path('signup/',views.SingUpView.as_view(),name='signup'),
    path('single_work/',views.SingeWorkView.as_view(),name='single_work'),
    path('thaks/',views.ThanksView.as_view(),name='thank'),
    path('proyektlar/',views.ProjectListView.as_view(),name='project_list'),
    re_path(r'^proyektlar/(?P<pk>\d+)/$',views.ProjectDetailView.as_view(),name='project_detail'),
    path('',views.PostToProjectView.as_view(),name='postproject_list'),
    re_path(r'^post/(?P<pk>\d+)/$',views.PostProjectDetail.as_view(),name='postproject_detail'),
    path('post/new/',views.PostProjectCreateView.as_view(),name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    path('drafts/',views.PostDraftsView.as_view(),name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
]



