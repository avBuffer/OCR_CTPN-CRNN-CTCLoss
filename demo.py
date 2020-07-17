import os
import sys
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob
from ocr import ocr


def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB'))
    result, image_framed = ocr(image)
    return result,image_framed


if __name__ == '__main__':
    img_path = 'data/imgs'
    out_path = 'data/result'
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    img_files = sorted(os.listdir(img_path))
    print('img_path=', img_path, ' img_files.len=', len(img_files))

    for idx, img in enumerate(img_files):
        t = time.time()
        img_file = os.path.join(img_path, img)
        result, image_framed = single_pic_proc(img_file)

        out_file = os.path.join(out_path, img)
        Image.fromarray(image_framed).save(out_file)

        txt_file = out_file.replace('.jpg', 'txt')
        p_txt_file = open(txt_file, 'w')
        
        print("Recognition Result:")
        for jdx, key in enumerate(result):
            print('jdx=', jdx, ' key=', result[key][1], ' result[key]=', result[key])            
            p_txt_file.write(str(jdx) + ' ' + result[key][1] + ' ' + str(round(result[key][0][-1] * 100, 2)) + '\n')
        
        p_txt_file.close()
        print('idx=', idx, ' img_file=', img_file, ' out_file=', out_file, ' txt_file=', txt_file, 
              "Mission complete, it took {:.3f}s".format(time.time() - t))
