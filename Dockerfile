FROM d3fk/python_in_bottle:latest
MAINTAINER f4prime
WORKDIR /home
ADD pvinit.py /home
# the following is a test
RUN mkdir /test
RUN python pvinit.py -r /test -c test-chain -n node0 node1 --clean
