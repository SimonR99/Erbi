FROM osrf/ros:humble-desktop


RUN mkdir -p ~/dev/src/erbi_nlp

COPY . /root/dev/src

WORKDIR /root/dev

RUN colcon build
RUN echo ". install/setup.bash" >> /opt/ros/humble/setup.bash

