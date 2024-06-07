FROM kalilinux/kali-rolling:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt -y install kali-linux-large && \
    useradd -m -s /bin/bash kali && \
    echo 'kali:kali' | chpasswd && \
    usermod -aG sudo kali && \
    chown -R kali:kali /home/kali

USER kali
WORKDIR /home/kali

CMD ["/bin/bash"]
