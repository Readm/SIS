#! /usr/bin/python
# coding:utf-8
import os

from CallRet import *
from ESPModify import *
from IndirectBranch import *
from script_tools import colorize
import collections

exception_info=[]

class File_Report():
    CR_file_name = 'CallBranch.outwritecallret.out'
    SP_file_name = 'CallBranch.outwritespins.out'
    IB_file_name = 'CallBranch.outwritebranchandcall.out'
    def __init__(self, path):
        self.path = path

    #def __str__(self):
    #    s = 'Call Ret Match: %f %% (%d/ %d)' % \
    #        (float(self.CR_match_total[0])/self.CR_match_total[1]*100, self.CR_match_total[0], self.CR_match_total[1])

    def run(self):
        self.run_CR()
        self.run_SP()
        self.run_IB()

    def run_CR(self):
        self.cr = CR_records(self.path + '/' + self.CR_file_name)
        self.CR_match_total = ([i.match for i in self.cr.data].count(True),len(self.cr.data))

    def run_SP(self):
        self.sp = SP_records(self.path + '/' + self.SP_file_name)
        self.SP_counter = collections.Counter([i.ins_type for i in self.sp.data])

    def run_IB(self):
        self.ib = IB_records(self.path + '/' + self.IB_file_name)
        self.exception_count = 0
        for i in self.ib.data:
            if i.ins.startswith('jmp') and 'rip' not in i.ins:
                if i.distance>0xFFFF:
                    self.exception_count +=1
                    exception_info.append(i.__str__())


    def report(self):
        print '==================================================='
        print "File name:", self.path.split('/')[-1]
        if hasattr(self, 'cr'):
            if self.CR_match_total[0] == self.CR_match_total[1]:
                print 'Call Ret Match: %f %% (%d/ %d)' % \
                      (float(self.CR_match_total[0])/self.CR_match_total[1]*100,
                       self.CR_match_total[0], self.CR_match_total[1])
            else:
                print colorize(
                    'Call Ret Match: %f %% (%d/ %d)' % \
                    (float(self.CR_match_total[0])/self.CR_match_total[1]*100,
                    self.CR_match_total[0], self.CR_match_total[1])
                    , 'red'
                )
        if hasattr(self, 'sp'):
            print 'SP modify counter:'
            print self.SP_counter
        if hasattr(self, 'ib'):
            print 'IndirectBranch Exceptions:', self.exception_count


class Report():
    def __init__(self, path):
        self.path = path
        self.SP_counter = collections.Counter()
        self.file_count = 0
        self.CR_not_match_count = 0
        self.CR_not_match_info = ''

    def run(self):
        for i in os.listdir(self.path):
            if not os.path.isfile(self.path+'/'+i):
                fr = File_Report(self.path+'/'+i)
                fr.run()
                fr.report()
                self.SP_counter.update(fr.SP_counter)
                self.file_count += 1
                if fr.CR_match_total[0] != fr.CR_match_total[1]:
                    self.CR_not_match_count += 1
                    self.CR_not_match_info +=\
                        'File name: '+fr.path+\
                        '\nCall Ret Match: %f %% (%d/ %d)' % \
                        (float(fr.CR_match_total[0])/fr.CR_match_total[1]*100,
                        fr.CR_match_total[0], fr.CR_match_total[1])



        print "Total:"
        print "File number: ", self.file_count
        print "SP Modify counter: ", self.SP_counter
        print "Call Ret Match exceptions counts(file number): ", self.CR_not_match_count
        print "Call Ret Not Match info: \n\n", self.CR_not_match_info
        #print "Indirect Branch info: \n"
        #for i in exception_info:
        #    print i

a = Report('./data/OutFile')
a.run()
