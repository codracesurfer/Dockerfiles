FROM python:3

ENV PATH="/opt/volatility3:${PATH}"

RUN apt update && apt install -y git wget

WORKDIR /opt
RUN git clone https://github.com/volatilityfoundation/volatility3.git

WORKDIR /opt/volatility3
RUN python3 -m pip install -r requirements.txt --break-system-packages

WORKDIR /opt/volatility3/volatility3/symbols
RUN wget https://downloads.volatilityfoundation.org/volatility3/symbols/windows.zip && \
    wget https://downloads.volatilityfoundation.org/volatility3/symbols/mac.zip && \
    wget https://downloads.volatilityfoundation.org/volatility3/symbols/linux.zip

WORKDIR /ctf

CMD [ "/bin/bash" ]