FROM osrf/ros:humble-desktop
RUN mkdir -p ~/dev/src/erbi_nlp

COPY . /root/dev/src

COPY requirements.txt ./

WORKDIR /root/dev

# Software Dependencies
#ex : RUN apt-get install festival

RUN colcon build

RUN sed -i "$d" /ros_entrypoint.sh
RUN echo 'source "/root/dev/install/setup.bash"' >> /ros_entrypoint.sh
RUN echo 'exec "$@"' >> /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
