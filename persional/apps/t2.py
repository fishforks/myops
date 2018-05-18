# -*- coding: utf-8 -*-

# import jenkins
# context = {}
# server = jenkins.Jenkins('http://192.168.25.12:8080', username="xiazy", password="18edb8794c4c0389b0b91e29bed08ba9")
# all_jobs = server.get_all_jobs(folder_depth=2)
# for job in all_jobs:
#     print job['fullname']
# server.build_job("pipe/pipe-jar")
# obj = server.get_build_console_output("pipe/pipe-jar",69)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView,CreateView, UpdateView

from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.base import ContentFile
import logging, traceback,json


class JsonfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'deploy/jsonfile-edit.html'
    context_object_name = "jsonfile"

    def get_context_data(self, **kwargs):
        context = super(JsonfileEditView, self).get_context_data(**kwargs)
        jsonfile_text = ''
        with open('/jsonfile/xm-fsp20-cust.json', 'r') as f:
            for line in f:
                jsonfile_text += line
        context['jsonfile_text'] = json.dumps(jsonfile_text)
        return context