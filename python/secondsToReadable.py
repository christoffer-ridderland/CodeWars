# https://www.codewars.com/kata/52685f7382004e774f0001f7
def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - 60 * (m + 60 * h)
    time = ""
    for t in [h, m, s]:
        if t < 10:
            time += "0"
        time += "{t}:".format(t = t)
    return time[:-1]