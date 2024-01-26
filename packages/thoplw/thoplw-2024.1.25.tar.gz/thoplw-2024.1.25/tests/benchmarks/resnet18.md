| Name                  | Input shape | Output shape |     MACs |   Params | Description        |
|:---------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| conv1                 |  3x224x224  |  64x112x112  |   6.47 % |   0.08 % | Conv2d k=7 p=3 s=2 |
| bn1                   |  64x112x112 |  64x112x112  |   0.18 % |   0.00 % | BatchNorm2d        |
| relu                  |  64x112x112 |  64x112x112  |   0.00 % |   0.00 % | ReLU               |
| maxpool               |  64x112x112 |   64x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| layer1.0.conv1        |   64x56x56  |   64x56x56   |   6.34 % |   0.32 % | Conv2d k=3 p=1 s=1 |
| layer1.0.bn1          |   64x56x56  |   64x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| layer1.0.relu         |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.0.conv2        |   64x56x56  |   64x56x56   |   6.34 % |   0.32 % | Conv2d k=3 p=1 s=1 |
| layer1.0.bn2          |   64x56x56  |   64x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv1        |   64x56x56  |   64x56x56   |   6.34 % |   0.32 % | Conv2d k=3 p=1 s=1 |
| layer1.1.bn1          |   64x56x56  |   64x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| layer1.1.relu         |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.1.conv2        |   64x56x56  |   64x56x56   |   6.34 % |   0.32 % | Conv2d k=3 p=1 s=1 |
| layer1.1.bn2          |   64x56x56  |   64x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| layer2.0.conv1        |   64x56x56  |  128x28x28   |   3.17 % |   0.63 % | Conv2d k=3 p=1 s=2 |
| layer2.0.bn1          |  128x28x28  |  128x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer2.0.relu         |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.0.conv2        |  128x28x28  |  128x28x28   |   6.34 % |   1.26 % | Conv2d k=3 p=1 s=1 |
| layer2.0.bn2          |  128x28x28  |  128x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer2.0.downsample.0 |   64x56x56  |  128x28x28   |   0.35 % |   0.07 % | Conv2d k=1 p=0 s=2 |
| layer2.0.downsample.1 |  128x28x28  |  128x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer2.1.conv1        |  128x28x28  |  128x28x28   |   6.34 % |   1.26 % | Conv2d k=3 p=1 s=1 |
| layer2.1.bn1          |  128x28x28  |  128x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer2.1.relu         |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.1.conv2        |  128x28x28  |  128x28x28   |   6.34 % |   1.26 % | Conv2d k=3 p=1 s=1 |
| layer2.1.bn2          |  128x28x28  |  128x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer3.0.conv1        |  128x28x28  |  256x14x14   |   3.17 % |   2.52 % | Conv2d k=3 p=1 s=2 |
| layer3.0.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| layer3.0.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.0.conv2        |  256x14x14  |  256x14x14   |   6.34 % |   5.04 % | Conv2d k=3 p=1 s=1 |
| layer3.0.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| layer3.0.downsample.0 |  128x28x28  |  256x14x14   |   0.35 % |   0.28 % | Conv2d k=1 p=0 s=2 |
| layer3.0.downsample.1 |  256x14x14  |  256x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| layer3.1.conv1        |  256x14x14  |  256x14x14   |   6.34 % |   5.04 % | Conv2d k=3 p=1 s=1 |
| layer3.1.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| layer3.1.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.1.conv2        |  256x14x14  |  256x14x14   |   6.34 % |   5.04 % | Conv2d k=3 p=1 s=1 |
| layer3.1.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| layer4.0.conv1        |  256x14x14  |   512x7x7    |   3.17 % |  10.08 % | Conv2d k=3 p=1 s=2 |
| layer4.0.bn1          |   512x7x7   |   512x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layer4.0.relu         |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | ReLU               |
| layer4.0.conv2        |   512x7x7   |   512x7x7    |   6.34 % |  20.17 % | Conv2d k=3 p=1 s=1 |
| layer4.0.bn2          |   512x7x7   |   512x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layer4.0.downsample.0 |  256x14x14  |   512x7x7    |   0.35 % |   1.12 % | Conv2d k=1 p=0 s=2 |
| layer4.0.downsample.1 |   512x7x7   |   512x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layer4.1.conv1        |   512x7x7   |   512x7x7    |   6.34 % |  20.17 % | Conv2d k=3 p=1 s=1 |
| layer4.1.bn1          |   512x7x7   |   512x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layer4.1.relu         |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | ReLU               |
| layer4.1.conv2        |   512x7x7   |   512x7x7    |   6.34 % |  20.17 % | Conv2d k=3 p=1 s=1 |
| layer4.1.bn2          |   512x7x7   |   512x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| avgpool               |   512x7x7   |   512x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| fc                    |     512     |     1000     |   0.03 % |   4.38 % | Linear             |
| Total                 |  3x224x224  |     1000     |   1.82 G |  11.70 M | ResNet             |