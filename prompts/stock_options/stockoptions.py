#!/usr/bin/python

def best(stock_prices):
  """"Given a list of prices, return the maximum profit.

  If no profit is possible, return 0.
  """










################################################
##      TESTING ONLY. NO NEED TO UPDATE.      ##
################################################
print("Running some tests...\n")
all_passed = True
if best([15, 10, 20, 22, 1, 9]) == 12:
    print u'\u2714' + " best([15, 10, 20, 22, 1, 9]) = 12"
else:
    print u'\u2717' + " best([15, 10, 20, 22, 1, 9]) = 12"
    all_passed = False
if best([1, 2, 3, 4, 5]) == 4:
    print u'\u2714' + " best([1, 2, 3, 4, 5]) = 4"
else:
    print u'\u2717' + " best([1, 2, 3, 4, 5]) = 4"
    all_passed = False
if best([2, 3, 10, 6, 4, 8, 1]) == 8:
    print u'\u2714' + " best([2, 3, 10, 6, 4, 8, 1]) = 8"
else:
    print u'\u2717' + " best([2, 3, 10, 6, 4, 8, 1]) = 8"
    all_passed = False
if best([7, 9, 5, 6, 3, 2]) == 2:
    print u'\u2714' + " best([7, 9, 5, 6, 3, 2]) = 2"
else:
    print u'\u2717' + " best([7, 9, 5, 6, 3, 2]) = 2"
    all_passed = False
if best([0, 100]) == 100:
    print u'\u2714' + " best([0, 100]) = 100"
else:
    print u'\u2717' + " best([0, 100]) = 100"
    all_passed = False
if best([5,4 ,3, 2, 1]) == 0:
    print u'\u2714' + " best([5,4 ,3, 2, 1]) = 0"
else:
    print u'\u2717' + " best([5,4 ,3, 2, 1]) = 0"
    all_passed = False
if best([100]) == 0:
    print u'\u2714' + " best([100]) = 0"
else:
    print u'\u2717' + " best([100]) = 0"
    all_passed = False
if best([100, 0]) == 0:
    print u'\u2714' + " best([100, 0]) = 0"
else:
    print u'\u2717' + " best([100, 0]) = 0"
    all_passed = False
if best([]) == 0:
    print u'\u2714' + " best([]) = 0"
else:
    print u'\u2717' + " best([]) = 0"
    all_passed = False

if all_passed == False:
    print("\nTest(s) failed! Please try again! :)")
else:
    print("\nAll tests passed! Great job! :)")
