from flask import Blueprint, render_template, request
from models import bank

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET", "POST"])
def user_panel():
    global current_user
    if request.method == "POST":
        action = request.form.get("action")
        if action == "create_account":
            name = request.form.get("name")
            email = request.form.get("email")
            address = request.form.get("address")
            account_type = request.form.get("account_type")
            current_user = bank.create_account(name, email, address, account_type)
        elif action == "deposit":
            amount = int(request.form.get("amount"))
            message = current_user.deposit(amount)
            return render_template("user.html", message=message)
        elif action == "withdraw":
            amount = int(request.form.get("amount"))
            message = current_user.withdraw(amount)
            return render_template("user.html", message=message)
        elif action == "check_balance":
            balance = current_user.check_balance()
            return render_template("user.html", balance=balance)
        elif action == "transaction_history":
            history = current_user.transaction_history()
            return render_template("user.html", history=history)
        elif action == "take_loan":
            amount = int(request.form.get("amount"))
            message = current_user.take_loan(amount)
            return render_template("user.html", message=message)
        elif action == "transfer":
            amount = int(request.form.get("amount"))
            recipient_account_number = int(request.form.get("recipient_account_number"))
            recipient = None
            for user in bank.users:
                if user.account_number == recipient_account_number:
                    recipient = user
                    break
            if recipient:
                message = current_user.transfer(amount, recipient)
            else:
                message = "Recipient not found."
            return render_template("user.html", message=message)
    return render_template("user.html")
