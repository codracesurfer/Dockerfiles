FROM ubuntu@sha256:c279a739b31ead4ebc3e9ce04937eb8b612799b52c26133eb3b4a056d08c31a6

ENV DEBIAN_FRONTEND="noninteractive"
ENV PATH="/home/user/.local/bin:${PATH}"


RUN apt update && apt -y install git xclip ruby sudo ruby-dev wget elfutils patchelf file gdb curl gcc strace ltrace tmux python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential && \
    useradd -m -s /bin/bash user && \
    echo 'user:user' | chpasswd && \
    usermod -aG sudo user && \
    chown -R user:user /home/user && \
    chmod +rw /home/user && \
    git clone https://github.com/pwndbg/pwndbg && \
    cd pwndbg && \
    ./setup.sh && \
    cp /root/.gdbinit /home/user/.gdbinit && \
    chown user:user /home/user/.gdbinit && \
    chmod -R 666 /var/lib/gems

USER user
WORKDIR /home/user/.local/bin
RUN python3 -m pip install --upgrade pip --break-system-packages && \
    python3 -m pip install --upgrade pwntools --break-system-packages && \
    python3 -m pip install --upgrade ROPgadget --break-system-packages && \
    gem install one_gadget && \
    gem install seccomp-tools && \
    wget https://github.com/io12/pwninit/releases/download/3.3.1/pwninit && \
    chmod +x pwninit && \
    echo "alias pwninit='pwninit --template-path ~/.config/pwninit_template.py; libcname=\$(ls libc*) && python3 -c \"from pwnlib.libcdb import unstrip_libc; unstrip_libc('\''\$libcname'\'')\"'" >> ~/.bashrc

WORKDIR /home/user/.config
COPY pwn_template.py .

WORKDIR /home/user
COPY .tmux.conf .

WORKDIR /home/user

CMD [ "/bin/bash" ]