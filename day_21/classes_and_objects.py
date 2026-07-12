# DAY 21


# LEVEL 1

class Statistics:
    def __init__(self, lst):
        self.lst = lst
        self.length = len(lst)
        self.order_lst()
    def order_lst(self):
        lst = self.lst
        length = self.length
        for i in range(length):
            for j in range(0, length - i - 1):
                if(lst[j] > lst[j + 1]):
                    tmp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = tmp
        self.lst = lst
    def count(self):
        return len(self.lst)
    def sum(self):
        return sum(self.lst)
    def min(self):
        return self.lst[0]
    def max(self):
        return self.lst[-1]
    def range(self):
        return self.max() - self.min()

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print(data.range())


# LEVEl 2

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income[0]
        return total
    def add_income(self, income, description):
        self.incomes.append((income, description))
    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense[0]
        return total
    def add_expense(self, expense, description):
        self.expenses.append((expense, description))
    def account_info(self):
        return f'{self.firstname} {self.lastname}.\nIncomes: {self.incomes}\nExpenses: {self.expenses}'
    def account_balance(self):
        return self.total_income() - self.total_expense()

incomes = [(100, 'Dividends'), (2500, 'Salary'), (678.9, 'Passive Income')]
expenses = [(900, 'Rent'), (600, 'Total bills'), (700, 'Groceries')]
p = PersonAccount('Saforgu', 'Mufa', incomes, expenses)

print(p.account_info())
print('Total Income: ', p.total_income())
print('Total Expense: ', p.total_expense())
print('Balance: ', p.account_balance())

p.add_income(60, 'Gift')
p.add_expense(90, 'Present')

print(p.account_info())
print('Total Income: ', p.total_income())
print('Total Expense: ', p.total_expense())
print('Balance: ', p.account_balance())
