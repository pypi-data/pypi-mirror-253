import torch
from torch import nn, Tensor
from zeta.nn import MultiheadAttention, FeedForward
from einpos import rearrange, reduce


class EEGConvEmbeddings(nn.Module):
    def __init__(
        self,
        num_channels,
        conv_channels,
        kernel_size,
        stride=1,
        padding=0,
    ):
        """
        Initializes the EEGConvEmbeddings module.

        Args:
        - num_channels (int): Number of EEG channels in the input data.
        - conv_channels (int): Number of output channels for the convolutional layer.
        - kernel_size (int): Size of the convolutional kernel.
        - stride (int, optional): Stride of the convolution. Default: 1.
        - padding (int, optional): Padding added to both sides of the input. Default: 0.
        """
        super(EEGConvEmbeddings, self).__init__()

        self.conv1 = nn.Conv1d(
            in_channels=num_channels,
            out_channels=conv_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
        )

        # Additional layers and operations can be added here

    def forward(self, x):
        """
        Forward pass of the EEGConvEmbeddings module.

        Args:
        - x (Tensor): Input tensor of shape (batch_size, num_channels, time_samples)

        Returns:
        - Tensor: Output tensor after convolution
        """
        x = self.conv1(x)
        return x


class FMRIEmbedding(nn.Module):
    def __init__(
        self,
        in_channels=1,
        out_channels=32,
        kernel_size=3,
        stride=1,
        padding=1,
    ):
        """
        Initializes an fMRI Embedding Network.

        Args:
        - in_channels (int): Number of input channels (scans/modalities).
        - out_channels (int): Number of output channels for the convolutional layer.
        - kernel_size (int): Size of the convolutional kernels.
        - stride (int): Stride of the convolutions.
        - padding (int): Padding added to the input.

        Example:
        model = fMRIEmbeddingNet()
        x = torch.randn(1, 1, 32, 32, 32)
        input_tensor = torch.randn(8, 1, 64, 64, 64)  # 8 fMRI scans
        output_tensor = model(input_tensor)
        print(output_tensor.shape)  # torch.Size([8, 32, 64, 64, 64])


        """
        super(FMRIEmbedding, self).__init__()

        self.conv1 = nn.Conv3d(
            in_channels, out_channels, kernel_size, stride, padding
        )
        # Additional layers can be added here as needed

    def forward(self, x):
        """
        Forward pass of the fMRI Embedding Network.

        Args:
        - x (Tensor): Input tensor of shape (batch_size, in_channels, D, H, W)

        Returns:
        - Tensor: Output embedding tensor
        """
        x = self.conv1(x)
        # Additional operations can be added here as needed
        return x


class MorpheusEncoder(nn.Module):
    """
    MorpheusEncoder is a module that performs encoding on EEG data using multi-head attention and feed-forward networks.

    Args:
        dim (int): The dimension of the input data.
        heads (int): The number of attention heads.
        depth (int): The number of layers in the encoder.
        dim_head (int): The dimension of each attention head.
        dropout (int): The dropout rate.
        num_channels (int): The number of input channels in the EEG data.
        conv_channels (int): The number of output channels after the convolutional layer.
        kernel_size (int): The size of the convolutional kernel.
        stride (int, optional): The stride of the convolutional layer. Defaults to 1.
        padding (int, optional): The padding size for the convolutional layer. Defaults to 0.
        ff_mult (int, optional): The multiplier for the feed-forward network hidden dimension. Defaults to 4.

    Attributes:
        dim (int): The dimension of the input data.
        heads (int): The number of attention heads.
        depth (int): The number of layers in the encoder.
        dim_head (int): The dimension of each attention head.
        dropout (int): The dropout rate.
        num_channels (int): The number of input channels in the EEG data.
        conv_channels (int): The number of output channels after the convolutional layer.
        kernel_size (int): The size of the convolutional kernel.
        stride (int): The stride of the convolutional layer.
        padding (int): The padding size for the convolutional layer.
        ff_mult (int): The multiplier for the feed-forward network hidden dimension.
        mha (MultiheadAttention): The multi-head attention module.
        ffn (FeedForward): The feed-forward network module.
        eeg_embedding (EEGConvEmbeddings): The EEG convolutional embedding module.

    """

    def __init__(
        self,
        dim: int,
        heads: int,
        depth: int,
        dim_head: int,
        dropout: int,
        num_channels,
        conv_channels,
        kernel_size,
        stride=1,
        padding=0,
        ff_mult: int = 4,
        *args,
        **kwargs,
    ):
        super(MorpheusEncoder, self).__init__()
        self.dim = dim
        self.heads = heads
        self.depth = depth
        self.dim_head = dim_head
        self.dropout = dropout
        self.num_channels = num_channels
        self.conv_channels = conv_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.ff_mult = ff_mult

        self.mha = MultiheadAttention(
            dim,
            heads,
            dropout,
            subln=True,
        )

        self.ffn = FeedForward(dim, dim, ff_mult, *args, **kwargs)

        self.eeg_embedding = EEGConvEmbeddings(
            num_channels, conv_channels, kernel_size, stride, padding
        )

    def forward(self, x: Tensor) -> Tensor:
        """
        Forward pass of the MorpheusEncoder module.

        Args:
            x (Tensor): The input tensor of shape (batch_size, seq_len, dim).

        Returns:
            Tensor: The output tensor of shape (batch_size, seq_len, dim).

        """
        x = self.eeg_embedding(x)
        print(x.shape)

        x = self.mha(x, x, x) + x

        x = self.ffn(x) + x

        return x


class MorpheusDecoder(nn.Module):
    def __init__(
        self,
        dim: int,
        heads: int,
        depth: int,
        dim_head: int,
        dropout: int,
        num_channels,
        conv_channels,
        kernel_size,
        in_channels,
        out_channels,
        stride=1,
        padding=0,
        ff_mult: int = 4,
        *args,
        **kwargs,
    ):
        super(MorpheusDecoder, self).__init__()
        self.dim = dim
        self.heads = heads
        self.depth = depth
        self.dim_head = dim_head
        self.dropout = dropout
        self.num_channels = num_channels
        self.conv_channels = conv_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.ff_mult = ff_mult

        self.frmi_embedding = nn.Linear(num_channels, dim)

        self.masked_attn = MultiheadAttention(
            dim,
            heads,
            dropout,
            subln=True,
        )

        self.mha = MultiheadAttention(
            dim,
            heads,
            dropout,
            subln=True,
        )

        self.frmni_embedding = FMRIEmbedding(
            in_channels, out_channels, kernel_size, stride, padding
        )

        self.ffn = FeedForward(dim, dim, ff_mult, *args, **kwargs)

        self.proj = nn.Linear(dim, num_channels)

        self.softmax = nn.Softmax(1)

    def forward(self, frmi: Tensor) -> Tensor:
        x = self.frmi_embedding(frmi)


class MorpheusTransformer(nn.Module):
    def __init__(self):
        pass

    def forward(self, x: Tensor):
        pass
