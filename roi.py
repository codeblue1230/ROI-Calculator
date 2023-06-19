import requests

class Income():
    def __init__(self):
        self.rent = 0
        self.extra_income_question = None
        self.extra_income = 0
        self.total_income = 0

    def monthly_income(self):
        
        print("Let's calculate your monthly income.")
        
        # Rent Income
        while True:
            try:    
                response_rent = int(input("What will you receive each month for rent? "))
                self.rent = response_rent
                break
            except:
                print("Sorry, you must type a number.")

        # Additional Income
        while True:
            extra_income_question = input("Do you want to include any additional income (storage, laundry, etc.)? Type 'Yes' or 'No' ")
            self.extra_income_question = extra_income_question
            if self.extra_income_question.lower() == 'yes':
                try:    
                    response_extra_income = int(input("How much would you like to add? "))
                    self.extra_income = response_extra_income
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.extra_income_question.lower() == 'no':
                print("There is no additional income to add.")
                break
            else:
                print("Sorry, you must type 'Yes' or 'No'")

        self.total_income = self.rent + self.extra_income
        print(f"Your total monthly income is ${self.total_income}.")


class Expenses():
    def __init__(self, i):
        self.tax = 0
        self.insurance = 0
        self.utility_question = None
        self.utilities = 0
        self.hoa_question = None
        self.hoa = 0
        self.lawn_question = None
        self.lawn = 0
        self.manager_question = None
        self.manager = 0
        self.mortgage_question = None
        self.mortgage = 0
        self.savings_question = None
        self.savings = 0
        self.misc_question = None
        self.misc = 0
        self.total_expenses = 0
        self.i = i
        self.percent = 0

    def monthly_expenses(self):
        
        print("Let's calculate your monthly expenses.")

        #Taxes
        while True:
            try:
                response_tax = int(input("How much do you expect to pay in taxes each month? "))
                self.tax = response_tax
                break
            except:
                print("Sorry, you must type a number.")               

        # Insurance
        while True:
            try:
                response_insurance = int(input("What will you pay per month for insurance? "))
                self.insurance = response_insurance
                break
            except:
                print("Sorry, you must type a number.")

        # Utilities
        while True:
            utility_question = input("Will you be paying the utilities or is the tenant responsible? Type 'L' for Landlord or 'T' for tenant. ")
            self.utility_question = utility_question
            if self.utility_question.lower() == 'l':
                try:
                    response_utilities = int(input("How much will the utilities cost each month? "))
                    self.utilities = response_utilities
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.utility_question.lower() == 't':
                print("The tenant is responsible for the utilities. Let's move on to HOA.")
                break
            else:
                print("Sorry, you must type 'L' or 'T'")

        # HOA
        while True:
            hoa_question = input("Does this dwelling have an HOA? Type 'Yes' or 'No': ")
            self.hoa_question = hoa_question
            if self.hoa_question.lower() == "yes":
                try:
                    response_hoa = int(input("What will the HOA cost each month? "))
                    self.hoa = response_hoa
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.hoa_question.lower() == "no":
                print("There are no HOA fees.")
                break
            else:
                print("Sorry, you must type 'Yes' or 'No'")

        # Lawn care
        while True:
            lawn_question = input("Will you be paying for lawn care? Type 'Yes' or 'No': ")
            self.lawn_question = lawn_question
            if self.lawn_question.lower() == 'yes':
                try:
                    response_lawn = int(input("How much is lawn care each month? "))
                    self.lawn = response_lawn
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.lawn_question.lower() == 'no':
                print("There is nothing to add for lawn care, let's continue.")
                break
            else:
                print("Sorry, you must type 'Yes' or 'No'")

        # Property Manager
        while True:
            manager_question = input("Will you need to pay a property manager? Type 'Yes' or 'No': ")
            self.manager_question = manager_question
            if self.manager_question.lower() == 'yes':
                try:
                    response_manager = int(input("What will you pay the property manager each month? "))
                    self.manager = response_manager
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.manager_question.lower() == "no":
                print("You will not be paying a property manager.")
                break
            else:
                print("Sorry, you must type 'Yes' or 'No'")

        # Mortgage
        while True:
            mortgage_question = input("Will you be paying a mortgage? Type 'Yes' or 'No': ")
            self.mortgage_question = mortgage_question
            if self.mortgage_question.lower() == 'yes':
                try:
                    response_mortgage = int(input("How much is the mortgage each month? "))
                    self.mortgage = response_mortgage
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.mortgage_question.lower() == 'no':
                print("No mortgage payments will be included in the expenses calculation.")
                break
            else:
                print("Sorry, you must type 'Yes' or 'No'")

        # Savings (Vacancy, Repairs, CapEx, etc...)
        while True:
            self.percent = self.i.total_income * 0.15
            print(f"We recommend putting ${round(self.percent)} (15% of your your total income) in an emergency")
            print("fund for instances such as vacancy, repairs, capital expenditures, etc.")
            savings_question = input("Would you like to include emergency funds in your budget? Type 'Yes' or 'No': ")
            self.savings_question = savings_question
            if self.savings_question.lower() == 'yes':
                try:
                    response_savings = int(input("How much do you want to put aside each month? "))
                    self.savings = response_savings
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.savings_question.lower() == 'no':
                print("Nothing will be put into an emergency fund.")
                break
            else:
                print("Sorry, you must type 'Yes' or 'No'")
        
        # Miscellaneous
        while True:
            misc_question = input("If there are any other expenses we haven't accounted for type 'Yes'. Otherwise type 'No': ")
            self.misc_question = misc_question 
            if self.misc_question.lower() == 'yes':
                try:
                    response_misc = int(input("What is the total of all the extra expenses you have? "))
                    self.misc = response_misc
                    break
                except:
                    print("Sorry, you must type a number.")
            elif self.misc_question.lower() == 'no':
                print("There are no miscellaneous expenses.")
                break
            else:
                print("Sorry, you must type 'Yes' or 'No'")

        total_expenses = self.tax + self.insurance + self.utilities + self.hoa + self.lawn + self.manager + self.mortgage + self.savings + self.misc
        self.total_expenses = total_expenses
        print(f"Your total monthly expenses come out to ${self.total_expenses}.")


