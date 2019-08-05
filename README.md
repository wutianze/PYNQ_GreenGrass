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
- In other two boards (one is for subscriber, one is for publisher), you will have a root-ca-certs.pem and xxx-setup.tar.gz respectively. Then unzip the package and put button.py|sensor.py in the same directory 
- Wait until the deployment is finished and then you can run publisher and subscriber processes finally.
- The test step is [here](https://docs.aws.amazon.com/zh_cn/greengrass/latest/developerguide/test-comms.html). In publisher board, you can run:
  ```shell
  python basicDiscovery.py --endpoint AWS_IOT_ENDPOINT --rootCA root-ca-cert.pem --cert publisher.cert.pem --key publisher.private.key --thingName HelloWorld_Publisher --topic 'hello/world/pubsub' --mode publish --message 'Hello, World! Sent from HelloWorld_Publisher'
  ```
  And in subscriber board, you run:
  ```shell
  python basicDiscovery.py --endpoint AWS_IOT_ENDPOINT --rootCA root-ca-cert.pem --cert subscriber.cert.pem --key subscriber.private.key --thingName HelloWorld_Subscriber --topic 'hello/world/pubsub' --mode subscribe
  ```
## Further
Now you have learned how to use aws greengrass, you can replace the "hello world" function with something cool. Maybe you can refer to [this](https://github.com/wutianze/PYNQ_GreenGrass/blob/master/demo-learning.md).
