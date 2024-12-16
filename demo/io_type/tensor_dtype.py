import bentoml
import torch
from pydantic import Field

class InputData(bentoml.IODescriptor):
    tensor: torch.Tensor = Field(description="输入的张量数据")

@bentoml.service
class TorchService:

    @bentoml.api
    def process_tensor(self, data: InputData) -> torch.Tensor:
        # 返回输入张量的转置
        input_tensor = torch.tensor(data.tensor)
        return input_tensor.T
