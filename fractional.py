class ItemValue:  
    def __init__(self, wt_, val_, ind_):
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        self.cost = val_ // wt_

    def __lt__(self, other):
        return self.cost < other.cost

def fractionalKnapSack(wt, val, capacity):
    iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]
    # Sorting items by cost
    iVal.sort(key=lambda x: x.cost, reverse=True)
    totalValue = 0
    for i in iVal:
        curWt = i.wt
        curVal = i.val
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = int(capacity - (curWt * fraction))
            break
    return totalValue

def main():
    while True:
        print("Menu:")
        print("1. Calculate Maximum Value in Knapsack")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            wt = list(map(int, input("Enter the weights separated by spaces: ").split()))
            val = list(map(int, input("Enter the values separated by spaces: ").split()))
            capacity = int(input("Enter the capacity of the knapsack: "))
            maxValue = fractionalKnapSack(wt, val, capacity)
            print("Maximum value in Knapsack =", maxValue)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
