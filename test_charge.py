# -*- coding: utf-8 -*-#
from websocket import create_connection
import json
import time
import urllib3


global false, null, true
false = null = true = ""
try:
    time_number = int(input("回充时间(分钟)："))
except BaseException as e:
    print"回充时间输入整数！"
try:
    navigation_times = int(input("导航循环次数："))
except BaseException as e:
    print"导航循环次数输入整数！"
map_name_data = input("输入地图名称: ")
navigation1 = input("输入导航起始点名称：")
navigation2 = input("输入导航终止点名称：")
navigation3 = input("输入充电点名称：")
try:
    times_number = input("请输入轮回次数：")
except BaseException as e:
    print"输入轮回次数输入整数！"
times = int(time_number) * 60

def charge_main():
    key = 'charge'
    key1 = 'batteryVoltage'
    key2 = 'charger'
    key3 = 'battery'
    ws = create_connection("ws://10.7.5.88:8089/gs-robot/notice/device_status")
    ws.send("token")
    data = ws.recv()
    s = json.dumps(data)
    s1 = json.loads(s)
    s = json.loads(s1)
    file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
    file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器充电状态：' + str(s[key2]) + "\n")
    file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器电池电压：' + str(s[key1]) + "\n")
    file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器电量：' + str(s[key3]) + "\n")
    file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器充电继电器状态：' + str(s[key]) + "\n")
    file_handle.close()
    return s[key],s[key1],s[key2],s[key3]
    time.sleep(2)
def work_underway():
    key = 'statusCode'

    try:
        ws = create_connection("ws://10.7.5.88:8089/gs-robot/notice/status")
        dataa = ws.recv()
        sss = json.dumps(dataa)
        sss1 = json.loads(sss)
        sss = json.loads(sss1)
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器任务状态：' + str(sss[key]) + "\n")
        file_handle.close()
        return sss[key]
    except BaseException as e:
        print"调用失败，重新调用！"
        pass
    time.sleep(2)


def start_task():
    print"机器开始导航到起始点：", navigation1
    http = 'http://10.7.5.88:8080/gs-robot/cmd/position/navigate?map_name='+map_name_data+'&position_name='+navigation1
    try:
        a = urllib3.PoolManager()
        r = a.request('GET', http)
        navigation = json.loads(r.data.decode('utf-8'))
        line = navigation['successed']
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器开始导航：' + str(navigation1) + "\n")
        file_handle.close()
        return navigation
    except BaseException as e:
        print"导航目标点1调用失败，重新调用！"
        pass
    time.sleep(2)

def start_task1():
    print"机器开始导航到终点：",navigation2
    httpp = 'http://10.7.5.88:8080/gs-robot/cmd/position/navigate?map_name='+map_name_data+'&position_name='+navigation2
    try:
        a1 = urllib3.PoolManager()
        r1 = a1.request('GET', httpp)
        navigationn = json.loads(r1.data.decode('utf-8'))
        linener = navigationn['successed']
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器开始导航：' + str(navigation2) + "\n")
        file_handle.close()
        return navigationn
    except BaseException as e:
        print"导航目标点2调用失败，重新调用！"
        pass
    time.sleep(2)

def start_task2():
    print"机器开始导航到充电点：", navigation3
    httppp = 'http://10.7.5.88:8080/gs-robot/cmd/position/navigate?map_name='+map_name_data+'&position_name='+navigation3
    try:
        a2 = urllib3.PoolManager()
        r2 = a2.request('GET', httppp)
        navigationnn = json.loads(r2.data.decode('utf-8'))
        linenered = navigationnn['successed']
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器开始导航：' + str(navigation3) + "\n")
        file_handle.close()
        return navigationnn
    except BaseException as e:
        print"导航充电桩调用失败，重新调用！"
        pass
    time.sleep(2)

def work_status():
    urll = 'http://10.7.5.88:8080/gs-robot/real_time_data/work_status'
    c = urllib3.PoolManager()
    try:
        d = c.request('GET',urll)
        b = json.loads(d.data.decode('utf-8'))
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '机器工作状态：' + str(b) + "\n")
        file_handle.close()
        line = b['successed']
    except BaseException as e:
        print"调用机器工作状态失败，重新调用！"
        pass
    time.sleep(2)

