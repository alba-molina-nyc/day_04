row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜"]
map = [row1, row2, row3] #nested list
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


horizonal = int(position[0]) #column first dig
vertical = int(position[1]) #row second dig

selected_row = map[vertical - 1]
selected_row[horizonal - 1] = "X"





