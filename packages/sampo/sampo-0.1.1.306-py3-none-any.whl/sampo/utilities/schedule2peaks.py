import numpy as np
from sortedcontainers import SortedList
from sampo.schemas.schedule import Schedule


def schedule2peaks(schedule: Schedule):
    df = schedule.full_schedule_df
    points = df[['start', 'finish']].to_numpy().copy()
    points[:, 1] += 1
    points = SortedList(set(points.flatten()))
    usage = np.zeros(len(points))
    for _, r in df.iterrows():
        start = points.bisect_left(r['start'])
        finish = points.bisect_left(r['finish'] + 1)
        swork = r['scheduled_work_object']
        total_count = sum([worker.count for worker in swork.workers], start=0)
        usage[start: finish] += total_count

    return usage[:-1], points[:-1]
