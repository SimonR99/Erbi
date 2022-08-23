FROM osrf/ros:humble-desktop

RUN mkdir -p ~/dev/src

WORKDIR /root/dev

RUN sed -i "$ d" /ros_entrypoint.sh
RUN echo 'source "/root/dev/install/setup.bash"' >> /ros_entrypoint.sh
RUN echo 'exec "$@"' >> /ros_entrypoint.sh

RUN mkdir -p ~/dev/src/erbi_base

RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get install python3-pip -y
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir tornado && \
    pip3 install --no-cache-dir simplejpeg && \
    pip3 install tensorflow &&\
    pip3 install tensorflow-addons &&\
    pip3 install tensorflow-datasets



COPY . /root/dev/src/erbi_base

WORKDIR /root/dev

RUN . /opt/ros/humble/setup.sh && colcon build --symlink-install --packages-select erbi_base

RUN echo ". install/setup.bash" >> /opt/ros/humble/setup.bash
