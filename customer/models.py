
from email.policy import default

from mongoengine import *

class User(Document):
    email = EmailField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    created_on = DateTimeField()
    published = BooleanField(default=False)

    @queryset_manager
    def objects(cls, queryset):
        return queryset.order_by('-created_on')

    
    @queryset_manager
    def live_posts(cls, queryset):
        return queryset.filter(published=True)

    def __str__(self):
        return self.title


    meta = {}

    meta = {
        'allow_inheritance': True,
        # TODO - Indexes
        'indexes': [
            # 'title',   # single-field index
            '$title',  # text index
            # '#title',  # hashed index
            # ('title', '-rating'),  # compound index
            # ('category', '_cls'),  # compound index
            # {
            #     'fields': ['created'],
            #     'expireAfterSeconds': 3600  # ttl index
            # }
        ]
    }

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()

class BlogPost(Post):
    page_views = IntField(default=0)
    body = StringField()


# TODO - Dynamic Document Schema
# from mongoengine import *

# class Page(DynamicDocument):
#     title = StringField(max_length=200, required=True)

# # Create a new page and add tags
# >>> page = Page(title='Using MongoEngine')
# >>> page.tags = ['mongodb', 'mongoengine']
# >>> page.save()

# >>> Page.objects(tags='mongoengine').count()
# >>> 1

# TODO - Dictionary Fields
# class SurveyResponse(Document):
#     date = DateTimeField()
#     user = ReferenceField(User)
#     answers = DictField()

# survey_response = SurveyResponse(date=datetime.now(), user=request.user)
# response_form = ResponseForm(request.POST)
# survey_response.answers = response_form.cleaned_data()
# survey_response.save()



# TODO - Generic Reference Fields
# class Link(Document):
#     url = StringField()

# class Post(Document):
#     title = StringField()

# class Bookmark(Document):
#     bookmark_object = GenericReferenceField()

# link = Link(url='http://hmarr.com/mongoengine/')
# link.save()

# post = Post(title='Using MongoEngine')
# post.save()

# Bookmark(bookmark_object=link).save()
# Bookmark(bookmark_object=post).save()

# TODO - Server side javascript execution
# def sum_field(document, field_name, include_negatives=True):
#     code = """
#     function(sumField) {
#         var total = 0.0;
#         db[collection].find(query).forEach(function(doc) {
#             var val = doc[sumField];
#             if (val >= 0.0 || options.includeNegatives) {
#                 total += val;
#             }
#         });
#         return total;
#     }
#     """
#     options = {'includeNegatives': include_negatives}
#     return document.objects.exec_js(code, field_name, **options)

# TODO - Filefield ( GridFS )
# https://mongoengine.readthedocs.io/en/v0.9.0/guide/gridfs.html