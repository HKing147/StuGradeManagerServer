import random
import pymysql


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9) # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st


def first_name(): #   随机取姓氏字典
    first_name_list = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈',
        '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华',
        '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏',
        '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方',
        '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺',
        '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅',
        '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆',
        '萧', '尹', '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧',
        '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝',
        '董', '梁'
    ]
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name


def second_name():
    # 随机取数组中字符，取到空字符则没有second_name
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name


def last_name():
    return GBK2312()


# 随机生成姓名(2~3位)
def create_name():
    name = first_name() + second_name() + last_name()
    return name


def create_ID(n):
    res = ''
    for each in range(n):
        res += str(random.randint(0, 9))
    return res


#AcadamyList=
"""
1. insert into NCU (AcadamyID,AcadamyName,AcadamyProfessor) values (%s,%s,%s)
2. insert into Acadamy (DepartmentID,DepartmentName,DepartmentProfessor) values (%s,%s,%s)
3. insert into Department (TROID,TROName,TROProfessor) values (%s,%s,%s)
4. insert into TRO (TeacherID,TeacherName,Job) values (%s,%s,%s)
5. insert into Course (CourseID,CourseName) values (%s,%s)
6. insert into Class (ClassID,ClassName) values (%s,%s)
7. insert into Student (StuID,StuName,Sex) values (%s,%s,%s)
"""
College = {1: "信息工程学院", 2: "机电工程学院", 3: "建筑工程学院"}
Department = {1: "计算机系", 2: "电子系"}
jiaoyan = {1: "教研室1", 2: "教研室2", 3: "教研室3"}
Class = {1: "计算机191班", 2: "计算机192班", 3: "计算机193班"}
Course = {1: "计算机网络", 2: "计算机组织与结构", 3: "离散数学", 4: "数据库系统概论"}
Teachers = {}
Students = {}
if __name__ == "__main__":
    con = pymysql.connect(host="localhost",
                          port=3306,
                          user='root',
                          password='root',
                          db='djangodb')
    cur = con.cursor()
    sql = ""
    # 创建学院
    for each in College:
        sql = "insert into college (cid,cname,ccharge) values (%s,'%s','%s')"
        ccharge = create_name()
        try:
            cur.execute(sql % (each, College[each], ccharge))
            con.commit()
            print("创建学院成功")
        except Exception as e:
            print(e)
            print("创建学院失败", each)
    # 创建系
    for each in Department:
        sql = "insert into department (did,dname,dcharge,cid) values (%s,'%s','%s',%s);"
        dcharge = create_name()
        try:
            cur.execute(sql % (each, Department[each], dcharge, 1))
            con.commit()
            print("创建系成功")
        except Exception as e:
            print(e)
            print("创建系失败", each)
    # 创建教研室
    for i in range(1, 20):
        jname = "教研室" + str(i)
        sql = "insert into jiaoyan (jid,jname,jcharge,did) values (%s,'%s','%s',%s)"
        jcharge = create_name()
        did = random.randint(1, 2)
        try:
            cur.execute(sql % (i, jname, jcharge, did))
            con.commit()
            print("创建教研室成功")
        except Exception as e:
            print(e)
            print("创建教研室失败", i)
    # 创建教师
    for i in range(1, 40):
        tname = create_name()
        trank = random.randint(1, 5)
        jid = random.randint(1, 20)
        sql = "insert into teacher (tid,tname,trank,jid) values (%s,'%s',%s,%s)"
        try:
            cur.execute(sql % (i, tname, trank, jid))
            con.commit()
            print("创建教师成功")
            Teachers[i] = tname
        except Exception as e:
            print(e)
            print("创建教师失败", i)
    # 创建班级
    for each in Class:
        sql = "insert into class (cid,cname,did) values (%s,'%s',%s)"
        try:
            cur.execute(sql % (each, Class[each], 1))
            con.commit()
            print("创建班级成功")
        except Exception as e:
            print(e)
            print("创建班级失败", each)
    # 创建学生
    for i in range(1, 200):
        sql = "insert into student (sid,sname,ssex,cid) values (%s,'%s',%s,%s)"
        sname = create_name()
        ssex = random.randint(0, 1)
        cid = random.randint(1, 3)
        try:
            cur.execute(sql % (i, sname, ssex, cid))
            con.commit()
            print("创建学生成功")
            Students[i] = sname
        except Exception as e:
            print(e)
            print("创建学生失败", i)
    # 创建课程
    for each in Course:
        sql = "insert into course (cid,cname) values (%s,'%s')"
        try:
            cur.execute(sql % (each, Course[each]))
            con.commit()
            print("创建课程成功")
        except Exception as e:
            print(e)
            print("创建课程失败", each)
    #print("教师：")
    #for each in Teachers:
    #    print(each, Teachers[each])
    #print("学生：")
    #for each in Students:
    #    print(each, Students[each])

    # 录入学生成绩
    for sid in Students:
        print("#####")
        for cid in range(1, 4):
            print("###########")
            sgrade = random.randint(50, 100)
            sql = "insert into stugrades (sid,cid,sgrade) values (%s,%s,%s)"
            try:
                cur.execute(sql % (sid, cid, sgrade))
                con.commit()
                print("录入成绩成功")
            except Exception as e:
                print(e)
                print("录入成绩失败")
    # 录入老师教授的班级及课程
    for claid in Class:
        for couid in Course:
            n = len(Teachers)
            tid = random.randint(1, n)
            sql = "insert into Teacher_Class_Course (tid,claid,couid) values (%s,%s,%s)"
            try:
                cur.execute(sql % (tid, claid, couid))
                con.commit()
                print("录入老师教授的班级课程成功")
            except Exception as e:
                print(e)
                print("录入老师教授的班级课程失败")

#    print(create_name())
#    print(create_ID(10))
