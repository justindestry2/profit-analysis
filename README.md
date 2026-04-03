Profit Analysis Tool

A Python-based tool that analyzes resale listings by comparing market prices across sources to identify potentially profitable flips.

The first version of this project focuses on Pokémon cards, with the long-term goal of expanding into other collectible and resale markets.

Overview -

This project evaluates whether a Pokémon card is a good deal based on estimated profit after eBay fees.
It was built as part of my Python learning journey, applying programming to a real-world use case: card reselling and market analysis.

Features

Calculates profit after estimated eBay fees (13%)

Categorizes deals as:
Good Deal
No Deal

Tracks:

- Total spent
- Total profit
- Number of good deals
- Supports multiple card entries in one session

Displays:

- Best deals
- Top 3 most profitable cards
- Session summary

Profit Formula

profit = pricecharting_price - (ebay_price * 1.13)

Tech Used -

- Python
- Command Line Interface (CLI)
- Lists & Dictionaries
- Functions
- File I/O (CSV)

Project Structure
- profit_analysis.py
- profit_data.csv
- README.md

How to Run -
- git clone https://github.com/justindestry2/profit-analysis.git
- cd profit-analysis
- python profit_analysis.py

Example Output

Card: Charizard PSA 10

eBay price: $120.00

PriceCharting price: $200.00

Profit: $56.00

Status: Good Deal

Future Improvements -
- Pull live data from eBay API
- Pull live data from PriceCharting
- Add filtering by grade, set, or card type
- Build a UI or dashboard
- Expand to other resale categories (e.g. sneakers, collectibles)

What I Learned - 
- Breaking programs into reusable functions
- Input validation using loops and exceptions
- Working with structured data (lists & dictionaries)
- Writing data to CSV files
- Applying Python to a real-world business problem

Long-Term Goal
This project is the foundation for a larger tool:
A live arbitrage tracker that scans marketplaces and identifies profitable opportunities in real time.

Author -

Justin Hall

Aspiring developer transitioning from retail leadership into tech
