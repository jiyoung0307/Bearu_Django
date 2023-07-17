from django.db import models
from user.models import User

class Post(models.Model):
    # 내가 pk를 설정할게
    # id=models.AutoField(primary_key=True)

    # 해당 글을 작성한 user가 삭제가 되도 글은 그대로 남길게
    # 누가 썼는지는 알 수 없으니 null로 설정할게
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   # user_id ()
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 글을 작성하면 그 시간을 저장할게
    reg_date = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(null=True)

    class Meta:
        # 만약 테이블 이름을 지정하지 않으면 add_model (ex: board_post)
        db_table="post"

class Comment(models.Model):
    # 해당 글을 지우면 그 댓글도 지울래
     # 해당 글을 지우면 그 댓글도 지울래
      # 해당 글을 지우면 그 댓글도 지울래
      
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   # post_id = 1
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comment"