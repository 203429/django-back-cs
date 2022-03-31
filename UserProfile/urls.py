# Django imports
from django.urls import path, re_path
from django.conf.urls import include

# View imports
from UserProfile.views import user_profile_view, user_profile_view_detail, user_profile_view_detail_data

urlpatterns = [
    re_path(r'^$', user_profile_view.as_view()),
    re_path(r'^(?P<pk>\d+)$', user_profile_view_detail.as_view()),
    re_path(r'^info/(?P<pk>\d+)$', user_profile_view_detail_data.as_view()),
]