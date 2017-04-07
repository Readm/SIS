#! /usr/bin/python
# coding:utf-8

import Dynamic

if __name__ == '__main__':
    import sys,os
    cmd = sys.argv[1]
    cmd = 'qemu-x86_64 /bin/'+cmd+' 2>error.txt'
    print cmd
    os.system(cmd)
    print 'Error Log:'
    os.system('cat error.txt')
    print "Count result:"
    Dynamic.count('./error.txt')
