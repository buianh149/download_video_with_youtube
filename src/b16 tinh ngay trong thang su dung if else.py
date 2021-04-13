print("Chuong trinh kiem tra ngay trong thang!")
month, year = [int(x) for x in input(" nhap month and year").split()]

if (1<= month <= 12):
   print("month", month)
   print("year", year)    
   if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)): # xet nam nhuan
      if month == 2:
         print("In month", month, "co 29 days")
   else : 
      if (month == 1 or month == 3 or month == 5 or month == 7 or 
      month == 8 or month == 10 or month == 12):
         print("In month", month, "co 31 days")
      elif month == 2:
         print("In month", month, "co 28 days")
      elif (month == 4 or month == 6 or month == 9 or month == 11):
         print("In month", month, "co 31 days")
else: 
   print("INVALID")      



