#!/bin/bash -e

source "/opt/ros/${DISTRO}/local_setup.bash"
cd /app
exec $@
