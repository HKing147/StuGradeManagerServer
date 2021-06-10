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


def getAcadamyList(request):
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from NCU;")
        total = len(cur.fetchall())
        sql = "select AcadamyID, AcadamyName,  AcadamyProfessor from NCU limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        acadamylist = [{"AcadamyID": each[0], "AcadamyName":each[1],
                        "AcadamyProfessor":each[2]} for each in cur.fetchall()]
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


def delAcadamy(request):
    AcadamyID = request.GET.get("AcadamyID")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from NCU where AcadamyID=%s;'
        print(sql % AcadamyID)
        cur.execute(sql, AcadamyID)
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


def CreateAcadamy(request):
    AcadamyID = request.GET.get("AcadamyID")
    AcadamyName = request.GET.get("AcadamyName")
    AcadamyProfessor = request.GET.get("AcadamyProfessor")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into NCU (AcadamyID,AcadamyName,AcadamyProfessor) values (%s,%s,%s);'
        print(sql % (AcadamyID, AcadamyName, AcadamyProfessor))
        cur.execute(sql, (AcadamyID, AcadamyName, AcadamyProfessor))
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
    # pass


def ModifyAcadamy(request):
    AcadamyID = request.GET.get("AcadamyID")
    AcadamyName = request.GET.get("AcadamyName")
    AcadamyProfessor = request.GET.get("AcadamyProfessor")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update NCU set AcadamyName=%s,AcadamyProfessor=%s where AcadamyID=%s;'
        print(sql % (AcadamyName, AcadamyProfessor, AcadamyID))
        cur.execute(sql, (AcadamyName, AcadamyProfessor, AcadamyID))
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


def getDepartmentList(request):
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    total = 0
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        cur.execute("select * from Acadamy;")
        total = len(cur.fetchall())
        sql = "select DepartmentID, DepartmentName,  DepartmentProfessor from Acadamy limit %s,%s;"
        cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
        Departmentlist = [{"DepartmentID": each[0], "DepartmentName":each[1],
                           "DepartmentProfessor":each[2]} for each in cur.fetchall()]
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


def delDepartment(request):
    DepartmentID = request.GET.get("DepartmentID")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'delete from Acadamy where DepartmentID=%s;'
        print(sql % DepartmentID)
        cur.execute(sql, DepartmentID)
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


def CreateDepartment(request):
    DepartmentID = request.GET.get("DepartmentID")
    DepartmentName = request.GET.get("DepartmentName")
    DepartmentProfessor = request.GET.get("DepartmentProfessor")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'insert into Acadamy (DepartmentID,DepartmentName,DepartmentProfessor) values (%s,%s,%s);'
        print(sql % (DepartmentID, DepartmentName, DepartmentProfessor))
        cur.execute(sql, (DepartmentID, DepartmentName, DepartmentProfessor))
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
    # pass


def ModifyDepartment(request):
    DepartmentID = request.GET.get("DepartmentID")
    DepartmentName = request.GET.get("DepartmentName")
    DepartmentProfessor = request.GET.get("DepartmentProfessor")
    res = {}
    try:
        con = pymysql.connect(host="localhost", port=3306,
                              user="root", password="root", db="djangodb")
        cur = con.cursor()
        sql = 'update Acadamy set DepartmentName=%s,DepartmentProfessor=%s where DepartmentID=%s;'
        print(sql % (DepartmentName, DepartmentProfessor, DepartmentID))
        cur.execute(sql, (DepartmentName, DepartmentProfessor, DepartmentID))
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


def test(request):
    print("请求头: ")
    print(request)
    print("请求头结束")
    """
        根据pagesize和pagenum查询数据
    """
    pagesize = int(request.GET.get("pagesize"))
    pagenum = int(request.GET.get("pagenum"))
    # print(request.GET.get("pagesize"))
    con = pymysql.Connect(host="localhost", user="root",
                          password="root", port=3306, db="mydb")
    # print(con)
    cur = con.cursor()
    # sql = "select mg_name, mg_mobile,  mg_email from sp_manager;"
    sql = "select mg_name, mg_mobile,  mg_email, sp_role.role_name, mg_state, mg_id from sp_role right outer join sp_manager on (sp_role.role_id=sp_manager.role_id) limit %s,%s;"
    cur.execute(sql, ((pagenum-1)*pagesize, pagenum*pagesize))
    res = []
    for each in cur.fetchall():
        one = {}
        one["id"] = each[5]
        one["username"] = each[0]
        one["mobile"] = each[1]
        one["email"] = each[2]
        one["role_name"] = each[3]
        one["mg_state"] = each[4]
        print(one)
        res.append(one)
    con.close()
    return JsonResponse({"data": {"total": 6,
                                  "pagenum": 1,
                                  "users":   res},
                         "meta": {
                             "msg": "获取管理员列表成功",
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
