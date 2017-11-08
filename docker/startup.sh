#!/bin/bash

set -ex

sudo /etc/init.d/ssh start
echo "circleci:circleci" | sudo chpasswd
/bin/bash
