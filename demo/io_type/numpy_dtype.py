import bentoml
import numpy as np
from pydantic import Field


class InputData(bentoml.IODescriptor):
    array: np.ndarray = Field(description="输入的多维数组")


@bentoml.service
class NumpyService:

    @bentoml.api
    def process_array(self, data: InputData) -> np.ndarray:
        # 返回输入数组的形状信息作为输出
        input_array = np.array(data.array)
        return input_array