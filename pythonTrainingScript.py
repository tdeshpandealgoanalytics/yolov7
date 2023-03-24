import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
import os
from datetime import date
from azure.storage.blob import BlobServiceClient

NAMESPACE_CONNECTION_STR = "Endpoint=sb://akshamodeltrainerqueue.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=uV6S2PCkenwicBgpdwLSqnFA14BBY2D9t+ASbE+6a84="
QUEUE_NAME = "model-trainer"

async def run():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:

        async with servicebus_client:
            # get the Queue Receiver object for the queue
            receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
            async with receiver:
                received_msgs = await receiver.receive_messages(max_wait_time=5, max_message_count=20)
                for msg in received_msgs:
                    
                    # complete the message so that the message is removed from the queue
                    await receiver.complete_message(msg)
                    return {"message": str(msg)}
while True:
    resp = asyncio.run(run())
    if resp:
        os.system("python train.py --workers 1 --epochs 10 --batch-size 4 --data data/customData.yaml --hyp data/hyp.scratch.tiny.yaml --cfg cfg/training/yolov7-tinyCustom.yaml --name mlops_trial --weights best.pt --project '/app/yolov7-custom/data/model'")



        os.system("python test.py --data data/ForTesting.yaml --batch 4 --conf 0.4 --iou 0.5 --weights runs/train/mlops_trial/weights/best.pt --name testingstats  --project '/app/yolov7-custom/data/model'")



        os.system("python test.py --data data/StatsonTrain.yaml --batch 4 --conf 0.4 --iou 0.5 --weights runs/train/mlops_trial/weights/best.pt --name trainingstats --project '/app/yolov7-custom/data/model'")



        os.system("python test.py --data data/StatsOnVal.yaml --batch 4 --conf 0.4 --iou 0.5 --weights runs/train/mlops_trial/weights/best.pt --name valstats --project '/app/yolov7-custom/data/model'")

       
                    
        print("Done sending messages", resp["message"])