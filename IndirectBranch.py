#! /usr/bin/python
# coding:utf-8

__all__ = ['IB_records']

file_name = 'CallBranch.outwritebranchandcall.out'
path = './data/'
subpath = 'test/'

class record():
    def __init__(self, lst):    # len(lst) == 3 str
        try:
            ip, target, ins = lst[0].split('  ',2)
        except:
            print lst[0]
        ip = int(ip.split(':')[-1], 16)
        target = int(target.split(':')[-1], 16)

        self.ins = ins.split(':',1)[-1].strip()
        self.distance = abs(target-ip)
        self.source = lst[1].split()[-1].strip()
        self.target = lst[2].split()[-1].strip()

    @property
    def not_ret(self):
        return not self.ins.split()[1]=='ret'

    @property
    def inter_lib(self):
        return not self.distance == self.target

    def __str__(self):
        return 'distance:%X' % self.distance+ '\tins:'+ self.ins + \
               '\tsource:'+ self.source + '\ttarget:' + self.target

class IB_records():
    def __init__(self, path):
        self.path =  path
        self.data = []      # list of records
        with open(self.path, 'r') as f:
            raw_data = f.readlines()
            for i in range(len(raw_data)/3):
                self.data.append(record(raw_data[i*3:i*3+3]))




