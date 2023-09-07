import h5py
import numpy as np

def aggregate_spliceai_dataset(li):
    new = h5py.File('new_file_name.h5','w')
    pp=0
    for file_name in li:
        f1=h5py.File(file_name,'r')
        for i in range(len(f1.keys())//2):
            xx=f1['X'+str(i)]
            yy=f1['Y'+str(i)]

            new.create_dataset('X' + str(pp), data=xx)
            new.create_dataset('Y' + str(pp), data=yy)
            pp+=1
        f1.close()
    new.close()
