from unittest import TestCase, main
from distilnlp import text_normalize

class TestNormalize(TestCase):
    def test_zh(self):
        self.assertEqual(text_normalize('人权是所有人与生俱来的权利,不分国籍、性别、宗教或任何其他身份.', 'zh'), 
                                   '人权是所有人与生俱来的权利，不分国籍、性别、宗教或任何其他身份。')
        self.assertEqual(text_normalize('他说："你好吗?"', 'zh'), 
                                   '他说：“你好吗？”')
        self.assertEqual(text_normalize('“他说："你好吗？"', 'zh'), 
                                   '他说：“你好吗？”')
        self.assertEqual(text_normalize('他说："你好吗？"”', 'zh'), 
                                   '他说：“你好吗？”')
        self.assertEqual(text_normalize('“他说：“你好吗？””', 'zh'), 
                                   '“他说：“你好吗？””')
        self.assertEqual(text_normalize('你知道吗？', 'zh'), 
                                   '你知道吗？')
        self.assertEqual(text_normalize('测试(一下)', 'zh'),
                                   '测试（一下）')

    def test_en(self):
        self.assertEqual(text_normalize('The project was started in 2007 by David Cournapeau as a Google Summer of Code project， \nand since then many volunteers have contributed.\nSee the About us page for a list of core contributors. ', lang='en'), 
                                   'The project was started in 2007 by David Cournapeau as a Google Summer of Code project, and since then many volunteers have contributed. See the About us page for a list of core contributors.')

        self.assertEqual(text_normalize('How are you?”', lang='en'), 
                                   'How are you?')
        self.assertEqual(text_normalize('"How are you?', lang='en'), 
                                   'How are you?')
        self.assertEqual(text_normalize('He said, "How are you?"', lang='en'), 
                                   'He said, "How are you?"')

    def test_zh_en(self):
        self.assertEqual(text_normalize('这是一句夹杂着英文的中文文本。He said： "Who speaks English?". 结束.', 'zh'), 
                                   '这是一句夹杂着英文的中文文本。He said: "Who speaks English?". 结束。')
        self.assertEqual(text_normalize('请注意 float.hex() 是实例方法，而 float.fromhex() 是类方法。', 'zh'), 
                                   '请注意 float.hex() 是实例方法，而 float.fromhex() 是类方法。')
        self.assertEqual(text_normalize('请注意 float.hex() 是实例方法，而 float.fromhex() 是类方法。', 'zh'), 
                                   '请注意 float.hex() 是实例方法，而 float.fromhex() 是类方法。')
        self.assertEqual(text_normalize('例如 var x = 42。', 'zh'),
                                   '例如 var x = 42。')
        self.assertEqual(text_normalize('就像这样 let { bar } = foo。', 'zh'),
                                   '就像这样 let { bar } = foo。')
        self.assertEqual(text_normalize('1. 几个代表团回顾了战略计划执行进展情况并展望未来', 'zh'),
                                   '1. 几个代表团回顾了战略计划执行进展情况并展望未来')
        self.assertEqual(text_normalize('在本议程项目下，审计委员会将向执行局提交2013年12月31日终了财政年度财政报告和已审计财务报表以及审计委员会的报告(A/69/5/Add.12)，供执行局参考。', 'zh'),
                                   '在本议程项目下，审计委员会将向执行局提交2013年12月31日终了财政年度财政报告和已审计财务报表以及审计委员会的报告(A/69/5/Add.12)，供执行局参考。')

    def test_zh_with_url(self):
        self.assertEqual(text_normalize('百度的网址是:  http：//baidu.com', 'zh'),
                                   '百度的网址是： http://baidu.com')
    def test_remove_emoji(self):
        self.assertEqual(text_normalize('This is an English sent😇ence.', lang='en'),
                                   'This is an English sentence.')
        self.assertEqual(text_normalize('这是中文⚓句子.', 'zh'),
                                   '这是中文句子。')
    
    def test_remove_invisible_symbols(self):
        self.assertEqual(text_normalize('This \u202Cis an\u202D English\f sentence.', lang='en'), 
                                         'This is an English sentence.')
    
    def test_remove_excess_symbols(self):
        self.assertEqual(text_normalize('“《联合国纪事》不是官方记录。', 'zh'), 
                                   '《联合国纪事》不是官方记录。')
        self.assertEqual(text_normalize('《联合国纪事》不是官方记录。”', 'zh'), 
                                   '《联合国纪事》不是官方记录。')
        self.assertEqual(text_normalize('"The UN Chronicle  is not an official record. ', lang='en'), 
                                   'The UN Chronicle is not an official record.')
        self.assertEqual(text_normalize('The UN Chronicle  is not an official record."', lang='en'), 
                                   'The UN Chronicle is not an official record.')

if __name__ == '__main__':
    main()