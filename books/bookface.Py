#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return bookface

class bookface(WeixinBook):
    title                 = u'΢�Ź��ںţ�bookface'
    description           = u'�����ǹµ���һ��һ����'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 7
    deliver_days = ['Everyday']
    feeds = [
            (u'С����Ϣ', 'http://weixin.sogou.com/home?stype=3&ie=utf-8&query=bookface&oi=25820]