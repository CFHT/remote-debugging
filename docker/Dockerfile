FROM circleci/python:2.7.13

RUN sudo apt-get install openssh-server
USER circleci
ADD pydevd.tgz /
ADD --chown=circleci:circleci demo1/src /app/demo1/
ADD --chown=circleci:circleci demo1/production/__init__.py /app/demo1/
ADD --chown=circleci:circleci demo1/production/__main__.py /app/demo1/
ADD --chown=circleci:circleci demo1/production/demo1.sh /bin/demo1.sh

ADD startup.sh /bin/startup.sh

ENTRYPOINT /bin/startup.sh
