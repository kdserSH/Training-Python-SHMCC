from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import alarmdb
from .alarm_parse import *
from .ssh import *

# Create your views here.
def index(request):
    data = alarmdb.objects.filter().order_by("Ne40")
    return render(request, 'index.html', {
        "data": data
    })

def search(request):
    nename = request.GET.get("ne", "")
    data = alarmdb.objects.filter(Ne40=nename).order_by("Id")
    a = ''
    if len(data) == 0:
        a = 'No Alarm'
    return render(request, 'index.html', {
        "data": data,
        "a": a
    })

def tongbu(request):
    path = 'alarms\\'
    user = 'gongsijie'  # 用户名
    passwd = 'Iamgsj@151'  # 密码
    command = 'dis alarm all'  # NE40指令
    threads = []
    print('Starting......')
    iplist = ['10.222.11.77',
              '10.222.11.78',
              '10.222.11.244',
              '10.222.11.245',
              '10.222.27.36',
              '10.222.27.37',
              '10.222.18.93',
              '10.222.18.94',
              '10.222.25.21',
              '10.222.25.22']  # 设备IP列表
    # threadList = [threading.Thread(target=ssh_command, args=(i, user, passwd, command, path)) for i in iplist]
    # [i.start() for i in threadList]
    # [i.join() for i in threadList]
    list = [(i, user, passwd, command, path) for i in iplist]
    p = multiprocessing.Pool(4)
    aList = p.map(ssh_command, list)
    print('End.')

    engine = create_engine(r'sqlite:///database.db')
    df = ne_alarms(path)
    # print(os.getcwd())
    # 入库
    df.to_sql(name='NE40-Alarm', con=engine, if_exists='replace', index=False)
    return HttpResponseRedirect('/')

