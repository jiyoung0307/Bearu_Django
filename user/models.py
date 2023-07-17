from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# AbstractUser
# - django 기본 유저 모델
# (이것저것 많이 포함되어있음, 각종 필드, 각종 함수(유저생성, 유저인증 등등))


class User(AbstractUser):
    nickname = models.CharField(max_length=30)

    class Meta:
        db_table="user"

# AbstractBaseUser
# - django 최소 유저 모델
# (필드:비밀번호, 마지막 로그인, 활성여부 3가지만 존재, 최소한의 함수만 존재)
# - 따라서, 로그인시 필요한 필드 등 많은 부분이 커스텀 가능
# - 하지만, 장고의 유저 관련 함수들을 직접 정의를 하여 사용 해야함