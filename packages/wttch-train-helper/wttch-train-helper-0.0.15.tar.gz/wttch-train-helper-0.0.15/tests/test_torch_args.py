from torch import nn

from wttch.train.torch import ArgParser

if __name__ == '__main__':
    args = ArgParser()

    print(args.batch_size)

    args.save_module(nn.Linear(100, 10))
