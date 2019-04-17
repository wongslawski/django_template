# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import codecs
# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from django.conf import settings
from settings import *;
import json
import logging
import time
import datetime
import pytz
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


tz = pytz.timezone('Asia/Shanghai')


def extract_title(request):
    try:
        title = request.POST.get("title", "")
        if title == "":
            title = json.loads(request.body).get("title", "")
        if title == "":
            return None
        if isinstance(title, unicode):
            title = title.encode("utf-8", "ignore")
        return title

    except Exception as ex:
        logging.error(ex)
    return None

@csrf_exempt
def adprofile(request):
    if request.method == "POST":
        title = extract_title(request)
        if title is None:
            result = {"status": -1, "msg": "param error! title must not be empty!"}
            return HttpResponse(json.dumps(result, ensure_ascii=False)) 
        result = {"status": 0, "msg": "succ", "title": title}
        result_str = json.dumps(result, ensure_ascii=False)
        logging.info(result_str)
        return HttpResponse(result_str)
