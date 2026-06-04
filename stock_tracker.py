# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "MSFT": 300
}

total_investment = 0

while True:

    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print("Investment Value:", investment)

    else:
        print("Stock not found!")

print("\nTotal Investment Value:", total_investment)
input("Press Enter to exit...") 


with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: " + str(total_investment))