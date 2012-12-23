#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import calendar
import datetime

class MyCalendar(calendar.HTMLCalendar):

    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        else:
            return ('<td class="%s">'
                    '<a href="/%04d/%02d/%02d">%d</a>'
                    '</td>' % (self.cssclasses[weekday], 
                               self._cur_year,
                               self._cur_month,
                               day,
                               day))

    def formatmonth(self, theyear, themonth, withyear=True):
        self._cur_year = theyear
        self._cur_month = themonth

        return super(MyCalendar, self).formatmonth(theyear, themonth, withyear)

if __name__ == "__main__":
    mc = MyCalendar()
    print mc.formatmonth(2012,12)
