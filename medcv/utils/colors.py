# !/usr/bin/env python
# -*- coding:utf-8 -*-


from random import randint


def generate_rand_color(n_color=1):
    return [(randint(0, 255), randint(0, 255), randint(0, 255)) for i in range(n_color)]

