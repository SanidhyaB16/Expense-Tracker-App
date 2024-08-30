#linear search for transaction data
def search_by_date(transaction,target_date):
    for transaction in transaction:
        if transaction["date"] == target_date:
         return transaction
    return "transaction not found."

def sort(transaction):
  n=len(transaction)
  for i in range(n-1):
    for j in range(0,n-i-1):
      if transaction[j]["date"] > transaction[j+1]["date"]:
        transaction[j],transaction[j+1] = transaction[j+1],transaction[j]
  return transaction 


def add_data(transaction):
    date = input("Enter date: ")
    amount = input("Enter amount: ")
    description = input("Enter description:")
    transaction.append({"date":date,"amount":amount,"description":description})
    return transaction

def remove_data(transaction):
  date = input("Enter date to remove: ")
  for i in transaction:
    if i["date"] == date:
      transaction.remove(i)
  return transaction

def sum_amount(transaction):
    sum=0
    year =input("Enter year: ")
    for transaction in transaction:
      if transaction['date'][5:] == year:
        sum += transaction["amount"]
    return sum
