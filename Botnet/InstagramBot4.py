from instapy import InstaPy

session = InstaPy(username="kraldonaltrump", password="trump1234")
session.login()

session.like_by_tags(["beşiktaş"], amount=2)
session.set_do_follow(True, percentage=50)