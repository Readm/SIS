#! /usr/bin/python
# coding:utf-8

import Dynamic

if __name__ == '__main__':
    import sys,os
    cmd = sys.argv[1]
    log_name = './log/'+cmd.replace(' ','_')+'.txt'
    cmd = 'qemu-x86_64 /bin/'+cmd+' 2>'+log_name
    print cmd
    os.system(cmd)
    print 'Error Log:'
    os.system('cat '+log_name)
    print "Count result:"
    ans = Dynamic.count(log_name)
    count_txt = sys.argv[1].replace(' ','_')+' '+' '.join(['%d'%i for i in ans])
    os.system('echo "' +count_txt+'">>ans.txt')