class Cashflow():
    def __init__(self, i, e):
        self.final_cash_flow = 0
        self.annual_cash_flow = 0
        self.i = i
        self.e = e

    def get_cash_flow(self):
        final_cash_flow = self.i.total_income - self.e.total_expenses
        self.final_cash_flow = final_cash_flow
        self.annual_cash_flow = self.final_cash_flow * 12
        if self.final_cash_flow < 0:
            print(f"You will be losing money. You would lose ${self.final_cash_flow} each month.")
        elif self.final_cash_flow > 0:
            print(f"You have a positive cash flow of ${self.final_cash_flow} every month.")
        else:
            print(f"You have a cash flow of $0. You are breaking competely even.")


class Roi():
    def __init__(self, c):
        self.c = c
        self.roi = 0
        self.total_investment = 0
        self.down_payment_question = None
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_question = None
        self.rehab = 0

    def get_roi(self):
        # print(self.c.i.total_income)
        while True:
            print("Lastly, we need to find out all of your investments to calculate your ROI.")
            down_payment_question = input("Are you putting a down payment on the property? Type 'Yes' or 'No': ")
            self.down_payment_question = down_payment_question
            if self.down_payment_question.lower() == 'no':
                print("There is no down payment.")
                break
            elif self.down_payment_question.lower() == 'yes':
                try:
                    next_down_question = int(input("How much money are you putting down? "))
                    self.down_payment = next_down_question
                    break
                except:
                    print("Sorry, you must type a number.")
            else:
                print("Sorry, you must type 'Yes' or 'No'")

        while True:
            try:
                closing_costs = int(input("How much are your closing costs? "))
                self.closing_costs = closing_costs
                break
            except:
                print("Sorry, you must type a number.")

        while True:
            rehab_question = input("Are you paying any additonal costs upfront? (rehab, repairs, etc.) Type 'Yes' or 'No': ")
            self.rehab_question = rehab_question
            if self.rehab_question.lower() == 'no':
                print("There are no additional upfront costs.")
                break
            elif self.rehab_question.lower() == 'yes':
                try:
                    next_rehab_question = int(input("How much extra money are you putting into this property? "))
                    self.rehab = next_rehab_question
                    break
                except:
                    print("Sorry, you must type a number.")
            else:
                print("Sorry, you must type a number.")
        
        self.total_investment = self.down_payment + self.closing_costs + self.rehab
        print(f"Your total investment is ${self.total_investment} and your annual cash flow is ${self.c.annual_cash_flow}")
        self.roi = (self.c.annual_cash_flow / self.total_investment) * 100
        print("We take your annual cash flow, divide it by your total investment, and multiply it by 100 to get the percentage.")
        print(f"That gives us an ROI of {round(self.roi, 2)}%.")


