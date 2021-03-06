# -*- coding: utf-8 -*-
from pylab import *
# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
# pylab
# 
# 安装：pip install matplotlib
# 
# figure(title) 创建一个Figure(图表)对象
# subplot(numRows, numCols, plotNum) 快速绘制包含多个子图的图表
# plot(x,y,style) 二维线画图函数,如果只提供一个列表或数组，则matplotlib假定它是一个y值序列,style = 'colorstyle' r* r- r^ ro
# title(text) 绘图标题
# xlabel(text) 添加x轴文本
# ylabel(text) 添加y轴文本
# text(x,y,text) 在坐标x,y里添加文本
# annotate() 使用箭头添加注释
# gray() 设置默认colormap为线性灰度色图
# axis([xmin，xmax，ymin，ymax]) 显示坐标轴，参数为'off'：不显示,'square'：横纵坐标的单位刻度不同，但一定是方形,'equal'：横纵坐标的单位刻度相同，不一定是方形
# contour() 绘制轮廓图
# savefig(path) 保存图片
# [a,b] = hist(x,n=10) 绘制直方图 
# x是一维向量，函数功能是将x中的最小和最大值之间的区间等分n份，横坐标是x值，纵坐标是该值的个数。
# 返回的a是落在该区间内的个数，b是该区间的起始位置坐标。
# 例：x = [1,2,3,4,5,6,1,2,5,4,7,8,5,6,4,6] n = 10, x的最小值和最大值是1,8 区间为7，等分10份，1份 = 0.7
# a = [ 2.,  2.,  1.,  0.,  3.,  3.,  0.,  3.,  1.,  1.],b=[ 1. ,  1.7,  2.4,  3.1,  3.8,  4.5,  5.2,  5.9,  6.6,  7.3,  8. ]
# 1.  - 1.7 区间 有2个 1 1
# 1.7 - 2.4 区间 有2个 2 2
# 2.4 - 3.1 区间 有1个 3
# 3.1 - 3.8 区间 有0个
# 3.8 - 4.5 区间 有3个 4 4 4
# 4.5 - 5.2 区间 有3个 5 5 5
# 5.2 - 5.9 区间 有0个
# 5.9 - 6.6 区间 有3个 6 6 6
# 6.6 - 7.3 区间 有1个 7
# 7.3 - 8.  区间 有1个 8
# 
# grid() 显示网格线
# imshow(im,cmap) 绘画图片 colormap 色图类型 : https://baike.baidu.com/item/colormap/19584499?fr=aladdin
# ginput(n) 鼠标取坐标点，n为取坐标点的数量
# show() 显示出绘图窗口
# array() 转为NumPy数组对象
# array.min() 最小像素
# array.max() 最大像素
# array.flatten() 返回一个折叠成一维的数组
# 
# 灰度变换函数
# 图像反转，底片效果,反相 f(x)=255-x
# 将图像像素值变换到 100...200 区间 f(x)=(100/255)x+100
# 对图像像素值求平方后得到的图像(二次函数变换，使较暗的像素值变得更小) f(x)=255(x/255)^2
# 
# 增强对比度 直方图均衡化
# 
# def histeq(img,nbr_bins=256):
#     # 获取直方图p(r)
#     imhist, bins = histogram(img.flatten(), nbr_bins, normed = True)
#     # 获取T(r)
#     cdf = imhist.cumsum() # cumulative distribution function
#     cdf = 255 * cdf /cdf[-1] 
#     # 获取s，并用s替换原始图像对应的灰度值
#     result = interp(img.flatten(),bins[:-1],cdf)
#     return result.reshape(img.shape),cdf
#     
# 图像平均
# def compute_average(filelist):
# 	averageim = array(Image.open(filelist[0]),'f')
# 	skipped = 0
# 	for path in filelist[1:]:
# 		try:
# 			averageim += array(Image.open(path),'f')
# 		except:
# 			skipped += 1
# 	averageim /= len(filelist) - skipped
# 	return array(averageim,'uint8')
#
# img = array(Image.open(xxx))
# x,y,color = img.shape()
# 一维系x，二维系y，三维是颜色通过
# 左右翻转
#   img[:,-1::-1] 二维y轴翻转
#
# 上下翻转
#   img[-1::-1] 一维y轴翻转
#
# 颜色翻转
#   img[...,-1::-1] 三维颜色通过翻转
#   ...代表省略前面的：冒号，1个冒号代表1个维度
