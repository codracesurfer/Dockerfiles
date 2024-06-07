#!/usr/bin/env python3

from pwn import *

{bindings}

elf = context.binary = {bin_name}
context.terminal = ["tmux", "splitw", "-v", "-p", "80"]

host = args.HOST or 'hostname'
port = int(args.PORT or 1337)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.REMOTE:
        return start_remote(argv, *a, **kw)
    else:
        return start_local(argv, *a, **kw)

gdbscript = '''
handle SIGALRM ignore
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================


io = start()



io.interactive()