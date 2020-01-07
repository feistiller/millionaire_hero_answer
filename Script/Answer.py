from Script.BAIDU_ocr import BORC
from Script.BDSearch import BDSearch
import re


class Answer:
    # 问题
    ask = ''
    # 多个选项
    answer = []
    # 图片
    image = ''
    best = ''

    def __init__(self, name):
        self.img_url = name

    # 读取图片并且转换为Base64
    def read_img(self):
        self.image = self.get_file_content(self.img_url)

    # 通过API获得图片中的文字赋值
    def get_text(self):
        b = BORC(self.image)
        data = self.wash_data(b.words)
        # ['题目','answer1','answer2','answer3']
        self.ask = data[0]
        self.answer = data[1:-1]

    # 通过搜索API处理得到答案
    def get_answer(self):
        result = []
        for item in self.answer:
            result.append({'key:': item, 'num': BDSearch.get_search_num(BDSearch(), self.ask + item)})
        r_max = result[0]
        for i in range(0, len(result)):
            print(i)
            if r_max['num'] < max[i]['num']:
                r_max = result[i]
        self.best = result[i]['key']

    # 控制流程
    def run(self):
        print("开始执行，读取图片")
        self.read_img()
        print("识别中……")
        self.get_text()
        print("识别完成")
        print("问题是：", self.ask)
        print("搜索中……")
        self.get_answer()
        print("答案是：", self.best)

    """ 读取图片 """

    @staticmethod
    def get_file_content(file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()

    @staticmethod
    def wash_data(data):
        m_list = []
        if 'words_result_num' in data:
            data = data['words_result']
            for i in range(0, len(data)):
                if re.match("^\d+.*\?$", data[i]['words']):
                    m_list.append(data[i]['words'])
                    m_list.append(data[i + 1]['words'])
                    m_list.append(data[i + 2]['words'])
                    m_list.append(data[i + 3]['words'])
                    # 第12题可能是4个答案
                    if '12' in data[i]['words']:
                        m_list.append(data[i + 4]['words'])
                    break
            return m_list
        else:
            print(data)
        return None
