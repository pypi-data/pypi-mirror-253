import os
import json
import shutil
import argparse

def find_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files


def process_json_file(file_path):
    # 打开JSON文件
    with open(file_path) as json_file:
        data = json.load(json_file)

        # 在这里对JSON数据进行修改
        # 例如，修改某个字段的值
        tests = data["tests"]
        test = tests.split('\n\n', 1)
        check_fun, test_check = test[0], test[1]
        lines = check_fun.splitlines()
        lines[0] = lines[0] + '\n    total_tests = 0\n    failed_tests = 0\n'
        for i in range(len(lines)):
            if ('assert candidate' in lines[i]):
                lines[i] = '\n    try:\n        total_tests += 1\n    ' + lines[i]
                lines[i] = lines[i] + '\n    except AssertionError:\n        failed_tests += 1\n'
            if (i == len(lines) - 1):
                lines[i] = lines[i] + '    print(total_tests, failed_tests)'
        check_fun = "".join(lines)
        new_tests = check_fun + '\n\n' + test_check
        data["tests"] = new_tests

    # 获取文件名和目录路径
    prefix = ""
    parent_directory = os.path.dirname(file_path)
    for _ in range(4):
        parent_directory, folder_name = os.path.split(parent_directory)
        prefix = os.path.join(folder_name, prefix)
    file_name = os.path.basename(file_path)
    destination_directory = "mod_tests"

    # 构建目标文件路径
    destination_path = os.path.join(destination_directory, prefix, file_name)
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    # 保存修改后的JSON文件到目标文件夹
    with open(destination_path, "w") as modified_file:
        json.dump(data, modified_file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, type=str)
    args = parser.parse_args()
    # 指定目录
    directory_path = args.path
    # 调用函数查找.json文件
    files = find_json_files(directory_path)
    # 逐个处理JSON文件
    for file in files:
        process_json_file(file)

if __name__ == "__main__":
    main()









# get_tests
# test = tests.split('\n\n', 1)
# check_fun, test_check = test[0], test[1]
# lines = check_fun.splitlines()
# lines[0] = lines[0] + '\n    total_tests = 0\n    failed_tests = 0\n'
# for i in range(len(lines)):
#     if('assert candidate' in lines[i]):
#         lines[i] = '\n    try:\n    ' + lines[i]
#         lines[i] = lines[i] + '\n        total_tests += 1\n    except AssertionError:\n        failed_tests += 1\n'
#     if(i == len(lines)-1):
#         lines[i] = lines[i] + '    print(total_tests, failed_tests)'
# check_fun = "".join(lines)
# new_tests = check_fun + '\n\n' + test_check
# print(new_tests)
