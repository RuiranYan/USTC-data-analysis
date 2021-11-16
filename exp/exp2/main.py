import re
import urllib.request, urllib.error

baseurl = "http://tiku.gaokao.com/gaokao/d347"


def askURL(url):
    # 请求伪装
    head = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 "
                          "Safari/537.36"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    # 报错机制
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 获取数据
def getData(baseurl):
    dataDic = {}
    linklist = []
    titlelist = []
    for i in range(10):
        # 找到不同页数的url规则url = baseurl + "?pg=" + page且一页有十张试卷
        page = str(10 * i + 1)
        url = baseurl + "?pg=" + page
        # print(url)
        html = askURL(url)
        # 获取标题列表
        titlelist = titlelist + re.findall(r'class="c-l2" target="_blank">(.*?)（word版）', html)
        # 获取链接列表
        linklist = linklist + re.findall(r'<a href="(.*?)" class="download"', html)
    # 生成字典
    for i in range(len(titlelist)):
        dataDic[titlelist[i]] = linklist[i]
    # print(titlelist)
    # print(linklist)
    # print(dic)
    # print("length of the dictionary is ",len(dic))
    return dataDic


# 数据保存
def saveData(dataDic):
    i = 0
    for x in dataDic:
        # 找到命名规则并修改
        name = x.replace("年", "_").replace("高考", "_").replace("试题", ".docx")
        # 对于不需要爬取的答案内容直接跳过
        if "答案" in x:
            continue
        # 此处filename可自由设置保存路径
        urllib.request.urlretrieve(dataDic[x], filename=f'./pachong/data/{name}')
        # print(dataDic[x])
        print("success")
        i = i + 1
        # 爬取30份后跳出
        if i == 30:
            break


if __name__ == '__main__':
    dataDic = getData(baseurl)
    saveData(dataDic)
