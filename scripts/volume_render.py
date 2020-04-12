import os
import glob
import tqdm
import cv2
from pyvr import volume_render

def main(volume_file, out):

    proj = volume_render(volume_file,
                    preset='muscle',
                    pos=(0, -1200, 0),
                    bg=(0, 0, 0),
                    rotate_angles=[0, 90, 180, 270])

    for i, p in enumerate(proj):
        cv2.imwrite(out + '_image_%d.jpg' % i,
                    p[:, :, ::-1])


if __name__ == '__main__':

    import config

    volume_dir = config.volume_dir
    volume_files = glob.glob(os.path.join(volume_dir, 'Pelvic-Ref-*/image.mhd'))

    out_dir = config.visualization_dir

    for f in tqdm.tqdm(volume_files, ncols=80):
        out = f.split(os.sep)[-2]
        out = os.path.join(out_dir, out)
        main(f, out)
