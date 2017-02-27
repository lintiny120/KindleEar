#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return bookface

class bookface(WeixinBook):
    title                 = u'微信公众号：bookface'
    description           = u'无人是孤岛，一书一世界'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 7
    deliver_days = ['Everyday']
    feeds = [
            (u'bookface', 'http://weixin.sogou.com/home?stype=3&ie=utf-8&query=bookface&oi=25820]
