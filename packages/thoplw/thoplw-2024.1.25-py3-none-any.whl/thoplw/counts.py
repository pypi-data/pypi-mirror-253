"""
Collection of the count functions.
"""

# Import standard libraries.
import functools

# Import 3rd-party packages.
import torch

# Import thoplw scripts.
from .description import description


def get_returned_dict(macs, layer, Xs, Y):
    """
    Format the given parameters and returns as dict.
    """
    # Compute the number of parameters.
    if macs is None: params = None
    else           : params = sum(p.numel() for p in layer.parameters())

    # Get input shape.
    try   : shape_in = [list(X.shape) for X in Xs]
    except: shape_in = None

    # Get output shape.
    try   : shape_out = list(Y.shape)
    except: shape_out = None

    # Returns as dict.
    return {"macs"       : macs,
            "params"     : params,
            "shapes_in"  : shape_in,
            "shape_out"  : shape_out,
            "description": description(layer, Xs, Y)}


def hook_func(layer, Xs, Y, count_func):
    """
    """
    layer.thoplw_log = get_returned_dict(count_func(layer, Xs, Y), layer, Xs, Y)


def get_hook_func(count_func):
    """
    Returns a function to be hooked to layer instances.
    """
    return functools.partial(hook_func, count_func=count_func)


def count_none(layer, Xs, Y):
    """
    Count function for ignored layers.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    return None


def count_zero(layer, Xs, Y):
    """
    Count function for layers that has zero MACs and zero parameters.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    return 0


def count_linear(layer, Xs, Y):
    """
    Count function for the fully connected layer.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    channels_in  = X.shape[1]
    channels_out = Y.shape[1]

    macs = channels_in * channels_out

    if layer.bias is not None:
        macs += layer.bias.numel()

    return macs


def count_convNd(layer, Xs, Y):
    """
    Count function for the convolution layers.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    def macs_conv1d(layer, X, Y):
        """
        Returns MACs of 1d conv.
        """
        c_o, c_i, k_l = layer.weight.shape
        _,   _,   o_l = tensor_out.shape
        return int(c_i * c_o * k_l * o_l)

    def macs_conv2d(layer, X, Y):
        """
        Returns MACs of 2d conv.
        """
        c_o, c_i, k_h, k_w = layer.weight.shape
        _,   _,   o_h, o_w = Y.shape
        return int(c_i * c_o * k_h * k_w * o_h * o_w)

    def macs_conv3d(layer, X, Y):
        """
        Returns MACs of 3d conv.
        """
        return None

    X, = Xs

    if   len(X.shape) == 3: macs = macs_conv1d(layer, X, Y)
    elif len(X.shape) == 4: macs = macs_conv2d(layer, X, Y)
    elif len(X.shape) == 5: macs = macs_conv3d(layer, X, Y)
    else                  : raise NotImplementedError(layer.__class__.__name__)

    if layer.bias is not None:
        macs += layer.bias.numel()

    return macs


def count_batchnorm(layer, Xs, Y):
    """
    Count function for the batch normalization layers.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    macs = 2 * X.numel()

    if hasattr(layer, "affine") or hasattr(layer, "elementwise_affine"):
        macs += 2 * X.numel()

    return macs


def count_layernorm(layer, Xs, Y):
    """
    Count function for the layer normalization layer.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    macs = 2 * X.numel()

    return macs


def count_instancenorm(layer, Xs, Y):
    """
    Count function for the instance normalization layers.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    macs = 2 * X.numel()

    return macs


def count_lrelu(layer, Xs, Y):
    """
    Count function for the leaky ReLU.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    macs = layer.weight.numel()

    return macs


def count_prelu(layer, Xs, Y):
    """
    Count function for the parametric ReLU.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    macs = layer.weight.numel()

    return macs


def count_softmax(layer, Xs, Y):
    """
    Count function for the softmax.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    macs = X.numel()

    return macs


