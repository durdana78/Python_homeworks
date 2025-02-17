def invest(amount, rate, years) :
    for i in range (1, years + 1) :
        print(f"year {i}: {(amount * ((1 + rate) ** i)) : .2f}")

amount_inserted = int(input("Insert the amount: "))
rate_inserted = int(input("Insert the rate: ")) / 100
years_inserted = int(input("Insert the years: "))
result = invest(amount_inserted, rate_inserted, years_inserted)
