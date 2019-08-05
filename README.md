# AWS IOT LAB
## Preparation
- > 3 PYNQ-Z2  
  > AWS account  
  > 1 switch  
- Connect to your boards successfully.
- Make sure your boards can access internet.

## Read and try first
[AWS Tutorial](https://docs.aws.amazon.com/zh_cn/greengrass/latest/developerguide/gg-gs.html)
## Step by Step
- Connect to your board.
- run the following commands on all boards.
  ```shell
  sudo adduser --system ggc_user
  sudo addgroup --system ggc_group
  ```
- In our lab, we will have one board used as core, two boards as device (one board used as publisher and the other used as subscriber).
- In the core board, you have to follow [module2](https://docs.aws.amazon.com/zh_cn/greengrass/latest/developerguide/module2.html) to set your board.
- In the device board, you have to follow [module4](https://docs.aws.amazon.com/zh_cn/greengrass/latest/developerguide/module4.html) to create your two devices. Please pay attention that the tutorial uses just one pc, we have to split the pc into two PYNQ boards. What you need to do is just replacing the two consoles opened in pc with two boards.
- Now, in your core board, you will have /greengrass and you should run the daemon process in it.
  ```shell
  cd /greengrass/ggc/core/
  sudo ./greengrassd start
  ```
- In other two boards (one is for subscriber, one is for publisher), you will have a root-ca-certs.pem and xxx-setup.tar.gz respectively. Then unzip the package and put button.py|sensor.py in the same directory.
- Edit the button.py|sensor.py, find places "xxxx" and replace them with your own settings.
- Deploy your group and wait until the deployment is finished and then you can run publisher and subscriber processes finally.
- The test step is [here](https://docs.aws.amazon.com/zh_cn/greengrass/latest/developerguide/test-comms.html). In publisher board, you can run:
  ```shell
  sudo python3 button.py
  ```
  And in subscriber board, you run:
  ```shell
  sudo python3 sensor.py
  ```
- Now when you press the button in publisher you can see leds in subscriber glitter. Also you can build a subscriber in AWS cloud. Search AWS IoT in *Services*. Choose *Test* and then *Subscribe to a topic*, fill the topic with yours(here hello/world/pubsub). In *MQTT payload display*, we choose the second *Display payloads as strings*. Now subscribe to the topic and you will find a new tip on the left, enter it and you can watch the information of the button actions.
## Further
Now you have learned how to use aws greengrass, you can replace the "hello world" function with something cool. Maybe you can refer to [this](https://github.com/wutianze/PYNQ_GreenGrass/blob/master/demo-learning.md).
