from django.shortcuts import render,HttpResponse
from .models import *
def index(request):
    # course_obj = Course.objects.filter(title='python').first()
    # content_type = ContentType.objects.filter(model='course').first()
    # #
    # # print(course_obj)
    # # print(content_type)
    # obj = Policy.objects.create(content_type=content_type,object_id=course_obj.id,price=30)
    # # # print(obj)
    # course_obj = Course.objects.filter(title='python').first()
    # Policy.objects.create(content_object=course_obj,price=40)
    # obj = Course.objects.filter(title='python').first()
    # print(obj.policy_list.all())
    # from django.contrib.contenttypes.fields import create_generic_related_manager
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    # Course.objects.update(title=Concat('pk','title'))
    # Course.objects.update(title=Concat('title',Value('666')))


    # import pymysql
    # from django.db import connection, connections
    # cursor = connection.cursor()
    # cursor.execute("""SELECT * from app01_course""")
    # row = cursor.fetchone()
    # print(row)
    # connection.close()

    # name_map = {'price':'newname'}
    # a = Course.objects.raw('select * from app01_policy',translations=name_map)
    # for i in a:
    #     print(i,i.newname)

    # lst = Course.objects.extra(where=['title like "1%"']).values()
    # print(lst)
    # for i in lst:
    #     print(i)
    # print(request.COOKIES.get('k'))
    # response = render(request,'index.html',{"lst":lst[0]})
    # response.set_cookie('k','v',expires=None)
    return render(request,'index.html')





    # return HttpResponse('ok')