class AlphaApi():
    def __init__(self):
        self.symbol = ''
        self.exchange = ''
        self.sector = ''
        self.desc = ''
        self.dividend = None
        self.dividend_share = None
        self.name = ''
        self.info = ''
        self.price = ''
        self.date = ''

    def get_api(self):
        while True:
            symbol_question = input("Enter a stock symbol: ")
            self.symbol = symbol_question
            r = requests.get(f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={self.symbol.upper()}&apikey=BIV0Y7IVUOQHL8NL")
            if r.status_code == 200:
                data = r.json()
                if data == {}:
                    print("Please check the stock symbol and try again.")
                else:
                    break
            else:
                print(f"Error: {r.status_code}")
                break
        
        while True:
            r = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.symbol.upper()}&apikey=BIV0Y7IVUOQHL8NL")
            if r.status_code == 200:
                the_price = r.json()
                if the_price == {}:
                    print("Please check they symbol and try again.")
                else:
                    break
            else:
                print(f"Error: {r.status_code}")
                break

        self.symbol = data["Symbol"]
        self.name = data["Name"]
        self.exchange = data["Exchange"]
        self.sector = data["Sector"]
        self.desc = data["Description"]
        self.dividend_share = float(data["DividendPerShare"])
        self.dividend = float(data["DividendYield"])

        while True:
            info_response = input(f"What do you want to know about {self.name.title()}? Type 'description', 'dividend', 'sector', 'price', 'exchange', or 'quit' to exit. ")
            self.info = info_response
            if self.info.lower() == 'description':
                print(self.desc)
            elif self.info.lower() == 'dividend':
                print(f"{self.name.title()} has an annual dividend yield of {round(self.dividend * 100, 2)}% and an amount of ${round(self.dividend_share, 2)}.")
            elif self.info.lower() == 'sector':
                print(f"{self.name.title()} is in the {self.sector.title()} sector.")
            elif self.info.lower() == 'exchange':
                print(f"{self.name.title()} is on the {self.exchange}.")
            elif self.info.lower() == 'price':
                try:
                    price_question = input("Input the most recent closed business day, otherwise your price may be inaccurate (YYYY-MM-DD): ")
                    self.price = the_price["Time Series (Daily)"][f"{price_question}"]["4. close"]
                    print(self.price)
                except:
                    print("Check the date you entered and try again.")
            elif self.info.lower() == 'quit':
                print("We hope, you enjoyed our stock market feature.")
                break
            else:
                print("Sorry, that is not a valid input.")


class RunIt():
    def __init__(self):
        self.test = None

    def run(self): 
        while True:
            response = input("Would you like to use the ROI Calculator? Type 'Yes' or 'No': ")

            if response.lower() == 'yes':
                income = Income()
                income.monthly_income()
                expenses = Expenses(income)
                expenses.monthly_expenses()
                cash_flow = Cashflow(income, expenses)
                cash_flow.get_cash_flow()
                roi_test = Roi(cash_flow)
                roi_test.get_roi()

            elif response.lower() == 'no':
                
                api_response = input("Would you like to use our stock market feature? Type 'Yes' or 'No': ")
                if api_response.lower() == 'yes':
                    api_test = AlphaApi()
                    api_test.get_api()
                elif api_response.lower() == 'no':
                    print("Thanks for stopping by Bigger Pockets. Good luck on your journey!")
                    break
                else:
                    print("Sorry, you must type 'Yes' or 'No'")

            else:
                print("Sorry, you must type 'Yes' or 'No'")


check = RunIt()
check.run()