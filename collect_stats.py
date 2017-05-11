import string
import sys

#------------------------------------------------------------
def get_stats(text):
    stats = {c:0 for c in string.ascii_lowercase}

    for c in text:
        if c in stats:
            stats[c] += 1
    return stats

#------------------------------------------------------------
if __name__ == "__main__":
    fd_in = open(sys.argv[1])

    stats = get_stats(fd_in.read().lower())

    for k in sorted(stats, reverse=True, key=stats.get):
        print("{0} -> {1}".format(k, stats[k]))
