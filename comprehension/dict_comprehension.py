

tea_prices_inr = {
    "Masala Chai": 50,
    "Green Tea": 40,
    "Black Tea": 45,
}

# Convert all the prices from INR to USD
tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}


print(tea_prices_usd)


