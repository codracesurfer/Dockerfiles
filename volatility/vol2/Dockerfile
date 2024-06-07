FROM python:2

ENV PATH="/opt/volatility2:${PATH}"

RUN apt update && apt install -y git

WORKDIR /opt
RUN git clone https://github.com/volatilityfoundation/volatility.git

WORKDIR /opt/volatility
RUN python2 setup.py install && \
    pip2 install pycryptodome distorm3 pefile yara-python

WORKDIR /ctf

CMD [ "/bin/bash" ]