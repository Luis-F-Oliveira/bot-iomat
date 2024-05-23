import json
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:
  def __init__(self):
    self.data = json.load(open('json/savedData.json', 'r', encoding='utf-8'))
    self.servers = json.load(open('json/servers.json', 'r', encoding='utf-8'))
    self.blacklist = json.load(open('json/blacklist.json', 'r', encoding='utf-8'))
  
  def send(self):
    emails = []
    banned_names = self.blacklist[0]['bannedNames']
    load_dotenv()

    for item in self.data:
      for name in item['names']:
        for person in self.servers:
          if name.lower() in person['Servidor'].lower():
            if name.lower() not in [n.lower() for n in banned_names]:
              emails.append({
                'name': person['Servidor'], 
                'email': person['EMAIL'],
                'url': item['url'],
                'order': item['order']
              })
              break

    email = os.getenv("EMAIL")
    password = os.getenv("APP_PASSWORD")

    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = email
    smtp_password =  password
    
    for items in emails:
      message = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Document</title>
        </head>
        <body>
          <div>
            <header style="background-image: linear-gradient(to right, #15e431, #062400);">
              <h1 style="margin-left: 20px; color: #fff;">
                Facilita Diário
              </h1>
            </header>
            <main>
              <p>
                Prezado(a), 
                <span style="background-color: #00ff2238; padding: 4px 6px; color: #000;">
                  <strong style="text-transform: capitalize;">{items['name']}.</strong>
                </span>
              </p>
              <p>
                Essa mensagem foi produzida pelo serviço "FACILITA DIÁRIO" da DIRETORIA DE GESTÃO DE PESSOAS. <br>
                Para mais informações sobre o serviço, entre em contato documentosgestaodepessoas@dp.mt.gov.br.
              </p>
              <div style="margin-top: 35px;">
                <h1 style="font-size: medium;">
                  {items['order']}
                </h1>
                <a href="{items['url']}">
                  {items['url']}
                </a>
              </div>
            </main>
            <footer style="margin-top: 50px;">
              <p>
                Este serviço é um projeto experimental da Diretoria de Gestão de Pessoas com o objetivo facilitar o 
                acompanhamento de publicações da Defensoria Pública pelos seus servidores, não substituindo, de qualquer 
                forma, a obrigação de acompanhamento do Diário Oficial diretamente dos sistemas do IOMAT.
              </p>
              <p>
                Destacamos que o acompanhamento somente compreende as publicações da Defensoria Pública do Estado de Mato Grosso.
              </p>
              <p>
                Se estiver enfrentando algum problema, perceber a falha na captura de informações ou deseja parar de receber os alertas, favor informar 
                pelo e-mail: documentosgestaodepessoas@dp.mt.gov.br
              </p>
            </footer>
          </div>
        </body>
        </html>
      """

      msg = MIMEMultipart()
      msg['From'] = email
      msg['To'] = items['email']
      msg['Subject'] = f'Facilita Diário - {items["name"]}'
      msg.attach(MIMEText(message, 'html'))

      server = smtplib.SMTP(smtp_host, smtp_port)
      server.starttls()
      server.login(smtp_user, smtp_password)
      server.sendmail(email, items['email'], msg.as_string())
      server.quit()
      print(f'Email enviado para: {items["email"]}')