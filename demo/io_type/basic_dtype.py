import bentoml
from pydantic import Field
import typing as t

@bentoml.service
class BasicTypeService:

  @bentoml.api
  def process_data(
      self,
      name: str = Field(description="用户的名字"),
      age: int = Field(description="用户的年龄"),
      interests: t.List[str] = Field(description="用户的兴趣列表"),
  ) -> t.Dict[str, t.Any]:
      """
      处理用户数据并返回格式化的结果。
      """
      return {
          "greeting": f"Hello, {name}!",
          "age_next_year": age + 1,
          "interests_count": len(interests),
          "summary": f"{name} 的兴趣爱好有 {', '.join(interests)}。"
      }