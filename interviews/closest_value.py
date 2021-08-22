
def closest_value(num_arr, value):
    min_diff = num_arr[0]

    for number in num_arr:
        if abs(number-value) < abs(min_diff-value):
            min_diff = number

    return min_diff


def closest_value_in_bst(tree, target):
    if not tree:
        return None

    current = tree
    closest_value = tree.value

    while current:

        # We've reached the end of the branch
        if current is None:
            return

        # Check current number distance
        current_distance = abs(current.value - target)
        min_distance = abs(closest_value - target)

        # Update the current closest value
        if current_distance < min_distance:
            closest_value = current.value

        # Navigate right on the tree
        if current.value < target:
            current = current.right

        elif current.value > target:
            current = current.left

        else:  # They're equal, so we found the minimal close value
            break

    return closest_value


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
