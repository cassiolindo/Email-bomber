def test(email_user, email_pass):
    try:
        conn = s.SMTP('smtp.gmail.com', 587)
        conn.starttls()
        conn.ehlo
        conn.login(email_user, email_pass)
        return True,conn

    except:
        print conn_error()
