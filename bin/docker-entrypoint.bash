#!/bin/bash
set -e

export ROS_ROOT=/opt/ros/kinetic/share/ros
export ROS_PACKAGE_PATH=/opt/ros/kinetic/share
export LD_LIBRARY_PATH=/opt/ros/kinetic/lib
export ROS_DISTRO=kinetic
export PYTHONPATH=/opt/ros/kinetic/lib/python2.7/dist-packages
export PKG_CONFIG_PATH=/opt/ros/kinetic/lib/pkgconfig
export CMAKE_PREFIX_PATH=/opt/ros/kinetic
export ROS_ETC_DIR=/opt/ros/kinetic/etc/ros
cd /app
exec $@
