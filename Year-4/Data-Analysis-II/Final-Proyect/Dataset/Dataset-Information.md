Dataset Information
Additional Information
The data is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required to assess if the product (bank term deposit) would be subscribed ('yes') or not ('no').
Classification Goal
The goal is to predict if the client will subscribe (yes/no) to a term deposit (variable y).
Bank Client Data:
    1. age (numeric)
    2. job : Type of job (categorical:
"admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services")
    3. marital : Marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
    4. education (categorical: "unknown","secondary","primary","tertiary")
    5. default: Has credit in default? (binary: "yes","no")
    6. balance: Average yearly balance, in euros (numeric)
    7. housing: Has housing loan? (binary: "yes","no")
    8. loan: Has personal loan? (binary: "yes","no")
Related with the Last Contact of the Current Campaign:
    1. contact: Contact communication type (categorical: "unknown","telephone","cellular")
    2. day: Last contact day of the month (numeric)
    3. month: Last contact month of the year (categorical: "jan", "feb", "mar", …, "nov", "dec")
    4. duration: Last contact duration, in seconds (numeric)
Other Attributes:
    1. campaign: Number of contacts performed during this campaign and for this client (numeric, includes last contact)
    2. pdays: Number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means the client was not previously contacted)
    3. previous: Number of contacts performed before this campaign and for this client (numeric)
    4. poutcome: Outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")
Output Variable (Desired Target):
    1. y - Has the client subscribed to a term deposit? (binary: "yes","no")
