| Name                                    | Input shape | Output shape |     MACs |   Params | Description        |
|:---------------------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.conv0                          |  3x224x224  |  64x112x112  |   2.69 % |   0.05 % | Conv2d k=7 p=3 s=2 |
| features.norm0                          |  64x112x112 |  64x112x112  |   0.07 % |   0.00 % | BatchNorm2d        |
| features.relu0                          |  64x112x112 |  64x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.pool0                          |  64x112x112 |   64x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.denseblock1.denselayer1.norm1  |   64x56x56  |   64x56x56   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer1.relu1  |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer1.conv1  |   64x56x56  |  128x56x56   |   0.59 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer1.norm2  |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer1.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer1.conv2  |  128x56x56  |   32x56x56   |   2.63 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer2.norm1  |   96x56x56  |   96x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer2.relu1  |   96x56x56  |   96x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer2.conv1  |   96x56x56  |  128x56x56   |   0.88 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer2.norm2  |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer2.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer2.conv2  |  128x56x56  |   32x56x56   |   2.63 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer3.norm1  |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer3.relu1  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer3.conv1  |  128x56x56  |  128x56x56   |   1.17 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer3.norm2  |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer3.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer3.conv2  |  128x56x56  |   32x56x56   |   2.63 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer4.norm1  |  160x56x56  |  160x56x56   |   0.05 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer4.relu1  |  160x56x56  |  160x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer4.conv1  |  160x56x56  |  128x56x56   |   1.46 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer4.norm2  |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer4.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer4.conv2  |  128x56x56  |   32x56x56   |   2.63 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer5.norm1  |  192x56x56  |  192x56x56   |   0.05 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer5.relu1  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer5.conv1  |  192x56x56  |  128x56x56   |   1.76 % |   0.12 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer5.norm2  |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer5.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer5.conv2  |  128x56x56  |   32x56x56   |   2.63 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer6.norm1  |  224x56x56  |  224x56x56   |   0.06 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer6.relu1  |  224x56x56  |  224x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer6.conv1  |  224x56x56  |  128x56x56   |   2.05 % |   0.14 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer6.norm2  |  128x56x56  |  128x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer6.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer6.conv2  |  128x56x56  |   32x56x56   |   2.63 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.transition1.norm               |  256x56x56  |  256x56x56   |   0.07 % |   0.01 % | BatchNorm2d        |
| features.transition1.relu               |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.transition1.conv               |  256x56x56  |  128x56x56   |   2.34 % |   0.16 % | Conv2d k=1 p=0 s=1 |
| features.transition1.pool               |  128x56x56  |  128x28x28   |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock2.denselayer1.norm1  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer1.relu1  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer1.conv1  |  128x28x28  |  128x28x28   |   0.29 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer1.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer1.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer1.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer2.norm1  |  160x28x28  |  160x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer2.relu1  |  160x28x28  |  160x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer2.conv1  |  160x28x28  |  128x28x28   |   0.37 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer2.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer2.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer2.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer3.norm1  |  192x28x28  |  192x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer3.relu1  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer3.conv1  |  192x28x28  |  128x28x28   |   0.44 % |   0.12 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer3.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer3.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer3.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer4.norm1  |  224x28x28  |  224x28x28   |   0.02 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer4.relu1  |  224x28x28  |  224x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer4.conv1  |  224x28x28  |  128x28x28   |   0.51 % |   0.14 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer4.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer4.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer4.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer5.norm1  |  256x28x28  |  256x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer5.relu1  |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer5.conv1  |  256x28x28  |  128x28x28   |   0.59 % |   0.16 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer5.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer5.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer5.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer6.norm1  |  288x28x28  |  288x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer6.relu1  |  288x28x28  |  288x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer6.conv1  |  288x28x28  |  128x28x28   |   0.66 % |   0.18 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer6.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer6.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer6.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer7.norm1  |  320x28x28  |  320x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer7.relu1  |  320x28x28  |  320x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer7.conv1  |  320x28x28  |  128x28x28   |   0.73 % |   0.20 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer7.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer7.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer7.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer8.norm1  |  352x28x28  |  352x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer8.relu1  |  352x28x28  |  352x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer8.conv1  |  352x28x28  |  128x28x28   |   0.80 % |   0.22 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer8.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer8.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer8.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer9.norm1  |  384x28x28  |  384x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer9.relu1  |  384x28x28  |  384x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer9.conv1  |  384x28x28  |  128x28x28   |   0.88 % |   0.24 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer9.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer9.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer9.conv2  |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer10.norm1 |  416x28x28  |  416x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer10.relu1 |  416x28x28  |  416x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer10.conv1 |  416x28x28  |  128x28x28   |   0.95 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer10.norm2 |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer10.relu2 |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer10.conv2 |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer11.norm1 |  448x28x28  |  448x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer11.relu1 |  448x28x28  |  448x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer11.conv1 |  448x28x28  |  128x28x28   |   1.02 % |   0.28 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer11.norm2 |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer11.relu2 |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer11.conv2 |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer12.norm1 |  480x28x28  |  480x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer12.relu1 |  480x28x28  |  480x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer12.conv1 |  480x28x28  |  128x28x28   |   1.10 % |   0.30 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer12.norm2 |  128x28x28  |  128x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| features.denseblock2.denselayer12.relu2 |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer12.conv2 |  128x28x28  |   32x28x28   |   0.66 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.transition2.norm               |  512x28x28  |  512x28x28   |   0.04 % |   0.01 % | BatchNorm2d        |
| features.transition2.relu               |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.transition2.conv               |  512x28x28  |  256x28x28   |   2.34 % |   0.65 % | Conv2d k=1 p=0 s=1 |
| features.transition2.pool               |  256x28x28  |  256x14x14   |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock3.denselayer1.norm1  |  256x14x14  |  256x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer1.relu1  |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer1.conv1  |  256x14x14  |  128x14x14   |   0.15 % |   0.16 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer1.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer1.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer1.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer2.norm1  |  288x14x14  |  288x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer2.relu1  |  288x14x14  |  288x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer2.conv1  |  288x14x14  |  128x14x14   |   0.16 % |   0.18 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer2.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer2.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer2.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer3.norm1  |  320x14x14  |  320x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer3.relu1  |  320x14x14  |  320x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer3.conv1  |  320x14x14  |  128x14x14   |   0.18 % |   0.20 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer3.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer3.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer3.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer4.norm1  |  352x14x14  |  352x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer4.relu1  |  352x14x14  |  352x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer4.conv1  |  352x14x14  |  128x14x14   |   0.20 % |   0.22 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer4.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer4.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer4.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer5.norm1  |  384x14x14  |  384x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer5.relu1  |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer5.conv1  |  384x14x14  |  128x14x14   |   0.22 % |   0.24 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer5.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer5.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer5.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer6.norm1  |  416x14x14  |  416x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer6.relu1  |  416x14x14  |  416x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer6.conv1  |  416x14x14  |  128x14x14   |   0.24 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer6.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer6.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer6.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer7.norm1  |  448x14x14  |  448x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer7.relu1  |  448x14x14  |  448x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer7.conv1  |  448x14x14  |  128x14x14   |   0.26 % |   0.28 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer7.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer7.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer7.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer8.norm1  |  480x14x14  |  480x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer8.relu1  |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer8.conv1  |  480x14x14  |  128x14x14   |   0.27 % |   0.30 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer8.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer8.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer8.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer9.norm1  |  512x14x14  |  512x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer9.relu1  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer9.conv1  |  512x14x14  |  128x14x14   |   0.29 % |   0.32 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer9.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer9.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer9.conv2  |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer10.norm1 |  544x14x14  |  544x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer10.relu1 |  544x14x14  |  544x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer10.conv1 |  544x14x14  |  128x14x14   |   0.31 % |   0.34 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer10.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer10.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer10.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer11.norm1 |  576x14x14  |  576x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer11.relu1 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer11.conv1 |  576x14x14  |  128x14x14   |   0.33 % |   0.36 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer11.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer11.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer11.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer12.norm1 |  608x14x14  |  608x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer12.relu1 |  608x14x14  |  608x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer12.conv1 |  608x14x14  |  128x14x14   |   0.35 % |   0.38 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer12.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer12.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer12.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer13.norm1 |  640x14x14  |  640x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer13.relu1 |  640x14x14  |  640x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer13.conv1 |  640x14x14  |  128x14x14   |   0.37 % |   0.40 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer13.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer13.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer13.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer14.norm1 |  672x14x14  |  672x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer14.relu1 |  672x14x14  |  672x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer14.conv1 |  672x14x14  |  128x14x14   |   0.38 % |   0.42 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer14.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer14.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer14.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer15.norm1 |  704x14x14  |  704x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer15.relu1 |  704x14x14  |  704x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer15.conv1 |  704x14x14  |  128x14x14   |   0.40 % |   0.45 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer15.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer15.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer15.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer16.norm1 |  736x14x14  |  736x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer16.relu1 |  736x14x14  |  736x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer16.conv1 |  736x14x14  |  128x14x14   |   0.42 % |   0.47 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer16.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer16.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer16.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer17.norm1 |  768x14x14  |  768x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer17.relu1 |  768x14x14  |  768x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer17.conv1 |  768x14x14  |  128x14x14   |   0.44 % |   0.49 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer17.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer17.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer17.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer18.norm1 |  800x14x14  |  800x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer18.relu1 |  800x14x14  |  800x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer18.conv1 |  800x14x14  |  128x14x14   |   0.46 % |   0.51 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer18.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer18.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer18.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer19.norm1 |  832x14x14  |  832x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer19.relu1 |  832x14x14  |  832x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer19.conv1 |  832x14x14  |  128x14x14   |   0.48 % |   0.53 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer19.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer19.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer19.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer20.norm1 |  864x14x14  |  864x14x14   |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer20.relu1 |  864x14x14  |  864x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer20.conv1 |  864x14x14  |  128x14x14   |   0.49 % |   0.55 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer20.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer20.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer20.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer21.norm1 |  896x14x14  |  896x14x14   |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer21.relu1 |  896x14x14  |  896x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer21.conv1 |  896x14x14  |  128x14x14   |   0.51 % |   0.57 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer21.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer21.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer21.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer22.norm1 |  928x14x14  |  928x14x14   |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer22.relu1 |  928x14x14  |  928x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer22.conv1 |  928x14x14  |  128x14x14   |   0.53 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer22.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer22.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer22.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer23.norm1 |  960x14x14  |  960x14x14   |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer23.relu1 |  960x14x14  |  960x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer23.conv1 |  960x14x14  |  128x14x14   |   0.55 % |   0.61 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer23.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer23.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer23.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer24.norm1 |  992x14x14  |  992x14x14   |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer24.relu1 |  992x14x14  |  992x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer24.conv1 |  992x14x14  |  128x14x14   |   0.57 % |   0.63 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer24.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer24.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer24.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer25.norm1 |  1024x14x14 |  1024x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer25.relu1 |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer25.conv1 |  1024x14x14 |  128x14x14   |   0.59 % |   0.65 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer25.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer25.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer25.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer26.norm1 |  1056x14x14 |  1056x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer26.relu1 |  1056x14x14 |  1056x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer26.conv1 |  1056x14x14 |  128x14x14   |   0.60 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer26.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer26.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer26.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer27.norm1 |  1088x14x14 |  1088x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer27.relu1 |  1088x14x14 |  1088x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer27.conv1 |  1088x14x14 |  128x14x14   |   0.62 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer27.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer27.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer27.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer28.norm1 |  1120x14x14 |  1120x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer28.relu1 |  1120x14x14 |  1120x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer28.conv1 |  1120x14x14 |  128x14x14   |   0.64 % |   0.71 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer28.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer28.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer28.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer29.norm1 |  1152x14x14 |  1152x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer29.relu1 |  1152x14x14 |  1152x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer29.conv1 |  1152x14x14 |  128x14x14   |   0.66 % |   0.73 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer29.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer29.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer29.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer30.norm1 |  1184x14x14 |  1184x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer30.relu1 |  1184x14x14 |  1184x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer30.conv1 |  1184x14x14 |  128x14x14   |   0.68 % |   0.75 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer30.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer30.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer30.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer31.norm1 |  1216x14x14 |  1216x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer31.relu1 |  1216x14x14 |  1216x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer31.conv1 |  1216x14x14 |  128x14x14   |   0.69 % |   0.77 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer31.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer31.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer31.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer32.norm1 |  1248x14x14 |  1248x14x14  |   0.02 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer32.relu1 |  1248x14x14 |  1248x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer32.conv1 |  1248x14x14 |  128x14x14   |   0.71 % |   0.79 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer32.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer32.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer32.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer33.norm1 |  1280x14x14 |  1280x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer33.relu1 |  1280x14x14 |  1280x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer33.conv1 |  1280x14x14 |  128x14x14   |   0.73 % |   0.81 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer33.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer33.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer33.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer34.norm1 |  1312x14x14 |  1312x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer34.relu1 |  1312x14x14 |  1312x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer34.conv1 |  1312x14x14 |  128x14x14   |   0.75 % |   0.83 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer34.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer34.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer34.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer35.norm1 |  1344x14x14 |  1344x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer35.relu1 |  1344x14x14 |  1344x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer35.conv1 |  1344x14x14 |  128x14x14   |   0.77 % |   0.85 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer35.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer35.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer35.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer36.norm1 |  1376x14x14 |  1376x14x14  |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer36.relu1 |  1376x14x14 |  1376x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer36.conv1 |  1376x14x14 |  128x14x14   |   0.79 % |   0.87 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer36.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer36.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer36.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer37.norm1 |  1408x14x14 |  1408x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer37.relu1 |  1408x14x14 |  1408x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer37.conv1 |  1408x14x14 |  128x14x14   |   0.80 % |   0.89 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer37.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer37.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer37.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer38.norm1 |  1440x14x14 |  1440x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer38.relu1 |  1440x14x14 |  1440x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer38.conv1 |  1440x14x14 |  128x14x14   |   0.82 % |   0.91 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer38.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer38.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer38.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer39.norm1 |  1472x14x14 |  1472x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer39.relu1 |  1472x14x14 |  1472x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer39.conv1 |  1472x14x14 |  128x14x14   |   0.84 % |   0.93 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer39.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer39.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer39.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer40.norm1 |  1504x14x14 |  1504x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer40.relu1 |  1504x14x14 |  1504x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer40.conv1 |  1504x14x14 |  128x14x14   |   0.86 % |   0.95 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer40.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer40.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer40.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer41.norm1 |  1536x14x14 |  1536x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer41.relu1 |  1536x14x14 |  1536x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer41.conv1 |  1536x14x14 |  128x14x14   |   0.88 % |   0.97 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer41.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer41.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer41.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer42.norm1 |  1568x14x14 |  1568x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer42.relu1 |  1568x14x14 |  1568x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer42.conv1 |  1568x14x14 |  128x14x14   |   0.90 % |   0.99 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer42.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer42.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer42.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer43.norm1 |  1600x14x14 |  1600x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer43.relu1 |  1600x14x14 |  1600x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer43.conv1 |  1600x14x14 |  128x14x14   |   0.91 % |   1.01 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer43.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer43.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer43.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer44.norm1 |  1632x14x14 |  1632x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer44.relu1 |  1632x14x14 |  1632x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer44.conv1 |  1632x14x14 |  128x14x14   |   0.93 % |   1.03 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer44.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer44.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer44.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer45.norm1 |  1664x14x14 |  1664x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer45.relu1 |  1664x14x14 |  1664x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer45.conv1 |  1664x14x14 |  128x14x14   |   0.95 % |   1.05 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer45.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer45.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer45.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer46.norm1 |  1696x14x14 |  1696x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer46.relu1 |  1696x14x14 |  1696x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer46.conv1 |  1696x14x14 |  128x14x14   |   0.97 % |   1.07 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer46.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer46.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer46.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer47.norm1 |  1728x14x14 |  1728x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer47.relu1 |  1728x14x14 |  1728x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer47.conv1 |  1728x14x14 |  128x14x14   |   0.99 % |   1.09 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer47.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer47.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer47.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer48.norm1 |  1760x14x14 |  1760x14x14  |   0.03 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer48.relu1 |  1760x14x14 |  1760x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer48.conv1 |  1760x14x14 |  128x14x14   |   1.01 % |   1.11 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer48.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock3.denselayer48.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer48.conv2 |  128x14x14  |   32x14x14   |   0.16 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.transition3.norm               |  1792x14x14 |  1792x14x14  |   0.03 % |   0.04 % | BatchNorm2d        |
| features.transition3.relu               |  1792x14x14 |  1792x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.transition3.conv               |  1792x14x14 |  896x14x14   |   7.17 % |   7.93 % | Conv2d k=1 p=0 s=1 |
| features.transition3.pool               |  896x14x14  |   896x7x7    |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock4.denselayer1.norm1  |   896x7x7   |   896x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer1.relu1  |   896x7x7   |   896x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer1.conv1  |   896x7x7   |   128x7x7    |   0.13 % |   0.57 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer1.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer1.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer1.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer2.norm1  |   928x7x7   |   928x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer2.relu1  |   928x7x7   |   928x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer2.conv1  |   928x7x7   |   128x7x7    |   0.13 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer2.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer2.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer2.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer3.norm1  |   960x7x7   |   960x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer3.relu1  |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer3.conv1  |   960x7x7   |   128x7x7    |   0.14 % |   0.61 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer3.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer3.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer3.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer4.norm1  |   992x7x7   |   992x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer4.relu1  |   992x7x7   |   992x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer4.conv1  |   992x7x7   |   128x7x7    |   0.14 % |   0.63 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer4.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer4.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer4.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer5.norm1  |   1024x7x7  |   1024x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer5.relu1  |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer5.conv1  |   1024x7x7  |   128x7x7    |   0.15 % |   0.65 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer5.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer5.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer5.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer6.norm1  |   1056x7x7  |   1056x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer6.relu1  |   1056x7x7  |   1056x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer6.conv1  |   1056x7x7  |   128x7x7    |   0.15 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer6.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer6.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer6.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer7.norm1  |   1088x7x7  |   1088x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer7.relu1  |   1088x7x7  |   1088x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer7.conv1  |   1088x7x7  |   128x7x7    |   0.16 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer7.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer7.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer7.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer8.norm1  |   1120x7x7  |   1120x7x7   |   0.00 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer8.relu1  |   1120x7x7  |   1120x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer8.conv1  |   1120x7x7  |   128x7x7    |   0.16 % |   0.71 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer8.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer8.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer8.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer9.norm1  |   1152x7x7  |   1152x7x7   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer9.relu1  |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer9.conv1  |   1152x7x7  |   128x7x7    |   0.16 % |   0.73 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer9.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer9.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer9.conv2  |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer10.norm1 |   1184x7x7  |   1184x7x7   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer10.relu1 |   1184x7x7  |   1184x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer10.conv1 |   1184x7x7  |   128x7x7    |   0.17 % |   0.75 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer10.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer10.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer10.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer11.norm1 |   1216x7x7  |   1216x7x7   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer11.relu1 |   1216x7x7  |   1216x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer11.conv1 |   1216x7x7  |   128x7x7    |   0.17 % |   0.77 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer11.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer11.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer11.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer12.norm1 |   1248x7x7  |   1248x7x7   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock4.denselayer12.relu1 |   1248x7x7  |   1248x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer12.conv1 |   1248x7x7  |   128x7x7    |   0.18 % |   0.79 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer12.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer12.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer12.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer13.norm1 |   1280x7x7  |   1280x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer13.relu1 |   1280x7x7  |   1280x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer13.conv1 |   1280x7x7  |   128x7x7    |   0.18 % |   0.81 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer13.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer13.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer13.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer14.norm1 |   1312x7x7  |   1312x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer14.relu1 |   1312x7x7  |   1312x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer14.conv1 |   1312x7x7  |   128x7x7    |   0.19 % |   0.83 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer14.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer14.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer14.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer15.norm1 |   1344x7x7  |   1344x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer15.relu1 |   1344x7x7  |   1344x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer15.conv1 |   1344x7x7  |   128x7x7    |   0.19 % |   0.85 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer15.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer15.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer15.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer16.norm1 |   1376x7x7  |   1376x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer16.relu1 |   1376x7x7  |   1376x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer16.conv1 |   1376x7x7  |   128x7x7    |   0.20 % |   0.87 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer16.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer16.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer16.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer17.norm1 |   1408x7x7  |   1408x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer17.relu1 |   1408x7x7  |   1408x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer17.conv1 |   1408x7x7  |   128x7x7    |   0.20 % |   0.89 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer17.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer17.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer17.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer18.norm1 |   1440x7x7  |   1440x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer18.relu1 |   1440x7x7  |   1440x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer18.conv1 |   1440x7x7  |   128x7x7    |   0.21 % |   0.91 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer18.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer18.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer18.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer19.norm1 |   1472x7x7  |   1472x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer19.relu1 |   1472x7x7  |   1472x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer19.conv1 |   1472x7x7  |   128x7x7    |   0.21 % |   0.93 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer19.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer19.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer19.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer20.norm1 |   1504x7x7  |   1504x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer20.relu1 |   1504x7x7  |   1504x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer20.conv1 |   1504x7x7  |   128x7x7    |   0.21 % |   0.95 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer20.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer20.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer20.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer21.norm1 |   1536x7x7  |   1536x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer21.relu1 |   1536x7x7  |   1536x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer21.conv1 |   1536x7x7  |   128x7x7    |   0.22 % |   0.97 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer21.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer21.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer21.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer22.norm1 |   1568x7x7  |   1568x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer22.relu1 |   1568x7x7  |   1568x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer22.conv1 |   1568x7x7  |   128x7x7    |   0.22 % |   0.99 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer22.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer22.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer22.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer23.norm1 |   1600x7x7  |   1600x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer23.relu1 |   1600x7x7  |   1600x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer23.conv1 |   1600x7x7  |   128x7x7    |   0.23 % |   1.01 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer23.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer23.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer23.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer24.norm1 |   1632x7x7  |   1632x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer24.relu1 |   1632x7x7  |   1632x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer24.conv1 |   1632x7x7  |   128x7x7    |   0.23 % |   1.03 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer24.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer24.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer24.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer25.norm1 |   1664x7x7  |   1664x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer25.relu1 |   1664x7x7  |   1664x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer25.conv1 |   1664x7x7  |   128x7x7    |   0.24 % |   1.05 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer25.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer25.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer25.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer26.norm1 |   1696x7x7  |   1696x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer26.relu1 |   1696x7x7  |   1696x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer26.conv1 |   1696x7x7  |   128x7x7    |   0.24 % |   1.07 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer26.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer26.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer26.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer27.norm1 |   1728x7x7  |   1728x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer27.relu1 |   1728x7x7  |   1728x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer27.conv1 |   1728x7x7  |   128x7x7    |   0.25 % |   1.09 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer27.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer27.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer27.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer28.norm1 |   1760x7x7  |   1760x7x7   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer28.relu1 |   1760x7x7  |   1760x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer28.conv1 |   1760x7x7  |   128x7x7    |   0.25 % |   1.11 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer28.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer28.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer28.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer29.norm1 |   1792x7x7  |   1792x7x7   |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer29.relu1 |   1792x7x7  |   1792x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer29.conv1 |   1792x7x7  |   128x7x7    |   0.26 % |   1.13 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer29.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer29.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer29.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer30.norm1 |   1824x7x7  |   1824x7x7   |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer30.relu1 |   1824x7x7  |   1824x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer30.conv1 |   1824x7x7  |   128x7x7    |   0.26 % |   1.15 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer30.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer30.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer30.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer31.norm1 |   1856x7x7  |   1856x7x7   |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer31.relu1 |   1856x7x7  |   1856x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer31.conv1 |   1856x7x7  |   128x7x7    |   0.27 % |   1.17 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer31.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer31.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer31.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer32.norm1 |   1888x7x7  |   1888x7x7   |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer32.relu1 |   1888x7x7  |   1888x7x7   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer32.conv1 |   1888x7x7  |   128x7x7    |   0.27 % |   1.19 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer32.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| features.denseblock4.denselayer32.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer32.conv2 |   128x7x7   |    32x7x7    |   0.04 % |   0.18 % | Conv2d k=3 p=1 s=1 |
| features.norm5                          |   1920x7x7  |   1920x7x7   |   0.01 % |   0.04 % | BatchNorm2d        |
| classifier                              |     1920    |     1000     |   0.04 % |   9.49 % | Linear             |
| Total                                   |  3x224x224  |     1000     |   4.39 G |  20.24 M | DenseNet           |