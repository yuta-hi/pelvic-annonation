import os
import glob
import tqdm
import cv2
from pyvr import surface_render

def main(volume_file, out):

    _cur_dir = os.path.dirname(os.path.abspath(__file__))
    preset_file = os.path.join(_cur_dir, 'preset/muscle.json')

    proj = surface_render(volume_file,
                    preset=preset_file,
                    pos=(0, -1200, 0),
                    bg=(0, 0, 0),
                    rotate_angles=[0, 90, 180, 270])

    for i, p in enumerate(proj):
        cv2.imwrite(out + '_label_%d.jpg' % i,
                    p[:, :, ::-1])


if __name__ == '__main__':

    import config

    label_dir = config.annotation_dir
    label_files = glob.glob(os.path.join(label_dir, 'Pelvic-Ref-*/label.mhd'))

    out_dir = config.visualization_dir

    for f in tqdm.tqdm(label_files, ncols=80):
        out = f.split(os.sep)[-2]
        out = os.path.join(out_dir, out)
        main(f, out)
