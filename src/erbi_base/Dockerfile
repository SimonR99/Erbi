FROM osrf/ros:humble-desktop

RUN mkdir -p ~/dev/src/erbi_base

COPY . /root/dev/src

WORKDIR /root/dev

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir tornado && \
    pip3 install --no-cache-dir simplejpeg  

RUN colcon build
RUN echo ". install/setup.bash" >> /opt/ros/humble/setup.bash

