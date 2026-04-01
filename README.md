Profit Analysis Tool (V1)

A Python-based tool that analyzes Pokemon card listings by comparing eBay prices to PriceCharting values to identify potentially profitable flips.

Overview -

This project helps identify whether a Pokemon card is a good deal based on potential profit after estimated eBay fees.
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
- Lists
- Dictionaries
- Functions

Project Structure
- profit_analysis_v1.py
- README.md
- 
How to Run -
- Clone the repository:
- git clone https://github.com/justindestry2/profit-analysis.git
- Navigate into the project folder:
- cd profit-analysis
- Run the program:
- python profit_analysis_v1.py

Example Output

Enter card name: Charizard PSA 10

Enter eBay price: 120

Enter PriceCharting price: 200

Profit: $56.00

Status: Good Deal

Future Improvements -
- Add input validation with try/except
- Export results to CSV
- Pull live data from eBay
- Pull live data from PriceCharting
- Add filtering by grade, set, or card type
- Build a simple UI or dashboard

What I Learned - 
- How to break a program into reusable functions
- How to work with loops and user input
- How to store structured data using dictionaries
- How to solve a real-world business problem with Python

Long-Term Goal
This project is the starting point for a larger tool: a live Pokemon card arbitrage tracker that scans marketplaces and highlights profitable opportunities in real time.

Author -

Justin Hall

Aspiring developer transitioning from retail leadership into tech
