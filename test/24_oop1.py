#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-18 23:39:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class People:

    def myname(self, name):
        self.names = name

    def say(self):
        print("people say my name is: ", self.names)


p = People()
p.myname('anxi')
p.say()
#People.say(p, "lalala")
