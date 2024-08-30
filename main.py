from Features import search_by_date,sort,add_data,remove_data,sum_amount
#list of dictionary in variable transactions
transaction=[
    {"date":"27-8-2024","amount":5000,"description":"shoe"},
    {"date":"26-8-2024","amount":200,"description":"fruit"},
    {"date":"28-8-2024","amount":10000,"description":"groceries"},
    {"date":"29-8-2024","amount":3000,"description":"dress"},
    {"date":"30-8-2024","amount":150000,"description":"laptop"}
]
flag = True
while flag:
  print("1. Add Transaction")
  print("2. searching Transaction")
  print("3. Sorting Transaction")
  print("4. Delete Transaction")
  print("5. Displaying Transaction")
  print("6. Exit ")
  print("7. Sum Amount")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    print("-"*50)
    print("Adding data")
    print("-"*50)
    transaction=add_data(transaction)
    print("-"*50)
  elif choice == 2:
    print("-"*50)
    print("searching data")
    print("-"*50)
    target_date = input("Enter date to search: ")
    print(search_by_date(transaction,target_date))
    print("-"*50)
  elif choice == 3:
    print("-"*50)
    print("sorting data")
    print("-"*50)
    transaction=sort(transaction)
    print("-"*50)
  elif choice == 4:
    print("-"*50)
    print("Deleting data")
    print("-"*50)
    transaction=remove_data(transaction)
    print("-"*50)
  elif choice == 5:
    print("-"*50)
    print("Displaying Transactions")
    print("-"*50)
    print(transaction)
    print("-"*50)
  elif choice == 6:
    print("-"*50)
    print("Exiting Application")
    flag = False
  elif choice == 7:
    print("-"*50)
    print("Sum amount")
    print(sum_amount(transaction))
    print("-"*50)
  else:
    print("please enter the correct choice")
    print("-"*50)
