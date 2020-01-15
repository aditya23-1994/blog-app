from django import template
from markdown import markdown

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.published.count()
def get_most_commmented_posts(count=5):
    return Post.published.annonate(total_comments=count('comments')).order_by('-total_comments')

@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_posts(count=5):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post':latest_post}

@register.filter(name='markdown')
def markdown_format(text):
    return (markdown(text))
