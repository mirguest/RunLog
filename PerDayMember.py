#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import torndb

class PerDayMemberManager(object):
    def __init__(self, database='runlog', host='127.0.0.1:3306', user='run', password='run'):
        self._db = torndb.Connection(
                                     host=host,
                                     database=database,
                                     user=user,
                                     password=password)

    def __del__(self):
        self._db.close()

    # Manage the user
    # Only query and insert are needed.

    def user_get_by_id(self, id):
        return self._db.get("select * from runners where id=%s", id)

    def user_get_by_ids(self, ids):
        return map(self.user_get_by_id, ids)

    def user_add(self, user, email):
        if self._db.get("select * from runners where email=%s", email):
            # The email is already exist
            return False
        self._db.execute("insert into runners (email, name) "
                         "values (%s, %s)", email, user)
        return True

    # Manage the Daily Run Log.
    def daily_runlog_add(self, runner_id, day):
        if self._db.get("select * from daily_run_log "
                        "where day=%s and runner_id=%s",
                        day, runner_id):
            return False
        self._db.execute("insert into daily_run_log (runner_id, day) "
                         "values (%s, %s)", runner_id, day)
        return True

    def daily_runlog_get_userids_by_day(self, day):
        ids= self._db.query("select runner_id from daily_run_log "
                            "where day=%s", day)
        return [id['runner_id'] for id in ids]

    def daily_runlog_get_users_by_day(self, day):
        ids = self.daily_runlog_get_userids_by_day(day)
        return self.user_get_by_ids(ids)

    def daily_runlog_get_days_by_userid(self, id):
        days = self._db.query("select day from daily_run_log "
                              "where runner_id=%s", id)
        return [day['day'] for day in days]

    # Some interface
    def get(self, data):
        users = self.daily_runlog_get_users_by_day(data)
        return [(user['id'],user['name']) for user in users if user]
    def add(self, date, userid):
        return self.daily_runlog_add(userid, date)

    def getusers(self):
        return self._db.query('select * from runners')

    def getlog(self, userid):
        return self.daily_runlog_get_days_by_userid(userid)

if __name__ == "__main__":
    mgr = PerDayMemberManager()
    print mgr.user_add(user="Lin Tao", email="lintao51@gmail.com")
    print mgr.user_add(user="Lin Tao", email="lintao51@gmail.com")
    print mgr.user_get_by_id(1)
    print mgr.user_get_by_ids([1])
    print mgr.daily_runlog_add(1, "2012/12/23")
    print mgr.daily_runlog_get_userids_by_day('2012/12/23')
    print mgr.daily_runlog_get_users_by_day('2012/12/23')
    print mgr.daily_runlog_get_days_by_userid(1)

    print "2012/12/23"
    print mgr.get('2012/12/23')
    print "2012/12/22"
    print mgr.add('2012/12/22', 1)
    print mgr.get('2012/12/22')
    print mgr.add('2012/12/23', 1)
    print mgr.getusers()
    print mgr.getlog(1)
