from Selenium.POM_Registration.test_bee_registration import browser_types
import csv


registered_users_TD = []

with open("../Test_Data/registered_users.csv", "r", newline="", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    header = next(csv_reader)  # Az első sort beolvassa, ha van fejléc
    for row in csv_reader:
        registered_users_TD.append(row)  # Minden sort kiír a terminálra


test_data = []
test_pieces = ""

for i in range(len(registered_users_TD)-1):
    test_pieces += "data_first_name: "+str(registered_users_TD[i][0]+"\n ")
    test_pieces += "data_last_name:  "+str(registered_users_TD[i][1]+"\n ")
    test_pieces += "data_phone:      "+str(registered_users_TD[i][2]+"\n ")
    test_pieces += "data_email:      "+str(registered_users_TD[i][3]+"\n ")
    test_pieces += "data_zip_code:   "+str(registered_users_TD[i][4]+"\n ")
    test_pieces += "data_city:       "+str(registered_users_TD[i][5]+"\n ")
    test_pieces += "data_password:   "+str(registered_users_TD[i][6]+"\n ")
    test_pieces += "data_address:    "+str(registered_users_TD[i][7]+"\n ;")
    test_data = test_pieces.split(";")

header = [
    "Key", "Name", "Status", "Precondition", "Objective", "Folder",
    "Priority", "Component", "Labels", "Owner", "Estimated Time",
    "Coverage (Issues)", "Coverage (Pages)",
    "Test Script (Step-by-Step) - Step",
    "Test Script (Step-by-Step) - Test Data",
    "Test Script (Step-by-Step) - Expected Result",
    "Test Script (Plain Text)", "Test Script (BDD)"
]
test_cases_keys = ["TE24SEPHOT-T1","TE24SEPHOT-T2","TE24SEPHOT-T3","TE24SEPHOT-T4"]

test_cases = []
for browser in range(len(browser_types)):
    for i in range(len(test_data)):
        precon ="Being able to access the website in:" + browser_types[browser]
        test_case = {
            "Key": "TE24SEPHOT-T"+str(i+1),
            "Name": "Automated Registration in "+browser_types[browser]+" "+str(i+1),
            "Status": "Approved",
            "Precondition": precon,
            "Objective": "testing various characters that names could have",
            "Folder": "/Automation",
            "Priority": "Normal",
            "Component": "",
            "Labels": "Automation",
            "Owner": "JIRAUSER12148",
            "Estimated Time": "00:01",
            "Coverage (Issues)": "",
            "Coverage (Pages)": "",
            "Test Script (Step-by-Step) - Step": "Enter the test data in "+ browser_types[browser],
            "Test Script (Step-by-Step) - Test Data": test_data[i],
            "Test Script (Step-by-Step) - Expected Result": "Succesfull registration.",
            "Test Script (Plain Text)": "",
            "Test Script (BDD)": ""
        }
        test_cases.append(test_case)
with open("jira_import.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(header)
    for test in test_cases:
        row = []
        for field in header:
            value = test.get(field, "")
            row.append(value)
        csv_writer.writerow(row)

print("Done")