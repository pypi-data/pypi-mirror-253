| Name                  | Input shape | Output shape |     MACs |   Params | Description        |
|:---------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| conv1                 |  3x224x224  |  64x112x112  |   0.52 % |   0.01 % | Conv2d k=7 p=3 s=2 |
| bn1                   |  64x112x112 |  64x112x112  |   0.01 % |   0.00 % | BatchNorm2d        |
| relu                  |  64x112x112 |  64x112x112  |   0.00 % |   0.00 % | ReLU               |
| maxpool               |  64x112x112 |   64x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| layer1.0.conv1        |   64x56x56  |  128x56x56   |   0.11 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| layer1.0.bn1          |  128x56x56  |  128x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.0.conv2        |  128x56x56  |  128x56x56   |   2.02 % |   0.12 % | Conv2d k=3 p=1 s=1 |
| layer1.0.bn2          |  128x56x56  |  128x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.0.conv3        |  128x56x56  |  256x56x56   |   0.45 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layer1.0.bn3          |  256x56x56  |  256x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.0.relu         |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.0.downsample.0 |   64x56x56  |  256x56x56   |   0.22 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| layer1.0.downsample.1 |  256x56x56  |  256x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv1        |  256x56x56  |  128x56x56   |   0.45 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layer1.1.bn1          |  128x56x56  |  128x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv2        |  128x56x56  |  128x56x56   |   2.02 % |   0.12 % | Conv2d k=3 p=1 s=1 |
| layer1.1.bn2          |  128x56x56  |  128x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.1.conv3        |  128x56x56  |  256x56x56   |   0.45 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layer1.1.bn3          |  256x56x56  |  256x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.1.relu         |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer1.2.conv1        |  256x56x56  |  128x56x56   |   0.45 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layer1.2.bn1          |  128x56x56  |  128x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.2.conv2        |  128x56x56  |  128x56x56   |   2.02 % |   0.12 % | Conv2d k=3 p=1 s=1 |
| layer1.2.bn2          |  128x56x56  |  128x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.2.conv3        |  128x56x56  |  256x56x56   |   0.45 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layer1.2.bn3          |  256x56x56  |  256x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer1.2.relu         |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| layer2.0.conv1        |  256x56x56  |  256x56x56   |   0.90 % |   0.05 % | Conv2d k=1 p=0 s=1 |
| layer2.0.bn1          |  256x56x56  |  256x56x56   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.0.conv2        |  256x56x56  |  256x28x28   |   2.02 % |   0.46 % | Conv2d k=3 p=1 s=2 |
| layer2.0.bn2          |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer2.0.conv3        |  256x28x28  |  512x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| layer2.0.bn3          |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.0.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.0.downsample.0 |  256x56x56  |  512x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=2 |
| layer2.0.downsample.1 |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.1.conv1        |  512x28x28  |  256x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| layer2.1.bn1          |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer2.1.conv2        |  256x28x28  |  256x28x28   |   2.02 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| layer2.1.bn2          |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer2.1.conv3        |  256x28x28  |  512x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| layer2.1.bn3          |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.1.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.2.conv1        |  512x28x28  |  256x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| layer2.2.bn1          |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer2.2.conv2        |  256x28x28  |  256x28x28   |   2.02 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| layer2.2.bn2          |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer2.2.conv3        |  256x28x28  |  512x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| layer2.2.bn3          |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.2.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer2.3.conv1        |  512x28x28  |  256x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| layer2.3.bn1          |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer2.3.conv2        |  256x28x28  |  256x28x28   |   2.02 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| layer2.3.bn2          |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer2.3.conv3        |  256x28x28  |  512x28x28   |   0.45 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| layer2.3.bn3          |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer2.3.relu         |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| layer3.0.conv1        |  512x28x28  |  512x28x28   |   0.90 % |   0.21 % | Conv2d k=1 p=0 s=1 |
| layer3.0.bn1          |  512x28x28  |  512x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| layer3.0.conv2        |  512x28x28  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=2 |
| layer3.0.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.0.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.0.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.0.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.0.downsample.0 |  512x28x28  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=2 |
| layer3.0.downsample.1 |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.1.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.1.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.1.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.1.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.1.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.1.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.1.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.2.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.2.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.2.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.2.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.2.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.2.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.2.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.3.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.3.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.3.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.3.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.3.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.3.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.3.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.4.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.4.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.4.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.4.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.4.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.4.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.4.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.5.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.5.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.5.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.5.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.5.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.5.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.5.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.6.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.6.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.6.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.6.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.6.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.6.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.6.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.7.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.7.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.7.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.7.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.7.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.7.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.7.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.8.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.8.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.8.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.8.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.8.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.8.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.8.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.9.conv1        |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.9.bn1          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.9.conv2        |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.9.bn2          |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.9.conv3        |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.9.bn3          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.9.relu         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.10.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.10.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.10.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.10.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.10.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.10.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.10.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.11.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.11.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.11.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.11.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.11.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.11.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.11.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.12.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.12.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.12.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.12.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.12.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.12.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.12.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.13.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.13.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.13.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.13.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.13.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.13.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.13.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.14.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.14.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.14.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.14.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.14.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.14.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.14.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.15.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.15.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.15.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.15.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.15.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.15.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.15.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.16.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.16.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.16.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.16.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.16.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.16.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.16.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.17.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.17.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.17.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.17.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.17.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.17.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.17.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.18.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.18.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.18.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.18.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.18.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.18.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.18.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.19.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.19.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.19.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.19.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.19.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.19.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.19.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.20.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.20.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.20.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.20.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.20.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.20.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.20.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.21.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.21.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.21.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.21.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.21.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.21.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.21.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer3.22.conv1       |  1024x14x14 |  512x14x14   |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.22.bn1         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.22.conv2       |  512x14x14  |  512x14x14   |   2.02 % |   1.86 % | Conv2d k=3 p=1 s=1 |
| layer3.22.bn2         |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.22.conv3       |  512x14x14  |  1024x14x14  |   0.45 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| layer3.22.bn3         |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer3.22.relu        |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| layer4.0.conv1        |  1024x14x14 |  1024x14x14  |   0.90 % |   0.83 % | Conv2d k=1 p=0 s=1 |
| layer4.0.bn1          |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | BatchNorm2d        |
| layer4.0.conv2        |  1024x14x14 |   1024x7x7   |   2.02 % |   7.43 % | Conv2d k=3 p=1 s=2 |
| layer4.0.bn2          |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer4.0.conv3        |   1024x7x7  |   2048x7x7   |   0.45 % |   1.65 % | Conv2d k=1 p=0 s=1 |
| layer4.0.bn3          |   2048x7x7  |   2048x7x7   |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.0.relu         |   2048x7x7  |   2048x7x7   |   0.00 % |   0.00 % | ReLU               |
| layer4.0.downsample.0 |  1024x14x14 |   2048x7x7   |   0.45 % |   1.65 % | Conv2d k=1 p=0 s=2 |
| layer4.0.downsample.1 |   2048x7x7  |   2048x7x7   |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.1.conv1        |   2048x7x7  |   1024x7x7   |   0.45 % |   1.65 % | Conv2d k=1 p=0 s=1 |
| layer4.1.bn1          |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer4.1.conv2        |   1024x7x7  |   1024x7x7   |   2.02 % |   7.43 % | Conv2d k=3 p=1 s=1 |
| layer4.1.bn2          |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer4.1.conv3        |   1024x7x7  |   2048x7x7   |   0.45 % |   1.65 % | Conv2d k=1 p=0 s=1 |
| layer4.1.bn3          |   2048x7x7  |   2048x7x7   |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.1.relu         |   2048x7x7  |   2048x7x7   |   0.00 % |   0.00 % | ReLU               |
| layer4.2.conv1        |   2048x7x7  |   1024x7x7   |   0.45 % |   1.65 % | Conv2d k=1 p=0 s=1 |
| layer4.2.bn1          |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer4.2.conv2        |   1024x7x7  |   1024x7x7   |   2.02 % |   7.43 % | Conv2d k=3 p=1 s=1 |
| layer4.2.bn2          |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | BatchNorm2d        |
| layer4.2.conv3        |   1024x7x7  |   2048x7x7   |   0.45 % |   1.65 % | Conv2d k=1 p=0 s=1 |
| layer4.2.bn3          |   2048x7x7  |   2048x7x7   |   0.00 % |   0.01 % | BatchNorm2d        |
| layer4.2.relu         |   2048x7x7  |   2048x7x7   |   0.00 % |   0.00 % | ReLU               |
| avgpool               |   2048x7x7  |   2048x1x1   |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| fc                    |     2048    |     1000     |   0.01 % |   1.61 % | Linear             |
| Total                 |  3x224x224  |     1000     |  22.84 G | 127.02 M | ResNet             |