from art import logo

print(logo)
print("Welcome toh the SECRET Auction Program")

auction_finish = False
players_bids = {}
top_bid = 0
top_player = ""

while not auction_finish:
    player_name = input("Enter Your Name:")
    bid = int(input("Enter Your Bid: $"))
    players_bids[f"{player_name}"] = bid
    question = input("Are there other bidders? Type 'yes' or 'no' :")
    if question == "yes":
        print("\n" * 20)
        auction_finish = False
    else:
        auction_finish = True

for key in players_bids:
    if players_bids[key] > top_bid:
        top_player = key
        top_bid = players_bids[key]

print(f"The winner is {top_player} with a bid of ${top_bid}")
