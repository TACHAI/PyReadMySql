import pymysql,os



def core_code():

    db = pymysql.connect(host="localhost",user="root",passwd="hzc778209",db="shxh",charset="utf8")
    cursor=db.cursor()

    # 委办局
    listDeptsql = """select id,dept_name from tbl_shxh_office"""

    cursor.execute(listDeptsql)
    listDept=cursor.fetchall()

    print(type(listDept))

    path =os.getcwd()

    for row in listDept:
        deptId = row[0]
        deptName = row[1]

        print('委办局名字：'+deptName)
        print('委办局id：'+str(deptId))

        # todo新建委办局名字为文件名的txt
        fd =open(path+'/shangxian/'+deptName+'.txt','a',encoding='utf-8')

        #  事项表
        listItemsql = """select id,value from tbl_shxh_item where office_id= %s"""

        cursor.execute(listItemsql,(deptId,))
        listItem=cursor.fetchall()

        for itemRow in listItem:

            itemId =itemRow[0]
            itemValue =itemRow[1]

            print('事项名：' + itemValue)

            # 事项名
            fd.write('\n事项名：' + itemValue)

            listOptionsql="""select question_alias,answer from tbl_zjly_yuanju where status='2' and online='0' and item_id= %s"""

            cursor.execute(listOptionsql,(itemId,))
            listOption=cursor.fetchall()
            for option in listOption:
                question=option[0]
                answer=option[1]

                fd.write('\n问题：'+question)
                fd.write('\n答案：'+answer+'\n')

                print(question)
                print(answer)




if __name__=='__main__':
    core_code()


