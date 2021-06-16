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


def getCollegeList(request):  # 获取学院列表
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from college where cid like '%s' or cname like '%s' or ccharge like '%s';" %
                    (query, query, query))
        total = len(cur.fetchall())
        sql = "select cid, cname,  ccharge from college where cid like '%s' or cname like '%s' or ccharge like '%s' limit %s,%s;"
        cur.execute(sql % (query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        CollegeList = [{"cid": each[0], "cname":each[1],
                        "ccharge":each[2]} for each in cur.fetchall()]
        print(CollegeList)
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
                                  "CollegeList":   CollegeList},
                         "meta": {
                             "msg": "获取学院列表成功",
                             "status": 200
    }})


def delCollege(request):  # 删除学院
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


def CreateCollege(request):  # 创建学院
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


def ModifyCollege(request):  # 修改学院
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from department,college where department.cid = college.cid and (did like '%s' or dname like '%s' or dcharge like '%s' or cname like '%s');" % (query, query, query, query))
        total = len(cur.fetchall())
        sql = "select did, dname, dcharge, cname from department,college where department.cid = college.cid and (did like '%s' or dname like '%s' or dcharge like '%s' or cname like '%s') limit %s,%s;"
        cur.execute(sql % (query, query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        DepartmentList = [{"did": each[0], "dname":each[1],
                           "dcharge":each[2], "cname":each[3]} for each in cur.fetchall()]
        print(DepartmentList)
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
                                  "DepartmentList":   DepartmentList},
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
    cname = request.GET.get("cname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from college where cname='%s';" % cname)
        cid = cur.fetchall()
        print(cid)
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
    cname = request.GET.get("cname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from college where cname='%s';" % cname)
        cid = cur.fetchall()
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from jiaoyan,department where jiaoyan.did=department.did and (jid like '%s' or jname like '%s' or jcharge like '%s' or dname like '%s');" % (
            query, query, query, query))
        # cur.execute("select * from jiaoyan;")
        total = len(cur.fetchall())
        sql = "select jid, jname,  jcharge, dname from jiaoyan,department where jiaoyan.did=department.did and (jid like '%s' or jname like '%s' or jcharge like '%s' or dname like '%s') limit %s,%s;"
        cur.execute(sql % (query, query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        JiaoYanList = [{"jid": each[0], "jname":each[1],
                        "jcharge":each[2], "dname":each[3]} for each in cur.fetchall()]
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
    dname = request.GET.get("dname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select did from department where dname='%s'" % dname)
        did = cur.fetchall()
        sql = 'insert into jiaoyan (jid,jname,jcharge,did) values (%s,%s,%s,%s);'
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
    dname = request.GET.get("dname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select did from department where dname='%s';" % dname)
        print("select did from department where dname=%s" % dname)
        did = cur.fetchall()
        sql = "update jiaoyan set jname=%s,jcharge=%s,did=%s where jid=%s;"
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from class,department where class.did=department.did and (class.cid like '%s' or cname like '%s' or dname like '%s');" % (query, query, query))
        total = len(cur.fetchall())
        sql = "select class.cid, cname, dname from class,department where class.did=department.did and (class.cid like '%s' or cname like '%s' or dname like '%s') limit %s,%s;"
        cur.execute(sql % (query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        ClassList = [{"cid": each[0], "cname":each[1],
                      "dname":each[2]} for each in cur.fetchall()]
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
    dname = request.GET.get("dname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select did from department where dname='%s';" % dname)
        did = cur.fetchall()
        sql = 'insert into class (cid,cname,did) values (%s,%s,%s);'
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
    dname = request.GET.get("dname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select did from department where dname='%s'" % dname)
        did = cur.fetchall()
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from teacher,jiaoyan where teacher.jid=jiaoyan.jid and (tid like '%s' or tname like '%s' or trank like '%s' or jname like '%s');" %
                    (query, query, query, query))
        total = len(cur.fetchall())
        sql = "select tid, tname, trank, jname from teacher,jiaoyan where teacher.jid=jiaoyan.jid and (tid like '%s' or tname like '%s' or trank like '%s' or jname like '%s') limit %s,%s;"
        cur.execute(sql % (query, query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        TeacherList = [{"tid": each[0], "tname":each[1],
                        "trank":each[2], "jname":each[3]} for each in cur.fetchall()]
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
    jname = request.GET.get("jname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        print("jname: "+jname)
        cur.execute("select jid from jiaoyan where jname='%s';" % jname)
        jid = cur.fetchall()
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
    jname = request.GET.get("jname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select jid from jiaoyan where jname='%s';" % jname)
        jid = cur.fetchall()
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from student,class where student.cid=class.cid and (sid like '%s' or sname like '%s' or ssex like '%s' or cname like '%s');" %
                    (query, query, query, query))
        total = len(cur.fetchall())
        sql = "select sid, sname, ssex, cname from student,class where student.cid=class.cid and (sid like '%s' or sname like '%s' or ssex like '%s' or cname like '%s') limit %s,%s;"
        cur.execute(sql % (query, query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        StudentList = [{"sid": each[0], "sname":each[1],
                        "ssex":each[2], "cname":each[3]} for each in cur.fetchall()]
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
    cname = request.GET.get("cname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from class where cname='%s';" % cname)
        cid = cur.fetchall()
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
    cname = request.GET.get("cname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from class where cname='%s';" % cname)
        cid = cur.fetchall()
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute(
            "select * from course where cid like '%s' or cname like '%s';" % (query, query))
        total = len(cur.fetchall())
        sql = "select cid, cname from course where cid like '%s' or cname like '%s' limit %s,%s;"
        cur.execute(sql % (query, query, (pagenum-1)*pagesize, pagesize))
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from stugrades,student,course where stugrades.sid=student.sid and stugrades.cid=course.cid and (student.sid like '%s' or sname like '%s' or cname like '%s' or sgrade like '%s');" % (query, query, query, query))
        total = len(cur.fetchall())
        sql = "select student.sid, sname, cname, sgrade from stugrades,student,course where stugrades.sid=student.sid and stugrades.cid=course.cid and (student.sid like '%s' or sname like '%s' or cname like '%s' or sgrade like '%s') order by student.sid limit %s,%s;"
        cur.execute(sql % (query, query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        GradeList = [{"sid": each[0], "sname":each[1], "cname":each[2], "sgrade":each[3]}
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
    cname = request.GET.get("cname")
    sgrade = request.GET.get("sgrade")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from course where cname='%s';" % cname)
        cid = cur.fetchall()
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
    cname = request.GET.get("cname")
    sgrade = request.GET.get("sgrade")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from course where cname='%s';" % cname)
        cid = cur.fetchall()
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
    query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select *  from Teacher_Class_Course,teacher,class,course where teacher.tid=Teacher_Class_Course.tid and class.cid=claid and course.cid=couid and (teacher.tid like '%s' or tname like '%s' or class.cname like '%s' or course.cname like '%s');" % (query, query, query, query))
        total = len(cur.fetchall())
        sql = "select teacher.tid, tname, class.cname, course.cname from Teacher_Class_Course,teacher,class,course where teacher.tid=Teacher_Class_Course.tid and class.cid=claid and course.cid=couid and (teacher.tid like '%s' or tname like '%s' or class.cname like '%s' or course.cname like '%s') limit %s,%s;"
        cur.execute(sql % (query, query, query, query,
                    (pagenum-1)*pagesize, pagesize))
        TeacherClassCourseList = [{"tid": each[0], "tname":each[1], "claname":each[2], "couname":each[3]}
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
    claname = request.GET.get("claname")
    couname = request.GET.get("couname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from class where cname='%s';" % claname)
        claid = cur.fetchall()
        cur.execute("select cid from course where cname='%s';" % couname)
        couid = cur.fetchall()
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
    claname = request.GET.get("claname")
    couname = request.GET.get("couname")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select cid from class where cname='%s';" % claname)
        claid = cur.fetchall()
        cur.execute("select cid from course where cname='%s';" % couname)
        couid = cur.fetchall()
        sql = "update Teacher_Class_Course set claid=%s, couid=%s where tid=%s;"
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


"""
    查询
"""


def QueryGradeByClass(request):  # 按班级查询课程成绩
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    cname = request.GET.get("cname")
    # query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select student.sid, sname, course.cname, sgrade from stugrades,student,course,class where stugrades.sid=student.sid and stugrades.cid=course.cid and class.cname='%s' and student.cid=class.cid;" % cname)
        total = len(cur.fetchall())
        sql = "select student.sid, sname, course.cname, sgrade from stugrades,student,course,class where stugrades.sid=student.sid and stugrades.cid=course.cid and class.cname='%s' and student.cid=class.cid order by student.sid limit %s,%s;"
        cur.execute(sql % (cname, (pagenum-1)*pagesize, pagesize))
        GradeList = [{"sid": each[0], "sname":each[1], "cname":each[2], "sgrade":each[3]}
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


def QuerySum(request):  # 查询课程分数段人数
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    cname = request.GET.get("cname")
    left = float(request.GET.get("left"))
    right = float(request.GET.get("right"))
    # query = '%'+request.GET.get("query")+'%'
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()

        cur.execute(
            "select * from stugrades,course,student where sgrade>=%s and sgrade<=%s and student.sid=stugrades.sid and course.cid=stugrades.cid and course.cname='%s';" % (left, right, cname))
        total = len(cur.fetchall())
        sql = "select student.sid,sname,cname,sgrade from stugrades,course,student where sgrade>=%s and sgrade<=%s and student.sid=stugrades.sid and course.cid=stugrades.cid and course.cname='%s' limit %s,%s;"
        cur.execute(sql % (left, right, cname, (pagenum-1)*pagesize, pagesize))
        GradeList = [{"sid": each[0], "sname":each[1], "cname":each[2], "sgrade":each[3]}
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
                "path": "CreateCollege",
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
                "path": "CreateJiaoYan",
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
                "authName": "录入老师教授的班级课程",
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
                "authName": "班级课程成绩",
                "path": "QueryGradeByClass",
                "children": [],
                "order": 1
            }, {
                "id": 32,
                "authName": "课程各分数段人数",
                "path": "QuerySum",
                "children": [],
                "order": 2
            }, {
                "id": 33,
                "authName": "学生总分及名次",
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
# {
#     value:[]
#     options:[{
#         value: '信息工程学院',
#         label: '信息工程学院',
#         children: [{
#           value: '计算机系',
#           label: '计算机系',
#           children: [{
#             value: '计算机191班',
#             label: '计算机191班'
#           }, {
#             value: '计算机192班',
#             label: '计算机192班'
#           }, {
#             value: '计算机193班',
#             label: '计算机193班'
#           }, {
#             value: '计算机194班',
#             label: '计算机194班'
#           }]
#         }, {
#           value: '电子系',
#           label: '电子系',
#           children: [{
#             value: '电子信息191班',
#             label: '电子信息191班'
#           }, {
#             value: '电子信息192班',
#             label: '电子信息192班'
#           }]
#         }]
#       }
#     ]
# }
# r = {'value': [],
#      'options': [
#     {'value': '信息工程学院', 'label': '信息工程学院',
#      'children': [
#          {'value': '计算机系', 'label': '计算机系', 'children': []},
#          {'value': '电子系', 'label': '电子系', 'children': []}
#      ]
#      },
#     {'value': '机电工程学院', 'label': '机电工程学院',
#      'children': [
#          {'value': '计算机系', 'label': '计算机系', 'children': []},
#          {'value': '电子系', 'label': '电子系', 'children': []}]},
#     {'value': '建筑工程学院', 'label': '建筑工程学院', 'children': [{'value': '计算机系', 'label': '计算机系', 'children': []}, {'value': '电子系', 'label': '电子系', 'children': []}]}]}
no = [(), ("cname", "college"), ("dname", "department", "college", "cid", "cname"),
      ("cname", "class", "department", "did", "dname")]

# select dname from department,college where department.cid=college.cid and college.cname='信息工程学院';


def f(curr, deep):
    res = {}
    res["value"] = curr
    res["label"] = curr
    if(deep > 3):
        return res
    sql = "select %s from %s,%s where %s.%s=%s.%s and %s.%s='%s';"
    print(sql % (no[deep][0], no[deep][1], no[deep][2], no[deep][1], no[deep]
          [3], no[deep][2], no[deep][3], no[deep][2], no[deep][4], curr))
    con = pymysql.connect(host="localhost", port=3306,
                          user="root", password="root", db="djangodb")
    cur = con.cursor()
    try:
        cur.execute(sql % (no[deep][0], no[deep][1], no[deep][2], no[deep][1],
                    no[deep][3], no[deep][2], no[deep][3], no[deep][2], no[deep][4], curr))
        result = cur.fetchall()
        # print(result)
        n = len(result)
        if(n == 0):
            print("#"*20)
            return res
        res["children"] = []
        for each in range(0, n):
            res["children"].append(f(result[each][0], deep+1))
            # print(result[each][0])
    except Exception as e:
        print(e)
    finally:
        # print(res)
        cur.close()
        con.close()
        return res


def getMenuTree(request):
    res = {}
    meta = {}
    # res["value"] = []
    data = {}
    data["options"] = []
    con = pymysql.connect(host="localhost", port=3306,
                          user="root", password="root", db="djangodb")
    cur = con.cursor()
    sql = "select cname from college;"
    try:
        cur.execute(sql)
        result = cur.fetchall()
        # print(result)
        for each in range(0, len(result)):
            data["options"].append(f(result[each][0], 2))
            print(result[each][0])
        res["meta"] = {"msg": "修改成功！", "status": 200}
    except Exception as e:
        print(e)
        res["meta"] = {"msg": "获取失败！", "status": 500}
    finally:
        print(res)
        cur.close()
        con.close()
    res["data"] = data
    print(res)
    return JsonResponse(res)


# getMenuTree(0)
