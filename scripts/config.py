import os
import numpy as np

_cur_dir = os.path.dirname(os.path.abspath(__file__))

dicom_dir = os.path.join(_cur_dir, '../.temp/Pelvic-Reference-Data')
volume_dir = os.path.join(_cur_dir, '../volumes')
annotation_dir = os.path.join(_cur_dir, '../annotations')
visualization_dir = os.path.join(_cur_dir, '../figs')

class_list = [
    'background',
    # bone group
    'pelvis',
    'femur',
    'sacrum',
    'spine',
    # hip group
    'gluteus_maximus_muscle',
    'gluteus_medius_muscle',
    'gluteus_minimus_muscle',
    'iliacus_muscle',
    'obturator_externus_muscle',
    'obturator_internus_muscle',
    'pectineus_muscle',
    'piriformis_muscle',
    'psoas_major_muscle',
    # thing group
    'adductor_muscles',
    'biceps_femoris_muscle',
    'gracilis_muscle',
    'rectus_femoris_muscle',
    'sartorius_muscle',
    'semimembranosus_muscle',
    'semitendinosus_muscle',
    'tensor_fasciae_latae_muscle',
    'vastus_lateralis_muscle_and_vastus_intermedius_muscle',
    'vastus_medialis_muscle',
    # abdomen group
    'erector_spinae_muscle',
    'quadratus_lumborum_muscle',
    'rectus_abdominis_muscle',
    'latissimus_dorsi_muscle',
    'oblique_muscle']

class_cmap = np.array([
    [0.00, 0.00, 0.00],
    # bone group
    [1.00, 1.00, 1.00],
    [1.00, 1.00, 1.00],
    [0.50, 0.50, 0.50],
    [1.00, 0.70, 0.70],
    # hip group
    [1.00, 1.00, 0.00],
    [0.00, 1.00, 0.00],
    [1.00, 0.50, 0.50],
    [0.50, 0.00, 0.50],
    [0.00, 0.00, 1.00],
    [1.00, 0.00, 0.00],
    [1.00, 0.00, 1.00],
    [1.00, 0.50, 0.00],
    [0.00, 1.00, 1.00],
    # thing group
    [0.00, 1.00, 1.00],
    [0.75, 1.00, 0.25],
    [1.00, 0.50, 0.50],
    [1.00, 0.00, 0.00],
    [1.00, 1.00, 0.00],
    [1.00, 0.50, 0.00],
    [1.00, 0.00, 1.00],
    [0.00, 0.00, 1.00],
    [0.50, 0.00, 0.50],
    [0.00, 1.00, 0.00],
    # abdomen group
    [0.50, 1.00, 0.00],
    [1.00, 0.00, 0.50],
    [1.00, 1.00, 0.50],
    [1.00, 0.65, 0.00],
    [0.50, 1.00, 1.00]])
