| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   0.56 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.08 % |   0.00 % | BatchNorm2d        |
| features.2   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.3   |  64x224x224 |  64x224x224  |  11.91 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.4   |  64x224x224 |  64x224x224  |   0.08 % |   0.00 % | BatchNorm2d        |
| features.5   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.6   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.7   |  64x112x112 | 128x112x112  |   5.96 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| features.8   | 128x112x112 | 128x112x112  |   0.04 % |   0.00 % | BatchNorm2d        |
| features.9   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.10  | 128x112x112 | 128x112x112  |  11.91 % |   0.11 % | Conv2d k=3 p=1 s=1 |
| features.11  | 128x112x112 | 128x112x112  |   0.04 % |   0.00 % | BatchNorm2d        |
| features.12  | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.13  | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.14  |  128x56x56  |  256x56x56   |   5.96 % |   0.21 % | Conv2d k=3 p=1 s=1 |
| features.15  |  256x56x56  |  256x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.16  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.17  |  256x56x56  |  256x56x56   |  11.91 % |   0.43 % | Conv2d k=3 p=1 s=1 |
| features.18  |  256x56x56  |  256x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.19  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.20  |  256x56x56  |  256x56x56   |  11.91 % |   0.43 % | Conv2d k=3 p=1 s=1 |
| features.21  |  256x56x56  |  256x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.22  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.23  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.24  |  256x28x28  |  512x28x28   |   5.96 % |   0.85 % | Conv2d k=3 p=1 s=1 |
| features.25  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.26  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.27  |  512x28x28  |  512x28x28   |  11.91 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.28  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.29  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.30  |  512x28x28  |  512x28x28   |  11.91 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.31  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.32  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.33  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.34  |  512x14x14  |  512x14x14   |   2.98 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.35  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.36  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.37  |  512x14x14  |  512x14x14   |   2.98 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.38  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.39  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.40  |  512x14x14  |  512x14x14   |   2.98 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.41  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.42  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.43  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   0.66 % |  74.27 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.11 % |  12.13 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.03 % |   2.96 % | Linear             |
| Total        |  3x224x224  |     1000     |  15.52 G | 138.37 M | VGG                |