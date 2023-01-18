import datetime
import pandas as pd
import pickle as pk

log_file = 'log.pk'


def log_queries(origin_point, destination_point):
    time = datetime.datetime.now()
    s = pd.Series(data=[time, origin_point, destination_point],
                  index=['time', 'origin_point', 'destination_point'])

    log_file = 'log.pk'

    with open(log_file, "ab+") as f:
        pk.dump(s, f)


def get_logged_data():
    data = []
    with open(log_file, 'rb') as fr:
        try:
            while True:
                data.append(pk.load(fr))
        except EOFError:
            pass

    return pd.concat(data, axis=1).T
