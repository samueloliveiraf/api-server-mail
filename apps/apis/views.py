from django.core.mail import EmailMultiAlternatives

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import parsers
from rest_framework import status


class SendEmailAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    parser_classes = (parsers.JSONParser,)

    def post(self, request, *args, **kwargs):
        json_email = request.data
        try:
            send_email(
                json_email['subject'],
                json_email['image'],
                json_email['email_from'],
                json_email['emails_destiny'],
                json_email['color'],
                json_email['body']
            )
            return Response(json_email, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f'Error {e}', status=status.HTTP_400_BAD_REQUEST)


def send_email(subject, image, email_from, emails_destiny, color, body):
    if ',' in emails_destiny:
        recipients = [r.strip() for r in emails_destiny.split(',')]
    else:
        recipients = [emails_destiny]

    subject, from_email, recipients = subject, email_from, recipients
    text_content = 'Email recebido'
    html_content = body_email(image, color, body)

    msg = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def body_email(image, color, body):
    dict_color = {
        'azul': '#303f9f',
        'vermelho': '#b71c1c',
        'verde': '#388e3c'
    }

    conteudo = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>App Cuca</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins" rel="stylesheet">
    </head>
    <title>E-mail cuca</title>
    <body>
        <div class="container" style="background-color: {dict_color[f'{color}']}; height: 680; border-radius: 26px; padding: 20px">
            <center>
                <div>
                    <img style="border-radius: 26px;" height="120" src="{image}" alt="logo">
                </div>
                <h3 style="color: white;">
                    {body}
                </h3>

            </center>
        </div>
    </body>
    </html>
    '''

    return conteudo
