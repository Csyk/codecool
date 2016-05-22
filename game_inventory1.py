# step 1
def display_inventory(inv):
    print('Inventory:\n')
    piece = list(inv.values()) # make a list from dictionary values
    gift = list(inv) # make an other list from keys
    for i in range(len(inv)):
        s = str(piece[i]) + " " + (gift[i]) # join pieces and gifts
        print(s)
        summ = sum(list(inv.values())) # count the items
    print("Total number of items: " + str(summ))

# step 2
def add_to_inventory(inv, added_items):
    for item in added_items:
        inv[item] = inv.get(item, 0)+1

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
invent = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

add_to_inventory(invent, dragon_loot)
display_inventory(invent)
