import sys
import time

data = "is sentence with some words this is a some. words this is a sentence with some words".split()


def inputwordsperminute(x):

    
    max_len=max([len(w) for w in data])
    pad = " "*max_len
    for w in data:
        sys.stdout.write('%s\r' % pad)
        sys.stdout.write("%s\r" % w)
        sys.stdout.flush()
        time.sleep((60.0/x))

print

inputwordsperminute(500)
