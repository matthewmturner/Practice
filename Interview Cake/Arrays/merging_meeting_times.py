# Question URL: https://www.interviewcake.com/question/python3/merging-ranges?course=fc1&section=array-and-string-manipulation

# For example
# [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# Would return
# [(0, 1), (3, 8), (9, 12)]

# Do not assume the meetings are in order. The meeting times are coming from multiple teams.

# Write a solution that's efficient even when we can't put a nice upper bound on the numbers
# representing our time ranges. Here we've simplified our times down to the number of 30-minute
# slots past 9:00 am. But we want the function to work even for very large numbers,
# like Unix timestamps. In any case, the spirit of the challenge is to merge meetings where
# start_time and end_time don't have an upper bound.

from typing import List

Times = List[tuple]


def merge_ranges(time_ranges: Times) -> Times:

    sorted_times = sorted(time_ranges, key=lambda t: t[0])

    current_start = None
    current_end = None
    condensed_times = []

    for i, time in enumerate(sorted_times):
        if i == 0:
            current_start = time[0]
            current_end = time[1]
        else:
            new_start = time[0]
            new_end = time[1]
            if (new_start < current_end) and (new_end < current_end):
                if i == len(time_ranges) - 1:
                    merged_time = current_start, current_end
                    condensed_times.append(merged_time)
                else:
                    next
            elif (new_start > current_end) or (new_end < current_end):
                merged_time = current_start, current_end
                condensed_times.append(merged_time)
                current_start = new_start
                current_end = new_end
            elif new_start < current_end:
                if new_end > current_end:
                    if i == len(time_ranges) - 1:
                        merged_time = current_start, new_end
                        condensed_times.append(merged_time)
                    else:
                        current_end = new_end
            else:
                merged_time = current_start, new_end
                condensed_times.append(merged_time)
                current_start = new_start
                current_end = new_end

    return condensed_times


times = [(1, 10), (2, 6), (3, 5), (7, 9)]
print(merge_ranges(times))
