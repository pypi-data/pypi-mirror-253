| Name                                    | Input shape | Output shape |     MACs |   Params | Description        |
|:---------------------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.conv0                          |  3x224x224  |  64x112x112  |   4.07 % |   0.12 % | Conv2d k=7 p=3 s=2 |
| features.norm0                          |  64x112x112 |  64x112x112  |   0.11 % |   0.00 % | BatchNorm2d        |
| features.relu0                          |  64x112x112 |  64x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.pool0                          |  64x112x112 |   64x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.denseblock1.denselayer1.norm1  |   64x56x56  |   64x56x56   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer1.relu1  |   64x56x56  |   64x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer1.conv1  |   64x56x56  |  128x56x56   |   0.89 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer1.norm2  |  128x56x56  |  128x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer1.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer1.conv2  |  128x56x56  |   32x56x56   |   3.99 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer2.norm1  |   96x56x56  |   96x56x56   |   0.04 % |   0.00 % | BatchNorm2d        |
| features.denseblock1.denselayer2.relu1  |   96x56x56  |   96x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer2.conv1  |   96x56x56  |  128x56x56   |   1.33 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer2.norm2  |  128x56x56  |  128x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer2.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer2.conv2  |  128x56x56  |   32x56x56   |   3.99 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer3.norm1  |  128x56x56  |  128x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer3.relu1  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer3.conv1  |  128x56x56  |  128x56x56   |   1.77 % |   0.20 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer3.norm2  |  128x56x56  |  128x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer3.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer3.conv2  |  128x56x56  |   32x56x56   |   3.99 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer4.norm1  |  160x56x56  |  160x56x56   |   0.07 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer4.relu1  |  160x56x56  |  160x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer4.conv1  |  160x56x56  |  128x56x56   |   2.22 % |   0.25 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer4.norm2  |  128x56x56  |  128x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer4.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer4.conv2  |  128x56x56  |   32x56x56   |   3.99 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer5.norm1  |  192x56x56  |  192x56x56   |   0.08 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer5.relu1  |  192x56x56  |  192x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer5.conv1  |  192x56x56  |  128x56x56   |   2.66 % |   0.30 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer5.norm2  |  128x56x56  |  128x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer5.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer5.conv2  |  128x56x56  |   32x56x56   |   3.99 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock1.denselayer6.norm1  |  224x56x56  |  224x56x56   |   0.10 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer6.relu1  |  224x56x56  |  224x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer6.conv1  |  224x56x56  |  128x56x56   |   3.10 % |   0.36 % | Conv2d k=1 p=0 s=1 |
| features.denseblock1.denselayer6.norm2  |  128x56x56  |  128x56x56   |   0.06 % |   0.01 % | BatchNorm2d        |
| features.denseblock1.denselayer6.relu2  |  128x56x56  |  128x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock1.denselayer6.conv2  |  128x56x56  |   32x56x56   |   3.99 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.transition1.norm               |  256x56x56  |  256x56x56   |   0.11 % |   0.01 % | BatchNorm2d        |
| features.transition1.relu               |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.transition1.conv               |  256x56x56  |  128x56x56   |   3.55 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| features.transition1.pool               |  128x56x56  |  128x28x28   |   0.01 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock2.denselayer1.norm1  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer1.relu1  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer1.conv1  |  128x28x28  |  128x28x28   |   0.44 % |   0.20 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer1.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer1.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer1.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer2.norm1  |  160x28x28  |  160x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer2.relu1  |  160x28x28  |  160x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer2.conv1  |  160x28x28  |  128x28x28   |   0.55 % |   0.25 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer2.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer2.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer2.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer3.norm1  |  192x28x28  |  192x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer3.relu1  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer3.conv1  |  192x28x28  |  128x28x28   |   0.67 % |   0.30 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer3.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer3.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer3.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer4.norm1  |  224x28x28  |  224x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer4.relu1  |  224x28x28  |  224x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer4.conv1  |  224x28x28  |  128x28x28   |   0.78 % |   0.36 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer4.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer4.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer4.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer5.norm1  |  256x28x28  |  256x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer5.relu1  |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer5.conv1  |  256x28x28  |  128x28x28   |   0.89 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer5.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer5.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer5.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer6.norm1  |  288x28x28  |  288x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer6.relu1  |  288x28x28  |  288x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer6.conv1  |  288x28x28  |  128x28x28   |   1.00 % |   0.46 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer6.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer6.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer6.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer7.norm1  |  320x28x28  |  320x28x28   |   0.03 % |   0.02 % | BatchNorm2d        |
| features.denseblock2.denselayer7.relu1  |  320x28x28  |  320x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer7.conv1  |  320x28x28  |  128x28x28   |   1.11 % |   0.51 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer7.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer7.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer7.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer8.norm1  |  352x28x28  |  352x28x28   |   0.04 % |   0.02 % | BatchNorm2d        |
| features.denseblock2.denselayer8.relu1  |  352x28x28  |  352x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer8.conv1  |  352x28x28  |  128x28x28   |   1.22 % |   0.56 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer8.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer8.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer8.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer9.norm1  |  384x28x28  |  384x28x28   |   0.04 % |   0.02 % | BatchNorm2d        |
| features.denseblock2.denselayer9.relu1  |  384x28x28  |  384x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer9.conv1  |  384x28x28  |  128x28x28   |   1.33 % |   0.61 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer9.norm2  |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer9.relu2  |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer9.conv2  |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer10.norm1 |  416x28x28  |  416x28x28   |   0.05 % |   0.02 % | BatchNorm2d        |
| features.denseblock2.denselayer10.relu1 |  416x28x28  |  416x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer10.conv1 |  416x28x28  |  128x28x28   |   1.44 % |   0.66 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer10.norm2 |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer10.relu2 |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer10.conv2 |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer11.norm1 |  448x28x28  |  448x28x28   |   0.05 % |   0.02 % | BatchNorm2d        |
| features.denseblock2.denselayer11.relu1 |  448x28x28  |  448x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer11.conv1 |  448x28x28  |  128x28x28   |   1.55 % |   0.71 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer11.norm2 |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer11.relu2 |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer11.conv2 |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock2.denselayer12.norm1 |  480x28x28  |  480x28x28   |   0.05 % |   0.02 % | BatchNorm2d        |
| features.denseblock2.denselayer12.relu1 |  480x28x28  |  480x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer12.conv1 |  480x28x28  |  128x28x28   |   1.66 % |   0.76 % | Conv2d k=1 p=0 s=1 |
| features.denseblock2.denselayer12.norm2 |  128x28x28  |  128x28x28   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock2.denselayer12.relu2 |  128x28x28  |  128x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock2.denselayer12.conv2 |  128x28x28  |   32x28x28   |   1.00 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.transition2.norm               |  512x28x28  |  512x28x28   |   0.06 % |   0.03 % | BatchNorm2d        |
| features.transition2.relu               |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.transition2.conv               |  512x28x28  |  256x28x28   |   3.55 % |   1.63 % | Conv2d k=1 p=0 s=1 |
| features.transition2.pool               |  256x28x28  |  256x14x14   |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock3.denselayer1.norm1  |  256x14x14  |  256x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer1.relu1  |  256x14x14  |  256x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer1.conv1  |  256x14x14  |  128x14x14   |   0.22 % |   0.41 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer1.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer1.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer1.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer2.norm1  |  288x14x14  |  288x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer2.relu1  |  288x14x14  |  288x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer2.conv1  |  288x14x14  |  128x14x14   |   0.25 % |   0.46 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer2.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer2.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer2.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer3.norm1  |  320x14x14  |  320x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer3.relu1  |  320x14x14  |  320x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer3.conv1  |  320x14x14  |  128x14x14   |   0.28 % |   0.51 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer3.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer3.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer3.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer4.norm1  |  352x14x14  |  352x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer4.relu1  |  352x14x14  |  352x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer4.conv1  |  352x14x14  |  128x14x14   |   0.30 % |   0.56 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer4.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer4.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer4.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer5.norm1  |  384x14x14  |  384x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer5.relu1  |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer5.conv1  |  384x14x14  |  128x14x14   |   0.33 % |   0.61 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer5.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer5.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer5.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer6.norm1  |  416x14x14  |  416x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer6.relu1  |  416x14x14  |  416x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer6.conv1  |  416x14x14  |  128x14x14   |   0.36 % |   0.66 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer6.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer6.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer6.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer7.norm1  |  448x14x14  |  448x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer7.relu1  |  448x14x14  |  448x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer7.conv1  |  448x14x14  |  128x14x14   |   0.39 % |   0.71 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer7.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer7.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer7.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer8.norm1  |  480x14x14  |  480x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| features.denseblock3.denselayer8.relu1  |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer8.conv1  |  480x14x14  |  128x14x14   |   0.42 % |   0.76 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer8.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer8.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer8.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer9.norm1  |  512x14x14  |  512x14x14   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer9.relu1  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer9.conv1  |  512x14x14  |  128x14x14   |   0.44 % |   0.81 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer9.norm2  |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer9.relu2  |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer9.conv2  |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer10.norm1 |  544x14x14  |  544x14x14   |   0.01 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer10.relu1 |  544x14x14  |  544x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer10.conv1 |  544x14x14  |  128x14x14   |   0.47 % |   0.86 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer10.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer10.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer10.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer11.norm1 |  576x14x14  |  576x14x14   |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer11.relu1 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer11.conv1 |  576x14x14  |  128x14x14   |   0.50 % |   0.91 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer11.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer11.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer11.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer12.norm1 |  608x14x14  |  608x14x14   |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer12.relu1 |  608x14x14  |  608x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer12.conv1 |  608x14x14  |  128x14x14   |   0.53 % |   0.97 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer12.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer12.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer12.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer13.norm1 |  640x14x14  |  640x14x14   |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer13.relu1 |  640x14x14  |  640x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer13.conv1 |  640x14x14  |  128x14x14   |   0.55 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer13.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer13.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer13.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer14.norm1 |  672x14x14  |  672x14x14   |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer14.relu1 |  672x14x14  |  672x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer14.conv1 |  672x14x14  |  128x14x14   |   0.58 % |   1.07 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer14.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer14.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer14.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer15.norm1 |  704x14x14  |  704x14x14   |   0.02 % |   0.03 % | BatchNorm2d        |
| features.denseblock3.denselayer15.relu1 |  704x14x14  |  704x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer15.conv1 |  704x14x14  |  128x14x14   |   0.61 % |   1.12 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer15.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer15.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer15.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer16.norm1 |  736x14x14  |  736x14x14   |   0.02 % |   0.04 % | BatchNorm2d        |
| features.denseblock3.denselayer16.relu1 |  736x14x14  |  736x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer16.conv1 |  736x14x14  |  128x14x14   |   0.64 % |   1.17 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer16.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer16.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer16.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer17.norm1 |  768x14x14  |  768x14x14   |   0.02 % |   0.04 % | BatchNorm2d        |
| features.denseblock3.denselayer17.relu1 |  768x14x14  |  768x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer17.conv1 |  768x14x14  |  128x14x14   |   0.67 % |   1.22 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer17.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer17.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer17.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer18.norm1 |  800x14x14  |  800x14x14   |   0.02 % |   0.04 % | BatchNorm2d        |
| features.denseblock3.denselayer18.relu1 |  800x14x14  |  800x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer18.conv1 |  800x14x14  |  128x14x14   |   0.69 % |   1.27 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer18.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer18.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer18.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer19.norm1 |  832x14x14  |  832x14x14   |   0.02 % |   0.04 % | BatchNorm2d        |
| features.denseblock3.denselayer19.relu1 |  832x14x14  |  832x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer19.conv1 |  832x14x14  |  128x14x14   |   0.72 % |   1.32 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer19.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer19.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer19.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer20.norm1 |  864x14x14  |  864x14x14   |   0.02 % |   0.04 % | BatchNorm2d        |
| features.denseblock3.denselayer20.relu1 |  864x14x14  |  864x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer20.conv1 |  864x14x14  |  128x14x14   |   0.75 % |   1.37 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer20.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer20.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer20.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer21.norm1 |  896x14x14  |  896x14x14   |   0.02 % |   0.04 % | BatchNorm2d        |
| features.denseblock3.denselayer21.relu1 |  896x14x14  |  896x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer21.conv1 |  896x14x14  |  128x14x14   |   0.78 % |   1.42 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer21.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer21.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer21.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer22.norm1 |  928x14x14  |  928x14x14   |   0.03 % |   0.05 % | BatchNorm2d        |
| features.denseblock3.denselayer22.relu1 |  928x14x14  |  928x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer22.conv1 |  928x14x14  |  128x14x14   |   0.80 % |   1.47 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer22.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer22.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer22.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer23.norm1 |  960x14x14  |  960x14x14   |   0.03 % |   0.05 % | BatchNorm2d        |
| features.denseblock3.denselayer23.relu1 |  960x14x14  |  960x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer23.conv1 |  960x14x14  |  128x14x14   |   0.83 % |   1.52 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer23.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer23.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer23.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock3.denselayer24.norm1 |  992x14x14  |  992x14x14   |   0.03 % |   0.05 % | BatchNorm2d        |
| features.denseblock3.denselayer24.relu1 |  992x14x14  |  992x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer24.conv1 |  992x14x14  |  128x14x14   |   0.86 % |   1.57 % | Conv2d k=1 p=0 s=1 |
| features.denseblock3.denselayer24.norm2 |  128x14x14  |  128x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock3.denselayer24.relu2 |  128x14x14  |  128x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.denseblock3.denselayer24.conv2 |  128x14x14  |   32x14x14   |   0.25 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.transition3.norm               |  1024x14x14 |  1024x14x14  |   0.03 % |   0.05 % | BatchNorm2d        |
| features.transition3.relu               |  1024x14x14 |  1024x14x14  |   0.00 % |   0.00 % | ReLU               |
| features.transition3.conv               |  1024x14x14 |  512x14x14   |   3.55 % |   6.50 % | Conv2d k=1 p=0 s=1 |
| features.transition3.pool               |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | AvgPool2d k=2 s=2  |
| features.denseblock4.denselayer1.norm1  |   512x7x7   |   512x7x7    |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer1.relu1  |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer1.conv1  |   512x7x7   |   128x7x7    |   0.11 % |   0.81 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer1.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer1.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer1.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer2.norm1  |   544x7x7   |   544x7x7    |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer2.relu1  |   544x7x7   |   544x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer2.conv1  |   544x7x7   |   128x7x7    |   0.12 % |   0.86 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer2.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer2.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer2.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer3.norm1  |   576x7x7   |   576x7x7    |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer3.relu1  |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer3.conv1  |   576x7x7   |   128x7x7    |   0.12 % |   0.91 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer3.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer3.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer3.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer4.norm1  |   608x7x7   |   608x7x7    |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer4.relu1  |   608x7x7   |   608x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer4.conv1  |   608x7x7   |   128x7x7    |   0.13 % |   0.97 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer4.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer4.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer4.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer5.norm1  |   640x7x7   |   640x7x7    |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer5.relu1  |   640x7x7   |   640x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer5.conv1  |   640x7x7   |   128x7x7    |   0.14 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer5.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer5.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer5.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer6.norm1  |   672x7x7   |   672x7x7    |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer6.relu1  |   672x7x7   |   672x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer6.conv1  |   672x7x7   |   128x7x7    |   0.15 % |   1.07 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer6.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer6.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer6.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer7.norm1  |   704x7x7   |   704x7x7    |   0.00 % |   0.03 % | BatchNorm2d        |
| features.denseblock4.denselayer7.relu1  |   704x7x7   |   704x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer7.conv1  |   704x7x7   |   128x7x7    |   0.15 % |   1.12 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer7.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer7.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer7.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer8.norm1  |   736x7x7   |   736x7x7    |   0.00 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer8.relu1  |   736x7x7   |   736x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer8.conv1  |   736x7x7   |   128x7x7    |   0.16 % |   1.17 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer8.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer8.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer8.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer9.norm1  |   768x7x7   |   768x7x7    |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer9.relu1  |   768x7x7   |   768x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer9.conv1  |   768x7x7   |   128x7x7    |   0.17 % |   1.22 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer9.norm2  |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer9.relu2  |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer9.conv2  |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer10.norm1 |   800x7x7   |   800x7x7    |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer10.relu1 |   800x7x7   |   800x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer10.conv1 |   800x7x7   |   128x7x7    |   0.17 % |   1.27 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer10.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer10.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer10.conv2 |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer11.norm1 |   832x7x7   |   832x7x7    |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer11.relu1 |   832x7x7   |   832x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer11.conv1 |   832x7x7   |   128x7x7    |   0.18 % |   1.32 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer11.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer11.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer11.conv2 |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer12.norm1 |   864x7x7   |   864x7x7    |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer12.relu1 |   864x7x7   |   864x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer12.conv1 |   864x7x7   |   128x7x7    |   0.19 % |   1.37 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer12.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer12.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer12.conv2 |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer13.norm1 |   896x7x7   |   896x7x7    |   0.01 % |   0.04 % | BatchNorm2d        |
| features.denseblock4.denselayer13.relu1 |   896x7x7   |   896x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer13.conv1 |   896x7x7   |   128x7x7    |   0.19 % |   1.42 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer13.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer13.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer13.conv2 |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer14.norm1 |   928x7x7   |   928x7x7    |   0.01 % |   0.05 % | BatchNorm2d        |
| features.denseblock4.denselayer14.relu1 |   928x7x7   |   928x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer14.conv1 |   928x7x7   |   128x7x7    |   0.20 % |   1.47 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer14.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer14.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer14.conv2 |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer15.norm1 |   960x7x7   |   960x7x7    |   0.01 % |   0.05 % | BatchNorm2d        |
| features.denseblock4.denselayer15.relu1 |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer15.conv1 |   960x7x7   |   128x7x7    |   0.21 % |   1.52 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer15.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer15.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer15.conv2 |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.denseblock4.denselayer16.norm1 |   992x7x7   |   992x7x7    |   0.01 % |   0.05 % | BatchNorm2d        |
| features.denseblock4.denselayer16.relu1 |   992x7x7   |   992x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer16.conv1 |   992x7x7   |   128x7x7    |   0.21 % |   1.57 % | Conv2d k=1 p=0 s=1 |
| features.denseblock4.denselayer16.norm2 |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| features.denseblock4.denselayer16.relu2 |   128x7x7   |   128x7x7    |   0.00 % |   0.00 % | ReLU               |
| features.denseblock4.denselayer16.conv2 |   128x7x7   |    32x7x7    |   0.06 % |   0.46 % | Conv2d k=3 p=1 s=1 |
| features.norm5                          |   1024x7x7  |   1024x7x7   |   0.01 % |   0.05 % | BatchNorm2d        |
| classifier                              |     1024    |     1000     |   0.04 % |  12.71 % | Linear             |
| Total                                   |  3x224x224  |     1000     |   2.90 G |   8.06 M | DenseNet           |