def task_status():
    task = 'http://10.7.5.88:8080/gs-robot/cmd/is_task_queue_finished'
    e = urllib3.PoolManager()
    try:
        f = e.request('GET', task)
        g = json.loads(f.data.decode('utf-8'))
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '导航任务是否完成：' + str(g) + "\n")
        file_handle.close()
        liner = g['data']
        return liner
    except BaseException as e:
        print"调用检查任务是否结束失败，重新调用！"
        pass
    time.sleep(2)

def cancel_task():
    print"取消当前导航任务"
    taskl = 'http://10.7.5.88:8080/gs-robot/cmd/stop_current_task'
    try:
        ee = urllib3.PoolManager()
        ff = ee.request('GET',taskl)
        gg = json.loads(ff.data.decode('utf-8'))
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '取消导航任务：' + str(gg) + "\n")
        file_handle.close()
        liner = gg['data']
    except BaseException as e:
        print"调用取消任务失败，重新调用！"
        pass
    time.sleep(2)



count = 1
i = 1
j = 1
def ceshi():
    global i,count,j
    while i <= int(times_number):
        file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
        file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) +'第'+str(i)+'轮: '+'导航循环次数：' + str(count) + "\n")
        file_handle.close()
        if count <= int(navigation_times):
            start_task()
            while True:
                work_status()
                over = task_status()
                if over == True:
                    start_task1()
                    while True:
                        work_status()
                        over = task_status()
                        if over == True:
                            count = count + 1
                            break
                        else:
                            continue
                    break
                else:
                    continue
        else:
            start_task2()
            while True:
                task_statuss = work_underway()
                if task_statuss == 409:
                    print"机器寻找对桩。。。"
                    continue
                elif task_statuss == 410:
                    print"机器移动到充电桩前！"
                    continue
                elif task_statuss == 411:
                    print"机器后退对桩。。。"
                    while True:
                        charge, batteryVoltage, charger, battery = charge_main()
                        if charge == True:
                            file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                            file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电中的时间："+str(time_number)+"  分钟" + "\n")
                            file_handle.close()
                            print"充电中的时间："+str(time_number)+"  分钟"
                            time.sleep(times)
                            file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                            file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电结束" + "\n")
                            file_handle.close()
                            print"充电结束"
                            i = i + 1
                            count = 1
                            j = 1
                            break
                        else:
                            if j <= 10:
                                j = j + 1
                                print"检查是否正常充电", charge
                                print j
                                time.sleep(2)
                            else:
                                j = 1
                                file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                                file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电失败" + "\n")
                                file_handle.close()
                                break

                    break
                elif task_statuss == 407:
                    while True:
                        charge, batteryVoltage, charger, battery = charge_main()
                        if charge == True:
                            file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                            file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电中的时间：" + str(
                                time_number) + "  分钟" + "\n")
                            file_handle.close()
                            print"充电中的时间：" + str(time_number) + "  分钟"
                            time.sleep(times)
                            file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                            file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电结束" + "\n")
                            file_handle.close()
                            print"充电结束"
                            i = i + 1
                            count = 1
                            j = 1
                            break
                        else:
                            if j <= 10:
                                j = j + 1
                                print"检查是否正常充电", charge
                                print j
                                time.sleep(2)
                            else:
                                j = 1
                                file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                                file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电失败" + "\n")
                                file_handle.close()
                                break
                    break
                elif task_statuss == 408:
                    print"充电失败"
                    file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                    file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电失败" + "\n")
                    file_handle.close()
                    i = i + 1
                    count = 1
                    cancel_task()
                    break
                elif task_statuss == 404:
                    print"充电点点不可达"
                    file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
                    file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "充电点点不可达" + "\n")
                    file_handle.close()
                    i = i + 1
                    count = 1
                    cancel_task()
                    break
                else:
                    print"导航到充电桩过程中。。。"
                    continue
    print "总轮回："+str(times_number)+"  "+"总次数："+str(navigation_times)+"  "+"已完成测试"
    file_handle = open(r'log/task_status'+time.strftime('%Y-%m-%d')+'.txt', 'a+')
    file_handle.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "总轮回："+str(times_number)+"  "+"总次数："+str(navigation_times)+"  "+"已完成测试"+"\n")
    file_handle.close()

if __name__ == '__main__':
    ceshi()
