| Name                  | Input shape | Output shape |     MACs |   Params | Description        |
|:---------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| conv1                 |  3x224x224  |  64x112x112  |   2.85 % |   0.04 % | Conv2d k=7 p=3 s=2 |
| bn1                   |  64x112x112 |  64x112x112  |   0.08 % |   0.00 % | BatchNorm2d        |
| relu                  |  64x112x112 |  64x112x112  |   0.00 % |   0.00 % | ReLU               |
| maxpool               |  64x112x112 |   64x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| layer1.0.conv1        |   64x56x56  |   64x56x56   |   0.31 % |   0.02 % | Conv2d k=1 p=0 s=1 |
| layer1.0.bn1          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.0.conv2        |   64x56x56  |   64x56x56   |   2.80 % |   0.14 % | Conv2d k=3 p=1 s=1 |
| layer1.0.bn2          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.0.conv3        |   64x56x56  |  256x56x56   |   1.24 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| layer1.0.bn3          |  256x56x56  |  256x56x56   |   0.08 % |   0.00 % | BatchNorm2d        |
| layer1.0.relu         |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.0.downsample.0 |   64x56x56  |  256x56x56   |   1.24 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| layer1.0.downsample.1 |  256x56x56  |  256x56x56   |   0.08 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv1        |  256x56x56  |   64x56x56   |   1.24 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| layer1.1.bn1          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv2        |   64x56x56  |   64x56x56   |   2.80 % |   0.14 % | Conv2d k=3 p=1 s=1 |
| layer1.1.bn2          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv3        |   64x56x56  |  256x56x56   |   1.24 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| layer1.1.bn3          |  256x56x56  |  256x56x56   |   0.08 % |   0.00 % | BatchNorm2d        |
| layer1.1.relu         |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.2.conv1        |  256x56x56  |   64x56x56   |   1.24 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| layer1.2.bn1          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.2.conv2        |   64x56x56  |   64x56x56   |   2.80 % |   0.14 % | Conv2d k=3 p=1 s=1 |
| layer1.2.bn2          |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer1.2.conv3        |   64x56x56  |  256x56x56   |   1.24 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| layer1.2.bn3          |  256x56x56  |  256x56x56   |   0.08 % |   0.00 % | BatchNorm2d        |
| layer1.2.relu         |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer2.0.conv1        |  256x56x56  |  128x56x56   |   2.49 % |   0.13 % | Conv2d k=1 p=0 s=1 |
| layer2.0.bn1          |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| layer2.0.conv2        |  128x56x56  |  128x28x28   |   2.80 % |   0.58 % | Conv2d k=3 p=1 s=2 |
| layer2.0.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.0.conv3        |  128x28x28  |  512x28x28   |   1.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layer2.0.bn3          |  512x28x28  |  512x28x28   |   0.04 % |   0.01 % | BatchNorm2d        |
| layer2.0.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.0.downsample.0 |  256x56x56  |  512x28x28   |   2.49 % |   0.51 % | Conv2d k=1 p=0 s=2 |
| layer2.0.downsample.1 |  512x28x28  |  512x28x28   |   0.04 % |   0.01 % | BatchNorm2d        |
| layer2.1.conv1        |  512x28x28  |  128x28x28   |   1.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layer2.1.bn1          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.1.conv2        |  128x28x28  |  128x28x28   |   2.80 % |   0.58 % | Conv2d k=3 p=1 s=1 |
| layer2.1.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.1.conv3        |  128x28x28  |  512x28x28   |   1.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layer2.1.bn3          |  512x28x28  |  512x28x28   |   0.04 % |   0.01 % | BatchNorm2d        |
| layer2.1.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.2.conv1        |  512x28x28  |  128x28x28   |   1.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layer2.2.bn1          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.2.conv2        |  128x28x28  |  128x28x28   |   2.80 % |   0.58 % | Conv2d k=3 p=1 s=1 |
| layer2.2.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.2.conv3        |  128x28x28  |  512x28x28   |   1.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layer2.2.bn3          |  512x28x28  |  512x28x28   |   0.04 % |   0.01 % | BatchNorm2d        |
| layer2.2.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.3.conv1        |  512x28x28  |  128x28x28   |   1.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layer2.3.bn1          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.3.conv2        |  128x28x28  |  128x28x28   |   2.80 % |   0.58 % | Conv2d k=3 p=1 s=1 |
| layer2.3.bn2          |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.3.conv3        |  128x28x28  |  512x28x28   |   1.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layer2.3.bn3          |  512x28x28  |  512x28x28   |   0.04 % |   0.01 % | BatchNorm2d        |
| layer2.3.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer3.0.conv1        |  512x28x28  |  256x28x28   |   2.49 % |   0.51 % | Conv2d k=1 p=0 s=1 |
| layer3.0.bn1          |  256x28x28  |  256x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| layer3.0.conv2        |  256x28x28  |  256x14x14   |   2.80 % |   2.30 % | Conv2d k=3 p=1 s=2 |
| layer3.0.bn2          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.0.conv3        |  256x14x14  |  1024x14x14  |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.0.bn3          |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| layer3.0.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.0.downsample.0 |  512x28x28  |  1024x14x14  |   2.49 % |   2.05 % | Conv2d k=1 p=0 s=2 |
| layer3.0.downsample.1 |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| layer3.1.conv1        |  1024x14x14 |  256x14x14   |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.1.bn1          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.1.conv2        |  256x14x14  |  256x14x14   |   2.80 % |   2.30 % | Conv2d k=3 p=1 s=1 |
| layer3.1.bn2          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.1.conv3        |  256x14x14  |  1024x14x14  |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.1.bn3          |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| layer3.1.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.2.conv1        |  1024x14x14 |  256x14x14   |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.2.bn1          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.2.conv2        |  256x14x14  |  256x14x14   |   2.80 % |   2.30 % | Conv2d k=3 p=1 s=1 |
| layer3.2.bn2          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.2.conv3        |  256x14x14  |  1024x14x14  |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.2.bn3          |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| layer3.2.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.3.conv1        |  1024x14x14 |  256x14x14   |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.3.bn1          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.3.conv2        |  256x14x14  |  256x14x14   |   2.80 % |   2.30 % | Conv2d k=3 p=1 s=1 |
| layer3.3.bn2          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.3.conv3        |  256x14x14  |  1024x14x14  |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.3.bn3          |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| layer3.3.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.4.conv1        |  1024x14x14 |  256x14x14   |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.4.bn1          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.4.conv2        |  256x14x14  |  256x14x14   |   2.80 % |   2.30 % | Conv2d k=3 p=1 s=1 |
| layer3.4.bn2          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.4.conv3        |  256x14x14  |  1024x14x14  |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.4.bn3          |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| layer3.4.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.5.conv1        |  1024x14x14 |  256x14x14   |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.5.bn1          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.5.conv2        |  256x14x14  |  256x14x14   |   2.80 % |   2.30 % | Conv2d k=3 p=1 s=1 |
| layer3.5.bn2          |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.5.conv3        |  256x14x14  |  1024x14x14  |   1.24 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| layer3.5.bn3          |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| layer3.5.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer4.0.conv1        |  1024x14x14 |  512x14x14   |   2.49 % |   2.05 % | Conv2d k=1 p=0 s=1 |
| layer4.0.bn1          |  512x14x14  |  512x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| layer4.0.conv2        |  512x14x14  |   512x7x7    |   2.80 % |   9.21 % | Conv2d k=3 p=1 s=2 |
| layer4.0.bn2          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.0.conv3        |   512x7x7   |   2048x7x7   |   1.24 % |   4.09 % | Conv2d k=1 p=0 s=1 |
| layer4.0.bn3          |   2048x7x7  |   2048x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| layer4.0.relu         |   2048x7x7  |   2048x7x7   |   0.00 % |   0.00 % | ReLU               |
| layer4.0.downsample.0 |  1024x14x14 |   2048x7x7   |   2.49 % |   8.19 % | Conv2d k=1 p=0 s=2 |
| layer4.0.downsample.1 |   2048x7x7  |   2048x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| layer4.1.conv1        |   2048x7x7  |   512x7x7    |   1.24 % |   4.09 % | Conv2d k=1 p=0 s=1 |
| layer4.1.bn1          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.1.conv2        |   512x7x7   |   512x7x7    |   2.80 % |   9.21 % | Conv2d k=3 p=1 s=1 |
| layer4.1.bn2          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.1.conv3        |   512x7x7   |   2048x7x7   |   1.24 % |   4.09 % | Conv2d k=1 p=0 s=1 |
| layer4.1.bn3          |   2048x7x7  |   2048x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| layer4.1.relu         |   2048x7x7  |   2048x7x7   |   0.00 % |   0.00 % | ReLU               |
| layer4.2.conv1        |   2048x7x7  |   512x7x7    |   1.24 % |   4.09 % | Conv2d k=1 p=0 s=1 |
| layer4.2.bn1          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.2.conv2        |   512x7x7   |   512x7x7    |   2.80 % |   9.21 % | Conv2d k=3 p=1 s=1 |
| layer4.2.bn2          |   512x7x7   |   512x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.2.conv3        |   512x7x7   |   2048x7x7   |   1.24 % |   4.09 % | Conv2d k=1 p=0 s=1 |
| layer4.2.bn3          |   2048x7x7  |   2048x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| layer4.2.relu         |   2048x7x7  |   2048x7x7   |   0.00 % |   0.00 % | ReLU               |
| avgpool               |   2048x7x7  |   2048x1x1   |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| fc                    |     2048    |     1000     |   0.05 % |   8.00 % | Linear             |
| Total                 |  3x224x224  |     1000     |   4.13 G |  25.61 M | ResNet             |