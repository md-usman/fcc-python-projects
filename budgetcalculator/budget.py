class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0.0
        self.spent = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        hasEnoughBalance = self.check_funds(amount)
        if hasEnoughBalance:
            self.ledger.append({"amount": amount * -1, "description": description})
            self.spent += amount
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, transfer_category=""):
        hasEnoughBalance = self.check_funds(amount)

        if hasEnoughBalance:
            self.balance -= amount
            self.spent += amount
            self.ledger.append({"amount": amount * -1, "description": f"Transfer to {transfer_category.category}"})
            transfer_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        numStars = (30 - len(self.category)) // 2
        firstLine = "*" * numStars + self.category + "*" * numStars
        for i in self.ledger:
            firstLine += "\n"
            length = len(i["description"])
            if length >= 23:
                appendSpaces = 0
            else:
                appendSpaces = 23 - length

            amountLength = len("{:.2f}".format(i["amount"]))
            if amountLength > 7:
                printAmount = "{:.2f}".format(i["amount"])[0:7]
            else:
                printAmount = " " * (7 - amountLength) + "{:.2f}".format(i["amount"])

            firstLine += i["description"][0:23] + " " * appendSpaces + printAmount
        firstLine += "\nTotal: " + str(self.get_balance())

        return firstLine


def create_spend_chart(categories):
    length = len(categories)
    totalWidth = 5 + length * 3
    string1 = "Percentage spent by category\n"
    totalSpent = 0

    for i in categories:
        totalSpent += i.spent

    percent = 100
    while percent >= 0:
        numSpace = 3 - len(str(percent))
        string1 += " " * numSpace + str(percent) + "| "
        for i in categories:
            spentPercent = ((i.spent / totalSpent * 100) // 10) * 10
            string1 += ("o" if spentPercent >= percent else " ") + "  "
        string1 += "\n"
        percent -= 10

    string1 += "    " + "-" * (totalWidth - 4) + "\n"

    catNames = []
    maxLen = 0
    for i in categories:
        catNames.append(i.category)
        if len(i.category) > maxLen:
            maxLen = len(i.category)

    for i in range(maxLen):
        string1 += "     "
        for j in catNames:
            string1 += (j[i] if (len(j) - 1) >= i else " ") + "  "

        if i < maxLen - 1:
            string1 += "\n"

    return string1

