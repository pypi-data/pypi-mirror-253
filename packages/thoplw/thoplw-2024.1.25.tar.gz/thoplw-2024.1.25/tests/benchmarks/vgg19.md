| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   0.44 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.2   |  64x224x224 |  64x224x224  |   9.42 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.3   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.4   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.5   |  64x112x112 | 128x112x112  |   4.71 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| features.6   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.7   | 128x112x112 | 128x112x112  |   9.42 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| features.8   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.9   | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.10  |  128x56x56  |  256x56x56   |   4.71 % |   0.21 % | Conv2d k=3 p=1 s=1 |
| features.11  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.12  |  256x56x56  |  256x56x56   |   9.42 % |   0.41 % | Conv2d k=3 p=1 s=1 |
| features.13  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.14  |  256x56x56  |  256x56x56   |   9.42 % |   0.41 % | Conv2d k=3 p=1 s=1 |
| features.15  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.16  |  256x56x56  |  256x56x56   |   9.42 % |   0.41 % | Conv2d k=3 p=1 s=1 |
| features.17  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.18  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.19  |  256x28x28  |  512x28x28   |   4.71 % |   0.82 % | Conv2d k=3 p=1 s=1 |
| features.20  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.21  |  512x28x28  |  512x28x28   |   9.42 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.22  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.23  |  512x28x28  |  512x28x28   |   9.42 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.24  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.25  |  512x28x28  |  512x28x28   |   9.42 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.26  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.27  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.28  |  512x14x14  |  512x14x14   |   2.36 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.29  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.30  |  512x14x14  |  512x14x14   |   2.36 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.31  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.32  |  512x14x14  |  512x14x14   |   2.36 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.33  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.34  |  512x14x14  |  512x14x14   |   2.36 % |   1.64 % | Conv2d k=3 p=1 s=1 |
| features.35  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.36  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   0.52 % |  71.53 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.09 % |  11.68 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.02 % |   2.85 % | Linear             |
| Total        |  3x224x224  |     1000     |  19.63 G | 143.67 M | VGG                |