# -*- coding: utf-8 -*-
import  jenkins
import  re,time,os,logging,traceback,json
from opsweb.settings import Jenkins_HTTP_URI, Jenkins_User, Jenkins_User_API_Token
from threading import Thread
from time import sleep
from deploy.models import Deploydcos
from datetime import datetime

jenkins_server = jenkins.Jenkins(Jenkins_HTTP_URI, username=Jenkins_User, password=Jenkins_User_API_Token)

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@async
def Jenkins_apply(project):
    last_build_number = jenkins_server.get_job_info(project)['lastCompletedBuild']['number']
    this_build_number = last_build_number + 1
    #判断当前是否有job在执行
    if jenkins_server.get_build_info(project,last_build_number)['building'] == False:
        jenkins_server.build_job(project)

        while  True:
            #判断构建是否完成,构建完成则返回最后一次构建id,和last_build_number进行判断，成功则返回日志,否则循环
            if jenkins_server.get_job_info(project)['lastCompletedBuild']['number'] == this_build_number:
                result = jenkins_server.get_build_console_output(project, this_build_number)
                buildstatus = re.search(r'Finished:(\s)(\S+)', result).group(2)
                deploy_time = datetime.now()
                d = Deploydcos.objects.filter(jobname__exact=project)
                if d.exists():
                    d.update(deploy_time=deploy_time,result=result,num=this_build_number,status=0,buildstatus=buildstatus)
                else:
                    Deploydcos.objects.create(jobname=project,deploy_time=deploy_time,result=result,num=this_build_number,buildstatus=buildstatus)
                jsonfile = "/jsonfile/%s.json" % project
                if os.access(jsonfile, os.F_OK):
                    image = re.search(r'\[INFO\] Building image(\s)(\S+)', result)
                    if image:
                        image = image.group(2)
                        with open(jsonfile, 'r+') as f:
                            j = json.load(f)
                            j['container']['docker']['image'] = image

                        with open(jsonfile, 'w+') as f:
                            json.dump(j, f, indent=2)

                break
            else:
                continue

    return this_build_number


