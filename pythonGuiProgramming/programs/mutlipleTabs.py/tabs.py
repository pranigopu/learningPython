# Importing other files...
from alwaysImportMe import *
from  covidVaccineDriveRegistration import *
from loanEligibility import *

# Reassignment is done just for conceptual clarity
cvdrTab = cvdrRoot
leTab = leRoot

tabControl.add(cvdrTab, text = 'COVID vaccine drive registration')
tabControl.add(leTab, text = 'Loan eligibility')
tabControl.pack(expand = 1, fill ="both")

root.mainloop()  