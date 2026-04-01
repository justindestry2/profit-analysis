# profit-analysis
A Python tool to identify profitable Pokémon card flips using eBay vs PriceCharting data.

Profit Analysis (V1) -
A Python-based tool that analyzes Pokémon card listings by comparing eBay prices to PriceCharting values to identify profitable flips.

Overview -
This project helps identify whether a Pokémon card is a good deal or not based on potential profit after fees.
It was built as part of my journey learning Python and applying programming to real-world use cases like reselling and market analysis.

Features -
Calculates profit after estimated eBay fees (13%)
Categorizes deals as:
-Good Deal
-No Deal

Tracks: 
Total cost
Total profit
Number of good deals
Supports multiple card entries in one session

Profit Formula -
profit = pricecharting_price - (ebay_price * 1.13)

Tech Used -
Python
CLI (Command Line Interface)
Basic data structures (lists, functions)

Project Structure -
profit_analysis_v1.py
README.md

How to Run -
Clone the repo:
git clone https://github.com/justindestry2/profit-analysis.git
Navigate into the folder:
cd profit-analysis
Run the program:
python profit_analysis_v1.py

Future Improvements (V2+ Roadmap) -
Store card data using dictionaries for better structure
Export results to CSV
Integrate live data from:
eBay API
PriceCharting
Add filtering (PSA grade, set, etc.)
Build a UI or web dashboard


What I Learned -
How to structure a multi-step Python program
Writing reusable functions
Managing loops and user input
Thinking in terms of real-world problem solving with code

Goal -
This project is part of a larger plan to build a live Pokémon card arbitrage tracker that can scan marketplaces and highlight profitable opportunities in real time.

Author -
Justin Hall
Aspiring developer transitioning from retail leadership into tech
