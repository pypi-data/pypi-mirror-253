| Name                           | Input shape | Output shape |     MACs |   Params | Description        |
|:------------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0.0                   |  3x224x224  |  16x112x112  |   8.72 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| features.0.1                   |  16x112x112 |  16x112x112  |   1.29 % |   0.00 % | BatchNorm2d        |
| features.1.block.0.0           |  16x112x112 |   16x56x56   |   0.73 % |   0.01 % | Conv2d k=3 p=1 s=2 |
| features.1.block.0.1           |   16x56x56  |   16x56x56   |   0.32 % |   0.00 % | BatchNorm2d        |
| features.1.block.0.2           |   16x56x56  |   16x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.1.block.1.avgpool     |   16x56x56  |    16x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.1.block.1.fc1         |    16x1x1   |    8x1x1     |   0.00 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| features.1.block.1.fc2         |    8x1x1    |    16x1x1    |   0.00 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| features.1.block.1.activation  |    8x1x1    |    8x1x1     |   0.00 % |   0.00 % | ReLU               |
| features.1.block.2.0           |   16x56x56  |   16x56x56   |   1.29 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| features.1.block.2.1           |   16x56x56  |   16x56x56   |   0.32 % |   0.00 % | BatchNorm2d        |
| features.2.block.0.0           |   16x56x56  |   72x56x56   |   5.81 % |   0.05 % | Conv2d k=1 p=0 s=1 |
| features.2.block.0.1           |   72x56x56  |   72x56x56   |   1.45 % |   0.01 % | BatchNorm2d        |
| features.2.block.0.2           |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.2.block.1.0           |   72x56x56  |   72x28x28   |   0.82 % |   0.03 % | Conv2d k=3 p=1 s=2 |
| features.2.block.1.1           |   72x28x28  |   72x28x28   |   0.36 % |   0.01 % | BatchNorm2d        |
| features.2.block.1.2           |   72x28x28  |   72x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.2.block.2.0           |   72x28x28  |   24x28x28   |   2.18 % |   0.07 % | Conv2d k=1 p=0 s=1 |
| features.2.block.2.1           |   24x28x28  |   24x28x28   |   0.12 % |   0.00 % | BatchNorm2d        |
| features.3.block.0.0           |   24x28x28  |   88x28x28   |   2.66 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| features.3.block.0.1           |   88x28x28  |   88x28x28   |   0.44 % |   0.01 % | BatchNorm2d        |
| features.3.block.0.2           |   88x28x28  |   88x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.3.block.1.0           |   88x28x28  |   88x28x28   |   1.00 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.3.block.1.1           |   88x28x28  |   88x28x28   |   0.44 % |   0.01 % | BatchNorm2d        |
| features.3.block.1.2           |   88x28x28  |   88x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.3.block.2.0           |   88x28x28  |   24x28x28   |   2.66 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| features.3.block.2.1           |   24x28x28  |   24x28x28   |   0.12 % |   0.00 % | BatchNorm2d        |
| features.4.block.0.0           |   24x28x28  |   96x28x28   |   2.91 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.4.block.0.1           |   96x28x28  |   96x28x28   |   0.48 % |   0.02 % | BatchNorm2d        |
| features.4.block.1.0           |   96x28x28  |   96x14x14   |   0.76 % |   0.09 % | Conv2d k=5 p=2 s=2 |
| features.4.block.1.1           |   96x14x14  |   96x14x14   |   0.12 % |   0.02 % | BatchNorm2d        |
| features.4.block.2.avgpool     |   96x14x14  |    96x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.4.block.2.fc1         |    96x1x1   |    24x1x1    |   0.00 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.4.block.2.fc2         |    24x1x1   |    96x1x1    |   0.00 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.4.block.2.activation  |    24x1x1   |    24x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.4.block.3.0           |   96x14x14  |   40x14x14   |   1.21 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| features.4.block.3.1           |   40x14x14  |   40x14x14   |   0.05 % |   0.01 % | BatchNorm2d        |
| features.5.block.0.0           |   40x14x14  |  240x14x14   |   3.03 % |   0.38 % | Conv2d k=1 p=0 s=1 |
| features.5.block.0.1           |  240x14x14  |  240x14x14   |   0.30 % |   0.04 % | BatchNorm2d        |
| features.5.block.1.0           |  240x14x14  |  240x14x14   |   1.89 % |   0.23 % | Conv2d k=5 p=2 s=1 |
| features.5.block.1.1           |  240x14x14  |  240x14x14   |   0.30 % |   0.04 % | BatchNorm2d        |
| features.5.block.2.avgpool     |  240x14x14  |   240x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.5.block.2.fc1         |   240x1x1   |    64x1x1    |   0.02 % |   0.60 % | Conv2d k=1 p=0 s=1 |
| features.5.block.2.fc2         |    64x1x1   |   240x1x1    |   0.03 % |   0.61 % | Conv2d k=1 p=0 s=1 |
| features.5.block.2.activation  |    64x1x1   |    64x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.5.block.3.0           |  240x14x14  |   40x14x14   |   3.03 % |   0.38 % | Conv2d k=1 p=0 s=1 |
| features.5.block.3.1           |   40x14x14  |   40x14x14   |   0.05 % |   0.01 % | BatchNorm2d        |
| features.6.block.0.0           |   40x14x14  |  240x14x14   |   3.03 % |   0.38 % | Conv2d k=1 p=0 s=1 |
| features.6.block.0.1           |  240x14x14  |  240x14x14   |   0.30 % |   0.04 % | BatchNorm2d        |
| features.6.block.1.0           |  240x14x14  |  240x14x14   |   1.89 % |   0.23 % | Conv2d k=5 p=2 s=1 |
| features.6.block.1.1           |  240x14x14  |  240x14x14   |   0.30 % |   0.04 % | BatchNorm2d        |
| features.6.block.2.avgpool     |  240x14x14  |   240x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.6.block.2.fc1         |   240x1x1   |    64x1x1    |   0.02 % |   0.60 % | Conv2d k=1 p=0 s=1 |
| features.6.block.2.fc2         |    64x1x1   |   240x1x1    |   0.03 % |   0.61 % | Conv2d k=1 p=0 s=1 |
| features.6.block.2.activation  |    64x1x1   |    64x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.6.block.3.0           |  240x14x14  |   40x14x14   |   3.03 % |   0.38 % | Conv2d k=1 p=0 s=1 |
| features.6.block.3.1           |   40x14x14  |   40x14x14   |   0.05 % |   0.01 % | BatchNorm2d        |
| features.7.block.0.0           |   40x14x14  |  120x14x14   |   1.51 % |   0.19 % | Conv2d k=1 p=0 s=1 |
| features.7.block.0.1           |  120x14x14  |  120x14x14   |   0.15 % |   0.02 % | BatchNorm2d        |
| features.7.block.1.0           |  120x14x14  |  120x14x14   |   0.95 % |   0.12 % | Conv2d k=5 p=2 s=1 |
| features.7.block.1.1           |  120x14x14  |  120x14x14   |   0.15 % |   0.02 % | BatchNorm2d        |
| features.7.block.2.avgpool     |  120x14x14  |   120x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.7.block.2.fc1         |   120x1x1   |    32x1x1    |   0.01 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| features.7.block.2.fc2         |    32x1x1   |   120x1x1    |   0.01 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| features.7.block.2.activation  |    32x1x1   |    32x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.7.block.3.0           |  120x14x14  |   48x14x14   |   1.82 % |   0.23 % | Conv2d k=1 p=0 s=1 |
| features.7.block.3.1           |   48x14x14  |   48x14x14   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.8.block.0.0           |   48x14x14  |  144x14x14   |   2.18 % |   0.27 % | Conv2d k=1 p=0 s=1 |
| features.8.block.0.1           |  144x14x14  |  144x14x14   |   0.18 % |   0.02 % | BatchNorm2d        |
| features.8.block.1.0           |  144x14x14  |  144x14x14   |   1.13 % |   0.14 % | Conv2d k=5 p=2 s=1 |
| features.8.block.1.1           |  144x14x14  |  144x14x14   |   0.18 % |   0.02 % | BatchNorm2d        |
| features.8.block.2.avgpool     |  144x14x14  |   144x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.8.block.2.fc1         |   144x1x1   |    40x1x1    |   0.01 % |   0.23 % | Conv2d k=1 p=0 s=1 |
| features.8.block.2.fc2         |    40x1x1   |   144x1x1    |   0.01 % |   0.23 % | Conv2d k=1 p=0 s=1 |
| features.8.block.2.activation  |    40x1x1   |    40x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.8.block.3.0           |  144x14x14  |   48x14x14   |   2.18 % |   0.27 % | Conv2d k=1 p=0 s=1 |
| features.8.block.3.1           |   48x14x14  |   48x14x14   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.9.block.0.0           |   48x14x14  |  288x14x14   |   4.36 % |   0.54 % | Conv2d k=1 p=0 s=1 |
| features.9.block.0.1           |  288x14x14  |  288x14x14   |   0.36 % |   0.05 % | BatchNorm2d        |
| features.9.block.1.0           |  288x14x14  |   288x7x7    |   0.57 % |   0.28 % | Conv2d k=5 p=2 s=2 |
| features.9.block.1.1           |   288x7x7   |   288x7x7    |   0.09 % |   0.05 % | BatchNorm2d        |
| features.9.block.2.avgpool     |   288x7x7   |   288x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.9.block.2.fc1         |   288x1x1   |    72x1x1    |   0.03 % |   0.81 % | Conv2d k=1 p=0 s=1 |
| features.9.block.2.fc2         |    72x1x1   |   288x1x1    |   0.03 % |   0.82 % | Conv2d k=1 p=0 s=1 |
| features.9.block.2.activation  |    72x1x1   |    72x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.9.block.3.0           |   288x7x7   |    96x7x7    |   2.18 % |   1.08 % | Conv2d k=1 p=0 s=1 |
| features.9.block.3.1           |    96x7x7   |    96x7x7    |   0.03 % |   0.02 % | BatchNorm2d        |
| features.10.block.0.0          |    96x7x7   |   576x7x7    |   4.36 % |   2.16 % | Conv2d k=1 p=0 s=1 |
| features.10.block.0.1          |   576x7x7   |   576x7x7    |   0.18 % |   0.09 % | BatchNorm2d        |
| features.10.block.1.0          |   576x7x7   |   576x7x7    |   1.13 % |   0.56 % | Conv2d k=5 p=2 s=1 |
| features.10.block.1.1          |   576x7x7   |   576x7x7    |   0.18 % |   0.09 % | BatchNorm2d        |
| features.10.block.2.avgpool    |   576x7x7   |   576x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.10.block.2.fc1        |   576x1x1   |   144x1x1    |   0.13 % |   3.25 % | Conv2d k=1 p=0 s=1 |
| features.10.block.2.fc2        |   144x1x1   |   576x1x1    |   0.13 % |   3.27 % | Conv2d k=1 p=0 s=1 |
| features.10.block.2.activation |   144x1x1   |   144x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.10.block.3.0          |   576x7x7   |    96x7x7    |   4.36 % |   2.16 % | Conv2d k=1 p=0 s=1 |
| features.10.block.3.1          |    96x7x7   |    96x7x7    |   0.03 % |   0.02 % | BatchNorm2d        |
| features.11.block.0.0          |    96x7x7   |   576x7x7    |   4.36 % |   2.16 % | Conv2d k=1 p=0 s=1 |
| features.11.block.0.1          |   576x7x7   |   576x7x7    |   0.18 % |   0.09 % | BatchNorm2d        |
| features.11.block.1.0          |   576x7x7   |   576x7x7    |   1.13 % |   0.56 % | Conv2d k=5 p=2 s=1 |
| features.11.block.1.1          |   576x7x7   |   576x7x7    |   0.18 % |   0.09 % | BatchNorm2d        |
| features.11.block.2.avgpool    |   576x7x7   |   576x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.11.block.2.fc1        |   576x1x1   |   144x1x1    |   0.13 % |   3.25 % | Conv2d k=1 p=0 s=1 |
| features.11.block.2.fc2        |   144x1x1   |   576x1x1    |   0.13 % |   3.27 % | Conv2d k=1 p=0 s=1 |
| features.11.block.2.activation |   144x1x1   |   144x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.11.block.3.0          |   576x7x7   |    96x7x7    |   4.36 % |   2.16 % | Conv2d k=1 p=0 s=1 |
| features.11.block.3.1          |    96x7x7   |    96x7x7    |   0.03 % |   0.02 % | BatchNorm2d        |
| features.12.0                  |    96x7x7   |   576x7x7    |   4.36 % |   2.16 % | Conv2d k=1 p=0 s=1 |
| features.12.1                  |   576x7x7   |   576x7x7    |   0.18 % |   0.09 % | BatchNorm2d        |
| avgpool                        |   576x7x7   |   576x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0                   |     576     |     1024     |   0.95 % |  23.13 % | Linear             |
| classifier.2                   |     1024    |     1024     |   0.00 % |   0.00 % | Dropout            |
| classifier.3                   |     1024    |     1000     |   1.65 % |  40.12 % | Linear             |
| Total                          |  3x224x224  |     1000     |  62.17 M |   2.55 M | MobileNetV3        |