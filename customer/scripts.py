from customer.models import *
Post.objects[0].update(**{'set__comments__$__name': "An"})