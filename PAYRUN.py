from PAYROLL2 import Payroll
# emp1=input('enter name:')
emp1=Payroll(100000,10000,20)


print("NAME:               Wendy")
print("GROSS SALARY :      "+str(emp1.gross_salary))
print("NSSF :              "+str(emp1.nssf_deductions))
print("TAXABLE INCOME:     "+str(emp1.taxable_income))
print("PAYE :              "+str(emp1.payee))
print("NHIF :              "+str(emp1.nhif_deductions))
print("TOTAL DEDUCTIONS :  "+str(emp1.total_deductions))
print("NET SALARY :        "+str(emp1.net_salary))
