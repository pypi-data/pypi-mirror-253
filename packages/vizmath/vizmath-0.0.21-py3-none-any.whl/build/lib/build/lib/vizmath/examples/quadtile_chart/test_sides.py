#%%
sides = ['top', 'right', 'bottom', 'left']
for current_side in sides:
    if side == current_side:
        next_index = (sides.index(current_side) + 1) % len(sides)
        side = sides[next_index]
        print(side)

#%%
def next_side(current_side):
    sides_order = ['top', 'right', 'bottom', 'left']
    current_index = sides_order.index(current_side)
    next_index = (current_index + 1) % len(sides_order)
    return sides_order[next_index]

# Example usage:
current_side = "invalid_input"  # Starting with an invalid input
for _ in range(4):  # Looping through all four sides
    print(current_side)
    current_side = next_side(current_side)