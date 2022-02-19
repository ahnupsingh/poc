import json
from customer.models import User, TextPost, Post, LinkPost, BlogPost

def serialize(query):
    return json.loads(query.to_json())

def create_user(details):
    # return User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
    return User(**details).save()

def create_post(fields):

    # TODO - Make use of Retrieving unique results
    # a, created = User.objects.get_or_create(name='User A', defaults={'age': 30})
    # b, created = User.objects.get_or_create(name='User A', defaults={'age': 40})
    # user = User.objects[0]
    # post1 = TextPost(title='Fun with MongoEngine', author=user, created_on="2020-10-20")
    # post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    # post1.tags = ['mongodb', 'mongoengine']
    # post1.save()

    return TextPost(**fields).save()

def create_blog(fields):
    return BlogPost(**fields).save()

def list_posts(params):
    posts = Post.objects

    search = params.get("search", "")
    if search:
        posts = posts.search_text(search)
        params.pop("search")

    return posts(**params)

def paginate(posts):
    # TODO - paginate using capability of Limiting and skipping results
    # users = User.objects[:5]
    # # All except for the first 5 people
    # users = User.objects[5:]
    # # 5 users, starting from the 10th user found
    # users = User.objects[10:15]
    pass

def increment_blog_views(blog):
    blog.update_one(inc__page_views=1)
    # blog.reload()
    # post.page_views
    return blog

def set_title(posts):
    posts.update_one(set__title='Example Post')
    posts.reload()
    posts.title

def add_tag_to_post(posts):
    # Push tags
    posts.update_one(push__tags='nosql')
    posts.reload()
    posts.tags

def update_post(post, values):
    updated_post_count = post.update(**values)
    return updated_post_count


def search_post(query):

    # TODO - Make use of query operators - django-filters
    # Page.objects(__raw__={'tags': 'coding'})

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