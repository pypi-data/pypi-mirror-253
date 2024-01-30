import time
from multiprocessing.pool import ThreadPool

import pandas as pd
import progressbar


def fetch_rows(cur):
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(cur.fetchall, ())

    # initialise progressbar
    bar = progressbar.ProgressBar(
        maxval=100,
        widgets=[progressbar.Bar("=", "[", "]"), " ", progressbar.Percentage()],
    )
    bar_start = False

    while not async_result.ready():
        if cur.stats["scheduled"]:
            if not bar_start:
                bar.start()
                bar_start = True
            perc = round(
                (cur.stats["completedSplits"] * 100.0) / (cur.stats["totalSplits"]), 2
            )
            bar.update(int(perc))
            time.sleep(1)
        else:
            perc = "0"
            print(cur.stats["state"] + "-" + perc + "%")
            time.sleep(4)
    if bar_start:
        bar.finish()
    print(cur.stats["state"] + "-" + str(cur.stats.get("progressPercentage", "")))

    rows = async_result.get()

    columns = [desc[0] for desc in cur.description]

    return pd.DataFrame(rows, columns=columns)
