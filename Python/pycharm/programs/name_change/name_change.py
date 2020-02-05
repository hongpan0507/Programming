import os

dir_path = "D:\\Dropbox (Univ. of Oklahoma)\\ARRC_hpan\\Engineering\\Design\\Library\\3D Model\\Antennas\\Patch\\CP_NSP_PF_SG_CT_5.8GHz\\"
old_common_name = "CP_NSP_PF_SG_5.8GHz"
new_common_name = "CP_NSP_PF_SG_CT_5.8GHz"

for file_name in os.listdir(dir_path):
    if file_name.find(old_common_name) != -1:   # replace name if found
        src = dir_path + file_name
        dst = dir_path + file_name.replace(old_common_name, new_common_name)
        # print(file_name)
        os.rename(src, dst)
        # print("Old Names: ")
        # print(src)
        print("New Names: ")
        print(dst)

