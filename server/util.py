import pickle
import json
import numpy as np
import pandas as pd

__data_description = None
__model = None
__data_columns = None

def get_classify_credit_score(age, annual_income, monthly_inhand_salary, num_bank_accounts,
       num_credit_card, interest_rate, delay_from_due_date,
       num_of_delayed_payment, changed_credit_limit,
       num_credit_inquiries, credit_mix, outstanding_debt,
       credit_history_age, payment_of_min_amount,
       amount_invested_monthly, monthly_balance
):

    df = pd.DataFrame(np.zeros((1, len(__data_columns))), columns=__data_columns)
    
    df.iloc[0, 0] = age
    df.iloc[0, 1] = annual_income
    df.iloc[0, 2] = monthly_inhand_salary
    df.iloc[0, 3] = num_bank_accounts
    df.iloc[0, 4] = num_credit_card
    df.iloc[0, 5] = interest_rate
    df.iloc[0, 6] = delay_from_due_date
    df.iloc[0, 7] = num_of_delayed_payment
    df.iloc[0, 8] = changed_credit_limit
    df.iloc[0, 9] = num_credit_inquiries
    df.iloc[0, 10] = credit_mix
    df.iloc[0, 11] = outstanding_debt
    df.iloc[0, 12] = credit_history_age
    df.iloc[0, 13] = payment_of_min_amount
    df.iloc[0, 14] = amount_invested_monthly
    df.iloc[0, 15] = monthly_balance

    return __model.predict(df)[0]

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __data_description

    with open("./artifacts/columns.json", "r") as f:
        json1= json.load(f)
        __data_columns=json1['data_columns']
        __data_description = json1['data_description']

    global __model
    if __model is None:
        with open('./artifacts/credit_score_classification_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_data_columns():
    return __data_columns

def get_data_description():
    return __data_description

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_data_description())
    print(get_classify_credit_score(24,19114.12,1824.843333,3,4,3,3,9,13.27,4.0,2.0,809.98,274.0,0.0,21.465380264657146,361.44400385378196))