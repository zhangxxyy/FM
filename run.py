import unittest
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from conf import config
# 遍历指定文件夹下及子包下的所有测试用例  test_
all = unittest.defaultTestLoader.discover("./testcase")##用例搜索路径


if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(all)  # 两个不能同时使用
    config.logging.info("测试开始"+"=")
    with open(config.report_file, "wb") as f:  # 二进制写模式;写在report文件下面
        HTMLTestRunner(stream=f, title="User接口测试报告", description="测试报告").run(all)
    config.logging.info("测试结束"+"=")