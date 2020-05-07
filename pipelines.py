# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi  
from scrapy.http import Request  
from scrapy.exceptions import DropItem  
#from scrapy.contrib.pipeline.images import ImagesPipeline  
import time  
import psycopg2 

class GplayPipeline(object):  

    def __init__(self):
        print("init connection to DB")
        # self.connection = psycopg2.connect(database="ggplay",
        #                              user="postgres",
        #                              password="Canh1234",
        #                              host="127.0.0.1",
        #                              port="5432")
        
    def process_item(self, item, spider):
        print("process items in pipeline")
        connection = psycopg2.connect(database="ggplay",
                                     user="postgres",
                                     password="Canh1234",
                                     host="127.0.0.1",
                                     port="5432")
        try:
            cursor = connection.cursor()
            cursor.execute("insert into new_apps(app_id, item_name, updated) values(%s, %s, %s)",(item["Link"], item["Item_name"], item["Updated"]))
            connection.commit()
        except(Exception,psycopg2.Error) as error:
            print("Error connecting", error)
            connection.rollback()
        finally:
            if connection:
                print("Close connection")
                cursor.close()
                connection.close()

        return item  
