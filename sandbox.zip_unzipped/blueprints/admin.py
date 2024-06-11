from flask import Blueprint, render_template, request
from models import Bank, Admin

admin_bp = Blueprint('admin', __name__)
admin = Admin()
bank = Bank("Example Bank")

@admin_bp.route('/', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create_account':
            name = request.form.get('name')
            email = request.form.get('email')
            address = request.form.get('address')
            account_type = request.form.get('account_type')
            admin.create_account(bank, name, email, address, account_type)
        elif action == 'delete_account':
            account_number = int(request.form.get('account_number'))
            admin.delete_account(bank, account_number)
        elif action == 'get_all_accounts':
            accounts = admin.get_all_accounts(bank)
            return render_template('admin.html', accounts=accounts)
        elif action == 'get_total_balance':
            total_balance = admin.get_total_balance(bank)
            return render_template('admin.html', total_balance=total_balance)
        elif action == 'get_total_loan_amount':
            total_loan_amount = admin.get_total_loan_amount(bank)
            return render_template('admin.html', total_loan_amount=total_loan_amount)
        elif action == 'on_loan_feature':
            bank.on_loan_feature()
        elif action == 'off_loan_feature':
            bank.off_loan_feature()
    return render_template('admin.html')