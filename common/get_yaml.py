# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/7 9:29

import yaml
import os


class HandleYaml:
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            # os.path.abspath('.')表示获取当前文件所在目录；os.path.dirname表示获取文件所在父目录；所以整个就是项目的所在路径
            print(root_dir)
            self.file_path = root_dir


    def get_data(self):
        fp = open(self.file_path, encoding='utf-8')
        data = yaml.load(fp, Loader=yaml.FullLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        return data
#
#
# if __name__ == '__main__':
#     test = HandleYaml()
#     p = test.get_data()
#     print(p['test_login_pass'])
