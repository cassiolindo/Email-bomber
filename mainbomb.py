def main():
    print banner()
    email_user = raw_input('INFORME SEU E-MAIL (GMAIL): ')
    email_pass = raw_input('INFORME SUA SENHA: ')

    validade,conn = test(email_user, email_pass)
    print '[!] CONEXÃO REALIZADA COM SUCESSO!'
    print conn
    if validade == True:
        send_emails(email_user,conn)
    else:
        print conn_error()
        sys.exit
