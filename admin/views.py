from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import pymysql
import json

from pymysql import cursors
# Create your views here.


# class DB:
#     def __init__(self) -> None:
#         self = pymysql.connect(host="localhost", port=3306,
#                                user="root", password="root", db="djangodb")

"""
    学院
"""


def getAcadamyList(request):  # 获取学院列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from college;")
        total = len(cur.fetchall())
        sql = "select cid, cname,  ccharge from college limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        acadamylist = [{"cid": each[0], "cname":each[1],
                        "ccharge":each[2]} for each in cur.fetchall()]
        print(acadamylist)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "acadamylist":   acadamylist},
                         "meta": {
                             "msg": "获取学院列表成功",
                             "status": 200
    }})


def delAcadamy(request):  # 删除学院
    cid = request.GET.get("cid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from college where cid=%s;'
        print(sql % cid)
        cur.execute(sql, cid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除学院失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def CreateAcadamy(request):  # 创建学院
    cid = request.GET.get("cid")
    cname = request.GET.get("cname")
    ccharge = request.GET.get("ccharge")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into college (cid,cname,ccharge) values (%s,%s,%s);'
        print(sql % (cid, cname, ccharge))
        cur.execute(sql, (cid, cname, ccharge))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建学院失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyAcadamy(request):  # 修改学院
    cid = request.GET.get("cid")
    cname = request.GET.get("cname")
    ccharge = request.GET.get("ccharge")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update college set cname=%s,ccharge=%s where cid=%s;'
        print(sql % (cname, ccharge, cid))
        cur.execute(sql, (cname, ccharge, cid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改学院信息失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    系
"""


def getDepartmentList(request):  # 获取系列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from department;")
        total = len(cur.fetchall())
        sql = "select did, dname,  dcharge, cid from department limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        Departmentlist = [{"did": each[0], "dname":each[1],
                           "dcharge":each[2], "cid":each[3]} for each in cur.fetchall()]
        print(Departmentlist)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "Departmentlist":   Departmentlist},
                         "meta": {
                             "msg": "获取系列表成功",
                             "status": 200
    }})


def delDepartment(request):  # 删除系
    did = request.GET.get("did")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from department where did=%s;'
        print(sql % did)
        cur.execute(sql, did)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除系失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def CreateDepartment(request):  # 创建系
    did = request.GET.get("did")
    dname = request.GET.get("dname")
    dcharge = request.GET.get("dcharge")
    cid = request.GET.get("cid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into department (did,dname,dcharge,cid) values (%s,%s,%s,%s);'
        print(sql % (did, dname,
              dcharge, cid))
        cur.execute(sql, (did, dname,
                    dcharge, cid))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建系失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyDepartment(request):  # 修改系
    did = request.GET.get("did")
    dname = request.GET.get("dname")
    dcharge = request.GET.get("dcharge")
    cid = request.GET.get("cid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update department set dname=%s,dcharge=%s,cid=%s where did=%s;'
        print(sql % (dname, dcharge,
              cid, did))
        cur.execute(sql, (dname, dcharge,
                    cid, did))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改系信息失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    教研室
"""


def getJiaoYanList(request):  # 获取教研室列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from jiaoyan;")
        total = len(cur.fetchall())
        sql = "select jid, jname,  jcharge, did from jiaoyan limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        JiaoYanList = [{"jid": each[0], "jname":each[1],
                        "jcharge":each[2], "did":each[3]} for each in cur.fetchall()]
        print(JiaoYanList)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "JiaoYanList":   JiaoYanList},
                         "meta": {
                             "msg": "获取教研室列表成功",
                             "status": 200
    }})


