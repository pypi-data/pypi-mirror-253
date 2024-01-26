import hashlib
import random
import secrets
import shutil
import string
import uuid


class Random:
    """
    随机生成一些测试数据
    """
    @staticmethod
    def random_file(data: str | None = None) -> tuple:
        """
        生成随机文件并返回文件路径和文件的 MD5 哈希值。

        该函数用于生成一个随机文件，并返回该文件的路径和MD5哈希值。
        可以通过传入参数指定文件内容，默认为None。函数首先生成一个随机字符串，
        并将其与UUID结合，作为临时文件的名称。然后，根据传入的内容将文件写入临时文件中。
        最后，使用hashlib库计算临时文件的MD5哈希值，并将临时文件移动到指定路径上。
        函数返回一个包含文件路径和MD5哈希值的元组。

        Args:
            data (str | None, optional): 文件内容，默认为 None。

        Returns:
            tuple: 包含文件路径和文件的 MD5 哈希值的元组。

        Example:
            ```python
            result = random_file(data='Hello, World!')
            print(result)  # 输出: ("./file", "a1b2c3d4e5f6...")
            ```
        """

        rand_str: list[str] = random.sample(
            string.ascii_letters + string.digits, 20)
        random_value: str = ''.join(rand_str) + '\n' + str(uuid.uuid4())

        temp_name = '.temp123qwe231'
        with open(temp_name, 'w') as w:
            if data is not None:
                w.write(f"{data}\n{random_value}")
            else:
                w.write(f"{random_value}")
        with open(temp_name, 'rb') as r:
            md5: str = hashlib.md5(r.read()).hexdigest()
        temp_path: str = f'./{md5}'
        shutil.move(temp_name, temp_path)
        return temp_path, md5

    @staticmethod
    def random_str(length: int, is_zh: bool = False, mark: bool = False, is_int: bool = False) -> str:
        """
        生成指定长度的随机字符串。

        Args:
            length (int): 字符串长度。
            is_zh (bool, optional): 是否包含中文字符，默认为 False。
            mark (bool, optional): 是否包含标点符号，默认为 False。
            is_int (bool, optional): 是否生成随机整数字符串，默认为 False。

        Returns:
            str: 生成的随机字符串。

        Example:
            ```python
            result = random_str(10)
            print(result)  # 输出: "random_str"
            ```
        """

        def generate_chinese():
            result = ""
            for _ in range(length):
                # 生成随机的中文字符
                char = chr(random.randint(0x4E00, 0x9FA5))
                result += char
            return result

        if is_zh:
            return generate_chinese()
        if is_int:
            return ''.join(str(secrets.randbelow(10)) for _ in range(length))

        from random import SystemRandom
        sys_random = SystemRandom()

        if mark:
            return "".join(
                sys_random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

        return "".join(sys_random.choice(string.ascii_letters + string.digits) for _ in range(length))
