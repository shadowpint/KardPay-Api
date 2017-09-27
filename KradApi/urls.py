

from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

import Api.urls
import users.urls
from KradApi import settings

urlpatterns = [
    # End points of social oauth.For more detail Go to the 'rest_framework_social_oauth2.urls' file
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    # Including all end points of admin panel.
    url(r'^admin/', include(admin.site.urls)),
    # Including all end points related to user. Go to 'users.urls' file
    url(r'^user/', include(users.urls)),
    # Including all end points related to aggregate records
    url(r'^krad/', include(Api.urls)),
]
urlpatterns += [
    # End point to access uploaded live or environment files from browser
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_URL,
        }),
    ]