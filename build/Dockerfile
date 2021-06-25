FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV GIT_SSL_NO_VERIFY=1
ARG SSH_USERNAME=student
ARG SSH_PASSWORD=student
ARG ZIP_PASS=test
ARG YARA=4.1.0

RUN apt-get update && apt-get install --no-install-recommends -y \
  openssh-server \
  vim \
  nano \
  automake \
  bison \
  flex \
  gcc \
  git \
  jq \
  libmagic-dev \
  libprotobuf-dev \
  libssl-dev \
  libtool \
  make \
  openssh-server \
  pkg-config \
  unzip

# install yara
RUN cd /tmp \
  && git clone --recursive --branch v$YARA https://github.com/VirusTotal/yara.git \
  && cd /tmp/yara \
  && ./bootstrap.sh \
  && sync \
  && ./configure \
    --with-crypto \
    --enable-magic \
    --enable-dotnet \
  && make \
  && make install \
  && ldconfig

WORKDIR /opt
COPY . /opt/

COPY malware.zip /opt
RUN unzip -P $ZIP_PASS malware.zip && rm -rf malware.zip

#setup user
RUN useradd -rm -s /bin/bash -u 1000 $SSH_USERNAME
RUN echo "$SSH_USERNAME:$SSH_PASSWORD" | chpasswd
RUN echo "uuid=\$(cat /proc/sys/kernel/random/uuid |cut -d '-' -f 1) \
&& mkdir \$uuid && cd \$uuid \
&& mkdir strelka \
&& mkdir output \
&& mkdir exercise-4 \
&& mkdir exercise-5 \
&& ln -s /opt/malware malware \
&& cp -R /opt/exercise-4/* exercise-4/ \
&& cp -R /opt/exercise-5/* exercise-5/ \
&& cp /opt/fileshot-config.yml fileshot-config.yml \
&& HOME=~/\$uuid" >> /home/$SSH_USERNAME/.bashrc
RUN chmod 701 /home && \
  sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
  mkdir /var/run/sshd

#setup ssh
# RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
EXPOSE 22

#cleanup
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
    /tmp/* /var/tmp/*

CMD ["/usr/sbin/sshd","-D"]

