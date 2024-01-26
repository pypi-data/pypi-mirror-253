| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   0.44 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.07 % |   0.00 % | BatchNorm2d        |
| features.2   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.3   |  64x224x224 |  64x224x224  |   9.39 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.4   |  64x224x224 |  64x224x224  |   0.07 % |   0.00 % | BatchNorm2d        |
| features.5   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.6   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.7   |  64x112x112 | 128x112x112  |   4.70 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| features.8   | 128x112x112 | 128x112x112  |   0.03 % |   0.00 % | BatchNorm2d        |
| features.9   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.10  | 128x112x112 | 128x112x112  |   9.39 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| features.11  | 128x112x112 | 128x112x112  |   0.03 % |   0.00 % | BatchNorm2d        |
| features.12  | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.13  | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.14  |  128x56x56  |  256x56x56   |   4.70 % |   0.21 % | Conv2d k=3 p=1 s=1 |
| features.15  |  256x56x56  |  256x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.16  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.17  |  256x56x56  |  256x56x56   |   9.39 % |   0.41 % | Conv2d k=3 p=1 s=1 |
| features.18  |  256x56x56  |  256x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.19  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.20  |  256x56x56  |  256x56x56   |   9.39 % |   0.41 % | Conv2d k=3 p=1 s=1 |
| features.21  |  256x56x56  |  256x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.22  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.23  |  256x56x56  |  256x56x56   |   9.39 % |   0.41 % | Conv2d k=3 p=1 s=1 |
| features.24  |  256x56x56  |  256x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.25  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.26  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.27  |  256x28x28  |  512x28x28   |   4.70 % |   0.82 % | Conv2d k=3 p=1 s=1 |
| features.28  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.29  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.30  |  512x28x28  |  512x28x28   |   9.39 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.31  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.32  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.33  |  512x28x28  |  512x28x28   |   9.39 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.34  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.35  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.36  |  512x28x28  |  512x28x28   |   9.39 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.37  |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.38  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.39  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.40  |  512x14x14  |  512x14x14   |   2.35 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.41  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.42  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.43  |  512x14x14  |  512x14x14   |   2.35 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.44  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.45  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.46  |  512x14x14  |  512x14x14   |   2.35 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.47  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.48  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.49  |  512x14x14  |  512x14x14   |   2.35 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.50  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.51  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.52  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   0.52 % |  71.52 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.09 % |  11.68 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.02 % |   2.85 % | Linear             |
| Total        |  3x224x224  |     1000     |  19.69 G | 143.69 M | VGG                |