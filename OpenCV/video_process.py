import cv2
import string, random,os


# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
#
# cap = cv2.VideoCapture("testin/WIN_20200421_11_20_20_Pro.mp4")
# testout = 'testout/video'

# while cap.isOpened():
#     ret, frame = cap.read()
#     print('frame.shape:', frame.shape)
#     # cv2.imshow('frame', frame)

    # key = cv2.waitKey(delay=40)
    # if key == ord('q'):
    #     break
    # elif key == ord('s'):
        # new_frame = cv2.flip(frame,0)
        # new_frame = cv2.flip(new_frame, 1)
        # cv2.imwrite(os.path.join(testout,id_generator() + '.jpg'), new_frame)
# cap.release()
# cv2.destroyAllWindows()

""" 0 逐帧显示视频"""
# import os
# import cv2
#
# # 视频
# folder = '../14_FloorPlanGenerator_slam/dataset/tour/SV_3tours/01_planB/01_planB'# Desktop\\'
# video = 'video.avi'
# video_name = video.split('.')[0]
# cap = cv2.VideoCapture(os.path.join(folder,video))
#
# c=0
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     if ret:
#         # show a frame
#         frame = cv2.resize(frame,(1024,512))
#         cv2.imshow('im',frame)
#         cv2.waitKey(100)
#         c += 1
#         print(c)
#     else:
#         break



""" 1. 从视频读取帧保存为图片"""
# folder = 'C:\\Users\\srcb03173\\Desktop\\01\PlanBdash\\'# Desktop\\'
# testout = 'C:\\Users\\srcb03173\\Desktop\\01\PlanBdash\\2k\\'
#
#
#
# # 输出视频路径
# #video_dir = 'testout/output.avi'
# # 帧率
# #fps = 24
# # 图片尺寸
# #img_size = (1366, 768)
#
# # fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # video_writer = cv2.VideoWriter(video_dir,fourcc,fps,img_size)
# # videos = os.listdir(folder)
# # for video in videos:
# video = '01_planBdash_1920.avi'
# video_name = video.split('.')[0]
# # out_folder = (os.path.join(testout,video_name))
# # os.makedirs(out_folder,exist_ok=True)
# cap = cv2.VideoCapture(os.path.join(folder,video))
# c=0
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     if ret:
#         # show a frame
#         resize_frame = cv2.resize(frame,(1920,960))
#         # cv2.imshow("capture", resize_frame)
#         # cv2.waitKey(200)
#         #print(c)
#         # keyframe_index = [28,300,530,898,1340,1760,2050,2360,2777,3240,3570] # 02
#         keyframe_index = [5,277,629,940]  # 01
#         # keyframe_index = [10,300,560,835,1200,1440,1880,2150,2580,2990]  # 03
#         if c in keyframe_index:
#             cv2.imwrite(os.path.join(testout, '%.4d' % (c) + '.jpg'), resize_frame)
#             # cut_area = frame[261:290,171:246,:]
#         # if c%20 == 0:
#         #     cv2.imwrite(os.path.join(testout,'%.3d'%(c) + '.jpg'),frame) #存储为图像
#         # video_writer.write(frame)
#         c=c+1
#         # if cv2.waitKey(100) & 0xFF == ord('q'):
#         #     break
#     else:
#         cap.release()
#         # cv2.destroyAllWindows()
#         # video_writer.release()
#         break




""" 2 将图片保存为视频"""
# import os
# import cv2
#
# img_root = 'testin//keyframe'
# fps = 10    #保存视频的FPS，可以适当调整
#
# #可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# videoWriter = cv2.VideoWriter('testout/Ke_03.avi',fourcc,fps,(640,320))#最后一个是保存图片的尺寸
# imgs = os.listdir(img_root)
# for i in range(1500):
#     img_path = img_root+'//keyframe_rgb_'+str(i)+'.jpg'
#     if os.path.isfile(img_path):
#         frame = cv2.imread(img_path) #keyframe_rgb_0
#         print(img_path)
#         videoWriter.write(frame)
#     else:
#         continue
# videoWriter.release()

""" 3 将视频resize"""
# import os
# import cv2
#
# # 原始视频
# folder = 'C:\\Users\\srcb03173\\Desktop\\no_correction'# Desktop\\'
# video = '02_planbdash_nocorrection.MP4'
# video_name = video.split('.')[0]
# cap = cv2.VideoCapture(os.path.join(folder,video))
#
# # resize 后
# fps = 30    #保存视频的FPS，可以适当调整
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# videoWriter = cv2.VideoWriter('testout/02_planbdash_nocorrection_1920.avi',fourcc,fps,(1920,960))#最后一个是保存图片的尺寸
#
# c=0
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     if ret:
#         # show a frame
#         c+=1
#         print(c)
#         frame = cv2.resize(frame,(1920,960))
#         videoWriter.write(frame)
#     else:
#         break
# videoWriter.release()


""" 4 多个视频合成一个视频"""
import os
import cv2
import numpy as np
import glob



# 原始视频
folder = 'kawamura/05/planB/videos'
path_out = os.path.join(folder, 'video.avi')
videos = os.listdir(folder)
capture = cv2.VideoCapture(os.path.join(folder,videos[0]))
fps = capture.get(cv2.CAP_PROP_FPS)

# resize 后的合成的一个视频
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter(path_out,fourcc,fps,(1920,960))#最后一个是保存图片的尺寸

for video in videos:
    print(video)
    video_name = video.split('.')[0]
    cap = cv2.VideoCapture(os.path.join(folder,video))

    c=0
    while(1):
        # get a frame
        ret, frame = cap.read()
        if ret:
            # show a frame
            c+=1
            print(c)
            frame = cv2.resize(frame,(1920,960))
            videoWriter.write(frame)
        else:
            break
videoWriter.release()









