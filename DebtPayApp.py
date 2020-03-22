##DebtPayApp
debt = 789000
money = input('how much money do you have?')
if int(money) < debt:
  print('Sorry sir, looks like your money is not enough to completely pay off the debt. Do you still want to proceed your payment?, then th debt left will be:' , debt-int(money))
elif int(money)==debt:
  print('Your money is precisely enough to pay off all the debt. Proceeding to continue your payment...')
else:
  print('Your money is more than enough to pay off the debt completely, here is the change:' , int(money)-debt)
##virgilnr
##Palembang,Indonesia
##TunasBangsa
