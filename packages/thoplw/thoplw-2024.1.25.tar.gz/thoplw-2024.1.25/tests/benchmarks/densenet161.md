| Name                                    | Input shape | Output shape |     MACs |   Params | Description        |
|:---------------------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.conv0                          |  3x224x224  |  96x112x112  |   2.26 % |   0.05 % | Conv2d k=7 p=3 s=2 |
| features.norm0                          |  96x112x112 |  96x112x112  |   0.06 % |   0.00 % | BatchNorm2d        |
| features.relu0                          |  96x112x112 |  96x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.pool0                          |  96x112x112 |   96x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.denseblock1.denselayer1.norm1  |   96x56x56  |   96x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer1.relu1  |   96x56x56  |   96x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer1.conv1  |   96x56x56  |  192x56x56   |   0.74 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer1.norm2  |  192x56x56  |  192x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer1.relu2  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer1.conv2  |  192x56x56  |   48x56x56   |   3.32 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer2.norm1  |  144x56x56  |  144x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer2.relu1  |  144x56x56  |  144x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer2.conv1  |  144x56x56  |  192x56x56   |   1.11 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer2.norm2  |  192x56x56  |  192x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer2.relu2  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer2.conv2  |  192x56x56  |   48x56x56   |   3.32 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer3.norm1  |  192x56x56  |  192x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer3.relu1  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer3.conv1  |  192x56x56  |  192x56x56   |   1.47 % |   0.13 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer3.norm2  |  192x56x56  |  192x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer3.relu2  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer3.conv2  |  192x56x56  |   48x56x56   |   3.32 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer4.norm1  |  240x56x56  |  240x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer4.relu1  |  240x56x56  |  240x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer4.conv1  |  240x56x56  |  192x56x56   |   1.84 % |   0.16 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer4.norm2  |  192x56x56  |  192x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer4.relu2  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer4.conv2  |  192x56x56  |   48x56x56   |   3.32 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer5.norm1  |  288x56x56  |  288x56x56   |   0.05 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer5.relu1  |  288x56x56  |  288x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer5.conv1  |  288x56x56  |  192x56x56   |   2.21 % |   0.19 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer5.norm2  |  192x56x56  |  192x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer5.relu2  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer5.conv2  |  192x56x56  |   48x56x56   |   3.32 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer6.norm1  |  336x56x56  |  336x56x56   |   0.05 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer6.relu1  |  336x56x56  |  336x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer6.conv1  |  336x56x56  |  192x56x56   |   2.58 % |   0.22 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer6.norm2  |  192x56x56  |  192x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer6.relu2  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer6.conv2  |  192x56x56  |   48x56x56   |   3.32 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.transition1.norm               |  384x56x56  |  384x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.transition1.relu               |  384x56x56  |  384x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.transition1.conv               |  384x56x56  |  192x56x56   |   2.95 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| features.transition1.pool               |  192x56x56  |  192x28x28   |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock2.denselayer1.norm1  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer1.relu1  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer1.conv1  |  192x28x28  |  192x28x28   |   0.37 % |   0.13 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer1.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer1.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer1.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer2.norm1  |  240x28x28  |  240x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer2.relu1  |  240x28x28  |  240x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer2.conv1  |  240x28x28  |  192x28x28   |   0.46 % |   0.16 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer2.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer2.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer2.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer3.norm1  |  288x28x28  |  288x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer3.relu1  |  288x28x28  |  288x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer3.conv1  |  288x28x28  |  192x28x28   |   0.55 % |   0.19 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer3.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer3.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer3.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer4.norm1  |  336x28x28  |  336x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer4.relu1  |  336x28x28  |  336x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer4.conv1  |  336x28x28  |  192x28x28   |   0.64 % |   0.22 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer4.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer4.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer4.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer5.norm1  |  384x28x28  |  384x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer5.relu1  |  384x28x28  |  384x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer5.conv1  |  384x28x28  |  192x28x28   |   0.74 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer5.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer5.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer5.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer6.norm1  |  432x28x28  |  432x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer6.relu1  |  432x28x28  |  432x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer6.conv1  |  432x28x28  |  192x28x28   |   0.83 % |   0.29 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer6.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer6.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer6.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer7.norm1  |  480x28x28  |  480x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer7.relu1  |  480x28x28  |  480x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer7.conv1  |  480x28x28  |  192x28x28   |   0.92 % |   0.32 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer7.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer7.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer7.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer8.norm1  |  528x28x28  |  528x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer8.relu1  |  528x28x28  |  528x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer8.conv1  |  528x28x28  |  192x28x28   |   1.01 % |   0.35 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer8.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer8.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer8.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer9.norm1  |  576x28x28  |  576x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer9.relu1  |  576x28x28  |  576x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer9.conv1  |  576x28x28  |  192x28x28   |   1.11 % |   0.38 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer9.norm2  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer9.relu2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer9.conv2  |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer10.norm1 |  624x28x28  |  624x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer10.relu1 |  624x28x28  |  624x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer10.conv1 |  624x28x28  |  192x28x28   |   1.20 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer10.norm2 |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer10.relu2 |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer10.conv2 |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer11.norm1 |  672x28x28  |  672x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer11.relu1 |  672x28x28  |  672x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer11.conv1 |  672x28x28  |  192x28x28   |   1.29 % |   0.45 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer11.norm2 |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer11.relu2 |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer11.conv2 |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer12.norm1 |  720x28x28  |  720x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer12.relu1 |  720x28x28  |  720x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer12.conv1 |  720x28x28  |  192x28x28   |   1.38 % |   0.48 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer12.norm2 |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer12.relu2 |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer12.conv2 |  192x28x28  |   48x28x28   |   0.83 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.transition2.norm               |  768x28x28  |  768x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.transition2.relu               |  768x28x28  |  768x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.transition2.conv               |  768x28x28  |  384x28x28   |   2.95 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| features.transition2.pool               |  384x28x28  |  384x14x14   |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock3.denselayer1.norm1  |  384x14x14  |  384x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer1.relu1  |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer1.conv1  |  384x14x14  |  192x14x14   |   0.18 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer1.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer1.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer1.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer2.norm1  |  432x14x14  |  432x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer2.relu1  |  432x14x14  |  432x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer2.conv1  |  432x14x14  |  192x14x14   |   0.21 % |   0.29 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer2.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer2.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer2.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer3.norm1  |  480x14x14  |  480x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer3.relu1  |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer3.conv1  |  480x14x14  |  192x14x14   |   0.23 % |   0.32 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer3.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer3.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer3.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer4.norm1  |  528x14x14  |  528x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer4.relu1  |  528x14x14  |  528x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer4.conv1  |  528x14x14  |  192x14x14   |   0.25 % |   0.35 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer4.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer4.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer4.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer5.norm1  |  576x14x14  |  576x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer5.relu1  |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer5.conv1  |  576x14x14  |  192x14x14   |   0.28 % |   0.38 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer5.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer5.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer5.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer6.norm1  |  624x14x14  |  624x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer6.relu1  |  624x14x14  |  624x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer6.conv1  |  624x14x14  |  192x14x14   |   0.30 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer6.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer6.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer6.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer7.norm1  |  672x14x14  |  672x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer7.relu1  |  672x14x14  |  672x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer7.conv1  |  672x14x14  |  192x14x14   |   0.32 % |   0.45 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer7.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer7.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer7.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer8.norm1  |  720x14x14  |  720x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer8.relu1  |  720x14x14  |  720x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer8.conv1  |  720x14x14  |  192x14x14   |   0.35 % |   0.48 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer8.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer8.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer8.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer9.norm1  |  768x14x14  |  768x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer9.relu1  |  768x14x14  |  768x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer9.conv1  |  768x14x14  |  192x14x14   |   0.37 % |   0.51 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer9.norm2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer9.relu2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer9.conv2  |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer10.norm1 |  816x14x14  |  816x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer10.relu1 |  816x14x14  |  816x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer10.conv1 |  816x14x14  |  192x14x14   |   0.39 % |   0.54 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer10.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer10.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer10.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer11.norm1 |  864x14x14  |  864x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer11.relu1 |  864x14x14  |  864x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer11.conv1 |  864x14x14  |  192x14x14   |   0.41 % |   0.57 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer11.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer11.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer11.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer12.norm1 |  912x14x14  |  912x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer12.relu1 |  912x14x14  |  912x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer12.conv1 |  912x14x14  |  192x14x14   |   0.44 % |   0.61 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer12.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer12.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer12.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer13.norm1 |  960x14x14  |  960x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer13.relu1 |  960x14x14  |  960x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer13.conv1 |  960x14x14  |  192x14x14   |   0.46 % |   0.64 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer13.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer13.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer13.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer14.norm1 |  1008x14x14 |  1008x14x14  |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer14.relu1 |  1008x14x14 |  1008x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer14.conv1 |  1008x14x14 |  192x14x14   |   0.48 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer14.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer14.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer14.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer15.norm1 |  1056x14x14 |  1056x14x14  |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer15.relu1 |  1056x14x14 |  1056x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer15.conv1 |  1056x14x14 |  192x14x14   |   0.51 % |   0.70 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer15.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer15.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer15.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer16.norm1 |  1104x14x14 |  1104x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer16.relu1 |  1104x14x14 |  1104x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer16.conv1 |  1104x14x14 |  192x14x14   |   0.53 % |   0.73 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer16.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer16.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer16.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer17.norm1 |  1152x14x14 |  1152x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer17.relu1 |  1152x14x14 |  1152x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer17.conv1 |  1152x14x14 |  192x14x14   |   0.55 % |   0.77 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer17.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer17.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer17.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer18.norm1 |  1200x14x14 |  1200x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer18.relu1 |  1200x14x14 |  1200x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer18.conv1 |  1200x14x14 |  192x14x14   |   0.58 % |   0.80 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer18.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer18.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer18.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer19.norm1 |  1248x14x14 |  1248x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer19.relu1 |  1248x14x14 |  1248x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer19.conv1 |  1248x14x14 |  192x14x14   |   0.60 % |   0.83 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer19.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer19.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer19.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer20.norm1 |  1296x14x14 |  1296x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer20.relu1 |  1296x14x14 |  1296x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer20.conv1 |  1296x14x14 |  192x14x14   |   0.62 % |   0.86 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer20.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer20.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer20.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer21.norm1 |  1344x14x14 |  1344x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer21.relu1 |  1344x14x14 |  1344x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer21.conv1 |  1344x14x14 |  192x14x14   |   0.64 % |   0.89 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer21.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer21.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer21.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer22.norm1 |  1392x14x14 |  1392x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer22.relu1 |  1392x14x14 |  1392x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer22.conv1 |  1392x14x14 |  192x14x14   |   0.67 % |   0.92 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer22.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer22.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer22.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer23.norm1 |  1440x14x14 |  1440x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer23.relu1 |  1440x14x14 |  1440x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer23.conv1 |  1440x14x14 |  192x14x14   |   0.69 % |   0.96 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer23.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer23.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer23.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer24.norm1 |  1488x14x14 |  1488x14x14  |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer24.relu1 |  1488x14x14 |  1488x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer24.conv1 |  1488x14x14 |  192x14x14   |   0.71 % |   0.99 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer24.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer24.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer24.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer25.norm1 |  1536x14x14 |  1536x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer25.relu1 |  1536x14x14 |  1536x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer25.conv1 |  1536x14x14 |  192x14x14   |   0.74 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer25.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer25.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer25.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer26.norm1 |  1584x14x14 |  1584x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer26.relu1 |  1584x14x14 |  1584x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer26.conv1 |  1584x14x14 |  192x14x14   |   0.76 % |   1.05 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer26.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer26.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer26.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer27.norm1 |  1632x14x14 |  1632x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer27.relu1 |  1632x14x14 |  1632x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer27.conv1 |  1632x14x14 |  192x14x14   |   0.78 % |   1.08 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer27.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer27.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer27.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer28.norm1 |  1680x14x14 |  1680x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer28.relu1 |  1680x14x14 |  1680x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer28.conv1 |  1680x14x14 |  192x14x14   |   0.81 % |   1.12 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer28.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer28.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer28.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer29.norm1 |  1728x14x14 |  1728x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer29.relu1 |  1728x14x14 |  1728x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer29.conv1 |  1728x14x14 |  192x14x14   |   0.83 % |   1.15 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer29.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer29.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer29.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer30.norm1 |  1776x14x14 |  1776x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer30.relu1 |  1776x14x14 |  1776x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer30.conv1 |  1776x14x14 |  192x14x14   |   0.85 % |   1.18 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer30.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer30.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer30.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer31.norm1 |  1824x14x14 |  1824x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer31.relu1 |  1824x14x14 |  1824x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer31.conv1 |  1824x14x14 |  192x14x14   |   0.87 % |   1.21 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer31.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer31.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer31.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer32.norm1 |  1872x14x14 |  1872x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer32.relu1 |  1872x14x14 |  1872x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer32.conv1 |  1872x14x14 |  192x14x14   |   0.90 % |   1.24 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer32.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer32.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer32.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer33.norm1 |  1920x14x14 |  1920x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer33.relu1 |  1920x14x14 |  1920x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer33.conv1 |  1920x14x14 |  192x14x14   |   0.92 % |   1.28 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer33.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer33.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer33.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer34.norm1 |  1968x14x14 |  1968x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer34.relu1 |  1968x14x14 |  1968x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer34.conv1 |  1968x14x14 |  192x14x14   |   0.94 % |   1.31 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer34.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer34.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer34.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer35.norm1 |  2016x14x14 |  2016x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer35.relu1 |  2016x14x14 |  2016x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer35.conv1 |  2016x14x14 |  192x14x14   |   0.97 % |   1.34 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer35.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer35.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer35.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer36.norm1 |  2064x14x14 |  2064x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer36.relu1 |  2064x14x14 |  2064x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer36.conv1 |  2064x14x14 |  192x14x14   |   0.99 % |   1.37 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer36.norm2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer36.relu2 |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer36.conv2 |  192x14x14  |   48x14x14   |   0.21 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.transition3.norm               |  2112x14x14 |  2112x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.transition3.relu               |  2112x14x14 |  2112x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.transition3.conv               |  2112x14x14 |  1056x14x14  |   5.57 % |   7.72 % | Conv2d k=1 p=0 s=1 |
| features.transition3.pool               |  1056x14x14 |   1056x7x7   |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock4.denselayer1.norm1  |   1056x7x7  |   1056x7x7   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer1.relu1  |   1056x7x7  |   1056x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer1.conv1  |   1056x7x7  |   192x7x7    |   0.13 % |   0.70 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer1.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer1.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer1.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer2.norm1  |   1104x7x7  |   1104x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer2.relu1  |   1104x7x7  |   1104x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer2.conv1  |   1104x7x7  |   192x7x7    |   0.13 % |   0.73 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer2.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer2.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer2.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer3.norm1  |   1152x7x7  |   1152x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer3.relu1  |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer3.conv1  |   1152x7x7  |   192x7x7    |   0.14 % |   0.77 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer3.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer3.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer3.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer4.norm1  |   1200x7x7  |   1200x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer4.relu1  |   1200x7x7  |   1200x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer4.conv1  |   1200x7x7  |   192x7x7    |   0.14 % |   0.80 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer4.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer4.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer4.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer5.norm1  |   1248x7x7  |   1248x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer5.relu1  |   1248x7x7  |   1248x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer5.conv1  |   1248x7x7  |   192x7x7    |   0.15 % |   0.83 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer5.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer5.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer5.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer6.norm1  |   1296x7x7  |   1296x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer6.relu1  |   1296x7x7  |   1296x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer6.conv1  |   1296x7x7  |   192x7x7    |   0.16 % |   0.86 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer6.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer6.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer6.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer7.norm1  |   1344x7x7  |   1344x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer7.relu1  |   1344x7x7  |   1344x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer7.conv1  |   1344x7x7  |   192x7x7    |   0.16 % |   0.89 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer7.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer7.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer7.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer8.norm1  |   1392x7x7  |   1392x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer8.relu1  |   1392x7x7  |   1392x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer8.conv1  |   1392x7x7  |   192x7x7    |   0.17 % |   0.92 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer8.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer8.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer8.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer9.norm1  |   1440x7x7  |   1440x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer9.relu1  |   1440x7x7  |   1440x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer9.conv1  |   1440x7x7  |   192x7x7    |   0.17 % |   0.96 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer9.norm2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer9.relu2  |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer9.conv2  |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer10.norm1 |   1488x7x7  |   1488x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer10.relu1 |   1488x7x7  |   1488x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer10.conv1 |   1488x7x7  |   192x7x7    |   0.18 % |   0.99 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer10.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer10.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer10.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer11.norm1 |   1536x7x7  |   1536x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer11.relu1 |   1536x7x7  |   1536x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer11.conv1 |   1536x7x7  |   192x7x7    |   0.18 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer11.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer11.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer11.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer12.norm1 |   1584x7x7  |   1584x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer12.relu1 |   1584x7x7  |   1584x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer12.conv1 |   1584x7x7  |   192x7x7    |   0.19 % |   1.05 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer12.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer12.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer12.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer13.norm1 |   1632x7x7  |   1632x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer13.relu1 |   1632x7x7  |   1632x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer13.conv1 |   1632x7x7  |   192x7x7    |   0.20 % |   1.08 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer13.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer13.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer13.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer14.norm1 |   1680x7x7  |   1680x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer14.relu1 |   1680x7x7  |   1680x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer14.conv1 |   1680x7x7  |   192x7x7    |   0.20 % |   1.12 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer14.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer14.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer14.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer15.norm1 |   1728x7x7  |   1728x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer15.relu1 |   1728x7x7  |   1728x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer15.conv1 |   1728x7x7  |   192x7x7    |   0.21 % |   1.15 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer15.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer15.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer15.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer16.norm1 |   1776x7x7  |   1776x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer16.relu1 |   1776x7x7  |   1776x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer16.conv1 |   1776x7x7  |   192x7x7    |   0.21 % |   1.18 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer16.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer16.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer16.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer17.norm1 |   1824x7x7  |   1824x7x7   |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer17.relu1 |   1824x7x7  |   1824x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer17.conv1 |   1824x7x7  |   192x7x7    |   0.22 % |   1.21 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer17.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer17.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer17.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer18.norm1 |   1872x7x7  |   1872x7x7   |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer18.relu1 |   1872x7x7  |   1872x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer18.conv1 |   1872x7x7  |   192x7x7    |   0.22 % |   1.24 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer18.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer18.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer18.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer19.norm1 |   1920x7x7  |   1920x7x7   |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer19.relu1 |   1920x7x7  |   1920x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer19.conv1 |   1920x7x7  |   192x7x7    |   0.23 % |   1.28 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer19.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer19.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer19.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer20.norm1 |   1968x7x7  |   1968x7x7   |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer20.relu1 |   1968x7x7  |   1968x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer20.conv1 |   1968x7x7  |   192x7x7    |   0.24 % |   1.31 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer20.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer20.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer20.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer21.norm1 |   2016x7x7  |   2016x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer21.relu1 |   2016x7x7  |   2016x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer21.conv1 |   2016x7x7  |   192x7x7    |   0.24 % |   1.34 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer21.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer21.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer21.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer22.norm1 |   2064x7x7  |   2064x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer22.relu1 |   2064x7x7  |   2064x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer22.conv1 |   2064x7x7  |   192x7x7    |   0.25 % |   1.37 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer22.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer22.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer22.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer23.norm1 |   2112x7x7  |   2112x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer23.relu1 |   2112x7x7  |   2112x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer23.conv1 |   2112x7x7  |   192x7x7    |   0.25 % |   1.40 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer23.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer23.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer23.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer24.norm1 |   2160x7x7  |   2160x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer24.relu1 |   2160x7x7  |   2160x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer24.conv1 |   2160x7x7  |   192x7x7    |   0.26 % |   1.43 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer24.norm2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer24.relu2 |   192x7x7   |   192x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer24.conv2 |   192x7x7   |    48x7x7    |   0.05 % |   0.29 % | Conv2d k=3 p=1 s=1 |
| features.norm5                          |   2208x7x7  |   2208x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| classifier                              |     2208    |     1000     |   0.03 % |   7.64 % | Linear             |
| Total                                   |  3x224x224  |     1000     |   7.85 G |  28.90 M | DenseNet           |