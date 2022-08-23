FROM erbi_base


RUN mkdir -p ~/dev/src/erbi_cv

COPY . /root/dev/src

WORKDIR /root/dev

RUN colcon build
RUN echo ". install/setup.bash" >> /opt/ros/humble/setup.bash

