FROM debian:stable-slim

ENV DEBIAN_FRONTEND noninteractive
ENV RUNNING_IN_DOCKER true
ENV PATH="/root/.local/bin:${PATH}"
ENV LC_ALL=C.UTF-8

RUN apt update && apt -y install git xclip ruby ruby-dev wget elfutils patchelf file gdb curl gcc strace ltrace tmux python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential zsh

RUN git clone https://github.com/pwndbg/pwndbg && \
    cd pwndbg && \
    ./setup.sh

WORKDIR /root/.local/bin
RUN python3 -m pip install --upgrade pip --break-system-packages && \
    python3 -m pip install --upgrade pwntools --break-system-packages && \
    python3 -m pip install --upgrade ROPgadget --break-system-packages && \
    gem install one_gadget && \
    gem install seccomp-tools && \
    wget https://github.com/io12/pwninit/releases/download/3.3.1/pwninit && \
    chmod +x pwninit

WORKDIR /root/.config
COPY pwn_template.py .

WORKDIR /root/.zsh
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting

WORKDIR /root/.tmux/yank
RUN git clone https://github.com/tmux-plugins/tmux-yank /root/.tmux/yank

WORKDIR /root
COPY .tmux.conf .
COPY .zshrc .
COPY .gdbinit .

WORKDIR /ctf

RUN usermod --shell /bin/zsh root

CMD [ "/bin/zsh" ]