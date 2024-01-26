| Name               | Input shape | Output shape |     MACs |   Params | Description        |
|:------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| conv1.0            |  3x224x224  |  24x112x112  |  18.24 % |   0.05 % | Conv2d k=3 p=1 s=2 |
| conv1.1            |  24x112x112 |  24x112x112  |   2.70 % |   0.01 % | BatchNorm2d        |
| conv1.2            |  24x112x112 |  24x112x112  |   0.00 % |   0.00 % | ReLU               |
| maxpool            |  24x112x112 |   24x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| stage2.0.branch1.0 |   24x56x56  |   24x28x28   |   0.38 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| stage2.0.branch1.1 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch1.2 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.0.branch1.3 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch1.4 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.0.branch2.0 |   24x56x56  |   24x56x56   |   4.05 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.0.branch2.1 |   24x56x56  |   24x56x56   |   0.68 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch2.2 |   24x56x56  |   24x56x56   |   0.00 % |   0.00 % | ReLU               |
| stage2.0.branch2.3 |   24x56x56  |   24x28x28   |   0.38 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| stage2.0.branch2.4 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch2.5 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.0.branch2.6 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch2.7 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.1.branch2.0 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.1.branch2.1 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.1.branch2.2 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.1.branch2.3 |   24x28x28  |   24x28x28   |   0.38 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| stage2.1.branch2.4 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.1.branch2.5 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.1.branch2.6 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.1.branch2.7 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.2.branch2.0 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.2.branch2.1 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.2.branch2.2 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.2.branch2.3 |   24x28x28  |   24x28x28   |   0.38 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| stage2.2.branch2.4 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.2.branch2.5 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.2.branch2.6 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.2.branch2.7 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.3.branch2.0 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.3.branch2.1 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.3.branch2.2 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.3.branch2.3 |   24x28x28  |   24x28x28   |   0.38 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| stage2.3.branch2.4 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.3.branch2.5 |   24x28x28  |   24x28x28   |   1.01 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| stage2.3.branch2.6 |   24x28x28  |   24x28x28   |   0.17 % |   0.01 % | BatchNorm2d        |
| stage2.3.branch2.7 |   24x28x28  |   24x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage3.0.branch1.0 |   48x28x28  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=2 |
| stage3.0.branch1.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.0.branch1.2 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.0.branch1.3 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.0.branch1.4 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.0.branch2.0 |   48x28x28  |   48x28x28   |   4.05 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.0.branch2.1 |   48x28x28  |   48x28x28   |   0.34 % |   0.01 % | BatchNorm2d        |
| stage3.0.branch2.2 |   48x28x28  |   48x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage3.0.branch2.3 |   48x28x28  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=2 |
| stage3.0.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.0.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.0.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.0.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.1.branch2.0 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.1.branch2.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.1.branch2.2 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.1.branch2.3 |   48x14x14  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| stage3.1.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.1.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.1.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.1.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.2.branch2.0 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.2.branch2.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.2.branch2.2 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.2.branch2.3 |   48x14x14  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| stage3.2.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.2.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.2.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.2.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.3.branch2.0 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.3.branch2.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.3.branch2.2 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.3.branch2.3 |   48x14x14  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| stage3.3.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.3.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.3.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.3.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.4.branch2.0 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.4.branch2.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.4.branch2.2 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.4.branch2.3 |   48x14x14  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| stage3.4.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.4.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.4.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.4.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.5.branch2.0 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.5.branch2.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.5.branch2.2 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.5.branch2.3 |   48x14x14  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| stage3.5.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.5.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.5.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.5.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.6.branch2.0 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.6.branch2.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.6.branch2.2 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.6.branch2.3 |   48x14x14  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| stage3.6.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.6.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.6.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.6.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.7.branch2.0 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.7.branch2.1 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.7.branch2.2 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.7.branch2.3 |   48x14x14  |   48x14x14   |   0.19 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| stage3.7.branch2.4 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.7.branch2.5 |   48x14x14  |   48x14x14   |   1.01 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| stage3.7.branch2.6 |   48x14x14  |   48x14x14   |   0.08 % |   0.01 % | BatchNorm2d        |
| stage3.7.branch2.7 |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage4.0.branch1.0 |   96x14x14  |    96x7x7    |   0.09 % |   0.06 % | Conv2d k=3 p=1 s=2 |
| stage4.0.branch1.1 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.0.branch1.2 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.0.branch1.3 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.0.branch1.4 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.0.branch2.0 |   96x14x14  |   96x14x14   |   4.05 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.0.branch2.1 |   96x14x14  |   96x14x14   |   0.17 % |   0.03 % | BatchNorm2d        |
| stage4.0.branch2.2 |   96x14x14  |   96x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage4.0.branch2.3 |   96x14x14  |    96x7x7    |   0.09 % |   0.06 % | Conv2d k=3 p=1 s=2 |
| stage4.0.branch2.4 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.0.branch2.5 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.0.branch2.6 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.0.branch2.7 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.1.branch2.0 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.1.branch2.1 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.1.branch2.2 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.1.branch2.3 |    96x7x7   |    96x7x7    |   0.09 % |   0.06 % | Conv2d k=3 p=1 s=1 |
| stage4.1.branch2.4 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.1.branch2.5 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.1.branch2.6 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.1.branch2.7 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.2.branch2.0 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.2.branch2.1 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.2.branch2.2 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.2.branch2.3 |    96x7x7   |    96x7x7    |   0.09 % |   0.06 % | Conv2d k=3 p=1 s=1 |
| stage4.2.branch2.4 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.2.branch2.5 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.2.branch2.6 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.2.branch2.7 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.3.branch2.0 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.3.branch2.1 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.3.branch2.2 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.3.branch2.3 |    96x7x7   |    96x7x7    |   0.09 % |   0.06 % | Conv2d k=3 p=1 s=1 |
| stage4.3.branch2.4 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.3.branch2.5 |    96x7x7   |    96x7x7    |   1.01 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| stage4.3.branch2.6 |    96x7x7   |    96x7x7    |   0.04 % |   0.03 % | BatchNorm2d        |
| stage4.3.branch2.7 |    96x7x7   |    96x7x7    |   0.00 % |   0.00 % | ReLU               |
| conv5.0            |   192x7x7   |   1024x7x7   |  21.61 % |  14.30 % | Conv2d k=1 p=0 s=1 |
| conv5.1            |   1024x7x7  |   1024x7x7   |   0.45 % |   0.30 % | BatchNorm2d        |
| conv5.2            |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | ReLU               |
| fc                 |     1024    |     1000     |   2.30 % |  74.56 % | Linear             |
| Total              |  3x224x224  |     1000     |  44.57 M |   1.37 M | ShuffleNetV2       |