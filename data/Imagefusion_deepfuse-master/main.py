# Demo - train the DeepFuse network & use it to generate an image

from __future__ import print_function

import time

from train_recons import train_recons
from generate import generate
from utils import list_images
import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# IS_TRAINING = True
IS_TRAINING = False

BATCH_SIZE = 2
EPOCHES = 4

MODEL_SAVE_PATH = '/home/bingyang/wby/data/Imagefusion_deepfuse-master/models/deepfuse_models/deepfuse_model_bs2_epoch4_all.ckpt'

# model_pre_path is just a pre-train model and not necessary. It is set as None when you want to train your own model.
# model_pre_path  = 'your own pre-train model'
model_pre_path  = None

def main():

    if IS_TRAINING:

        original_imgs_path = list_images('D:/ImageDatabase/Image_fusion_MSCOCO/original/')

        print('\nBegin to train the network ...\n')
        train_recons(original_imgs_path, MODEL_SAVE_PATH, model_pre_path, EPOCHES, BATCH_SIZE, debug=True)

        print('\nSuccessfully! Done training...\n')
    else:

        output_save_path = '/home/bingyang/wby/1/'
        # sourceA_name = 'image'
        # sourceB_name = 'image'
        sourceA_name = 'IR'
        sourceB_name = 'VIS'
        print('\nBegin to generate pictures ...\n')

        content_name = '/home/bingyang/wby/1/1.png'
        style_name = '/home/bingyang/wby/1/2.png'

        for i in range(1):
            index = i + 1
            content_path = content_name
            style_path = style_name
            # content_path = content_name + str(index) + '_left.png'
            # style_path = style_name + str(index) + '_right.png'
            generate(content_path, style_path, MODEL_SAVE_PATH, model_pre_path, index, output_path=output_save_path)

        # print('\ntype(generated_images):', type(generated_images))
        # print('\nlen(generated_images):', len(generated_images), '\n')


if __name__ == '__main__':
    main()

