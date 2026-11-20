import smtplib
import datetime as dt
import random
my_email = "chiswaswar@gmail.com"
receiver_email = "esthersitangaika@gmail.com"
my_password = "zvmwarqodfehqhal"
now = dt.datetime.now()
weekday = now.weekday()
if weekday==3:
    with open("quote.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote=random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=f"Subject:Be Motivated!\n\n{quote}".encode("utf-8")
                            )