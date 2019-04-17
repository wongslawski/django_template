# -*- coding: utf-8 -*-

import sys
import json
import urllib,urllib2
import threading

reload(sys)
sys.setdefaultencoding( "utf-8" )

def post_request(url, params, is_json_format, export_dict):
    data = json.dumps(params) if is_json_format else urllib.urlencode(params)
    req = urllib2.Request(url, data)
    if is_json_format:
        req.add_header("Content-Type", "application/json")
    try:
        res = urllib2.urlopen(req)
        result_str = res.read()
        output = json.loads(result_str) if is_json_format else result_str
        res.close()
        return output
    except Exception as ex:
        print >> sys.stderr, ex
    return None

def test_post():
    textmod = {"k": "v"}
    textmod = json.dumps(textmod)
    header_dict = {"Content-Type": "application/json"}
    url = "http://x.x.x.x:9010/polls/yourservice"
    req = urllib2.Request(url=url,data=textmod,headers=header_dict)
    res = urllib2.urlopen(req)
    res = res.read()
    print >> sys.stdout, res

def test_get():
    url = "http://x.x.x.x:9010/polls/yourservice"
    textmod = {"k": "v"}
    textmod = urllib.urlencode(textmod)
    req = urllib2.Request(url = '%s%s%s' % (url,'?',textmod))
    res = urllib2.urlopen(req)
    res = res.read()
    print >> sys.stdout, res

# python test.py
if __name__ == "__main__":
    pass