def delJiaoYan(request):  # 删除教研室
    jid = request.GET.get("jid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from jiaoyan where jid=%s;'
        print(sql % jid)
        cur.execute(sql, jid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def CreateJiaoYan(request):  # 创建教研室
    jid = request.GET.get("jid")
    jname = request.GET.get("jname")
    jcharge = request.GET.get("jcharge")
    did = request.GET.get("did")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into department (jid,jname,jcharge,did) values (%s,%s,%s,%s);'
        print(sql % (jid, jname,
              jcharge, did))
        cur.execute(sql, (jid, jname,
                    jcharge, did))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyJiaoYan(request):  # 修改教研室
    jid = request.GET.get("jid")
    jname = request.GET.get("jname")
    jcharge = request.GET.get("jcharge")
    did = request.GET.get("did")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update department set jname=%s,jcharge=%s,did=%s where jid=%s;'
        print(sql % (jname, jcharge,
              did, jid))
        cur.execute(sql, (jname, jcharge,
                    did, jid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    班级
"""


def getClassList(request):  # 获取班级列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from class;")
        total = len(cur.fetchall())
        sql = "select cid, cname, did from class limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        ClassList = [{"cid": each[0], "cname":each[1],
                      "did":each[2]} for each in cur.fetchall()]
        print(ClassList)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "ClassList":   ClassList},
                         "meta": {
                             "msg": "获取班级列表成功",
                             "status": 200
    }})


def delClass(request):  # 删除班级
    cid = request.GET.get("cid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from class where cid=%s;'
        print(sql % cid)
        cur.execute(sql, cid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def CreateClass(request):  # 创建班级
    cid = request.GET.get("cid")
    cname = request.GET.get("cname")
    did = request.GET.get("did")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into class (cid,cname,did) values (%s,%s,%s,%s);'
        print(sql % (cid, cname, did))
        cur.execute(sql, (cid, cname, did))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyClass(request):  # 修改班级
    cid = request.GET.get("cid")
    cname = request.GET.get("cname")
    did = request.GET.get("did")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update class set cname=%s,did=%s where cid=%s;'
        print(sql % (cname, did, cid))
        cur.execute(sql, (cname, did, cid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    教师
"""


def getTeacherList(request):  # 获取教师列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from teacher;")
        total = len(cur.fetchall())
        sql = "select tid, tname, trank, jid from teacher limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        TeacherList = [{"tid": each[0], "tname":each[1],
                        "trank":each[2], "jid":each[3]} for each in cur.fetchall()]
        print(TeacherList)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "TeacherList":   TeacherList},
                         "meta": {
                             "msg": "获取教师列表成功",
                             "status": 200
    }})


