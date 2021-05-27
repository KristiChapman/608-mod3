class Purchase(object):
    def _init_(self, amount):
        self.amount = amount
        self.tip = tip
        self.tax = tax

def calculateTax(self, taxPercent):
    return self.amount * taxPercent/100.0
    
def calculateTip(self, tipPercent):
    return self.amount * tipPercent/100.0
    
def calculateTotal(self, taxPercent, tipPercent):
    return self.amount * (1 + taxPercent/100.0 + tipPercent/100)
    
# Create Purchase object given an amount
purchase = Purchase(100.0)
# Set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

# Use the object to calculate tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# Display some useful information
print ('Tax: ', tax)
print ('Tip: ', tip)
print ('Total: ', purchase.caculateTotal(taxPercent, tipPercent))