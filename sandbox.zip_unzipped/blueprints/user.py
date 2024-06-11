from flask import Blueprint, render_template, request
from models import Bank, Account

user_bp = Blueprint("user", __name__)
bank = Bank("Example Bank")


@user_bp.route("/", methods=["GET", "POST"])
def user_panel():
    message = None
    balance = None
    history = None

    if request.method == "POST":
        action = request.form.get("action")
        account_number = int(request.form.get("account_number"))
        account = next(
            (user for user in bank.users if user.account_number == account_number), None
        )

        if account:
            if action == "create_account":
                name = request.form.get("name")
                email = request.form.get("email")
                address = request.form.get("address")
                account_type = request.form.get("account_type")
                account = Account(name, email, address, account_type)
                bank.create_account(name, email, address, account_type)
                message = "Account created successfully."
            elif action == "deposit":
                amount = float(request.form.get("amount"))
                message = account.deposit(amount)
            elif action == "withdraw":
                amount = float(request.form.get("amount"))
                message = account.withdraw(amount)
            elif action == "check_balance":
                balance = account.check_balance()
            elif action == "transaction_history":
                history = account.transaction_history()
            elif action == "take_loan":
                amount = float(request.form.get("amount"))
                message = account.take_loan(amount)
            elif action == "transfer":
                amount = float(request.form.get("amount"))
                recipient_account_number = int(
                    request.form.get("recipient_account_number")
                )
                recipient = next(
                    (
                        user
                        for user in bank.users
                        if user.account_number == recipient_account_number
                    ),
                    None,
                )
                if recipient:
                    message = account.transfer(amount, recipient)
                else:
                    message = "Recipient account not found."
        else:
            message = "Account not found."

    return render_template(
        "user.html", message=message, balance=balance, history=history
    )
