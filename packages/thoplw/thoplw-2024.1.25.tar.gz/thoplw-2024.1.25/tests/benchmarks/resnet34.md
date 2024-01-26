| Name                  | Input shape | Output shape |     MACs |   Params | Description        |
|:---------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| conv1                 |  3x224x224  |  64x112x112  |   3.21 % |   0.04 % | Conv2d k=7 p=3 s=2 |
| bn1                   |  64x112x112 |  64x112x112  |   0.09 % |   0.00 % | BatchNorm2d        |
| relu                  |  64x112x112 |  64x112x112  |   0.00 % |   0.00 % | ReLU               |
| maxpool               |  64x112x112 |   64x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| layer1.0.conv1        |   64x56x56  |   64x56x56   |   3.14 % |   0.17 % | Conv2d k=3 p=1 s=1 |
| layer1.0.bn1          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.0.relu         |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.0.conv2        |   64x56x56  |   64x56x56   |   3.14 % |   0.17 % | Conv2d k=3 p=1 s=1 |
| layer1.0.bn2          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv1        |   64x56x56  |   64x56x56   |   3.14 % |   0.17 % | Conv2d k=3 p=1 s=1 |
| layer1.1.bn1          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.1.relu         |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.1.conv2        |   64x56x56  |   64x56x56   |   3.14 % |   0.17 % | Conv2d k=3 p=1 s=1 |
| layer1.1.bn2          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.2.conv1        |   64x56x56  |   64x56x56   |   3.14 % |   0.17 % | Conv2d k=3 p=1 s=1 |
| layer1.2.bn1          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.2.relu         |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.2.conv2        |   64x56x56  |   64x56x56   |   3.14 % |   0.17 % | Conv2d k=3 p=1 s=1 |
| layer1.2.bn2          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer2.0.conv1        |   64x56x56  |  128x28x28   |   1.57 % |   0.34 % | Conv2d k=3 p=1 s=2 |
| layer2.0.bn1          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.0.relu         |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.0.conv2        |  128x28x28  |  128x28x28   |   3.14 % |   0.68 % | Conv2d k=3 p=1 s=1 |
| layer2.0.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.0.downsample.0 |   64x56x56  |  128x28x28   |   0.17 % |   0.04 % | Conv2d k=1 p=0 s=2 |
| layer2.0.downsample.1 |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.1.conv1        |  128x28x28  |  128x28x28   |   3.14 % |   0.68 % | Conv2d k=3 p=1 s=1 |
| layer2.1.bn1          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.1.relu         |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.1.conv2        |  128x28x28  |  128x28x28   |   3.14 % |   0.68 % | Conv2d k=3 p=1 s=1 |
| layer2.1.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.2.conv1        |  128x28x28  |  128x28x28   |   3.14 % |   0.68 % | Conv2d k=3 p=1 s=1 |
| layer2.2.bn1          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.2.relu         |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.2.conv2        |  128x28x28  |  128x28x28   |   3.14 % |   0.68 % | Conv2d k=3 p=1 s=1 |
| layer2.2.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.3.conv1        |  128x28x28  |  128x28x28   |   3.14 % |   0.68 % | Conv2d k=3 p=1 s=1 |
| layer2.3.bn1          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.3.relu         |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.3.conv2        |  128x28x28  |  128x28x28   |   3.14 % |   0.68 % | Conv2d k=3 p=1 s=1 |
| layer2.3.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.0.conv1        |  128x28x28  |  256x14x14   |   1.57 % |   1.35 % | Conv2d k=3 p=1 s=2 |
| layer3.0.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.0.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.0.conv2        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.0.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.0.downsample.0 |  128x28x28  |  256x14x14   |   0.17 % |   0.15 % | Conv2d k=1 p=0 s=2 |
| layer3.0.downsample.1 |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.1.conv1        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.1.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.1.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.1.conv2        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.1.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.2.conv1        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.2.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.2.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.2.conv2        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.2.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.3.conv1        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.3.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.3.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.3.conv2        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.3.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.4.conv1        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.4.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.4.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.4.conv2        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.4.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.5.conv1        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.5.bn1          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.5.relu         |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| layer3.5.conv2        |  256x14x14  |  256x14x14   |   3.14 % |   2.70 % | Conv2d k=3 p=1 s=1 |
| layer3.5.bn2          |  256x14x14  |  256x14x14   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer4.0.conv1        |  256x14x14  |   512x7x7    |   1.57 % |   5.41 % | Conv2d k=3 p=1 s=2 |
| layer4.0.bn1          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.0.relu         |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | ReLU               |
| layer4.0.conv2        |   512x7x7   |   512x7x7    |   3.14 % |  10.82 % | Conv2d k=3 p=1 s=1 |
| layer4.0.bn2          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.0.downsample.0 |  256x14x14  |   512x7x7    |   0.17 % |   0.60 % | Conv2d k=1 p=0 s=2 |
| layer4.0.downsample.1 |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.1.conv1        |   512x7x7   |   512x7x7    |   3.14 % |  10.82 % | Conv2d k=3 p=1 s=1 |
| layer4.1.bn1          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.1.relu         |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | ReLU               |
| layer4.1.conv2        |   512x7x7   |   512x7x7    |   3.14 % |  10.82 % | Conv2d k=3 p=1 s=1 |
| layer4.1.bn2          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.2.conv1        |   512x7x7   |   512x7x7    |   3.14 % |  10.82 % | Conv2d k=3 p=1 s=1 |
| layer4.2.bn1          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.2.relu         |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | ReLU               |
| layer4.2.conv2        |   512x7x7   |   512x7x7    |   3.14 % |  10.82 % | Conv2d k=3 p=1 s=1 |
| layer4.2.bn2          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| avgpool               |   512x7x7   |   512x1x1    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| fc                    |     512     |     1000     |   0.01 % |   2.35 % | Linear             |
| Total                 |  3x224x224  |     1000     |   3.68 G |  21.81 M | ResNet             |