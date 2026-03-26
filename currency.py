# currency.py

# Get amounts from the user
CO = float(input('How much do you have in pesos? '))
PE = float(input('How much do you have in soles? '))
BR = float(input('How much do you have in reais? '))

# Convert to USD
USD_CO = CO / 17.39   # Example conversion rate
USD_PE = PE / 3.36
USD_BR = BR / 5.20

# Calculate total USD
total = USD_CO + USD_PE + USD_BR

# Display the result
print(f"Total in USD: {total:.2f}")