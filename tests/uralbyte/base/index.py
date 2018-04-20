from sqlite3 import connect
from time import time
from os.path import isfile


class TaskManager:
    def __init__(self, db_file='db.db'):
        self.db = connect(db_file)
        self.create_table()

    def create_table(self):
        self.db.execute(
            """create table if not exists tasks
                                  (id integer primary key autoincrement,
                                   name varchar(255) not null,
                                   comment text,
                                   startTime datetime not null,
                                   endTime datetime,
                                   unique (name, comment, startTime));""")

    def new_task(self):
        name = input("Task name? ")
        comment = input("Comment? ")
        start_time = input(
            "Start time Day/Month/Year Hour:Minute:Second (press Enter if right now): "
        )
        if not start_time:
            time1 = int(time())
        else:
            from datetime import datetime as dt
            time1 = (dt.strptime(start_time, '%Y/%m/%d %H:%M:%S')).timestamp()
        self.db.execute(
            """insert into tasks
               (name, comment, startTime)
               values
               ("{name}","{comment}","{time}")""".format(
                name=name,
                comment=comment,
                time=time1)
        )
        self.db.commit()

    def get_task(self, id=None):
        if not id:
            data = self.db.execute('select * from tasks').fetchall()
        else:
            data = (self.db.execute("""select * from tasks
                                       where
                                       id = '{id}'""".format(id=id)).fetchall())
        return data

    def end_task(self, task_id, end_time=int(time())):
        self.db.execute("""update tasks
                           set endTime = "{}"
                           where id = "{}"
                           and
                           endTime is null""".format(end_time, task_id))
        self.db.commit()
