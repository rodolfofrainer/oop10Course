from flat_info import Bill, Flatmate
from report_generation import PdfReport


bill_total = float(input('Bill amount: '))
bill_period = input('Bill period: ')

flatmate1_name = input('First flatmate name: ')
flatmate1_period = int(
    input(f'Amount of days {flatmate1_name.title()} stayed in house: '))

flatmate2_name = input('Second flatmate name: ')
flatmate2_period = int(
    input(f'Amount of days {flatmate2_name.title()} stayed in house: '))

the_bill = Bill(amount=bill_total, period=bill_period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_period)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_period)

pdf = PdfReport(filename=f'{the_bill.period}')
pdf.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
