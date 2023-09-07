import h5py
import numpy as np

new = h5py.File('gtex_with_pnas_train_dataset_agg.h5','w')
li = ['gtex_with_pnas_train_dataset1.h5','gtex_with_pnas_train_dataset2.h5']



pp=0
for file_name in li:
    f1=h5py.File(file_name,'r')
    print('key len for %s : %d' %(file_name,len(f1.keys())//2))
    for i in range(len(f1.keys())//2):
        xx=f1['X'+str(i)]
        yy=f1['Y'+str(i)]

        new.create_dataset('X' + str(pp), data=xx)
        new.create_dataset('Y' + str(pp), data=yy)
        pp+=1
    f1.close()
new.close()
pp
