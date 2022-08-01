def test():
    for x in range(0,5):
        if x == 5:
            print("This is False")
            return False
        print("This is True")
        return True

is_on = True
listing = []

listing.append(test())

print(listing)