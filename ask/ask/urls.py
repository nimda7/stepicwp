"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import qa.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', qa.views.questions_list_all),
    url(r'^login/', qa.views.login, name='login'),
    url(r'^signup/', qa.views.signup, name='signup'),
    url(r'^ask/', qa.views.question_add, name='ask'),
    url(r'^popular/', qa.views.questions_list_popular, name='popular'),
    url(r'^new/', qa.views.test, name='new'),
    url(r'^answer/', qa.views.answer, name='answer'),
    url(r'^question/(?P<id>\d+)/$', qa.views.qa_full, name='question'),
]
