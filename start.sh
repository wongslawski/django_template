#!/bin/sh

#service_root_path="/Users/wanglei/work/mysite/"

#nohup ${service_root_path}/manage.py runserver 0.0.0.0:8000  --noreload 2>&1 > ${service_root_path}/logs/service.log  &

#python manage.py runserver 0.0.0.0:8000 --noreload  &

mkdir logs
nohup python manage.py runserver 0.0.0.0:9010  --noreload &
