def findhighestbid(bidding):
    highest_bid=0 
    winner=""
    for name in bidding:
       if bidding[name]>highest_bid:
           highest_bid=bidding[name]
           winner=name
    print(f"Winner is {winner} with bid {highest_bid}")

bidding={}
bid=True
while bid:
    name = input('Enter Name: ')
    bid_price = float(input('Bid price: '))
    bidding[name]=bid_price
    ans=input("More Users want to bid :")
    if ans.lower()!="yes":
        bid=False
        findhighestbid(bidding)


