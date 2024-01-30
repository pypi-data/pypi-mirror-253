"""
功能：
    对归档数据进行检测
    1. 检测 tar 压缩包是否完整
    2. 检查文件目录是否符合归档规范
    3. 提取 tags.json 和 README.md 文件内容
    
参数说明：
    @param: archive_dir     训练数据归档 tar 压缩包文件夹路径
    
Author:
    Lily-20240130
"""
import os
import tarfile
import hashlib
from tqdm import tqdm

# TODO 创建 log 文件进行归档数据检测记录
def create_log(archive_tar):
    tar_name = os.path.basename(archive_tar)
    check_log = f'check_log/{tar_name}_check_log.log'
    if not os.path.exists(os.path.dirname(check_log)):
        os.makedirs(os.path.dirname(check_log))
        
    with open(check_log, 'w') as f:
        f.write(f"Check log of {tar_name}\n\n1.Check details")
    return check_log


# TODO 检查 log 记录
def write_check_log(check_log, log_content):
    with open(check_log, 'a', encoding='utf-8') as f:
        f.write(f"{log_content}")
    return check_log


# TODO 计算归档 tar 文件的校验和
def calculate_md5(file_path, block_size=8192):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(block_size*50000), b''):
            md5.update(chunk)
    return md5.hexdigest()


# TODO 匹配归档的 tar 和 md5 文件的校验和
def verify_tar_integrity(tar_file_path, md5_file_path, check_log):
    # * 读取 MD5 文件中的校验和 
    with open(md5_file_path, 'r') as md5_file:
        expected_md5 = md5_file.read().strip().split(' ')[0]
    # * 计算实际 tar 文件的 MD5
    actual_md5 = calculate_md5(tar_file_path)
    # * 比较校验和
    if actual_md5 == expected_md5:
        pass_content = f"\nPass: MD5 verification passed. The tar file is intact.\n"
        pass_log = write_check_log(check_log, pass_content)
        return True
    else:
        error_content = f"\nError: MD5 verification failed. The tar file may be corrupted.\n"
        error_log = write_check_log(check_log, error_content)
        return False
        

# TODO 获取tar压缩包内的第一级文件和所有文件名称
def get_tar_dirs_files(archive_tar):
    archive_dirs, archive_img = [], []
    with tarfile.open(archive_tar, 'r') as archive:
        archive_names = archive.getnames()      # * 归档的所有文件
        dataset_name = archive.getnames()[0]    # * 归档数据名称
        for archive_file in archive_names:                          
            if archive_file == archive.getnames()[0]:
                continue
            archive_dir_name = archive_file.split("/")[1]
            archive_dirs.append(archive_dir_name)
            
            if len(archive_file.split("/")) == 3:
                archive_img.append(archive_file.split("/")[1] + os.path.sep + archive_file.split("/")[2])
            
        archive_imgs = list(set(archive_img))
        archive_dirs = list(set(archive_dirs))
    return dataset_name, archive_dirs, archive_imgs


# TODO 归档数据和模板文件匹配检查
def compare_template_and_archive(archive_tar, check_log):
    # * Step 1: 数据归档名称添加
    data_instruction_name = f'{archive_tar.split(os.path.sep)[-1].split("_")[0]}_Data_Instruction.pdf'

    # * Step 2: 模板一级目录所有文件
    template_files = ['train', 'val', 'test', 'README.md', 'tags.json', data_instruction_name]     # 罗列出所有归档的模板文件
        
    # * Step 3: 归档文件与模板文件比较是否齐全
    dataset_name, archive_dirs, archive_img_lab = get_tar_dirs_files(archive_tar)   # 获取归档文件
    img_lab_files = write_check_log(check_log, f'The datasets includes {archive_img_lab}\n')
    for file in template_files:                                 
        if file not in archive_dirs:
            if file == 'test':
                continue
            missing_content=f'Error: {file} is missing in the archive.\n'
            missing_log = write_check_log(check_log, missing_content)
        
    # * Step 4:归档文件与模板文件比较，列出比模板多余的文件        
    for all_file in archive_dirs:                                
        if all_file not in template_files:
            more_content=f'Error: {all_file} is more in the archive.\n'
            more_log = write_check_log(check_log, more_content)     
            
    # * Step 5:获取 tags.json 和 README.md 文件内容       
    tags_path = dataset_name + '/' + 'tags.json'
    readme_path = dataset_name + '/' + 'README.md'
    with tarfile.open(archive_tar, 'r') as archive:
        if 'tags.json' in archive_dirs:
            # * 获取tags.json的文件对象
            tags_json_file = archive.extractfile(tags_path)
            tags_json_content = [tags_json_file.readline().decode('utf-8') for _ in range(30)]
            tags_no_empty_lines = [line.strip() for line in tags_json_content]
            write_tags = '\n'.join(tags_no_empty_lines)
            tags_content=f'\n2.tags.json的前30行\n{write_tags}\n'
            tags_log = write_check_log(check_log, tags_content)
            
        if 'README.md' in archive_dirs:
            # 获取README.md的文件对象
            readme_file = archive.extractfile(readme_path)
            readme_content = [readme_file.readline().decode('utf-8') for _ in range(40)]
            readme_no_empty_lines = [line.strip() for line in readme_content]
            write_readme = '\n'.join(readme_no_empty_lines)
            reamde_all_content=f'\n3.README.md\n{write_readme}\n'
            readme_log = write_check_log(check_log, reamde_all_content)       
    return

  
# TODO 获取所有文件
def all_file_re_path(path, fileType=["tar"]):
    Dirlist, Filelist = [], []
    for home, dirs, files in os.walk(path):
        # 获得所有文件夹
        for dirname in dirs:
            Dirlist.append(os.path.join(home, dirname))
        # 获得所有文件
        for filename in files:
            if filename.split(".")[-1].lower() in fileType:
                Filelist.append(os.path.join(home, filename))
    return Filelist


# TODO main
def check_archive_dataset(archive_dir):
    tar_files = all_file_re_path(archive_dir)
    for tar_path in tqdm(tar_files, desc="Processing tars", unit="tar"):
        # ! 创建归档数据检查 log
        check_log = create_log(tar_path)
        
        # ! md5 文件存在判断
        md5_path = os.path.join(os.path.dirname(tar_path), os.path.basename(tar_path) + '.md5')
        if not os.path.exists(md5_path):
            md5_miss = f"\nError: No {md5_path}\n"
            pass_log = write_check_log(check_log, md5_miss)   
            print('No',  md5_path)
            # continue
        else:
            # ! 归档 tar 文件完整性查验
            verify_tar_integrity(tar_path, md5_path, check_log)
        
        # ! 归档文件和模板文件匹配检查
        compare_template_and_archive(tar_path, check_log)
        
    print('Check finished!!!')
    return check_log
       
              
if __name__ == '__main__':
    archive_dir = r'E:\project\0_Tools\tarfile\test'
    check_archive_dataset(archive_dir)