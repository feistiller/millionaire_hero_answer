from aip import AipOcr
import configparser


class BORC:
    baidu_api = []
    client = None
    img = ''
    words = []

    def __init__(self, img):
        self.img = img
        conf = configparser.ConfigParser()
        conf.read('config.ini')
        baidu_api = conf.items('BAIDU')
        self.baidu_urls = conf['BAIDU_OCR_API_URL']['COMMON_OCR_URL']
        self.client = AipOcr(baidu_api[1][1], baidu_api[2][1], baidu_api[3][1])
        self.send_img()

    def send_img(self):
        self.words = self.client.basicGeneral(self.img)
