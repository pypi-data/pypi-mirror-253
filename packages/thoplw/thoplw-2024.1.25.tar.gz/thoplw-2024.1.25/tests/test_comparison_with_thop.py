"""
"""

# Import standard packages.
import sys

# Import 3rd-party packages.
import torch
import torchvision
import thop

# Import thoplw package.
sys.path.append("..")
import thoplw


def main():
    """
    """
    list_models = {
        "alexnet": torchvision.models.alexnet,

        "vgg11"   : torchvision.models.vgg11,
        "vgg13"   : torchvision.models.vgg13,
        "vgg16"   : torchvision.models.vgg16,
        "vgg19"   : torchvision.models.vgg19,
        "vgg11_bn": torchvision.models.vgg11_bn,
        "vgg13_bn": torchvision.models.vgg13_bn,
        "vgg16_bn": torchvision.models.vgg16_bn,
        "vgg19_bn": torchvision.models.vgg19_bn,

        "resnet18" : torchvision.models.resnet18,
        "resnet34" : torchvision.models.resnet34,
        "resnet50" : torchvision.models.resnet50,
        "resnet101": torchvision.models.resnet101,
        "resnet152": torchvision.models.resnet152,

        "squeezenet1.0": torchvision.models.squeezenet1_0,
        "squeezenet1.1": torchvision.models.squeezenet1_1,

        "densenet121": torchvision.models.densenet121,
        "densenet161": torchvision.models.densenet161,
        "densenet169": torchvision.models.densenet169,
        "densenet201": torchvision.models.densenet201,

        "googlenet"   : torchvision.models.googlenet,
        "inception_v3": torchvision.models.inception_v3,

        "shufflenet_v2_x0.5": torchvision.models.shufflenet_v2_x0_5,
        "shufflenet_v2_x1.0": torchvision.models.shufflenet_v2_x1_0,

        "mobilenet_v2"      : torchvision.models.mobilenet_v2,
        "mobilenet_v3_large": torchvision.models.mobilenet_v3_large,
        "mobilenet_v3_small": torchvision.models.mobilenet_v3_small,

        "resnext50_32x4d" : torchvision.models.resnext50_32x4d,
        "resnext101_32x8d": torchvision.models.resnext101_32x8d,

        "wide_resnet50_2" : torchvision.models.wide_resnet50_2,
        "wide_resnet101_2": torchvision.models.wide_resnet101_2,

        "mnasnet_0.5": torchvision.models.mnasnet0_5,
        "mnasnet_1.0": torchvision.models.mnasnet1_0,
    }

    for name, model_init_func in list_models.items():

        model = model_init_func(weights=None)

        # Create input tensor.
        if name == "inception_v3": tensor = torch.randn(1, 3, 299, 299)
        else                     : tensor = torch.randn(1, 3, 224, 224)

        # Run thoplw
        macs, params, layer_info = thoplw.profile(model, tensor, verbose=False)

        # Run thop
        macs_ref, params_ref = thop.profile(model, inputs=(tensor,), verbose=False)
        macs_ref = int(macs_ref)
        params_ref = int(params_ref)

        # Compute error rates.
        error_macs   = abs(macs - macs_ref) / macs_ref
        error_params = abs(params - params_ref) / params_ref

        # Results.
        if (error_macs < 0.01) and (error_params < 0.01): result = "\033[36mPASSED\033[0m"
        else                                            : result = "\033[31mFAILED\033[0m"

        print("[%s]" % name)
        print("thoplw: ", macs, params)
        print("thop  : ", macs_ref, params_ref)
        print("errors = %.2f%%, %.2f%%" % (100*error_macs, 100*error_params))
        print(result)
        print()


if __name__ == "__main__":
    main()


# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
