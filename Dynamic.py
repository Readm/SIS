#! /usr/bin/python
# coding:utf-8

window = 128
dis = 0x4000

win_lst = []
win_lst_inr = []
win_lst_inm = []

def count(f):
    with open(f,'r') as _input:
        line_num = 0
        INR_num, INM_num, I_SP_num = 0,0,0
        INR_src = set([])
        INR_dst = set([])
        INM_src = set([])
        INM_dst = set([])
        I_SP_set = set([])

        lst_dis = 0
        lst_inr_dis = 0
        lst_inm_dis = 0
        total_num = 0

        max_win_count = 0
        max_inr_win_count = 0
        max_inm_win_count = 0

        hide_dist = 0

        def num_in_win(last_lenth, array):
            if last_lenth>window: del array[:]
            elif last_lenth<0: del array[:]

            else:
                array.append(last_lenth)
                while sum(array)>window:
                    del array[0]

            return len(array)+1

        for line in _input:
            line_num+=1
            if line.startswith('INR'):
                lst_dis = int(line.split()[-1])
                jmp_dis = int(line.split()[6],16)
                if jmp_dis<dis:
                    hide_dist+=lst_dis
                    continue
                else:
                    lst_dis+=hide_dist
                    hide_dist = 0

                INR_num += 1
                INR_src.add(line.split()[4])
                INR_dst.add(line.split()[2])

                total_num += lst_dis

                win_count =  num_in_win(lst_dis,win_lst)
                max_win_count = max(max_win_count, win_count)

                lst_inr_dis += lst_dis
                inr_win_count = num_in_win(lst_inr_dis, win_lst_inr)
                max_inr_win_count= max(max_inr_win_count, inr_win_count)

                lst_inr_dis = 0
                lst_inm_dis += lst_dis

                #if win_count>5:
                 #   print win_count, '|', win_lst
                  #  print line_num,line

            elif line.startswith('INM'):
                lst_dis = int(line.split()[-1])
                jmp_dis = int(line.split()[6],16)
                if jmp_dis<dis:
                    hide_dist+=lst_dis
                    continue
                else:
                    lst_dis+=hide_dist
                    hide_dist = 0

                INM_num += 1
                INM_src.add(line.split()[4])
                INM_dst.add(line.split()[2])

                total_num += lst_dis

                if lst_dis<dis:
                    hide_dist+=lst_dis
                    continue
                else:
                    lst_dis+=hide_dist
                    hide_dist = 0

                win_count =  num_in_win(lst_dis,win_lst)
                max_win_count = max(max_win_count, win_count)

                lst_inm_dis += lst_dis
                inm_win_count = num_in_win(lst_inm_dis, win_lst_inm)
                max_inm_win_count= max(max_inm_win_count, inm_win_count)


                lst_inm_dis = 0
                lst_inr_dis += lst_dis

            elif line.startswith('I_SP'):
                I_SP_num += 1
                I_SP_set.add(line.split()[1])

    print 'INR: %d INM: %d I_SP: %d' %(INR_num,INM_num,I_SP_num),
    print 'INR_S/D %d/%d, INM_S/D %d/%d, I_SP_set %d' % (len(INR_src), len(INR_dst), len(INM_src), len(INM_dst), len(I_SP_set)),
    print 'max count %d, max inr count %d, max inm count %d' % (max_win_count, max_inr_win_count, max_inm_win_count),
    print "Total ins: %d." % (total_num)
    return (INR_num, INM_num, I_SP_num, len(INR_src), len(INR_dst), len(INM_src), len(INM_dst), len(I_SP_set),max_win_count, max_inr_win_count, max_inm_win_count,window,total_num)


if __name__ == '__main__':
    import sys
    f = sys.argv[1]
    count(f)

