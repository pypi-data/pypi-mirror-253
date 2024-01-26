"""
Apply thoplw for models in TorchVision.
"""

# Import standard packages.
import argparse
import pathlib
import sys

# Import 3rd-party packages.
import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision
import thop

# Import thoplw package.
sys.path.append("..")
import thoplw


def parse_args():
    """
    Parse command line arguments.

    Returns:
        (argparse.Namespace): Parsed command line arguments.
    """
    # Create parser instance.
    fmtcls = lambda prog: argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=32)
    parser = argparse.ArgumentParser(description=__doc__.strip(), formatter_class=fmtcls, add_help=False)

    # Define group: model options.
    group = parser.add_argument_group("Model options")
    group.add_argument("--model", metavar="STR", type=str, default="all",
                       help="name of neural network model")

    # Define group: model options.
    group = parser.add_argument_group("Output options")
    group.add_argument("--dump", action="store_true",
                        help="save results as Markdown format")

    # Define group: other options.
    group6 = parser.add_argument_group("Other options")
    group6.add_argument("-h", "--help", action="help",
                        help="show this message and exit")

    return parser.parse_args()


def main(args):
    """
    Entry point of this script.

    Args:
        args (argparse.Namespace): Parsed command line arguments.
    """
    list_model_functions = {
        "alexnet": torchvision.models.alexnet,

        "vgg11"   : torchvision.models.vgg11,
        "vgg11_bn": torchvision.models.vgg11_bn,
        "vgg13"   : torchvision.models.vgg13,
        "vgg13_bn": torchvision.models.vgg13_bn,
        "vgg16"   : torchvision.models.vgg16,
        "vgg16_bn": torchvision.models.vgg16_bn,
        "vgg19"   : torchvision.models.vgg19,
        "vgg19_bn": torchvision.models.vgg19_bn,

        "resnet18" : torchvision.models.resnet18,
        "resnet34" : torchvision.models.resnet34,
        "resnet50" : torchvision.models.resnet50,
        "resnet101": torchvision.models.resnet101,
        "resnet152": torchvision.models.resnet152,

        "wide_resnet50_2" : torchvision.models.wide_resnet50_2,
        "wide_resnet101_2": torchvision.models.wide_resnet101_2,

        "resnext50_32x4d" : torchvision.models.resnext50_32x4d,
        "resnext101_32x8d": torchvision.models.resnext101_32x8d,

        "densenet121": torchvision.models.densenet121,
        "densenet161": torchvision.models.densenet161,
        "densenet169": torchvision.models.densenet169,
        "densenet201": torchvision.models.densenet201,

        "googlenet": torchvision.models.googlenet,
        "inception_v3": torchvision.models.inception_v3,

        "squeezenet1.0": torchvision.models.squeezenet1_0,
        "squeezenet1.1": torchvision.models.squeezenet1_1,

        "mobilenet_v2"      : torchvision.models.mobilenet_v2,
        "mobilenet_v3_small": torchvision.models.mobilenet_v3_small,
        "mobilenet_v3_large": torchvision.models.mobilenet_v3_large,

        "shufflenet_v2_x0.5": torchvision.models.shufflenet_v2_x0_5,
        "shufflenet_v2_x1.0": torchvision.models.shufflenet_v2_x1_0,

        "mnasnet_0.5": torchvision.models.mnasnet0_5,
        "mnasnet_1.0": torchvision.models.mnasnet1_0,
    }

    # Get the list of models to compute MACs and params.
    if args.model == "all": list_model_names = list(list_model_functions.keys())
    else                  : list_model_names = [args.model]

    # Initialize result container.
    results = dict()

    for name in list_model_names:

        # Get model instance.
        model = list_model_functions[name](weights=None)

        # Create input tensor.
        if name == "inception_v3": tensor = torch.randn(1, 3, 299, 299)
        else                     : tensor = torch.randn(1, 3, 224, 224)

        # Run thoplw.
        macs, params, layer_info = thoplw.profile(model, tensor)

        # If `--dump` is specified, save as Markdown file.
        if args.dump:

            # Dump layer-wise info as a Markdown fie.
            filepath = pathlib.Path("benchmarks/%s.md" % name.replace(".", "_"))
            filepath.write_text(layer_info.summary(kind="md", fmt="ratio"))
            print(filepath)

            # Store results.
            results[name] = (macs, params)

        # Otherwise, print summary.
        else:
            print(layer_info.summary(kind="text", fmt="ratio"))
            print()

    import pickle
    with open("result.pickle", "rb") as ifp:
        results = pickle.load(ifp)

    # If `--dump` is specified, save summary figure.
    if args.dump:

        model_families = {
            "AlexNet"            : ["alexnet"],
            "VGG family"         : ["vgg11", "vgg13", "vgg16", "vgg19"],
            "ResNet family"      : ["resnet18", "resnet34", "resnet50", "resnet101", "resnet152"],
            "WideResNet family"  : ["wide_resnet50_2", "wide_resnet101_2"],
            "ResNext family"     : ["resnext50_32x4d", "resnext101_32x8d"],
            "DenseNet family"    : ["densenet121", "densenet169", "densenet201", "densenet161"],
            "Inception family"   : ["googlenet", "inception_v3"],
            "SqueezeNet family"  : ["squeezenet1.0", "squeezenet1.1"],
            "MobileNet V2"       : ["mobilenet_v2"],
            "MobileNet V3 family": ["mobilenet_v3_small", "mobilenet_v3_large"],
            "ShuffleNet family"  : ["shufflenet_v2_x0.5", "shufflenet_v2_x1.0"],
            "MnasNet family"     : ["mnasnet_0.5", "mnasnet_1.0"],
        }

        plt.figure(figsize=(10, 5))

        for family_name, model_names in model_families.items():

            xs = [results[name][0] / 1E9 for name in model_names]
            ys = [results[name][1] / 1E6 for name in model_names]

            plt.plot(xs, ys, "-o", label=family_name)

            for x, y, name in zip(xs, ys, model_names):
                plt.text(x, y, name)

        plt.xscale("log")
        plt.yscale("log")
        plt.legend(loc="lower left", bbox_to_anchor=(1, 0))
        plt.xlabel("MADDs")
        plt.ylabel("Number of parameters")
        plt.xticks([0.1, 1, 10], ["100 [M]", "1 [G]" ,"10 [G]"])
        plt.yticks([1, 10, 100], ["1 [M]", "10 [M]", "100 [M]"])
        plt.xlim([0.03, 40])
        plt.ylim([1, 200])
        plt.grid(True, which="major", alpha=1.0)
        plt.grid(True, which="minor", alpha=0.3)
        plt.tight_layout()
        plt.show("benchmarks/madds-vs-parameters_raw.svg")


if __name__ == "__main__":
    main(parse_args())


# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
