from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from .models import StockBasic
import quant.data.tushare_data  as ts
import quant.data.futu_api  as futu_api
import json
from django.core import serializers
from django.db import connection
import logging
import time
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
 

def index(request):
    return HttpResponse("Hello, world.")

 
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
 

#数据名称 & 更新or新建 
def data_update(request):
    name = request.GET.get('name')

    is_success = False
    if(name=="stock_basic"):
        StockBasic.objects.all().delete()
        StockBasic.objects.bulk_create(ts.stock_basic())
        is_success = True
    elif(name=="stock_trade_daily"):
        ts.daily_trade()

    res = {"is_success":is_success}

    print("name==",name, " is_success==", is_success)

    return JsonResponse(res, safe=False)

def run_sql(sql):
    
    t1 = time.time()
    with connection.cursor() as cursor:
        cursor.execute(sql)
        cursor.execute(sql)
        total = cursor.fetchall()
    t2 = time.time()
    logger.warn("sql exc time:" + str((t2-t1))+ " " + sql)
    return total






def query_table(request,db_type='postgresql'):

    table_name = request.GET.get('table_name')
    page = request.GET.get('page')
    size = request.GET.get('size')
    where = request.GET.get('where')

    #start = (int(page)-1)*int(size)

    

    with connection.cursor() as cursor:
        sql = 'select * from ' + table_name;
        limit_sql = ""
        where_sql = ""

        if(page != None and size!=None):
            start = (int(page)-1)*int(size)
            if(db_type=='mysql'):
                limit_sql = ' limit ' + str(start) + ',' + size
            elif(db_type=='postgresql'):
                limit_sql = ' limit ' + size  + ' offset ' + str(start)
        if(where!=None):
            where_sql = ' where ' + where
        sql = sql + where_sql + limit_sql
        print("sql---"+sql)
        cursor.execute(sql)
        #data = cursor.fetchall()
        data = dictfetchall(cursor)
        sql = 'select count(*) from ' + table_name + where_sql  #+ limit_sql
        cursor.execute(sql)
        total = cursor.fetchall()[0][0]

    res = {"total":total,"data":data}

    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})



def chart_data(request):
    #chart_type = request.GET.get('type')
    sql = 'select * from stock_trade_daily where trade_date="20210301"'

    stock_basic = run_sql("select * from stock_basic")
    
    return JsonResponse(run_sql(sql),safe=False, json_dumps_params={'ensure_ascii': False})

    




def meta_tables(request,db_type="postgresql"):
    with connection.cursor() as cursor:
        if (db_type=="mysql"):
            cursor.execute("show table status like '%quant%'")
            #cursor.execute("SELECT * FROM information_schema.tables  WHERE table_schema = 'quant'")
            data = dictfetchall(cursor)
        else:
            data= {}

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})



def futu_info(request):
    res = futu_api.accinfo_query()
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})

    # null;
