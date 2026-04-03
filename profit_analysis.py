def get_card_name():
    while True:
        card_name = input("Card name: Type 'done' to finish. ")
        if len(card_name.strip()) == 0:
            print("Please enter a card name.")
            continue
        return card_name.strip()

def get_ebay_price():
    while True:
        try:
            card_price = float(input("eBay price: "))

            if card_price <= 0:
                print("Please enter a positive card price.")
                continue
            return card_price

        except ValueError:
            print("Please enter a valid card price.")

def get_pricecharting_price():
    while True:
        try:
            pcharting_price = float(input("PriceCharting price: "))
            if pcharting_price <= 0:
                print("Please enter a positive price.")
                continue
            return pcharting_price
        except ValueError:
            print("Please enter a valid card price.")
            continue

def calculate_profit(ebay,pricecharting):
    return pricecharting - (ebay * 1.13)

def profit_status(profit):
    if profit <= 50:
        return "No Deal!"
    else:
        return "Good Deal!"

def main():
    total_cost = 0
    total_profit = 0
    good_deals = 0

    cards = []

    while True:
        card = get_card_name()
        if card == "done":
            break

        ebay_price = get_ebay_price()
        pc_price = get_pricecharting_price()
        profit = calculate_profit(ebay_price, pc_price)
        total_profit += profit
        total_cost += ebay_price


        status = profit_status(profit)
        if status == "Good Deal!":
            good_deals += 1

        cards.append({
            "name": card,
            "ebay_price": ebay_price,
            "pricecharting_price": pc_price,
            "profit": profit,
            "status": status,
        })

        print(f"\nCard: {card}")
        print(f"eBay price: ${ebay_price:.2f}")
        print(f"Price Charting price: ${pc_price:.2f}")
        print(f"Profit:  ${profit:.2f}")
        print(f"Status: {status}")

    print("----BEST DEALS----")
    best_cards = []

    for i in cards:
        if i["status"] == "Good Deal!":
            best_cards.append(i)
            print(f"\nCard: {i['name'].title()} | Profit:  ${i['profit']:.2f}")

    print("----TOP 3 DEALS----")

    if cards:
        top_three = sorted(cards, key=lambda card: card["profit"], reverse=True)[:3]

        for i, card in enumerate(top_three, start=1):
            print(f"{i}. {card['name'].title()} | Profit: ${card['profit']:.2f} | Status: {card['status']}")

    print("----SUMMARY----")
    print(f"Total spent: {total_cost:.2f}")
    print(f"Total profit: {total_profit:.2f}")
    print(f"Good deals: {good_deals}")

if __name__ == "__main__":
    main()

