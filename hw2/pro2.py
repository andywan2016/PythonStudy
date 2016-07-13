from pro1b import genlimit



def decimal2(num):
	pivot=True
	i=2
	while pivot:
		ls=genlimit(decimals(num),i)
        lth=len(ls)
#for a finite stirng,just return
        if lth<i:
            return ls

		ls_1=ls[0:ls-1]
        in_pv=ls[-1]

        if in_pv not in ls_1:
            i+=1
            continue
        else:
            new_len=(lth-ls.index(in_pv)-2)+i
            expand_ls=genlimit()(decimals(num),new_len)
            left_ls=expand_ls[ls.index(in_pv):i]
            right_ls=expand_ls[i:len(expand_ls)]

            if (left_ls==right_ls).all():
                return expand_ls

            else:
                i+=1
                continue










		




