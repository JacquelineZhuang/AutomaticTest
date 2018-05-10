#_*_ utf-8 _*_
import HTMLTestRunner
import os
import unittest
import time


report_path = os.path.dirname(os.path.abspath('.'))+'/test_report/'
now= time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

HtmlFile = report_path +now+"HTMLTemplate.html"
fp= open(HtmlFile,"wb")

suite = unittest.TestLoader().discover("testsuits")

if __name__ =='__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream =fp , title = u"项目测试报告",description=u"用例测试情况" )
    runner.run(suite)



