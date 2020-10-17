# convert 0 to 1

import os

files=os.listdir('YOLO_copy')
for j in files:
    with open('YOLO_copy/'+j,'r+') as f:
        count=0
        for i in f.readlines():
            f.seek(count)
            f.write('1')
            n = len(i)
            count+=n


0 - pedestrian

1 - head 

2 - number plate


path of 1 => /media/media/vidooly/myfiles/DeepLearning/ml/projects/user/alaap/YOLOv4/data/data_faces/images
path of 2 => /media/media/vidooly/myfiles/DeepLearning/ml/projects/user/alaap/YOLOv4/data/data_plate/

ml/projects/users/minhaj/pedestrian_detection/data/raw/download_google_drive/alaap_copy/sur_train


11500+7750+88358 +79642+11488+11518
3080+2300+


base='/ml/projects/users/minhaj/pedestrian_detection/data/raw/download_google_drive/'

ad_train
    ad_01 - 80358
    ad_02 - 79642
    ad_03 - 11480
sur_train - 11518
val = 10000


https://github.com/gjy3035/Awesome-Crowd-Counting/blob/master/src/Datasets.md


root path: /ml/projects/users/minhaj/pedestrian_detection/darknet/

weight file path: ./build/darknet/x64/data/backup/head_only/yolov4-head-only_best.weights

cfg: /ml/projects/users/minhaj/pedestrian_detection/darknet/cfg/yolov4-head-only.cfg


import os 
 
for j in l2: 
     with open('labels_2/'+j,'r+') as f: 
         count=0 
         for i in f.readlines(): 
             f.seek(count) 
             f.write('1') 
             n = len(i) 
             count+=n                                                                          
 
import os
# add 1 to 0  
for j in os.listdir('../ad_01_copy'): 
    if j.split('.')[-1]=='txt':
        with open('../ad_01_copy/'+j,'r') as o: 
            for line in o.readlines():  
                with open(j,'a') as f: 
                    f.write(line) 

#remove unwanted

import os
plots=os.listdir('test')
with open('plot.txt','r') as f:
    keep=[i.strip() for i in f.readlines()]
for i in plots: 
        if i.split('.')[-1]!='txt' and i not in keep:  
            try: 
                os.remove('compressed_half_2/'+i) 
                os.remove('compressed_half_2/'+i.split('.')[0]+'.txt') 
            except Exception as r: 
                print(r)
                




wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1UcR-zVoMs7DH5dj3N1bswkiQTA4dmKF4' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1UcR-zVoMs7DH5dj3N1bswkiQTA4dmKF4" -O gun_2.zip && rm -rf /tmp/cookies.txt

https://drive.google.com/file/d//view?usp=sharing

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1CnZL8JhOOcWRX5oYbPdLyqHUQOT3n_Zc' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1CnZL8JhOOcWRX5oYbPdLyqHUQOT3n_Zc" -O all.rar && rm -rf /tmp/cookies.txt


/home/vidooly/ml/projects/users/minhaj/pedestrian_detection/darknet/build/darknet/x64/data/backup/ ismai weights h, 1000.weghts last.weights dekhlio
/home/vidooly/ml/projects/users/minhaj/pedestrian_detection/darknet/build/darknet/x64/data/traffic.data 
/home/vidooly/ml/projects/users/minhaj/pedestrian_detection/darknet/build/darknet/x64/data/traffic.names
/home/vidooly/ml/projects/users/minhaj/pedestrian_detection/darknet/cfg/yolov4-traffic.cfg

Angeles is Obsidian Security, a startup offering cybersecurity for cloud services.

for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done

ls | sort -R | head -1200 | xargs mv ./ -t ../../val/unsafe/


Size Comparison - Biggest vs Smallest Objects in the Universe
https://www.youtube.com/watch?v=aUUVzoDMDGE



E-mail: jobs@nnaisense.com

https://youtu.be/k70xBg8en-4