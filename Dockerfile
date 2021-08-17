ARG ros_distro=melodic

FROM ros:${ros_distro}

ARG ros_distro

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update \
    && apt-get install -y wget gnupg lsb-release \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py \
    && python3 /tmp/get-pip.py \
    && pip install pipenv

COPY Pipfile* /app/
WORKDIR /app
RUN pipenv sync

COPY . /app

ENV DISTRO=$ros_distro
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/app/bin/docker-entrypoint.bash"]
CMD ["pipenv run python bin/rosbag_analyzer.py --help"]
