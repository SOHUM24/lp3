def knapsack_dp(W, wt, val, n):

    K = [[0 for x in range(W + 1)] for x in range(n + 1)]


    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

def main():
    while True:
        print("0-1 Knapsack Problem Solver")
        print("1. Calculate maximum profit for a custom set of items")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter the number of items: "))
            val = list(map(int, input("Enter the values of items separated by spaces: ").split()))
            wt = list(map(int, input("Enter the weights of items separated by spaces: ").split()))
            W = int(input("Enter the knapsack capacity: "))

            if len(val) != n or len(wt) != n:
                print("Error: Number of values and weights must match the number of items.")
                continue

            print("Maximum possible profit =", knapsack_dp(W, wt, val, n))

        elif choice == 2:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
