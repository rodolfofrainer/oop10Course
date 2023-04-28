from fpdf import FPDF


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
    Creates a Pdf file that contains flatmate data(
        name, due amount for period
    )
    and the period of bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # Creates totals for each flatmate
        flatmate1_pay = round(flatmate1.pays(bill, flatmate2), 2)
        flatmate2_pay = round(flatmate2.pays(bill, flatmate1), 2)

        # Creates pdf object
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image('files/house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(
            w=0, h=80, txt='Flatmate Bill', align='C', ln=1
        )

        # Insert period label and values
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=200, h=40, txt=f'Period: {bill.period}', ln=1)

        # Flatmate1
        pdf.set_font(family='Times', size=16)
        pdf.cell(
            w=175, h=40,
            txt=f'{flatmate1.name}: {flatmate1_pay}',
            ln=1
        )

        # Flatmate2
        pdf.cell(
            w=175, h=40,
            txt=f'{flatmate2.name}: {flatmate2_pay}',
            ln=1
        )

        # Period total
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(
            w=175, h=40,
            txt=f'Total: {round(float(bill.amount), 2)}',
            ln=1
        )

        # Saves pdf
        pdf.output(f"{self.filename}.pdf")


bill = Bill(amount=120, period="September 2022")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

john_pay = john.pays(bill, marry)
marry_pay = marry.pays(bill, john)

pdf = PdfReport(filename='Report1')
pdf.generate(flatmate1=john, flatmate2=marry, bill=bill)
