from customer.helpers import get_request_body, get_request_params

from customer.models import User, TextPost, Post, LinkPost, BlogPost
from customer.methods import serialize


from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from customer.seriallizers import UserSerializer

class UserDetailView(View):
    def get(self, request, pk):
        user = User.objects(id=pk)
        return JsonResponse({"users": serialize(user)})

    @csrf_exempt
    def put(self, request):
        pass
class UserView(View):
    def get(self, request):
        users = User.objects
        return JsonResponse({"users": serialize(users)})

    @csrf_exempt
    def post(self, request):
        # TODO - Get or Create
        from customer.methods import create_user
        details = get_request_body(request)
        new_user = create_user(details)
        return JsonResponse(serialize(new_user))

class PostView(View):

    def get(self, request):
        posts = Post.objects
        params = get_request_params(request)
        from customer.methods import list_posts
        posts = list_posts(params)
        return JsonResponse({"posts": serialize(posts)})

    def post(self, request):
        details = get_request_body(request)
        user_id = details.pop("user")
        details["author"] = User.objects(id=user_id)[0]

        from customer.methods import create_post, create_blog
        new_post = create_blog(details)

        return JsonResponse(serialize(new_post))

    
    def put(self, request):
        details = get_request_body(request)
        id = details.pop("id")
        post = BlogPost.objects(id=id)

        from customer.methods import increment_blog_views
        blog = increment_blog_views(post)

        return JsonResponse({"view_count": serialize(blog)})

class PostDetailView(View):
    def get(self, request, pk):
        try:
            post = Post.objects(id=pk)[0]
        except:
            return JsonResponse({"remarks": "Cannot find post."})
        return JsonResponse(serialize(post))

    def put(self, request, pk):
        details = get_request_body(request)
        post = Post.objects(id=pk)[0]

        from customer.methods import update_post
        post_count = update_post(post, details)

        return JsonResponse({"remarks": f"{post_count} post updated"})

    
    def delete(self, request, pk):
        post = Post.objects(id=pk)
        try:
            post.delete()
        except:
            return JsonResponse({"remarks": "Unable to Delete"})
        return JsonResponse({"remarks": "Deleted successfully."})

def list_posts():
    for post in Post.objects:
        print(post.title)
    
    # TODO - paginate using capability of Limiting and skipping results
        # users = User.objects[:5]
        # # All except for the first 5 people
        # users = User.objects[5:]
        # # 5 users, starting from the 10th user found
        # users = User.objects[10:15]

    # TODO - Serialize objects
    # [<LinkPost: LinkPost object>, <TextPost: TextPost object>]
    return Post.objects


def update_post(id):
    # TODO - Atomic updates
    post = BlogPost.objects(id=post.id)
    post.update_one(inc__page_views=1)
    post.reload()  # the document has been changed, so we need to reload it
    post.page_views

    # Set title
    BlogPost.objects(id=post.id).update_one(set__title='Example Post')
    post.reload()
    post.title

    # Push tags
    BlogPost.objects(id=post.id).update_one(push__tags='nosql')
    post.reload()
    post.tags


def search_post(query):

    # TODO - Make use of query operators - django-filters
    # Page.objects(__raw__={'tags': 'coding'})

    # TODO - Here we are looping through all documents
    for post in Post.objects:
        print(post.title)
        print('=' * len(post.title))

        if isinstance(post, TextPost):
            print(post.content)
        
        print

        if isinstance(post, LinkPost):
            print('Link:', post.link_url)

        print

def search_post_by_tag(tag):
    posts = Post.objects(tags='mongodb')
    for post in posts:
        print(post.title)
    print('Found %d posts with tag "mongodb"' % posts.count())


def delete_post(id):
    return Post.objects(id=id).delete()

# TODO - Text Search
# document = News.objects.search_text('testing').first()