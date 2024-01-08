import logging
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .main import bot
import telebot
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def sendmail(subject="obhovo",message="toshkentda obhovo", from_email='saidakrom12345678@gmail.com', recipient_list=['mamajonovibrokhimjon@gmail.com']):
    return HttpResponse("Sended")

def main(request):
    return HttpResponse("siz kirdingiz ")

@csrf_exempt
def bot(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse("Telegram Bot")
    if request.method == 'POST':
        update = telebot.types.Update.de_json(
            request.body.decode("utf-8"))
        try:
            bot.process_new_updates([update])
        except Exception as e:
            logging.error(e)
        return HttpResponse(status=200)