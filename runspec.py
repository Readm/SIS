#! /usr/bin/python
# coding:utf-8


import Dynamic, os, subprocess, time

case_path = []
run_path = []

int_list = ['400.perlbench',
            '401.bzip2',
            '403.gcc',
            '429.mcf',
            '445.gobmk',
            '456.hmmer',
            '458.sjeng',
            '462.libquantum',
            '464.h264ref',
            '471.omnetpp',
            '473.astar',
            '483.xalancbmk']
for i in int_list:
    case_path.append('/home/readm/SPEC/benchspec/CPU2006/'+i+'/run/')

build_path = [i+'build_base_sis.0000'  for i in case_path]

# build
#for path in build_path:
#    os.chdir(path)
#    #os.system('. ~/SPEC/shrc; specmake')
#    os.system('')
#    print path
#
run_path = [i+'run_base_ref_sis.0000' for i in case_path]

for path in run_path:
    try:
        os.chdir(path)
        p = subprocess.Popen('. ~/SPEC/shrc; specinvoke -n', stdout=subprocess.PIPE, shell=True)
        res = p.stdout.read()
        for line in res.split('\n'):
            if line.startswith('#'): continue
            elif line.startswith('..'):
                if 1:   #run
                    cmd = 'qemu-x86_64 '+line
                    cmd= cmd.replace('>>','>')
                    print cmd
                    time_start=time.time()
                    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                    p.wait()
                    time_end=time.time()
                    print 'Time:', time_end-time_start
                    with open('/home/readm/SIS/time-log.txt','a') as l:
                        l.write(cmd+'\n')
                        l.write('time: '+str(time_end-time_start)+'\n')


                if 1:   #count
                    cmd = line.split()[-1]
                    with open('/home/readm/SIS/count-log.txt','a') as l:
                        l.write(line+'\n')
                        p = subprocess.Popen('python /home/readm/SIS/Dynamic.py ./'+cmd, stdout=subprocess.PIPE, shell=True)
                        p.wait()
                        res = p.stdout.read()
                        l.write(res)
    except Exception,e:
        print 'Error:',e


    print 'finish: ', path

