"""
"""

# Import 3rd-party packages.
import torch


def get_size_str(size):
    """
    Returns a string expression of the given size.

    Args:
        size (tuple): Size of a tensor.

    Returns:
        (str): String expression of the given size.
    """
    # If the input size is an integer, return it and exit.
    if isinstance(size, int):
        return size

    # Get list of unique elements.
    num_element = len(set(list(size)))

    # Returns the string expression of the given size.
    if num_element == 1: return str(size[0])
    else               : return str(size)


def description(layer, Xs, Y):
    """
    """
    desc_func = DESC_FUNCTIONS.get(layer.__class__, desc_nameonly)

    return desc_func(layer, Xs, Y)


def desc_nameonly(layer, Xs, Y):
    """
    """
    return layer.__class__.__name__


def desc_convNd(layer, Xs, Y):
    """
    """
    return "%s k=%s p=%s s=%s" % (layer.__class__.__name__,
                                  get_size_str(layer.kernel_size),
                                  get_size_str(layer.padding),
                                  get_size_str(layer.stride))


def desc_pooling(layer, Xs, Y):
    """
    """
    if hasattr(layer, "kernel_size"):
        return "%s k=%s s=%s" % (layer.__class__.__name__,
                                 get_size_str(layer.kernel_size),
                                 get_size_str(layer.stride))

    else:
        return layer.__class__.__name__


# Map from layer classes to hook functions.
DESC_FUNCTIONS = {

    # Fully connected layers.
    torch.nn.Linear: desc_nameonly,

    # Convolution layers.
    torch.nn.Conv1d: desc_convNd,
    torch.nn.Conv2d: desc_convNd,
    torch.nn.Conv3d: desc_convNd,

    # Transposed convolution layers.
    torch.nn.ConvTranspose1d: desc_convNd,
    torch.nn.ConvTranspose2d: desc_convNd,
    torch.nn.ConvTranspose3d: desc_convNd,

    # Pooling layers.
    torch.nn.MaxPool1d        : desc_pooling,
    torch.nn.MaxPool2d        : desc_pooling,
    torch.nn.MaxPool3d        : desc_pooling,
    torch.nn.AdaptiveMaxPool1d: desc_pooling,
    torch.nn.AdaptiveMaxPool2d: desc_pooling,
    torch.nn.AdaptiveMaxPool3d: desc_pooling,
    torch.nn.AvgPool1d        : desc_pooling,
    torch.nn.AvgPool2d        : desc_pooling,
    torch.nn.AvgPool3d        : desc_pooling,
    torch.nn.AdaptiveAvgPool1d: desc_pooling,
    torch.nn.AdaptiveAvgPool2d: desc_pooling,
    torch.nn.AdaptiveAvgPool3d: desc_pooling,

    # # RNN layers.
    # torch.nn.RNNCell : count_rnn_cell,
    # torch.nn.GRUCell : count_gru_cell,
    # torch.nn.LSTMCell: count_lstm_cell,
    # torch.nn.RNN     : count_rnn,
    # torch.nn.GRU     : count_gru,
    # torch.nn.LSTM    : count_lstm,
}


# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
