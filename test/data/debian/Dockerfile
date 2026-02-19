FROM debian:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    sudo \
    git \
    python3-venv 

    #todo: check if python3, venv and pip is already available

RUN useradd -m -s /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER developer
WORKDIR /home/developer

ENTRYPOINT ["/usr/bin/bash"]