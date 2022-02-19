from customer.models import User, TextPost, Post, LinkPost, BlogPost

def create_user():
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()

def create_post(user):

    # TODO - Make use of Retrieving unique results
    # a, created = User.objects.get_or_create(name='User A', defaults={'age': 30})
    # b, created = User.objects.get_or_create(name='User A', defaults={'age': 40})
    user = User.objects[0]
    post1 = TextPost(title='Fun with MongoEngine', author=user, created_on="2020-10-20")
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

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