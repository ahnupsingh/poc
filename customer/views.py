from customer.helpers import get_request_body, get_request_params

from customer.models import User, TextPost, Post, LinkPost, BlogPost, Comment
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


class CommentView(View):

    def get(self, request, pk):
        post = Post.objects(id=pk)[0]
        comments = post.comments
        return JsonResponse({"posts": serialize(comments)})

    def post(self, request, pk):
        details = get_request_body(request)
        post = Post.objects(id=pk)[0]
        comment = Comment(**details)

        from customer.methods import add_comment
        new_post = add_comment(post, comment)

        return JsonResponse(serialize(new_post))

# TODO - Transactions