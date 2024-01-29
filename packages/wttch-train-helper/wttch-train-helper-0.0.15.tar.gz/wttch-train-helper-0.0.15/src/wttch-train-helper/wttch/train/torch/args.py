from argparse import ArgumentParser

import torch
from torch import nn

from .utils import try_gpu, set_device_local, set_dtype_local


class ArgParser:
    """
    对 argparse.ArgumentParser 进行一些训练的预处理。
    """
    cuda_no: int
    dtype: int
    epochs: int
    batch_size: int
    module_name: str

    def __init__(self):
        self.parse = ArgParser.create_parser()  # type: ArgumentParser

        self.args = self.parse.parse_args()

        self._preprocess_arg()

    def _preprocess_arg(self):
        """
        预处理一些参数。

        如果参数有设备序号、训练 dtype 会将数据写入 thread local。
        """
        self.cuda_no = self.args.cuda_no
        self.dtype = self.args.dtype
        self.epochs = self.args.epochs
        self.batch_size = self.args.batch_size
        self.module_name = self.args.module_name

        # 设置设备
        if self.cuda_no is not None:
            set_device_local(try_gpu(self.cuda_no))
        # 设置 dtype
        if self.dtype is not None:
            if self.dtype == 32:
                set_dtype_local(torch.float32)
            else:
                set_dtype_local(torch.float64)

    def save_module(self, module: nn.Module):
        """
        保存模型。
        按 arg parse 解析的模型名称保存模型。
        """
        append = '' if self.args.module_name.endswith('.pkl') else '.pkl'

        torch.save(module.state_dict(), f'{self.args.module_name}{append}')

    @classmethod
    def create_parser(cls):
        """
        获取训练参数。
        """
        argparse = ArgumentParser("设置训练参数")

        argparse.add_argument("-e", "--epochs", type=int, default=36, help="训练轮次")
        argparse.add_argument("-b", "--batch-size", type=int, default=64, help="批处理大小")

        argparse.add_argument("-d", "--cuda-no", type=int, default=None, help="使用的 cuda 设备序号")
        argparse.add_argument("-t", "--dtype", type=int, default=32,
                              choices=[32, 64], help="dtype 使用 float32 还是 float64")

        argparse.add_argument("-m", "--module-name", type=str, default="module.pkl", help="模型保存名称")

        return argparse