def delTeacher(request):  # 删除教师
    tid = request.GET.get("tid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from teacher where tid=%s;'
        print(sql % tid)
        cur.execute(sql, tid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def CreateTeacher(request):  # 创建教师
    tid = request.GET.get("tid")
    tname = request.GET.get("tname")
    trank = request.GET.get("trank")
    jid = request.GET.get("jid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into teacher (tid,tname,trank,jid) values (%s,%s,%s,%s);'
        print(sql % (tid, tname, trank, jid))
        cur.execute(sql, (tid, tname, trank, jid))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyTeacher(request):  # 修改教师
    tid = request.GET.get("tid")
    tname = request.GET.get("tname")
    trank = request.GET.get("trank")
    jid = request.GET.get("jid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update teacher set tname=%s,trank=%s,jid=%s where tid=%s;'
        print(sql % (tname, trank, jid, tid))
        cur.execute(sql, (tname, trank, jid, tid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    学生
"""


def getStudentList(request):  # 获取学生列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from student;")
        total = len(cur.fetchall())
        sql = "select sid, sname, ssex, cid from student limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        StudentList = [{"sid": each[0], "sname":each[1],
                        "ssex":each[2], "cid":each[3]} for each in cur.fetchall()]
        print(StudentList)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "StudentList":   StudentList},
                         "meta": {
                             "msg": "获取学生列表成功",
                             "status": 200
    }})


def delStudent(request):  # 删除学生
    sid = request.GET.get("sid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from student where sid=%s;'
        print(sql % sid)
        cur.execute(sql, sid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def CreateStudent(request):  # 创建学生
    sid = request.GET.get("sid")
    sname = request.GET.get("sname")
    ssex = request.GET.get("ssex")
    cid = request.GET.get("cid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into student (sid,sname,ssex,cid) values (%s,%s,%s,%s);'
        print(sql % (sid, sname, ssex, cid))
        cur.execute(sql, (sid, sname, ssex, cid))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyStudent(request):  # 修改学生
    sid = request.GET.get("sid")
    sname = request.GET.get("sname")
    ssex = request.GET.get("ssex")
    cid = request.GET.get("cid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update student set sname=%s,ssex=%s,cid=%s where sid=%s;'
        print(sql % (sname, ssex, cid, sid))
        cur.execute(sql, (sname, ssex, cid, sid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    课程
"""


def getCourseList(request):  # 获取课程列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from course;")
        total = len(cur.fetchall())
        sql = "select cid, cname from course limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        CourseList = [{"cid": each[0], "cname":each[1]}
                      for each in cur.fetchall()]
        print(CourseList)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "CourseList":   CourseList},
                         "meta": {
                             "msg": "获取课程列表成功",
                             "status": 200
    }})


def delCourse(request):  # 删除课程
    cid = request.GET.get("cid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from course where cid=%s;'
        print(sql % cid)
        cur.execute(sql, cid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def CreateCourse(request):  # 创建课程
    cid = request.GET.get("cid")
    cname = request.GET.get("cname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into course (cid,cname) values (%s,%s);'
        print(sql % (cid, cname))
        cur.execute(sql, (cid, cname))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyCourse(request):  # 修改课程
    cid = request.GET.get("cid")
    cname = request.GET.get("cname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update course set cname=%s where cid=%s;'
        print(sql % (cname, cid))
        cur.execute(sql, (cname, cid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    成绩
"""


def getGradeList(request):  # 获取成绩列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from stugrades;")
        total = len(cur.fetchall())
        sql = "select sid, cid, sgrade from stugrades limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        GradeList = [{"sid": each[0], "cid":each[1], "sgrade":each[2]}
                     for each in cur.fetchall()]
        print(GradeList)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "GradeList":   GradeList},
                         "meta": {
                             "msg": "获取成绩列表成功",
                             "status": 200
    }})


def delGrade(request):  # 删除成绩
    sid = request.GET.get("sid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from stugrades where sid=%s;'
        print(sql % sid)
        cur.execute(sql, sid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def InputGrade(request):  # 录入成绩
    sid = request.GET.get("sid")
    cid = request.GET.get("cid")
    sgrade = request.GET.get("sgrade")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into stugrades (sid,cid,sgrade) values (%s,%s,%s);'
        print(sql % (sid, cid, sgrade))
        cur.execute(sql, (sid, cid, sgrade))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "录入成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建失败！")
        res["meta"] = {"msg": "录入失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyGrade(request):  # 修改成绩
    sid = request.GET.get("sid")
    cid = request.GET.get("cid")
    sgrade = request.GET.get("sgrade")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update stugrades set cid=%s, sgrade=%s where sid=%s;'
        print(sql % (cid, sgrade, sid))
        cur.execute(sql, (cid, sgrade, sid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


"""
    老师教授的班级课程
"""


def getTeacherClassCourseList(request):  # 获取老师教授的班级课程列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from Teacher_Class_Course;")
        total = len(cur.fetchall())
        sql = "select tid, claid, couid from Teacher_Class_Course limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        TeacherClassCourseList = [{"tid": each[0], "claid":each[1], "couid":each[2]}
                                  for each in cur.fetchall()]
        print(TeacherClassCourseList)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
        print("total: ", end="")
        print(total)
        print("##########")
    return JsonResponse({"data": {"total": total,
                                  "pagenum": 1,
                                  "TeacherClassCourseList":   TeacherClassCourseList},
                         "meta": {
                             "msg": "获取老师教授的班级课程列表成功",
                             "status": 200
    }})


def delTeacherClassCourse(request):  # 删除老师教授的班级课程
    tid = request.GET.get("tid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from Teacher_Class_Course where tid=%s;'
        print(sql % tid)
        cur.execute(sql, tid)
        con.commit()
        # 删除成功
        res["meta"] = {"msg": "删除成功！", "status": 200}
    except Exception as e:
        # 删除失败
        print(e)
        print("删除失败！")
        res["meta"] = {"msg": "删除失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def InputTeacherClassCourse(request):  # 录入老师教授的班级课程
    tid = request.GET.get("tid")
    claid = request.GET.get("claid")
    couid = request.GET.get("couid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into Teacher_Class_Course (tid,claid,couid) values (%s,%s,%s);'
        print(sql % (tid, claid, couid))
        cur.execute(sql, (tid, claid, couid))
        con.commit()
        # 插入成功
        res["meta"] = {"msg": "创建成功！", "status": 200}
    except Exception as e:
        # 插入失败
        print(e)
        print("创建失败！")
        res["meta"] = {"msg": "创建失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)


def ModifyTeacherClassCourse(request):  # 修改老师教授的班级课程
    tid = request.GET.get("tid")
    claid = request.GET.get("claid")
    couid = request.GET.get("couid")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update Teacher_Class_Course set claid=%s couid=%s where tid=%s;'
        print(sql % (claid, couid, tid))
        cur.execute(sql, (claid, couid, tid))
        con.commit()
        # 修改成功
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        # 修改失败
        print(e)
        print("修改失败！")
        res["meta"] = {"msg": "修改失败！", "status": 400}
    finally:
        cur.close()
        con.close()
        return JsonResponse(res)



def menu(request):
    res = {
        "data": [{
            "id":
            1,
            "authName":
            "创建",
            "path":
            "users",
            "children": [{
                "id": 11,
                "authName": "创建学院",
                "path": "CreateAcadamy",
                "children": [],
                "order": 1
            }, {
                "id": 12,
                "authName": "创建系",
                "path": "CreateDepartment",
                "children": [],
                "order": 2
            }, {
                "id": 13,
                "authName": "创建教研室",
                "path": "CreateTRO",
                "children": [],
                "order": 3
            }, {
                "id": 14,
                "authName": "创建学生班级",
                "path": "CreateClass",
                "children": [],
                "order": 4
            }],
            "order":
            1
        }, {
            "id":
            2,
            "authName":
            "录入",
            "path":
            "rights",
            "children": [{
                "id": 21,
                "authName": "录入老师信息",
                "path": "InputTea",
                "children": [],
                "order": 1
            }, {
                "id": 22,
                "authName": "录入学生信息",
                "path": "InputStu",
                "children": [],
                "order": 2
            }, {
                "id": 23,
                "authName": "录入课程信息",
                "path": "InputCou",
                "children": [],
                "order": 3
            }, {
                "id": 24,
                "authName": "录入老师讲授的课程",
                "path": "InputTeaCou",
                "children": [],
                "order": 4
            }, {
                "id": 25,
                "authName": "录入各班开设的课程",
                "path": "InputClassCou",
                "children": [],
                "order": 5
            }, {
                "id": 26,
                "authName": "录入课程成绩",
                "path": "InputGrade",
                "children": [],
                "order": 6
            }],
            "order":
            2
        }, {
            "id":
            3,
            "authName":
            "查询",
            "path":
            "Query",
            "children": [{
                "id": 31,
                "authName": "按班级查询课程成绩",
                "path": "QueryGrade",
                "children": [],
                "order": 1
            }, {
                "id": 32,
                "authName": "统计某课程的各分数段人数",
                "path": "QuerySum",
                "children": [],
                "order": 2
            }, {
                "id": 33,
                "authName": "统计学生所有课程总分及所在班级名次",
                "path": "QueryRank",
                "children": [],
                "order": 3
            }],
            "order":
            3
        }, {
            "id":
            4,
            "authName":
            "订单管理",
            "path":
            "orders",
            "children": [{
                "id": 41,
                "authName": "订单列表",
                "path": "orders",
                "children": [],
                "order": 0
            }],
            "order":
            4
        }, {
            "id":
            5,
            "authName":
            "数据统计",
            "path":
            "reports",
            "children": [{
                "id": 51,
                "authName": "数据报表",
                "path": "reports",
                "children": [],
                "order": 0
            }],
            "order":
            5
        }],
        "meta": {
            "msg": "获取菜单列表成功",
            "status": 200
        }
    }
    # res = {
    #     "id": "125",
    #     "authName":
    #         "用户管理",
    #         "path":
    #         "users",
    #         "children": [{
    #             "id": "110",
    #             "authName": "用户列表",
    #             "path": "users",
    #             "children": [],
    #             "order": "0"
    #         }]
    # }
    return JsonResponse(res)
    # json_str = json.dumps(res, ensure_ascii=False)
    # print(json_str)
    # # 响应状态
    # status = "200 OK"
    # # 响应头
    # response_header = [("Server", "PWS2.0"), ("Content-Type",
    #                                           "application/json; charset=utf-8"), ("Access-Control-Allow-Origin", "*"), ("Access-Control-Request-Headers", "authorization")]
    # # 处理后的数据
    # # res = "1"
    # # print(res)
    # return status, response_header, json_str
