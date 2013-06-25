#coding=utf-8
from uliweb import expose, functions

def post_save(sender, instance, created, data, old_data):
    """
    用来处理教程某个章节被评论时发送消息通知的处理
    """
    from uliweb import request
    from uliweb.utils.textconvert import text2html
    
    authors = instance.chapter.tutorial.authors.ids()
    if request.user.id in authors:
        authors.remove(request.user.id)
    
    message = u"""<p>%s 评论了教程 《<a href="/tutorial/view_chapter/%d">%s</a>》</p>
%s
""" % (unicode(instance.modified_user), instance._chapter_, unicode(instance.chapter),
    text2html(instance.content))
    functions.send_message(request.user, authors, message, type='2')
    
    users = [x.id for x in functions.parse_user(instance.content)]
    diff = set(users) - set(authors)
    message = u"""<p>%s 评论教程 《<a href="/tutorial/view_chapter/%d">%s</a>》时提到了你</p>
%s
""" % (unicode(instance.modified_user), instance._chapter_, unicode(instance.chapter),
    text2html(instance.content))
    functions.send_message(request.user, list(diff), message, type='2')
    
import re
re_at = re.compile(u'@[a-zA-Z0-9_\u4E00-\u9FFF\.]+')
def forumpost_post_save(sender, instance, created, data, old_data):
    """
    处理论坛发贴时当有@用户时发送消息进行通知
    """
    from uliweb.orm import get_model
    from uliweb import request
    
    User = get_model('user')
    
    message = u"""用户 %s 在论坛提到了你，查看: <a href="/id/%d">%s</a>""" % (unicode(instance.posted_by), instance.id, unicode(instance.topic.subject))
    for user in functions.parse_user(instance.content):
        functions.send_message(instance.posted_by, user, message, type='2')
