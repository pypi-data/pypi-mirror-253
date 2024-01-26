| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   1.14 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.17 % |   0.00 % | BatchNorm2d        |
| features.2   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.3   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.4   |  64x112x112 | 128x112x112  |  12.11 % |   0.06 % | Conv2d k=3 p=1 s=1 |
| features.5   | 128x112x112 | 128x112x112  |   0.08 % |   0.00 % | BatchNorm2d        |
| features.6   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.7   | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.8   |  128x56x56  |  256x56x56   |  12.11 % |   0.22 % | Conv2d k=3 p=1 s=1 |
| features.9   |  256x56x56  |  256x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.10  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.11  |  256x56x56  |  256x56x56   |  24.21 % |   0.44 % | Conv2d k=3 p=1 s=1 |
| features.12  |  256x56x56  |  256x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.13  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.14  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.15  |  256x28x28  |  512x28x28   |  12.11 % |   0.89 % | Conv2d k=3 p=1 s=1 |
| features.16  |  512x28x28  |  512x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.17  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.18  |  512x28x28  |  512x28x28   |  24.21 % |   1.78 % | Conv2d k=3 p=1 s=1 |
| features.19  |  512x28x28  |  512x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.20  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.21  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.22  |  512x14x14  |  512x14x14   |   6.05 % |   1.78 % | Conv2d k=3 p=1 s=1 |
| features.23  |  512x14x14  |  512x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.24  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.25  |  512x14x14  |  512x14x14   |   6.05 % |   1.78 % | Conv2d k=3 p=1 s=1 |
| features.26  |  512x14x14  |  512x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.27  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.28  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   1.35 % |  77.34 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.22 % |  12.63 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.05 % |   3.08 % | Linear             |
| Total        |  3x224x224  |     1000     |   7.64 G | 132.87 M | VGG                |