# from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
# from django.contrib.auth.models import User
# from django.dispatch import receiver,Signal


# notification=Signal(providing_args=['request','user'])

# @receiver(notification)
# def notification_msg(sender,**kwargs):
#     print('custom signal run')


# @receiver(user_logged_in)
# def login_success(sender, request, user ,**kwargs):
#     print('yes signal is working')


# @receiver(user_logged_out)
# def login_logout(sender, request, user ,**kwargs):
#     print('yes logout signal is working')


# @receiver(user_login_failed)
# def login_failed(sender, request, user ,**kwargs):
#     print('yes failed signal is working')
# # user_logged_in.connect(login_success,sender=User)
