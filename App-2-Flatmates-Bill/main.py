class Bill:
    """
    Creates a bill object
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate object 
    which will be used to split the bill proportionally
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / \
            (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a Pdf file that contains flatmate data(name, due amount for period)
    and the period of bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill = Bill(amount=120, period="March 2022")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

john_pay = john.pays(bill, marry)
marry_pay = marry.pays(bill, john)

print(f'John pays: {john_pay}')
print(f'Marry pays: {marry_pay}')
print(f'Total: {marry_pay+john_pay}')
