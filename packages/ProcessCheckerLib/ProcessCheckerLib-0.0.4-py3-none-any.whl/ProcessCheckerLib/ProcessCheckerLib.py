import requests,os,sys,traceback
import schedule
import threading
import psutil
from flask import Flask,request
from random import randint
def TracebackChecker(Type,value,tb):
    err='Error: '+str(Type)+' '+str(value)+'. '+'line:'+str(traceback.extract_tb(tb)[-1].lineno)
    TBsend=requests.post('http://127.0.0.1:1488/tb',json={'name':os.path.basename(sys.argv[0]),'traceback':err})
def scriptTracker():
    PIDsend=requests.post('http://127.0.0.1:1488/PID',json={'name':os.path.basename(sys.argv[0]),'pid':str(os.getpid())})
    sys.excepthook = TracebackChecker
    sys.unraisablehook = TracebackChecker
def StartChecker(code,token,chatID):
    #создание словаря для отслеживания, живы ли процессы, и списка-буффера для правильного удаления элементов словаря
    processes={}
    buffernames=[]
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    #функция дающая рандомное количество секунд
    def randtime():
        time=str(randint(0,59))
        if len(time)==1:
            time='0'+time
        return time

    #функция отсчета времени для задач Schedule
    def timc():
        while True:
            schedule.run_pending()

    #запуск функции timc() в параллельный поток
    timcc=threading.Thread(target=timc)
    timcc.start()

    #функция отправляющая серверу данные о том, что клиент онлайн
    def OnlineTap(idu):
        s=requests.get('https://api.telegram.org/bot'+token+'/sendMessage',
            params={'chat_id':chatID,'text':'!;!;! '+idu})

    #функция для отправки серверу данных об исключениях в скриптах и остановках скриптов
    def sck(idu,name,mode=1,text=''):
        if mode==1:
            s=requests.get('https://api.telegram.org/bot'+token+'/sendMessage',
                params={'chat_id':chatID,'text':'!:!:!%%%'+idu+'%%%'+name})
        elif mode==2:
            s=requests.get('https://api.telegram.org/bot'+token+'/sendMessage',
                params={'chat_id':chatID,'text':'!=!=!%%%'+idu+'%%%'+name+'%%%'+text})
        elif mode==3:
            s = requests.get('https://api.telegram.org/bot' + token + '/sendMessage',
                params={'chat_id': chatID, 'text': '$&$&$%%%' + idu + '%%%' + name})

    #постановка задач Schedule для отправки серверу данных о том, что клиент онлайн
    schedule.every().hour.at("14:"+randtime()).do(OnlineTap,code)
    schedule.every().hour.at("29:"+randtime()).do(OnlineTap,code)
    schedule.every().hour.at("44:"+randtime()).do(OnlineTap,code)
    schedule.every().hour.at('59:'+randtime()).do(OnlineTap,code)

    #функция для общения с скриптами посредством Flask приложения
    def sockR():
    
        #создание Flask веб-приложения
        app = Flask(__name__)
        
        #отслеживание, если клиент отправит сообщение '/PID', то выполнится функция new_PID() 
        @app.route('/PID', methods=['POST'])
        def new_PID(): #функция для добавления целевого процесса в processes
            data = request.json
            processes[data['name']]=data['pid']
            sck(code, data['name'], 3)
            return 1

        #
        @app.route('/tb',methods=['POST'])
        def send_tb():
            data = request.json
            sck(code,data['name'],2,data['traceback'])
        if __name__ == '__main__':
            app.run(host='127.0.0.1', port=1488)

    #
    sockr=threading.Thread(target=sockR)
    sockr.start()

    #
    while True:
        for n in processes.keys():
            if not(psutil.pid_exists(int(processes[n]))):
                sck(code,n)
                buffernames.append(n)
        for n in buffernames:
            processes.pop(n)
        buffernames.clear()
