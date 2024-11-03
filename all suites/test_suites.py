import unittest
#import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
import sys
sys.path.insert(0,"..")
from tests.hometestcases import Homepage_test
from tests.logintestcases import loginpage_test


tc1 = unittest.TestLoader().loadTestsFromTestCase(loginpage_test)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Homepage_test)

masterTestSuite = unittest.TestSuite([tc1,tc2])

report ='C:/Users/SAIMASHARONI/Desktop/office file/Automation/working/bn/report'
runner = HTMLTestRunner(combine_reports=True, report_name="Project Report", output= report)
runner.run(masterTestSuite)
