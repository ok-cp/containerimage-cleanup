from subprocess import Popen,PIPE
from datetime import datetime
import os
import sys
import time

dateformat = '[%Y-%m-%d %H:%M:%S]'
def main():
        print('{0} Cleanup Container Images....'.format(datetime.now().strftime(dateformat)))
        until_hours = os.environ['UNTIL_HOURS']
        docker_label_key = os.environ['DOCKER_LABEL_KEY']
        docker_label_value = os.environ['DOCKER_LABEL_VALUE']
        pruneImage(docker_label_key, docker_label_value, until_hours)


def pruneImage(key, value, hours) :
        print('{0} Docker Image Until Hours={1}, Label={2}, Valye={3}'.format(datetime.now().strftime(dateformat), hours, key, value))
        outputs = Popen(["docker", "image", "prune", "-a", "--filter",  str("label=%s=%s" % (key, value)), "--filter", str("until=%dh" % int(hours))], stdin=PIPE,stdout=PIPE).communicate(input="y".encode())
        print('{0} {1}'.format(datetime.now().strftime(dateformat), outputs))

if __name__ == "__main__":
    main()