def main():
    principal = 1000
    rate = 0.05
    time = 5
    n = 4
    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal
    print("Compound interest:", compound_interest)

if __name__ == "__main__":
    main()
