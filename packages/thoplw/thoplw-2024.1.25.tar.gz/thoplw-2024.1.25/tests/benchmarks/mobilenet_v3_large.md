| Name                           | Input shape | Output shape |     MACs |   Params | Description        |
|:------------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0.0                   |  3x224x224  |  16x112x112  |   2.31 % |   0.01 % | Conv2d k=3 p=1 s=2 |
| features.0.1                   |  16x112x112 |  16x112x112  |   0.34 % |   0.00 % | BatchNorm2d        |
| features.1.block.0.0           |  16x112x112 |  16x112x112  |   0.77 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1.block.0.1           |  16x112x112 |  16x112x112  |   0.34 % |   0.00 % | BatchNorm2d        |
| features.1.block.0.2           |  16x112x112 |  16x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.1.block.1.0           |  16x112x112 |  16x112x112  |   1.37 % |   0.00 % | Conv2d k=1 p=0 s=1 |
| features.1.block.1.1           |  16x112x112 |  16x112x112  |   0.34 % |   0.00 % | BatchNorm2d        |
| features.2.block.0.0           |  16x112x112 |  64x112x112  |   5.48 % |   0.02 % | Conv2d k=1 p=0 s=1 |
| features.2.block.0.1           |  64x112x112 |  64x112x112  |   1.37 % |   0.00 % | BatchNorm2d        |
| features.2.block.0.2           |  64x112x112 |  64x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.2.block.1.0           |  64x112x112 |   64x56x56   |   0.77 % |   0.01 % | Conv2d k=3 p=1 s=2 |
| features.2.block.1.1           |   64x56x56  |   64x56x56   |   0.34 % |   0.00 % | BatchNorm2d        |
| features.2.block.1.2           |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.2.block.2.0           |   64x56x56  |   24x56x56   |   2.06 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| features.2.block.2.1           |   24x56x56  |   24x56x56   |   0.13 % |   0.00 % | BatchNorm2d        |
| features.3.block.0.0           |   24x56x56  |   72x56x56   |   2.31 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| features.3.block.0.1           |   72x56x56  |   72x56x56   |   0.39 % |   0.01 % | BatchNorm2d        |
| features.3.block.0.2           |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.3.block.1.0           |   72x56x56  |   72x56x56   |   0.87 % |   0.01 % | Conv2d k=3 p=1 s=1 |
| features.3.block.1.1           |   72x56x56  |   72x56x56   |   0.39 % |   0.01 % | BatchNorm2d        |
| features.3.block.1.2           |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.3.block.2.0           |   72x56x56  |   24x56x56   |   2.31 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| features.3.block.2.1           |   24x56x56  |   24x56x56   |   0.13 % |   0.00 % | BatchNorm2d        |
| features.4.block.0.0           |   24x56x56  |   72x56x56   |   2.31 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| features.4.block.0.1           |   72x56x56  |   72x56x56   |   0.39 % |   0.01 % | BatchNorm2d        |
| features.4.block.0.2           |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.4.block.1.0           |   72x56x56  |   72x28x28   |   0.60 % |   0.03 % | Conv2d k=5 p=2 s=2 |
| features.4.block.1.1           |   72x28x28  |   72x28x28   |   0.10 % |   0.01 % | BatchNorm2d        |
| features.4.block.1.2           |   72x28x28  |   72x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.4.block.2.avgpool     |   72x28x28  |    72x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.4.block.2.fc1         |    72x1x1   |    24x1x1    |   0.00 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| features.4.block.2.fc2         |    24x1x1   |    72x1x1    |   0.00 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| features.4.block.2.activation  |    24x1x1   |    24x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.4.block.3.0           |   72x28x28  |   40x28x28   |   0.96 % |   0.05 % | Conv2d k=1 p=0 s=1 |
| features.4.block.3.1           |   40x28x28  |   40x28x28   |   0.05 % |   0.00 % | BatchNorm2d        |
| features.5.block.0.0           |   40x28x28  |  120x28x28   |   1.61 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.5.block.0.1           |  120x28x28  |  120x28x28   |   0.16 % |   0.01 % | BatchNorm2d        |
| features.5.block.0.2           |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.5.block.1.0           |  120x28x28  |  120x28x28   |   1.00 % |   0.05 % | Conv2d k=5 p=2 s=1 |
| features.5.block.1.1           |  120x28x28  |  120x28x28   |   0.16 % |   0.01 % | BatchNorm2d        |
| features.5.block.1.2           |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.5.block.2.avgpool     |  120x28x28  |   120x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.5.block.2.fc1         |   120x1x1   |    32x1x1    |   0.00 % |   0.07 % | Conv2d k=1 p=0 s=1 |
| features.5.block.2.fc2         |    32x1x1   |   120x1x1    |   0.00 % |   0.07 % | Conv2d k=1 p=0 s=1 |
| features.5.block.2.activation  |    32x1x1   |    32x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.5.block.3.0           |  120x28x28  |   40x28x28   |   1.61 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.5.block.3.1           |   40x28x28  |   40x28x28   |   0.05 % |   0.00 % | BatchNorm2d        |
| features.6.block.0.0           |   40x28x28  |  120x28x28   |   1.61 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.6.block.0.1           |  120x28x28  |  120x28x28   |   0.16 % |   0.01 % | BatchNorm2d        |
| features.6.block.0.2           |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.6.block.1.0           |  120x28x28  |  120x28x28   |   1.00 % |   0.05 % | Conv2d k=5 p=2 s=1 |
| features.6.block.1.1           |  120x28x28  |  120x28x28   |   0.16 % |   0.01 % | BatchNorm2d        |
| features.6.block.1.2           |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.6.block.2.avgpool     |  120x28x28  |   120x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.6.block.2.fc1         |   120x1x1   |    32x1x1    |   0.00 % |   0.07 % | Conv2d k=1 p=0 s=1 |
| features.6.block.2.fc2         |    32x1x1   |   120x1x1    |   0.00 % |   0.07 % | Conv2d k=1 p=0 s=1 |
| features.6.block.2.activation  |    32x1x1   |    32x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.6.block.3.0           |  120x28x28  |   40x28x28   |   1.61 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.6.block.3.1           |   40x28x28  |   40x28x28   |   0.05 % |   0.00 % | BatchNorm2d        |
| features.7.block.0.0           |   40x28x28  |  240x28x28   |   3.21 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.7.block.0.1           |  240x28x28  |  240x28x28   |   0.32 % |   0.02 % | BatchNorm2d        |
| features.7.block.1.0           |  240x28x28  |  240x14x14   |   0.18 % |   0.04 % | Conv2d k=3 p=1 s=2 |
| features.7.block.1.1           |  240x14x14  |  240x14x14   |   0.08 % |   0.02 % | BatchNorm2d        |
| features.7.block.2.0           |  240x14x14  |   80x14x14   |   1.61 % |   0.35 % | Conv2d k=1 p=0 s=1 |
| features.7.block.2.1           |   80x14x14  |   80x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.8.block.0.0           |   80x14x14  |  200x14x14   |   1.34 % |   0.29 % | Conv2d k=1 p=0 s=1 |
| features.8.block.0.1           |  200x14x14  |  200x14x14   |   0.07 % |   0.01 % | BatchNorm2d        |
| features.8.block.1.0           |  200x14x14  |  200x14x14   |   0.15 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.8.block.1.1           |  200x14x14  |  200x14x14   |   0.07 % |   0.01 % | BatchNorm2d        |
| features.8.block.2.0           |  200x14x14  |   80x14x14   |   1.34 % |   0.29 % | Conv2d k=1 p=0 s=1 |
| features.8.block.2.1           |   80x14x14  |   80x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.9.block.0.0           |   80x14x14  |  184x14x14   |   1.23 % |   0.27 % | Conv2d k=1 p=0 s=1 |
| features.9.block.0.1           |  184x14x14  |  184x14x14   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.9.block.1.0           |  184x14x14  |  184x14x14   |   0.14 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.9.block.1.1           |  184x14x14  |  184x14x14   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.9.block.2.0           |  184x14x14  |   80x14x14   |   1.23 % |   0.27 % | Conv2d k=1 p=0 s=1 |
| features.9.block.2.1           |   80x14x14  |   80x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.10.block.0.0          |   80x14x14  |  184x14x14   |   1.23 % |   0.27 % | Conv2d k=1 p=0 s=1 |
| features.10.block.0.1          |  184x14x14  |  184x14x14   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.10.block.1.0          |  184x14x14  |  184x14x14   |   0.14 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.10.block.1.1          |  184x14x14  |  184x14x14   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.10.block.2.0          |  184x14x14  |   80x14x14   |   1.23 % |   0.27 % | Conv2d k=1 p=0 s=1 |
| features.10.block.2.1          |   80x14x14  |   80x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.11.block.0.0          |   80x14x14  |  480x14x14   |   3.21 % |   0.70 % | Conv2d k=1 p=0 s=1 |
| features.11.block.0.1          |  480x14x14  |  480x14x14   |   0.16 % |   0.03 % | BatchNorm2d        |
| features.11.block.1.0          |  480x14x14  |  480x14x14   |   0.36 % |   0.08 % | Conv2d k=3 p=1 s=1 |
| features.11.block.1.1          |  480x14x14  |  480x14x14   |   0.16 % |   0.03 % | BatchNorm2d        |
| features.11.block.2.avgpool    |  480x14x14  |   480x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.11.block.2.fc1        |   480x1x1   |   120x1x1    |   0.02 % |   1.05 % | Conv2d k=1 p=0 s=1 |
| features.11.block.2.fc2        |   120x1x1   |   480x1x1    |   0.02 % |   1.05 % | Conv2d k=1 p=0 s=1 |
| features.11.block.2.activation |   120x1x1   |   120x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.11.block.3.0          |  480x14x14  |  112x14x14   |   4.50 % |   0.98 % | Conv2d k=1 p=0 s=1 |
| features.11.block.3.1          |  112x14x14  |  112x14x14   |   0.04 % |   0.01 % | BatchNorm2d        |
| features.12.block.0.0          |  112x14x14  |  672x14x14   |   6.30 % |   1.37 % | Conv2d k=1 p=0 s=1 |
| features.12.block.0.1          |  672x14x14  |  672x14x14   |   0.22 % |   0.05 % | BatchNorm2d        |
| features.12.block.1.0          |  672x14x14  |  672x14x14   |   0.51 % |   0.11 % | Conv2d k=3 p=1 s=1 |
| features.12.block.1.1          |  672x14x14  |  672x14x14   |   0.22 % |   0.05 % | BatchNorm2d        |
| features.12.block.2.avgpool    |  672x14x14  |   672x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.12.block.2.fc1        |   672x1x1   |   168x1x1    |   0.05 % |   2.05 % | Conv2d k=1 p=0 s=1 |
| features.12.block.2.fc2        |   168x1x1   |   672x1x1    |   0.05 % |   2.06 % | Conv2d k=1 p=0 s=1 |
| features.12.block.2.activation |   168x1x1   |   168x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.12.block.3.0          |  672x14x14  |  112x14x14   |   6.30 % |   1.37 % | Conv2d k=1 p=0 s=1 |
| features.12.block.3.1          |  112x14x14  |  112x14x14   |   0.04 % |   0.01 % | BatchNorm2d        |
| features.13.block.0.0          |  112x14x14  |  672x14x14   |   6.30 % |   1.37 % | Conv2d k=1 p=0 s=1 |
| features.13.block.0.1          |  672x14x14  |  672x14x14   |   0.22 % |   0.05 % | BatchNorm2d        |
| features.13.block.1.0          |  672x14x14  |   672x7x7    |   0.35 % |   0.31 % | Conv2d k=5 p=2 s=2 |
| features.13.block.1.1          |   672x7x7   |   672x7x7    |   0.06 % |   0.05 % | BatchNorm2d        |
| features.13.block.2.avgpool    |   672x7x7   |   672x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.13.block.2.fc1        |   672x1x1   |   168x1x1    |   0.05 % |   2.05 % | Conv2d k=1 p=0 s=1 |
| features.13.block.2.fc2        |   168x1x1   |   672x1x1    |   0.05 % |   2.06 % | Conv2d k=1 p=0 s=1 |
| features.13.block.2.activation |   168x1x1   |   168x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.13.block.3.0          |   672x7x7   |   160x7x7    |   2.25 % |   1.95 % | Conv2d k=1 p=0 s=1 |
| features.13.block.3.1          |   160x7x7   |   160x7x7    |   0.01 % |   0.01 % | BatchNorm2d        |
| features.14.block.0.0          |   160x7x7   |   960x7x7    |   3.21 % |   2.79 % | Conv2d k=1 p=0 s=1 |
| features.14.block.0.1          |   960x7x7   |   960x7x7    |   0.08 % |   0.07 % | BatchNorm2d        |
| features.14.block.1.0          |   960x7x7   |   960x7x7    |   0.50 % |   0.44 % | Conv2d k=5 p=2 s=1 |
| features.14.block.1.1          |   960x7x7   |   960x7x7    |   0.08 % |   0.07 % | BatchNorm2d        |
| features.14.block.2.avgpool    |   960x7x7   |   960x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.14.block.2.fc1        |   960x1x1   |   240x1x1    |   0.10 % |   4.19 % | Conv2d k=1 p=0 s=1 |
| features.14.block.2.fc2        |   240x1x1   |   960x1x1    |   0.10 % |   4.20 % | Conv2d k=1 p=0 s=1 |
| features.14.block.2.activation |   240x1x1   |   240x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.14.block.3.0          |   960x7x7   |   160x7x7    |   3.21 % |   2.79 % | Conv2d k=1 p=0 s=1 |
| features.14.block.3.1          |   160x7x7   |   160x7x7    |   0.01 % |   0.01 % | BatchNorm2d        |
| features.15.block.0.0          |   160x7x7   |   960x7x7    |   3.21 % |   2.79 % | Conv2d k=1 p=0 s=1 |
| features.15.block.0.1          |   960x7x7   |   960x7x7    |   0.08 % |   0.07 % | BatchNorm2d        |
| features.15.block.1.0          |   960x7x7   |   960x7x7    |   0.50 % |   0.44 % | Conv2d k=5 p=2 s=1 |
| features.15.block.1.1          |   960x7x7   |   960x7x7    |   0.08 % |   0.07 % | BatchNorm2d        |
| features.15.block.2.avgpool    |   960x7x7   |   960x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| features.15.block.2.fc1        |   960x1x1   |   240x1x1    |   0.10 % |   4.19 % | Conv2d k=1 p=0 s=1 |
| features.15.block.2.fc2        |   240x1x1   |   960x1x1    |   0.10 % |   4.20 % | Conv2d k=1 p=0 s=1 |
| features.15.block.2.activation |   240x1x1   |   240x1x1    |   0.00 % |   0.00 % | ReLU               |
| features.15.block.3.0          |   960x7x7   |   160x7x7    |   3.21 % |   2.79 % | Conv2d k=1 p=0 s=1 |
| features.15.block.3.1          |   160x7x7   |   160x7x7    |   0.01 % |   0.01 % | BatchNorm2d        |
| features.16.0                  |   160x7x7   |   960x7x7    |   3.21 % |   2.79 % | Conv2d k=1 p=0 s=1 |
| features.16.1                  |   960x7x7   |   960x7x7    |   0.08 % |   0.07 % | BatchNorm2d        |
| avgpool                        |   960x7x7   |   960x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0                   |     960     |     1280     |   0.53 % |  22.33 % | Linear             |
| classifier.2                   |     1280    |     1280     |   0.00 % |   0.00 % | Dropout            |
| classifier.3                   |     1280    |     1000     |   0.55 % |  23.26 % | Linear             |
| Total                          |  3x224x224  |     1000     | 234.21 M |   5.51 M | MobileNetV3        |