from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import util

app = FastAPI()

# Handling CORS (Access-Control-Allow-Origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/get_data_columns')
def get_data_columns():
    # FastAPI automatically converts dicts to JSON
    return {
        'data_columns': util.get_data_columns()
    }

@app.get('/get_data_description')
def get_data_description():
    # FastAPI automatically converts dicts to JSON
    return {
        'data_columns_description': util.get_data_description()
    }
    
@app.post('/classify_credit_score')
def classify_credit_score(
    age:int = Form(...), 
    annual_income:float = Form(...), 
    monthly_inhand_salary:float = Form(...), 
    num_bank_accounts:int = Form(...),
    num_credit_card:int = Form(...), 
    interest_rate:float = Form(...), 
    delay_from_due_date:float = Form(...),
    num_of_delayed_payment:float = Form(...),
    changed_credit_limit:float = Form(...),
    num_credit_inquiries:float = Form(...),
    credit_mix:int = Form(...), 
    outstanding_debt:float = Form(...),
    credit_history_age:int = Form(...), 
    payment_of_min_amount:int = Form(...),
    amount_invested_monthly:float = Form(...), 
    monthly_balance:float = Form(...)
):
    credit_score = util.get_classify_credit_score(age, annual_income, monthly_inhand_salary, num_bank_accounts,
       num_credit_card, interest_rate, delay_from_due_date,
       num_of_delayed_payment, changed_credit_limit,
       num_credit_inquiries, credit_mix, outstanding_debt,
       credit_history_age, payment_of_min_amount,
       amount_invested_monthly, monthly_balance)
    label_map = {
    0: 'Poor',
    1: 'Standard',
    2: 'Good'
    }
    return {
        'credit_score': label_map[credit_score]
    }

if __name__ == "__main__":
    import uvicorn
    print("Starting Python FastAPI Server For Home Price Prediction...")
    util.load_saved_artifacts()
    # FastAPI usually runs via uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)