def count_avgpool(layer, Xs, Y):
    """
    Count function for the average pooling layers.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    X_size = torch.tensor(list(X.shape[2:]), dtype=torch.int32)
    Y_size = torch.tensor(list(Y.shape[2:]), dtype=torch.int32)
    k_size = (X_size / Y_size).to(torch.int32)

    macs = Y.numel() * k_size.numel()

    return macs


def count_upsample(layer, Xs, Y):
    """
    Count function for the upsampling layers.

    Args:
        layer (torch.nn.Module): Layer instance.
        Xs    (list)           : List of input tensor.
        Y     (torch.Tensor)   : Output tensor.
    """
    X, = Xs

    if   layer.mode == "nearest" : macs = 0
    elif layer.mode == "linear"  : macs = 4 * Y.numel()
    elif layer.mode == "bilinear": macs = 6 * Y.numel()
    elif layer.mode == "bicubic" : macs = 20 * Y.numel()
    else                         : raise NotImplementedError("Not implemented")

    return macs


# def _count_rnn_cell(input_size, hidden_size, bias=True):
#     # h' = \tanh(W_{ih} x + b_{ih}  +  W_{hh} h + b_{hh})
#     total_ops = hidden_size * (input_size + hidden_size) + hidden_size
#     if bias:
#         total_ops += hidden_size * 2
# 
#     return total_ops
# 
# 
# def count_rnn_cell(m: nn.RNNCell, x: torch.Tensor, y: torch.Tensor):
#     total_ops = _count_rnn_cell(m.input_size, m.hidden_size, m.bias)
# 
#     batch_size = x[0].size(0)
#     total_ops *= batch_size
# 
#     m.total_ops += torch.DoubleTensor([int(total_ops)])
# 
# 
# def _count_gru_cell(input_size, hidden_size, bias=True):
#     total_ops = 0
#     # r = \sigma(W_{ir} x + b_{ir} + W_{hr} h + b_{hr}) \\
#     # z = \sigma(W_{iz} x + b_{iz} + W_{hz} h + b_{hz}) \\
#     state_ops = (hidden_size + input_size) * hidden_size + hidden_size
#     if bias:
#         state_ops += hidden_size * 2
#     total_ops += state_ops * 2
# 
#     # n = \tanh(W_{in} x + b_{in} + r * (W_{hn} h + b_{hn})) \\
#     total_ops += (hidden_size + input_size) * hidden_size + hidden_size
#     if bias:
#         total_ops += hidden_size * 2
#     # r hadamard : r * (~)
#     total_ops += hidden_size
# 
#     # h' = (1 - z) * n + z * h
#     # hadamard hadamard add
#     total_ops += hidden_size * 3
# 
#     return total_ops
# 
# 
# def count_gru_cell(m: nn.GRUCell, x: torch.Tensor, y: torch.Tensor):
#     total_ops = _count_gru_cell(m.input_size, m.hidden_size, m.bias)
# 
#     batch_size = x[0].size(0)
#     total_ops *= batch_size
# 
#     m.total_ops += torch.DoubleTensor([int(total_ops)])
# 
# 
# def _count_lstm_cell(input_size, hidden_size, bias=True):
#     total_ops = 0
# 
#     # i = \sigma(W_{ii} x + b_{ii} + W_{hi} h + b_{hi}) \\
#     # f = \sigma(W_{if} x + b_{if} + W_{hf} h + b_{hf}) \\
#     # o = \sigma(W_{io} x + b_{io} + W_{ho} h + b_{ho}) \\
#     # g = \tanh(W_{ig} x + b_{ig} + W_{hg} h + b_{hg}) \\
#     state_ops = (input_size + hidden_size) * hidden_size + hidden_size
#     if bias:
#         state_ops += hidden_size * 2
#     total_ops += state_ops * 4
# 
#     # c' = f * c + i * g \\
#     # hadamard hadamard add
#     total_ops += hidden_size * 3
# 
#     # h' = o * \tanh(c') \\
#     total_ops += hidden_size
# 
#     return total_ops
# 
# 
# def count_lstm_cell(m: nn.LSTMCell, x: torch.Tensor, y: torch.Tensor):
#     total_ops = _count_lstm_cell(m.input_size, m.hidden_size, m.bias)
# 
#     batch_size = x[0].size(0)
#     total_ops *= batch_size
# 
#     m.total_ops += torch.DoubleTensor([int(total_ops)])
# 
# 
# def count_rnn(m: nn.RNN, x, y):
#     bias = m.bias
#     input_size = m.input_size
#     hidden_size = m.hidden_size
#     num_layers = m.num_layers
# 
#     if isinstance(x[0], PackedSequence):
#         batch_size = torch.max(x[0].batch_sizes)
#         num_steps = x[0].batch_sizes.size(0)
#     else:
#         if m.batch_first:
#             batch_size = x[0].size(0)
#             num_steps = x[0].size(1)
#         else:
#             batch_size = x[0].size(1)
#             num_steps = x[0].size(0)
# 
#     total_ops = 0
#     if m.bidirectional:
#         total_ops += _count_rnn_cell(input_size, hidden_size, bias) * 2
#     else:
#         total_ops += _count_rnn_cell(input_size, hidden_size, bias)
# 
#     for i in range(num_layers - 1):
#         if m.bidirectional:
#             total_ops += _count_rnn_cell(hidden_size * 2, hidden_size, bias) * 2
#         else:
#             total_ops += _count_rnn_cell(hidden_size, hidden_size, bias)
# 
#     # time unroll
#     total_ops *= num_steps
#     # batch_size
#     total_ops *= batch_size
# 
#     m.total_ops += torch.DoubleTensor([int(total_ops)])
# 
# 
# def count_gru(m: nn.GRU, x, y):
#     bias = m.bias
#     input_size = m.input_size
#     hidden_size = m.hidden_size
#     num_layers = m.num_layers
# 
#     if isinstance(x[0], PackedSequence):
#         batch_size = torch.max(x[0].batch_sizes)
#         num_steps = x[0].batch_sizes.size(0)
#     else:
#         if m.batch_first:
#             batch_size = x[0].size(0)
#             num_steps = x[0].size(1)
#         else:
#             batch_size = x[0].size(1)
#             num_steps = x[0].size(0)
# 
#     total_ops = 0
#     if m.bidirectional:
#         total_ops += _count_gru_cell(input_size, hidden_size, bias) * 2
#     else:
#         total_ops += _count_gru_cell(input_size, hidden_size, bias)
# 
#     for i in range(num_layers - 1):
#         if m.bidirectional:
#             total_ops += _count_gru_cell(hidden_size * 2, hidden_size, bias) * 2
#         else:
#             total_ops += _count_gru_cell(hidden_size, hidden_size, bias)
# 
#     # time unroll
#     total_ops *= num_steps
#     # batch_size
#     total_ops *= batch_size
# 
#     m.total_ops += torch.DoubleTensor([int(total_ops)])
# 
# 
# def count_lstm(m: nn.LSTM, x, y):
#     bias = m.bias
#     input_size = m.input_size
#     hidden_size = m.hidden_size
#     num_layers = m.num_layers
# 
#     if isinstance(x[0], PackedSequence):
#         batch_size = torch.max(x[0].batch_sizes)
#         num_steps = x[0].batch_sizes.size(0)
#     else:
#         if m.batch_first:
#             batch_size = x[0].size(0)
#             num_steps = x[0].size(1)
#         else:
#             batch_size = x[0].size(1)
#             num_steps = x[0].size(0)
# 
#     total_ops = 0
#     if m.bidirectional:
#         total_ops += _count_lstm_cell(input_size, hidden_size, bias) * 2
#     else:
#         total_ops += _count_lstm_cell(input_size, hidden_size, bias)
# 
#     for i in range(num_layers - 1):
#         if m.bidirectional:
#             total_ops += _count_lstm_cell(hidden_size * 2, hidden_size, bias) * 2
#         else:
#             total_ops += _count_lstm_cell(hidden_size, hidden_size, bias)
# 
#     # time unroll
#     total_ops *= num_steps
#     # batch_size
#     total_ops *= batch_size
# 
#     m.total_ops += torch.DoubleTensor([int(total_ops)])



# Publish only functions named `count_*`.
__all__  = [func_name for func_name in dir() if func_name.startswith("count_")]
__all__ += ["get_hook_func"]


# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
