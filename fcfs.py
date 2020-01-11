tasks = {}
delay = 40

with open('tasks_file.txt', 'r') as input_file:
    for task in input_file.readlines():
        line = task.replace('[','').replace(']','').split(',')
        interval, task_income = str(line[1]).split('.')
        task_time = line[2]
        # tasks.append((interval, task_income, line[3]))
        if int(interval) in tasks:
            tasks[int(interval)].append((int(task_income[:2]), int(task_time)))
        else:
            tasks[int(interval)] = []
            tasks[int(interval)].append((int(task_income[:2]), int(task_time)))


for key, value in sorted(tasks.items()):

    sorted_income_tasks = sorted(value, key=lambda x: x[0])
    iterator = 0
    tasks_in_interval = len(sorted_income_tasks)
    last_task_not_end = True
    income_times = [x[0] for x in sorted_income_tasks]
    system_is_used = False
    count_task = 0
    idle_time = 0
    overload_flag = 1
    cpu_time = 0
    income_tasks = []
    next_task = None
    current_task_time_start = None
    end_current_task = None
    current_task = None
    end_tasks = []
    income_tasks_in_time = True
    while last_task_not_end:
        if len(income_tasks) >= 7:
            overload_flag = 0.5
        else:
            overload_flag = 1
            if cpu_time % 1 != 0:
                cpu_time += 0.5
        if iterator in income_times:
            income_tasks_in_time = True
            while income_tasks_in_time:
                if system_is_used:
                    income_tasks.append(sorted_income_tasks.pop(0))
                    income_times.pop(0)
                else:
                    current_task = sorted_income_tasks.pop(0)
                    current_task_time_start = iterator
                    count_task += 1
                    system_is_used = True
                    end_current_task = iterator + current_task[1]
                    income_times.pop(0)
                if iterator not in income_times:
                    income_tasks_in_time = False
        if system_is_used and cpu_time == end_current_task:
            system_is_used = False
            end_tasks.append([current_task, current_task_time_start, iterator])
            if not income_tasks and not sorted_income_tasks:
                last_task_not_end = False
        if not system_is_used and income_tasks:
            current_task = income_tasks.pop(0)
            current_task_time_start = iterator
            count_task += 1
            system_is_used = True
            end_current_task = cpu_time + current_task[1]
            if end_current_task % 1 != 0:
                end_current_task += 0.5
        if not system_is_used:
            idle_time += 1
        iterator += 1
        cpu_time += overload_flag
    print(key, end_tasks)
    with open('end_file.txt', 'a') as output_file:
        output_file.write('Period: {}, idle time: {}, tasks: {}\n'.format(key, idle_time, len(end_tasks)))
        for iter, task in enumerate(end_tasks):
            is_delay = False
            if task[0][0] + delay <= task[2]:
                is_delay = True

            output_file.write('Task ID: {}, task income: {}, task start: {}, task end: {}, delay: {}\n'.format(
                str(iter), str(task[0][0]), str(task[1]), str(task[2]), str(is_delay)
            ))
