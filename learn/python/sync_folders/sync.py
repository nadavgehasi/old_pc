from os import listdir
import os
from shutil import copy2
import tqdm

def calc_missing_files(source, dest):
    missing_list = []
    source_files = listdir(source)
    dest_files = listdir(dest)
    for f in source_files:
        if f not in dest_files:
            missing_list.append(f)
    return missing_list

def get_all_files_and_folders_in_path(path):
    all_files = []
    all_dirs = []
    for root, directories, files in os.walk(path):
        [all_files.append(os.path.join(root, f)) for f in files]
        [all_dirs.append(os.path.join(root, d)) for d in directories]
    return all_dirs, all_files

def recursive_missing_files_and_folders(source, dest):
    source_folders, source_files = get_all_files_and_folders_in_path(source)
    dest_folders, dest_files = get_all_files_and_folders_in_path(dest)
    missing_folders = []
    missing_files = []
    for folder in source_folders:
        if folder.replace(source, dest) not in dest_folders:
            missing_folders.append(folder)
    for f in source_files:
        if f.replace(source, dest) not in dest_files:
            missing_files.append(f)
    return missing_folders, missing_files

def create_folders(folders, source, dest):
    failed_folders = []
    print("There are {} missing folder".format(len(folders)))
    print("Start Creating missing folders")
    for folder in tqdm.tqdm(folders):
        try:
            os.makedirs(folder.replace(source,dest))
        except Exception as e:
            failed_folders.append(folder)
            print("failed to crea the folder {}".format(folder.replace(source, dest)))
    print("Failed to create {} folders".format(len(failed_folders)))
    return failed_folders

def recursive_sync_folders(source, dest):
    missing_folders, missing_files = recursive_missing_files_and_folders(source, dest)
    create_folders(missing_folders, source, dest)
    failed_files = []
    print("There are {} filest to sync".format(len(missing_files)))
    print("Start syncing")
    for f in tqdm.tqdm(missing_files):
        try:
            copy2(f, f.replace(source, dest))
        except Exception as e:
            print("Failed to copy the file: {} to {}".format(f, f.replace(source,dest)))
            failed_files.append(f)
    print("Finished with {} failed files".format(len(failed_files)))
    return failed_files
    
def sync_folders(source, dest):
    files_to_sync = calc_missing_files(source, dest)
    failed_files = []
    print("There are {} filest to sync".format(len(files_to_sync)))
    print("Start syncing")
    for f in tqdm.tqdm(files_to_sync):
        try:
            copy2(os.path.join(source, f), dest)
        except Exception as e:
            print("Failed to copy the file: {}".format(f))
            failed_files.append(f)
    print("Finished with {} failed files".format(len(failed_files)))
    return failed_files
