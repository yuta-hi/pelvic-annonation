import os
import glob
import numpy as np
import tqdm
import warnings
from pydicom import dcmread
import SimpleITK as sitk

def write_mhd(out, volume, spacing, origin):

    volume = volume.transpose(2,0,1)
    volume = sitk.GetImageFromArray(volume)
    volume.SetSpacing(spacing)
    volume.SetOrigin(origin)
    sitk.WriteImage(volume, out, True)


def convert_dicom(root_dir):

    files = glob.glob(os.path.join(root_dir, '*.dcm'))

    slices = []
    for f in files:
        data = dcmread(f)

        if not hasattr(data, 'SliceLocation'):
            warnings.warn('The attribute `SliceLocation` is not found..')
            continue

        slices.append(data)

    # ensure they are in the correct order
    slices = sorted(slices, key=lambda s: s.SliceLocation)

    # pixel aspects, assuming all slices are the same
    ps = slices[0].PixelSpacing
    ss = slices[0].SliceThickness

    spacing = (float(ps[0]), float(ps[1]), float(ss))
    origin = slices[0].ImagePositionPatient

    # create 3D volume
    dtype = slices[0].pixel_array.dtype
    w, h = slices[0].pixel_array.shape
    z = len(slices)
    volume = np.zeros((w, h, z))

    for i, s in enumerate(slices):

        assert s.PixelSpacing == ps
        assert s.SliceThickness == ss

        pixel_array = s.pixel_array.astype(np.float32)
        pixel_array *= float(s.RescaleSlope)
        pixel_array += float(s.RescaleIntercept)

        volume[:, :, i] = pixel_array

    volume = volume.astype(dtype)

    return volume, spacing, origin


if __name__ == '__main__':

    import config

    dicom_dir = config.dicom_dir
    dicom_dirs = glob.glob(os.path.join(dicom_dir, 'Pelvic-Ref-*/*/*CT*'))

    out_dir = config.volume_dir

    for d in tqdm.tqdm(dicom_dirs, ncols=80):

        if not os.path.isdir(d):
            continue

        out = d.split(os.sep)[-3]
        out = os.path.join(out_dir, out, 'image.mhd')
        os.makedirs(os.path.dirname(out), exist_ok=True)

        volume, spacing, origin = convert_dicom(d)
        write_mhd(out, volume, spacing, origin)
