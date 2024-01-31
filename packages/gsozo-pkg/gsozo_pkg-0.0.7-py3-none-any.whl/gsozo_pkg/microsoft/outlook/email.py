import win32com.client as win32
import pythoncom
from jinja2 import Template

def build_template(template_path, opts={}):
    with open(template_path, "r", encoding='utf8') as f:
        template = Template(f.read())

    return template.render(**opts)


def sender(template_path, sender, to, cc, subject, body_template_opts, send=False):
    """
    Send e-mail using outlook app
    NOTE: if you want to use de default account instead of select, leave 'sender' empty string ""

    Example
    -------
    sender_outlook(
        'my_template.html', #Under template folder
        'my_email@tosend.com.br' # Required
        'to@email1.com;to@email2.com',
        '', #To not use CC leave as empty string
        'Investor reminder – DARF collection',
        {},
        False,
    )
    """

    pythoncom.CoInitialize()

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = to
    mail.CC = cc
    mail.Subject = subject
    mail.HTMLBody = build_template(template_path, body_template_opts)

    for acc in outlook.Session.Accounts:
        if acc.SmtpAddress == sender:
            from_acc = acc

    # mail_item.SendUsingAccount = send_account not working
    # the following statement performs the function instead
    mail._oleobj_.Invoke(*(64209, 0, 8, 0, from_acc))

    if send:
        mail.Send()
    else:
        mail.Display()
