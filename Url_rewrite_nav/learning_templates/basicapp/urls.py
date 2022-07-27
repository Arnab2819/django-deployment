from django.conf.urls import url
from basicapp import views

##Template Tagging
app_name = 'basicapp'
urlpatterns = [
    url('relative/',views.relative,name='relative'),
    url('others/',views.others,name='others'), 
]
