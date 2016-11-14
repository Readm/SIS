#! /usr/bin/python
# coding:utf-8

file_name = 'CallBranch.outwritecallret.out'
path = './data/'
subpath = 'test/'

class record():
    def __init__(self, s):
        if s.strip().endswith("True"):
            self.match = True
        else:
            self.match = False
            self.record = s


class CR_records():
    def __init__(self, path):
        self.path =  path
        self.data = []      # list of records
        with open(self.path, 'r') as f:
            raw_data = f.readlines()
            for i in raw_data:
                self.data.append(record(i))

a = CR_records(path+subpath+file_name)
for i in a.data:
    print i.match