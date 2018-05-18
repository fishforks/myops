#!/usr/bin/env python
#coding:utf-8
import json
import ansible.runner                               # 导入提供API的模块 runner
runner = ansible.runner.Runner(                     # 运行函数
    module_name = 'shell',                          # 模块名，每行后面得有个 逗号
    module_args = 'date',                           # 模块参数,即要执行的操作
    pattern ='*',                                   # 匹配的主机，和在命令行匹配一样，支持正则，分组等
    forks = 5,                                      # 并发执行梳理
    host_list = '/etc/ansible/hosts',               # 指定host文件，默认走/etc/ansible/hosts
    environment = {'LANG':'zh_CN.UTF-8','LC_CTYPE':'zh_CN.UTF-8'}     # 加上这个可以避免中文乱码
)
data = runner.run()
# print data                                 # 输出结果为字典类型
print json.dumps(data,indent=4)              # 转换为json