#torch

[TOC]
## 张量 Tensors

### torch.is_tensor
    torch.is_tensor(obj)

如果obj 是一个pytorch张量，则返回True

### torch.is_storage
    torch.is_storage(obj)

如何obj 是一个pytorch storage对象，则返回True

### torch.set_default_tensor_type
    torch.set_default_tensor_type(t)

### torch.numel
    torch.numel(input)->int

返回input 张量中的元素个数

>参数: input (Tensor) – 输入张量

例子:

```python
>>> a = torch.randn(1,2,3,4,5)
>>> torch.numel(a)
120
>>> a = torch.zeros(4,4)
>>> torch.numel(a)
16
```

### torch.set_printoptions
    torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None)

设置打印选项。 完全参考自 Numpy。

参数:

> precision – 浮点数输出的精度位数 (默认为8 )  
threshold – 阈值，触发汇总显示而不是完全显示(repr)的数组元素的总数 （默认为1000）  
edgeitems – 汇总显示中，每维（轴）两端显示的项数（默认值为3）  
linewidth – 用于插入行间隔的每行字符数（默认为80）。Thresholded matricies will ignore this parameter.  
profile – pretty打印的完全默认值。 可以覆盖上述所有选项 (默认为short, full)


## 创建操作 Creation Ops

### torch.eye

    torch.eye(n, m=None, out=None)

返回一个2维张量，对角线位置全1，其它位置全0

### torch.from_numpy

    torch.from_numpy(ndarray) → Tensor

Numpy桥，将numpy.ndarray 转换为pytorch的 Tensor。 返回的张量tensor和numpy的ndarray共享同一内存空间。修改一个会导致另外一个也被修改。返回的张量不能改变大小。

### torch.linspace

    torch.linspace(start, end, steps=100, out=None) → Tensor

返回一个1维张量，包含在区间start 和 end 上均匀间隔的steps个点。 输出1维张量的长度为steps。

### torch.logspace

    torch.logspace(start, end, steps=100, out=None) → Tensor

返回一个1维张量，包含在区间 10start 和 10end上以对数刻度均匀间隔的steps个点。 输出1维张量的长度为steps。

### torch.ones
    
    torch.ones(*sizes, out=None) → Tensor

返回一个全为1 的张量，形状由可变参数sizes定义。

### torch.rand
    
    torch.rand(*sizes, out=None) → Tensor

返回一个张量，包含了从区间[0,1)的均匀分布中抽取的一组随机数，形状由可变参数sizes 定义。

### torch.randn
    
    torch.randn(*sizes, out=None) → Tensor

返回一个张量，包含了从标准正态分布(均值为0，方差为 1，即高斯白噪声)中抽取一组随机数，形状由可变参数sizes定义。 参数:

### torch.randperm
    
    torch.randperm(n, out=None) → LongTensor

给定参数n，返回一个从0 到n -1 的随机整数排列。

### torch.arange

    torch.arange(start, end, step=1, out=None) → Tensor

返回一个1维张量，长度为 floor((end−start)/step)。包含从start到end，以step为步长的一组序列值(默认步长为1)。

### torch.range
    
    torch.range(start, end, step=1, out=None) → Tensor

返回一个1维张量，有 floor((end−start)/step)+1 个元素。包含在半开区间[start, end）从start开始，以step为步长的一组值。 step 是两个值之间的间隔，即 xi+1=xi+step

> 警告：建议使用函数 torch.arange()

### torch.zeros

    torch.zeros(*sizes, out=None) → Tensor

返回一个全为标量 0 的张量，形状由可变参数sizes 定义。

## 索引,切片,连接,换位 Indexing, Slicing, Joining, Mutating Ops

###torch.cat

    torch.cat(inputs, dimension=0) → Tensor

在给定维度上对输入的张量序列seq 进行连接操作。

### torch.chunk
    torch.chunk(tensor, chunks, dim=0)
在给定维度(轴)上将输入张量进行分块儿。
###torch.gather
    torch.gather(input, dim, index, out=None) → Tensor
沿给定轴dim，将输入索引张量index指定位置的值进行聚合。
>注意： 返回的张量不与原始张量共享内存空间。

###torch.t
    torch.t(input, out=None) → Tensor
输入一个矩阵（2维张量），并转置0, 1维。 可以被视为函数transpose(input, 0, 1)的简写函数。
### torch.transpose
    torch.transpose(input, dim0, dim1, out=None) → Tensor
返回输入矩阵input的转置。交换维度dim0和dim1。 输出张量与输入张量共享内存，所以改变其中一个会导致另外一个也被修改。


## torch.utils.data

### class torch.utils.data.Dataset
    class torch.utils.data.TensorDataset(data_tensor, target_tensor)
表示Dataset的抽象类。

所有其他数据集都应该进行子类化。所有子类应该override__len__和__getitem__，前者提供了数据集的大小，后者支持整数索引，范围从0到len(self)。

包装数据和目标张量的数据集。

通过沿着第一个维度索引两个张量来恢复每个样本。

参数：

data_tensor (Tensor) －　包含样本数据
target_tensor (Tensor) －　包含样本目标（标签）
###class torch.utils.data.DataLoader
    class torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, num_workers=0, collate_fn=<function default_collate>, pin_memory=False, drop_last=False)
数据加载器。组合数据集和采样器，并在数据集上提供单进程或多进程迭代器。

参数：

dataset (Dataset) – 加载数据的数据集。
batch_size (int, optional) – 每个batch加载多少个样本(默认: 1)。
shuffle (bool, optional) – 设置为True时会在每个epoch重新打乱数据(默认: False).
sampler (Sampler, optional) – 定义从数据集中提取样本的策略。如果指定，则忽略shuffle参数。
num_workers (int, optional) – 用多少个子进程加载数据。0表示数据将在主进程中加载(默认: 0)
collate_fn (callable, optional) –
pin_memory (bool, optional) –
drop_last (bool, optional) – 如果数据集大小不能被batch size整除，则设置为True后可删除最后一个不完整的batch。如果设为False并且数据集的大小不能被batch size整除，则最后一个batch将更小。(默认: False)