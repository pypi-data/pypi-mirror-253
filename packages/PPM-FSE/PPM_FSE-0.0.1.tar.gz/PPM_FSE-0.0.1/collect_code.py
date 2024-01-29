
import json
import os
import argparse


def mod_json(subfolders,path):
    # 遍历每个子文件夹
    for subfolder_path in subfolders:

        json_file_path = os.path.join(subfolder_path, os.path.basename(subfolder_path) + '.results.json')
        # 读取json文件内容
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            results = data['results']


        # txt_file_path = os.path.join(os.path.basename(path) +'.json')
        txt_file_path = 'codegen2b.txt'
        for i in range(len(results)):
            print(results[i]['program'])
            print()
            # with open(txt_file_path, 'a') as txt_file:
            #     json.dump(results[i]['program'], txt_file, indent=4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, type=str)
    args = parser.parse_args()

    parent_folder_path = args.path  # 替换为父级目录的路径
    subfolders = [f.path for f in os.scandir(parent_folder_path) if f.is_dir()]
    mod_json(subfolders,args.path)

if __name__ == "__main__":
    main()


