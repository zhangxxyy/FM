import unittest
import requests
from lib import db
from lib import load_data
import json
from conf import config


class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  ###整个测试类（准备方法）只执行一次
        cls.sheet = load_data.get_sheet(config.data_path, "注册")  # cls.sheet公用方法

    def test_user_reg_normal(self):
        case_data= load_data.get_case(self.sheet,"test_user_reg_normal")
        # NAME = "张三丰"
        # if db.check_user("张三丰"):  # 环境准备
        #     db.del_user("张三丰")
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res= json.loads(case_data[4])
        res = requests.post(url=url, json=data)
        self.assertEqual(excepted_res, res.json())
        # self.assertTrue(db.check_user(NAME))

        db.del_user("张三丰")   # 环境清理

    def test_user_reg_use_exist(self):
        case_data2= load_data.get_case(self.sheet,"test_user_reg_use_exist")
        url = case_data2[2]
        data = json.loads(case_data2[3])
        excepted_res2= json.loads(case_data2[4])
        res2 = requests.post(url=url, json=data)

        self.assertEqual(excepted_res2, res2.json())