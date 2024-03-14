import os
path = os.getcwd()
file_all = path + "\hashtg.txt"
new_hash = path + "\hashall.txt"
finall_hash = path + "\hashal.txt"
dubli = path + "\dubli.txt"
with open(file_all, encoding='utf-8') as f:
    file_all_read = f.read()
    with open(new_hash, encoding='utf-8') as n:
        for i in n:
            if i in file_all_read:
                new = open(dubli, 'a')
                new.write(f'{i}')
                new.close
                
            else:
                new2 = open(finall_hash, 'a')
                new2.write(f'{i}')
                new2.close
os.remove(new_hash)
    