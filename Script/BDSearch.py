import urllib3



class BDSearch:

    # 现仅通过查询相关连的数目
    def get_search_num(self, text):
        url = 'https://www.baidu.com/s?wd=' + text
        # print(url)
        self.search(url)

    # 请求网页返回结果
    def search(self, url):
        http = urllib3.PoolManager(num_pools=5)
        res = http.request('GET', url)
        res = res.data.decode()
        self.get_num(res)

    # 解析网页结果
    @staticmethod
    def get_num(html):
        print(html)
