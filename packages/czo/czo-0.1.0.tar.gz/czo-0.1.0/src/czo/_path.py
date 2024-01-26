import os
import shutil
import sys


class Path:
    """
    处理文件相关的功能
    """

    @staticmethod
    def clear_directory(path):
        """
        清空指定目录下的所有文件和子目录。

        Args:
            path:要清空的目录
        """
        if not os.path.exists(path):
            sys.exit("要清空的目录不存在")

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    @staticmethod
    def clear_key_file(dir_path, keyword) -> None:
        """
        删除一个目录下包含关键字的文件

        Args:
            dir_path: 要检索的目录
            keyword:文件名中包含的关键字
        """
        file_list = [os.path.join(dir_path, j) for dir_path, dirnames, filenames in
                     os.walk(dir_path) for j in filenames]
        for target_file in file_list:
            if keyword in target_file:
                os.remove(target_file)

    @staticmethod
    def del_key_row(file: str, key: str) -> None:
        """
        删除文件中和 key 相等的行

        Args:
            file : str
            key : str 
        """
        with open(file, 'r', encoding='utf8') as f:
            lines: list[str] = f.readlines()
        with open(file, 'w', encoding='utf8') as f:
            for line in lines:
                if line.strip('\n') != key:
                    f.write(line)

    @staticmethod
    def get_dir_file_list(path: str) -> list:
        """
        获取path下所有文件的路径，包括子目录。
        """
        return [
            os.path.join(root, fn)
            for root, dirs, files in os.walk(path)
            for fn in files
        ]

    @staticmethod
    def mkdir_dir(path) -> None:
        """
        如果目录不存在就创建

        Args:
            path:目录
        """
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def get_project_path(project_name: str) -> str:
        """
        根据项目名称获取项目根目录绝对路径
        """
        curPath: str = os.path.abspath(os.path.dirname(__file__))
        return curPath[:curPath.find(project_name) + len(project_name)]
