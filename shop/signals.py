


# def set_username(sender,instance, **kwargs):
#     if not instance.username:
#         username = instance.email.split('@')[0]
#         counter = 1
#         while Employee.objects.filter(username=username):
#             username = instance.email.split('@')[0] + str(counter)
#             counter+=1
#         instance.username = username
# models.signals.pre_save.connect(set_username, sender=Employee)