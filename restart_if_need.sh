ls_date=`date +"%Y-%m-%d %H-%M-%S"`
ps -ef | grep wordseg | grep -v "grep"| grep -v "restart_if_need.sh"
active_cnt=`ps -ef | grep runserver |grep 9010 | grep -v "grep"| grep -v "restart_if_need.sh" | wc -l`
if [ $active_cnt -ne 0 ]; then
    echo "$ls_date - $active_cnt process found, skip restart"
    exit 0
fi
echo "$ls_date - $active_cnt process found, perform restart"
mkdir logs
#alert
nohup /opt/anaconda2/bin/python2.7 manage.py runserver 0.0.0.0:9010 --noreload &
