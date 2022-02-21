
# TODO - Authentication 

# # from mongoengine.django.auth import User
# from django.model.exceptions import DoesNotExist

# def login_required(func, request, *args, **kwargs):
#     def wrap(func, request, *args, **kwargs):
#         try:
#             user = User.objects.get(username='bob')#request.POST['username'])
#             if user.check_password('bobpass'):#request.POST['password']):
#                 user.backend = 'mongoengine.django.auth.MongoEngineBackend'
#                 request.session.set_expiry(60 * 60 * 1) # 1 hour timeout
#                 return func(request, *args, **kwargs)
#             else:
#                 print("malament")
#                 raise 
#         except DoesNotExist as e:
#             raise e
#     return wrap(func, request, *args, **kwargs)
