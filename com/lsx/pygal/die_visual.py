#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : die_visual.py
# @Author: Armote
# @Date  : 2018/10/19 0019
# @Desc  :掷骰子
from com.lsx.pygal.die import Die
import pygal
import datetime

class DieVisual():
    """让我们一起掷骰子玩"""

    def playDie():
        die = Die()
        #掷几次骰子,并将结果存储在一个列表中
        results = []
        for roll_num in range(1000):
            result = die.roll()
            results.append(result)

        #查看结果
        print(results)
        #分析结果:统计6种结果的次数
        frequencies = []
        for value in range(1,die.num_sides+1):
            frequency = results.count(value)
            frequencies.append(frequency)

        #对结果进行可视化
        hist = pygal.Bar()

        hist.title = "摇骰子看结果咧"
        hist.x_labels = ['1','2','3','4','5','6']
        hist.x_title = "Resule"
        hist.y_title="结果频率"

        hist.add('D6',frequencies)
        fileName = 'D:/file/die_visual' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.svg'
        hist.render_to_file(fileName)

        print(frequencies)


    playDie()