#! /usr/bin/python
# coding:utf-8

from capstone import *
import pwnlib

def jmp_filter(op_str):
    if 'rip' in op_str:
        return False
    if '[' in op_str:
        return False
    if '0x' in op_str:
        return False
    return True

MAX_LEN = 8

def find_in_stream(data):
    gadget_set = set()


    for offset in xrange(len(data)):
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        sub_data=data[offset:offset+MAX_LEN]

        i = None
        try:
            i = md.disasm(sub_data, offset).next()
        except StopIteration:
            continue


        if i.mnemonic == 'jmp':
            if jmp_filter(i.op_str):
                print("0x%x:\t%s\t%s\t" %(i.address, i.mnemonic, i.op_str))
                gadget_set.add(i.op_str)

    return float(len(gadget_set))/len(data)


PATH = r'/home/readm/benchmark/practical/noninteractive/'

file_list = []

with open(r'./elflist.txt') as f:
    global file_list
    file_list = f.readlines()

for file in file_list:
    e = pwnlib.elf.load(PATH+file.strip())
    for seg in e.executable_segments:
        if len(seg.data())==504: continue
        rate = find_in_stream(seg.data())
        print "%s\nGagedts per 0x8000:%f\tSeg_size:%d"%(file.strip(),rate*0x4000,len(seg.data()) )


#e = pwnlib.elf.load('./hello')
#for i in e.executable_segments[:]:
#    print dir(i)
#    print i.header
#    print len(i.data())
#    for j in i.data()[:50]:
#        print hex(ord(j)),


#CODE = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"

#md = Cs(CS_ARCH_X86, CS_MODE_64)
#for i in md.disasm(CODE, 0x1000):
#    print("0x%x:\t%s\t%s\t" %(i.address, i.mnemonic, i.op_str))
#    print i.bytes