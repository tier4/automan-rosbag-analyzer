from ubuntu:16.04

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
RUN apt-get update && \
    apt-get install -y wget ros-kinetic-ros-base --allow-unauthenticated
RUN echo ". /opt/ros/kinetic/setup.bash" >> ~/.bashrc

RUN cd /tmp && wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip install pipenv
RUN echo "export PATH=${HOME}/.local/bin:$PATH" >> ~/.bashrc

COPY Pipfile* /app/
WORKDIR /app
RUN export PATH=${HOME}/.local/bin:/usr/local/python370/bin:${PATH} && pipenv install --skip-lock

COPY . /app
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/app/bin/docker-entrypoint.bash"]
CMD ["pipenv run python libs/rosbag_analyzer.py --help"]
