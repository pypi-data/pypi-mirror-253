__all__ = ["year_progress"]


def year_progress():
    dt = __import__("datetime").datetime
    now = dt.now()
    start = dt(now.year, 1, 1, 0, 0, 0, 0).timestamp()
    end = dt(now.year, 12, 31, 23, 59, 59, 999999).timestamp()
    return (now.timestamp() - start) / (end - start) * 100
