"""StuGradeManagerServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admin.views import test
from admin.views import menu
from admin.views import CreateAcadamy
from admin.views import getAcadamyList
from admin.views import delAcadamy
from admin.views import ModifyAcadamy

from admin.views import CreateDepartment
from admin.views import getDepartmentList
from admin.views import delDepartment
from admin.views import ModifyDepartment
# from admin.views import *
urlpatterns = [
    path('users/', test),
    path('menu/', menu),
    # 学院
    path('CreateAcadamy/', CreateAcadamy),
    path('getAcadamyList/', getAcadamyList),
    path('delAcadamy/', delAcadamy),
    path('ModifyAcadamy/', ModifyAcadamy),
    # 系
    path('CreateDepartment/', CreateDepartment),
    path('getDepartmentList/', getDepartmentList),
    path('delDepartment/', delDepartment),
    path('ModifyDepartment/', ModifyDepartment)
]
