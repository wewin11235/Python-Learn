"""定义 learning_logs 的 URL 模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # index page
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^topics/?$', views.topics, name='topics'),

    # 特定主题详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 添加新主题
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]