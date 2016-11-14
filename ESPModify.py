#! /usr/bin/python
# coding:utf-8

file_name = 'CallBranch.outwritespins.out'
path = './data/'
subpath = 'test/'

class record():
    def __init__(self, s):
        self.ins = s.strip()

    @property
    def ins_type(self):
        return self.ins.split()[0]

    def is_type(self, s):
        return s in self.ins_type

class SP_records():
    def __init__(self, path):
        self.path =  path
        self.data = []      # list of records
        with open(self.path, 'r') as f:
            raw_data = f.readlines()
            for i in raw_data:
                self.data.append(record(i))


a = SP_records(path+subpath+file_name)

import collections
c = collections.Counter()
c.update([i.ins_type for i in a.data])
print c

for i in a.data:
    if i.ins_type=='mov':
        print i.ins