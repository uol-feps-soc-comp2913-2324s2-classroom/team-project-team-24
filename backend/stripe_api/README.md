# Stripe
To test stripe payment locally you need to setup the listener
## Running test
1. Run `./stripe.exe login`
2. Press 'enter' and log into my strip account:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Email: sc22lacb@leeds.ac.uk  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pwd: Team24-SEP
3. Click 'Allow'
4. Run `./stripe.exe listen --forward-to 127.0.0.1:5001/webhook`
5. Make sure the secret key displayed is the same one as in the top of `memberships.py` in the `WEBHOOK_SECRET` variable.

