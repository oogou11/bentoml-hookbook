import bentoml
import pandas as pd
from pydantic import Field

# 定义输入数据模型
class InputData(bentoml.IODescriptor):
    df: pd.DataFrame = Field(description="输入的 DataFrame 数据")

# 创建 BentoML 服务
@bentoml.service
class PandasService:

    @bentoml.api
    def process_dataframe(self, data: InputData) -> pd.DataFrame:
        # 处理 DataFrame，返回相同的 DataFrame 作为示例
        return data.df
