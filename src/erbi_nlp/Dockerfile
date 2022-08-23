FROM erbi_base

RUN mkdir -p ~/dev/src/erbi_nlp

COPY . /root/dev/src

COPY ./utility/chatbot /root/dev/install/erbi_nlp/lib/python3.10/site-packages/erbi_nlp/chatbot

WORKDIR /root/dev

RUN colcon build
RUN echo ". install/setup.bash" >> /opt/ros/humble/setup.bash



