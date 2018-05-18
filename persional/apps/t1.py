# -*- coding: utf-8 -*-

import jenkins
context = {}
server = jenkins.Jenkins('http://192.168.25.12:8080', username="xiazy", password="18edb8794c4c0389b0b91e29bed08ba9")
all_jobs = server.get_all_jobs(folder_depth=2)

# for job in all_jobs:
#     print job['fullname']
# server.build_job("pipe/pipe-jar")
obj = server.get_build_console_output("pipe/pipe-jar",69)
print obj

