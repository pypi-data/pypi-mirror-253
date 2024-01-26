"""
Test the minimal example shown in the README.
"""

import sys
sys.path.append("..")

import torch, torchvision, thoplw

# Instanciate the target model.
model = torchvision.models.resnet18()

# Compute MACs, number of parameters, and details of each layer.
macs, params, layers_info = thoplw.profile(model, tensor=torch.randn(1, 3, 224, 224))

# Print the total MACs and number of parameters.
print("Total MACs and params:")
print("  - Macs   =", macs)
print("  - Params =", params)
print()

# Print layer details.
print(layers_info.summary())

# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
