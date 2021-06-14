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
from django.urls import path
from admin.views import menu
# 学院
from admin.views import CreateAcadamy
from admin.views import getAcadamyList
from admin.views import delAcadamy
from admin.views import ModifyAcadamy
# 系
from admin.views import CreateDepartment
from admin.views import getDepartmentList
from admin.views import delDepartment
from admin.views import ModifyDepartment
# 教研室
from admin.views import CreateJiaoYan
from admin.views import getJiaoYanList
from admin.views import delJiaoYan
from admin.views import ModifyJiaoYan
# 班级
from admin.views import CreateClass
from admin.views import getClassList
from admin.views import delClass
from admin.views import ModifyClass
# 教师
from admin.views import CreateTeacher
from admin.views import getTeacherList
from admin.views import delTeacher
from admin.views import ModifyTeacher
# 学生
from admin.views import CreateStudent
from admin.views import getStudentList
from admin.views import delStudent
from admin.views import ModifyStudent
# 课程
from admin.views import CreateCourse
from admin.views import getCourseList
from admin.views import delCourse
from admin.views import ModifyCourse
# 成绩
from admin.views import InputGrade
from admin.views import getGradeList
from admin.views import delGrade
from admin.views import ModifyGrade
# 老师教授的班级课程
from admin.views import InputTeacherClassCourse
from admin.views import getTeacherClassCourseList
from admin.views import delTeacherClassCourse
from admin.views import ModifyTeacherClassCourse
# from admin.views import *
urlpatterns = [
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
    path('ModifyDepartment/', ModifyDepartment),
    # 教研室
    path('CreateJiaoYan/', CreateJiaoYan),
    path('getJiaoYanList/', getJiaoYanList),
    path('delJiaoYan/', delJiaoYan),
    path('ModifyJiaoYan/', ModifyJiaoYan),
    # 教室
    path('CreateClass/', CreateClass),
    path('getClassList/', getClassList),
    path('delClass/', delClass),
    path('ModifyClass/', ModifyClass),
    # 教师
    path('CreateTeacher/', CreateTeacher),
    path('getTeacherList/', getTeacherList),
    path('delTeacher/', delTeacher),
    path('ModifyTeacher/', ModifyTeacher),
    # 学生
    path('CreateStudent/', CreateStudent),
    path('getStudentList/', getStudentList),
    path('delStudent/', delStudent),
    path('ModifyStudent/', ModifyStudent),
    # 课程
    path('CreateCourse/', CreateCourse),
    path('getCourseList/', getCourseList),
    path('delCourse/', delCourse),
    path('ModifyCourse/', ModifyCourse),
    # 成绩
    path('InputGrade/', InputGrade),
    path('getGradeList/', getGradeList),
    path('delGrade/', delGrade),
    path('ModifyGrade/', ModifyGrade),
    # 老师教授的班级课程
    path('InputTeacherClassCourse/', InputTeacherClassCourse),
    path('getTeacherClassCourseList/', getTeacherClassCourseList),
    path('delTeacherClassCourse/', delTeacherClassCourse),
    path('ModifyTeacherClassCourse/', ModifyTeacherClassCourse)
]
