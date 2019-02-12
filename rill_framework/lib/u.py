import datetime
from selenium import webdriver
from PIL import Image
import math
import operator
from functools import reduce

"""
@author:bournli
@date:2019/1/31
"""
def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')


days = ['20180422', '20180423', '20180424','20180425', '20180426', '20180427', '20180428']

def td(t=0):
    day = today()
    td = '19700101'

    for i,d in enumerate(days):
        if d >= day:
            td = days[i+t]
            break
    return td

def test_trade_day():
    assert '20180422' == td(-3)
    assert '20180426' == td(1)

# add cmp fun by bournli on 2019/1/130


def image_contrast(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(reduce(operator.add,  list(map(lambda a, b: (a-b)**2, h1, h2)))/len(h1))
    return result

def image_cmp_result(img1):
    #img1 = r"./elementshot_exp.png"  # 指定图片路径
    img2 = r"./elementshot.png"
    result = image_contrast(img1, img2)
    return result

