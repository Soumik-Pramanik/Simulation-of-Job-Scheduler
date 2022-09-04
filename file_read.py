###############################################
## reading the JobArrival.txt file.
with open('JobArrival.txt','r') as f:
    for line in f:
        line = line.split()
        try:
            jobid, day, hr, mem, cpu, exe = int(line[1]), int(line[4]), int(line[7]), int(line[9]), int(
                line[11]), int(line[13])
            jobs_dictionary[jobid] = (day, hr, mem, cpu, exe)
        except IndexError:
            continue

    for job, values in jobs_dictionary.items():
        jobid, day, hr, mem, cpu, exe = job, values[0], values[1], values[2], values[3], values[4]
        if hr != current_hour:
            hr_diff = hr - current_hour
            if day != current_day:
                hr_diff += 24

            for _ in range(hr_diff):
                every_hour_update()
            current_hour = hr

        if day != current_day:
            daily_update()
            current_day = day

        ## Assignning the jobs to Wroker Nodes. 
        for n in range(9):
            if n < 3:
                heapq.heappush(queue[n], (jobid,))
            elif n < 6:
                gross_value = exe * mem * cpu
                heapq.heappush(queue[n], (gross_value, jobid))
            else:
                heapq.heappush(queue[n], (exe, jobid))

daily_update()
every_hour_update()
