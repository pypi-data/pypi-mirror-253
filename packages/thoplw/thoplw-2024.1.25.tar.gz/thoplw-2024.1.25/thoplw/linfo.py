"""
"""

# Import 3rd-party packages.
import torch

# Import thoplw scripts.
from .description import description
from .format      import clever_format, format_table


class LayersInfo:
    """
    Summarize and format the layer detail information.
    """
    def __init__(self, model_name, shape_input):
        """
        Constructor.

        Args:
            model_name  (str)       : Name of the target NN model.
            shape_input (torch.Size): Shape of input tensor.
        """
        self.name  = model_name
        self.info  = list()
        self.shape = shape_input

    def append(self, layer_name, layer_log):
        """
        Append layer information.

        Args:
            layer_name (str) : Layer name.
            layer_log  (dict): Log dictionary generated on the forward inference.
        """
        self.info.append((layer_name, layer_log))

    def summary(self, kind="text", fmt="raw"):
        """
        Summarize layer infomation in a table format.

        Args:
            kind (str): Kind of the output table.
            fmt  (str): Format of the value.

        Returns:
            (str): String of summary table.
        """
        def is_effective_info(name, layer_log):
            """
            Returns True if the given layer should appear in the output table.
            """
            if   layer_log["macs"]   is None: return False
            elif layer_log["params"] is None: return False
            else                            : return True

        def get_shape(shape):
            """
            Returns input/output tensor shape as a string.
            """
            if isinstance(shape[0], list):
                return ", ".join(get_shape(s) for s in shape)
            return "x".join(str(v) for v in shape[1:])

        def get_value(value, val_norm):
            """
            Returns value in an appropriate expression.
            """
            if   value is None  : return "-"
            elif fmt == "clever": return clever_format(value)
            elif fmt == "ratio" : return "%5.2f %%" % (100 * value / val_norm)
            else                : return str(value)

        def fixed_length(list_strs, lr):
            """
            """
            len_max = max(len(s) for s in list_strs)
            if   lr == "l": return [s.ljust(len_max)  for s in list_strs]
            elif lr == "r": return [s.rjust(len_max)  for s in list_strs]
            elif lr == "c": return [s.center(len_max) for s in list_strs]
            else          : raise ValueError("Unknown value of the arg 'lr=%s'" % lr)

        # Drop unnecessary layers.
        list_info = [info for info in self.info if is_effective_info(*info)]

        # Compute total values.
        total_macs, total_params = self.total()

        # Append column name.
        list_name      = ["Name"]
        list_shape_in  = ["Input shape"]
        list_shape_out = ["Output shape"]
        list_macs      = ["MACs"]
        list_params    = ["Params"]
        list_desc      = ["Description"]

        # Append table body.
        list_name      += [name                                   for name, log in list_info]
        list_shape_in  += [get_shape(log["shapes_in"])            for name, log in list_info]
        list_shape_out += [get_shape(log["shape_out"])            for name, log in list_info]
        list_macs      += [get_value(log["macs"],   total_macs)   for name, log in list_info]
        list_params    += [get_value(log["params"], total_params) for name, log in list_info]
        list_desc      += [log["description"]                     for name, log in list_info]

        # Convert total values in an appropriate expression if necessary.
        if fmt in ["clever", "ratio"]:
            total_macs, total_params = clever_format([total_macs, total_params])

        # Append total row.
        list_name      += ["Total"]
        list_shape_in  += [list_shape_in[1]]
        list_shape_out += [list_shape_out[-1]]
        list_macs      += [str(total_macs)]
        list_params    += [str(total_params)]
        list_desc      += [self.name]

        # Make each string a fixed length.
        list_name      = fixed_length(list_name,      lr="l")
        list_shape_in  = fixed_length(list_shape_in,  lr="c")
        list_shape_out = fixed_length(list_shape_out, lr="c")
        list_macs      = fixed_length(list_macs,      lr="r")
        list_params    = fixed_length(list_params,    lr="r")
        list_desc      = fixed_length(list_desc,      lr="l")

        # Create table data.
        table_data = [list_name, list_shape_in, list_shape_out, list_macs, list_params, list_desc]

        return format_table(table_data, kind=kind)

    def total(self):
        """
        Compute total MACs and the number of parameters.

        Returns:
            (tuple): A pair of (MACs, the number of parameters).
        """
        # Initialize the returned values.
        total_macs   = 0
        total_params = 0

        # Add MACs and the number of parameters for all layers.
        for name, layer_info_dict in self.info:
            if (layer_info_dict["macs"] is not None) and (layer_info_dict["params"] is not None):
                total_macs   += layer_info_dict["macs"]
                total_params += layer_info_dict["params"]

        return (total_macs, total_params)


# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
