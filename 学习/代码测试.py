import unittest
from 学习.pree import get_formatted_name

'''模块unittestt提供了代码测试工具'''
# 创建测试用例
# 方法名均以test开头

class NameTestCase(unittest.TestCase):
    '''测试name_funcation.py'''
    def test_first_last_name(self):
        '''能够正确处理像janis joplin这样的名字吗？'''
        name = get_formatted_name('janis','joplin')
        self.assertEqual(name,'Janis Joplin')

    def test_first_last_middle_name(self):
        '''是否能够处理wo cao ak 这样的名字'''
        name = get_formatted_name('wo','cao','ak')
        self.assertEqual(name,'Wo Cao Ak')

unittest.main()

# 多种断言方法
# 1.assertEqual(a,b)核实a==b
# 2.assertNotEqual(a,b)核实a!=b
# 3.assertTrure(x)
# 4.assertFause(x)
# 5.assertIn(item,list)核实item在list中
