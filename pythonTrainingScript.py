import os
os.system("python train.py --workers 1 --epochs 10 --batch-size 4 --data data/customData.yaml --hyp data/hyp.scratch.tiny.yaml --cfg cfg/training/yolov7-tinyCustom.yaml --name mlops_trial --weights best.pt")



os.system("python test.py --data data/ForTesting.yaml --batch 4 --conf 0.4 --iou 0.5 --weights runs/train/mlops_trial/weights/best.pt --name testingstats")



os.system("python test.py --data data/StatsonTrain.yaml --batch 4 --conf 0.4 --iou 0.5 --weights runs/train/mlops_trial/weights/best.pt --name trainingstats")



os.system("python test.py --data data/StatsOnVal.yaml --batch 4 --conf 0.4 --iou 0.5 --weights runs/train/mlops_trial/weights/best.pt --name valstats")
