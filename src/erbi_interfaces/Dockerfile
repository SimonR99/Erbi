FROM osrf/ros:humble-desktop

RUN mkdir -p ~/dev/src

WORKDIR /root/dev

RUN sed -i "$ d" /ros_entrypoint.sh
RUN echo 'source "/root/dev/install/setup.bash"' >> /ros_entrypoint.sh
RUN echo 'exec "$@"' >> /ros_entrypoint.sh

RUN mkdir -p ~/dev/src/erbi_interfaces

RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get install python3-pip -y
RUN pip3 install tensorflow
RUN pip3 install tensorflow-addons
RUN pip3 install tensorflow-datasets

COPY . /root/dev/src/erbi_interfaces

WORKDIR /root/dev

RUN . /opt/ros/humble/setup.sh && colcon build --symlink-install --packages-select erbi_interfaces

RUN echo ". install/setup.bash" >> /opt/ros/humble/setup.bash
