# -*- coding: utf-8 -*-
import shlex
def bash(cmd):
    return shlex.os.system(cmd)