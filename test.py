import xlrd
import xlwt
from nose2.compat import unittest
from ClassUnderTest import*
class test(unittest.TestCase):
  print "Unit testcases for the Complience Engine"
  def runTest(self):
    c1 = ClassUnderTest()
    wbr = xlrd.open_workbook("data.xls")
    sheetr = wbr.sheet_by_name('Double')
    wbw = xlwt.Workbook()
    sheetw = wbw.add_sheet('result')
    rCount = sheetr.nrows
    cCount = sheetr.ncols
    cx = 0
    try:
     for rx in range(sheetr.nrows):      
        rx = rx + 1
        self.assertEqual(sheetr.cell(rx, cx+1).value, c1.method1((sheetr.cell(rx, cx).value)), 'test case Failed')
        val = sheetr.cell(rx, cx).value
        sheetw.write(rx, cx, val)
        print sheetr.cell(rx, cx)
        print sheetr.cell(rx, cx+1)
        print "Test case passed"
    except IndexError, e:
        pass

    
 
if __name__ == '__main__':
    unittest.main()
     
