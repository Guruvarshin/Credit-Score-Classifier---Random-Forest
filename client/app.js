$(document).ready(function() {
    $.get("/api/proxy/get_data_description", function(data) {
        if(data && data.data_columns_description) {
            const list = $("#descriptionList");
            list.empty();
            const columns = ["Age", "Annual_Income", "Monthly_Inhand_Salary", "Num_Bank_Accounts", "Num_Credit_Card", "Interest_Rate", "Delay_from_due_date", "Num_of_Delayed_Payment", "Changed_Credit_Limit", "Num_Credit_Inquiries", "Credit_Mix", "Outstanding_Debt", "Credit_History_Age", "Payment_of_Min_Amount", "Amount_invested_monthly", "Monthly_Balance"];
            
            columns.forEach((col, index) => {
                list.append(`
                    <div class="group">
                        <span class="text-sky-400 font-bold block group-hover:text-sky-300 transition-colors">${col.replace(/_/g, ' ')}</span>
                        <span class="text-slate-500 group-hover:text-slate-400">${data.data_columns_description[index]}</span>
                    </div>
                `);
            });
        }
    });
});

function predictScore() {
    const resText = $("#resultText");
    const badge = $("#badge");
    
    resText.text("...").removeClass("text-emerald-400 text-rose-400 text-amber-400 text-slate-800 scale-110");
    badge.text("Processing...").removeClass("bg-emerald-500/10 text-emerald-400 bg-rose-500/10 text-rose-400 bg-amber-500/10 text-amber-400 border-emerald-500/20");

    const payload = {
        age: parseFloat($("#Age").val()),
        annual_income: parseFloat($("#Annual_Income").val()),
        monthly_inhand_salary: parseFloat($("#Monthly_Inhand_Salary").val()),
        num_bank_accounts: parseFloat($("#Num_Bank_Accounts").val()),
        num_credit_card: parseFloat($("#Num_Credit_Card").val()),
        interest_rate: parseFloat($("#Interest_Rate").val()),
        delay_from_due_date: parseFloat($("#Delay_from_due_date").val()),
        num_of_delayed_payment: parseFloat($("#Num_of_Delayed_Payment").val()),
        changed_credit_limit: parseFloat($("#Changed_Credit_Limit").val()),
        num_credit_inquiries: parseFloat($("#Num_Credit_Inquiries").val()),
        credit_mix: parseFloat($("#Credit_Mix").val()),
        outstanding_debt: parseFloat($("#Outstanding_Debt").val()),
        credit_history_age: parseFloat($("#Credit_History_Age").val()),
        payment_of_min_amount: parseFloat($("#Payment_of_Min_Amount").val()),
        amount_invested_monthly: parseFloat($("#Amount_invested_monthly").val()),
        monthly_balance: parseFloat($("#Monthly_Balance").val())
    };

    $.post("/api/proxy/classify_credit_score", payload, function(data) {
        const score = data.credit_score;
        resText.text(score).addClass("scale-110");
        
        if(score === "Good") {
            resText.addClass("text-emerald-400");
            badge.text("Low Risk Profile").addClass("bg-emerald-500/10 text-emerald-400 border-emerald-500/20");
        } else if(score === "Standard") {
            resText.addClass("text-amber-400");
            badge.text("Moderate Risk Profile").addClass("bg-amber-500/10 text-amber-400 border-amber-500/20");
        } else {
            resText.addClass("text-rose-400");
            badge.text("High Risk Profile").addClass("bg-rose-500/10 text-rose-400 border-rose-500/20");
        }
    });
}