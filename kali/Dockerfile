FROM kalilinux/kali-rolling:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt -y install kali-linux-everything && \
    useradd -m -s /bin/zsh kali && \
    echo 'kali:kali' | chpasswd && \
    usermod -aG sudo kali && \
    chown -R kali:kali /home/kali

RUN usermod --shell /bin/zsh kali

USER kali
WORKDIR /home/kali/.zsh
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting

WORKDIR /home/kali/.tmux/yank
RUN git clone https://github.com/tmux-plugins/tmux-yank /home/kali/.tmux/yank

WORKDIR /home/kali
COPY .tmux.conf .
COPY .zshrc .

CMD ["/bin/zsh"]
