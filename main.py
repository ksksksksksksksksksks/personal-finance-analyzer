import csv
from collections import defaultdict
from pathlib import Path


def load_expenses(file_path):
    expenses = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "date": row["date"],
                "category": row["category"],
                "amount": float(row["amount"])
            })

    return expenses


def analyze_expenses(expenses):
    total = 0
    categories = defaultdict(float)

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]

        total += amount
        categories[category] += amount

    return total, categories


def print_report(total, categories):
    print("\n===== FINANCIAL REPORT =====")

    print(f"\nTotal expenses: {total:,.2f} RUB")

    print("\nExpenses by category:")

    for category, amount in sorted(
        categories.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        percentage = amount / total * 100

        print(
            f"{category}: {amount:,.2f} RUB "
            f"({percentage:.1f}%)"
        )


def main():
    file_path = Path("data/expenses.csv")

    expenses = load_expenses(file_path)

    total, categories = analyze_expenses(expenses)

    print_report(total, categories)


if __name__ == "__main__":
    main()