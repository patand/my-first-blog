# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import main_page, events_json


urlpatterns = patterns('',
    url(r'^$', main_page),
    url(r'^add/$', 'add_page', name='add_page'),
    url(r'^main/$', TemplateView.as_view(template_name="notes/base.html"), name='notes'),
    url(r'^events_json/', 'notes.views.events_json', name='events_json'),
    url(r'^events_drag/', 'notes.views.eventsdrag', name='events_drag'),
    #url(r'^add/$', 'add_page', name='add_page'),
    #url(r'^events_json/', TemplateResponse'notes.views.events_json', name="notes/mytemplate.html"),                  
    #url(r'^events2_json/', 'notes.views.events2_json', name='events2_json'),
)



urlpatterns += patterns('projet2.notes.admin',
                        
                        # url(r'^success$', 'success', name = 'success'),
                         url(r'^import_xls2$', 'import_xls2', name= 'import_xls2'),
                         
                        )
