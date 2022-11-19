import os
import random
import datetime
import shutil
import glob2
import queue
from chinese_calendar import is_workday
from datetime import timedelta

begin_str = "2022/07/30"
end_str = "2022/11/19"
begin_hour = 9
end_hour = 17
is_955 = True
src_root = "D:/project_2022/code"
dis_root = "D:/project_2022/empty"
date_template = "%Y/%m/%d"
time_template = "%02d.%02d"

begin = datetime.datetime.strptime(begin_str, date_template)
end = datetime.datetime.strptime(end_str, date_template)
choose = begin
choose_str = choose.strftime(date_template)

work_list = []
while choose_str != end_str:
    choose_str = choose.strftime(date_template)
    work = True
    if is_955 and not is_workday(choose):
        work = False

    if not work:
        choose = choose + timedelta(days=1)
        continue

    times = random.randint(2, 3)

    for i in range(times):
        hour = random.randint(9, 17)
        minute = random.randint(0, 59)
        work_list.append([choose_str, time_template % (hour, minute)])

    choose = choose + timedelta(days=1)
print(work_list)
print(len(work_list))

task_list = []
code_list = glob2.glob(src_root+'/**')
for code_file in code_list:
    if os.path.isdir(code_file):
        continue
    src_dir = os.path.dirname(code_file)
    dis_file = code_file.replace(src_root, dis_root)
    dis_dir = src_dir.replace(src_root, dis_root)

    if not os.path.exists(dis_dir):
        os.makedirs(dis_dir)
    shutil.copy(code_file, dis_file)
    task_list.append([dis_file.replace(dis_root, '').replace("\\", '/').strip('/'), os.path.basename(dis_file)])
print(task_list)
print(len(task_list))

base_commit_times = len(task_list)//len(work_list)
if base_commit_times == 0:
    base_commit_times = 1
    commit_time_sum = len(task_list)
else:
    commit_time_sum = len(work_list)
commit_list = [base_commit_times for i in range(commit_time_sum)]
more_commit = len(task_list)-len(work_list) * base_commit_times
if more_commit > 0:
    for i in range(more_commit):
        commit_list[i] += 1

random.shuffle(commit_list)

print(commit_list)
print(sum(commit_list))

task_queue = queue.Queue()
for task in task_list:
    task_queue.put(task)

time_queue = queue.Queue()
for time in work_list:
    time_queue.put(time)

for commit_time in commit_list:
    time = time_queue.get()
    os.system('time {}'.format(time[1]))
    os.system('date {}'.format(time[0]))
    for i in range(commit_time):
        task = task_queue.get()
        os.system(
            f'cd {dis_root} && git add {task[0]}')
        os.system(
            f'cd {dis_root} && git commit -m "add {task[1]}" ')

