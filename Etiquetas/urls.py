from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^etiquetas/get/all/$', 'etiquetas.views.etiqueta_list'),
    url(r'^etiquetas/get/(?P<id>[^/]+)/$', 'etiquetas.views.etiqueta_detail'),
    url(r'^etiquetas/add/$', 'etiquetas.views.etiqueta_add'),
    url(r'^etiquetas/save/(?P<id>[^/]+)/$', 'etiquetas.views.etiqueta_save'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
