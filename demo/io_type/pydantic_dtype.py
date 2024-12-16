import bentoml
from pydantic import BaseModel, Field

# 定义用户信息的Pydantic模型
class UserProfile(BaseModel):
    name: str = Field(..., description="用户的名字", examples=["刘备"])
    age: int = Field(..., description="用户的年龄", examples=[25])
    email: str = Field(..., description="用户的邮箱地址", examples=["liubei@qq.com"])

# 定义 BentoML 服务
@bentoml.service
class PydanticService:

    @bentoml.api
    def process_user(self, user: UserProfile) -> dict:
        return {
            "status": "success",
            "message": f"Processed data for {user.name}, age {user.age}, email {user.email}"
        }