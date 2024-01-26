| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   0.76 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.11 % |   0.00 % | BatchNorm2d        |
| features.2   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.3   |  64x224x224 |  64x224x224  |  16.29 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.4   |  64x224x224 |  64x224x224  |   0.11 % |   0.00 % | BatchNorm2d        |
| features.5   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.6   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.7   |  64x112x112 | 128x112x112  |   8.14 % |   0.06 % | Conv2d k=3 p=1 s=1 |
| features.8   | 128x112x112 | 128x112x112  |   0.06 % |   0.00 % | BatchNorm2d        |
| features.9   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.10  | 128x112x112 | 128x112x112  |  16.29 % |   0.11 % | Conv2d k=3 p=1 s=1 |
| features.11  | 128x112x112 | 128x112x112  |   0.06 % |   0.00 % | BatchNorm2d        |
| features.12  | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.13  | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.14  |  128x56x56  |  256x56x56   |   8.14 % |   0.22 % | Conv2d k=3 p=1 s=1 |
| features.15  |  256x56x56  |  256x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.16  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.17  |  256x56x56  |  256x56x56   |  16.29 % |   0.44 % | Conv2d k=3 p=1 s=1 |
| features.18  |  256x56x56  |  256x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.19  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.20  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.21  |  256x28x28  |  512x28x28   |   8.14 % |   0.89 % | Conv2d k=3 p=1 s=1 |
| features.22  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.23  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.24  |  512x28x28  |  512x28x28   |  16.29 % |   1.77 % | Conv2d k=3 p=1 s=1 |
| features.25  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.26  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.27  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.28  |  512x14x14  |  512x14x14   |   4.07 % |   1.77 % | Conv2d k=3 p=1 s=1 |
| features.29  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.30  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.31  |  512x14x14  |  512x14x14   |   4.07 % |   1.77 % | Conv2d k=3 p=1 s=1 |
| features.32  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.33  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.34  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   0.90 % |  77.23 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.15 % |  12.61 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.04 % |   3.08 % | Linear             |
| Total        |  3x224x224  |     1000     |  11.36 G | 133.06 M | VGG                |