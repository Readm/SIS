#!/bin/sh
cd ~/qemu_eclipse/
pwd
./configure --target-list=x86_64-softmmu,x86_64-linux-user,i386-linux-user --disable-xen --disable-vnc --disable-vnc-png --disable-vnc-jpeg --disable-vnc-sasl --disable-blobs --disable-bluez --disable-bsd-user
