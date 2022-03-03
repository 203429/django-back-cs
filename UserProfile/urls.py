# Django imports
from django.urls import path, re_path
from django.conf.urls import include

# View imports
from UserProfile.views import userProfileView, userProfileViewDetail

urlpatterns = [
    re_path(r'^$', userProfileView.as_view()),
    re_path(r'^(?P<pk>\d+)$', userProfileViewDetail.as_view()),
]