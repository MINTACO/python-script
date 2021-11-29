import os


# 深度遍历文件夹内文件路径
def get_all_file_path(dir_path):
    result = {}
    for root, subdirs, files in os.walk(dir_path):
        # print(files)
        for filename in files:
            # 获取文件路径
            # result.append(os.path.join(root, file))
            # print(os.path.join(root, file))
            result[filename] = os.path.join(root, filename)
    return result

