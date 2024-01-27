# import prevampire as pv
from prevampire import prevampire as pv
import numpy.testing as npt
import shutil
import os
import pandas as pd
import numpy as np
from distutils.dir_util import copy_tree
from pandas.testing import assert_frame_equal
import warnings

raw_img_file = './prevampire/tests/data/rawimgtif/'
input_file = './prevampire/tests/data/input/'
output_file = './prevampire/tests/data/output/'

# def _remove_all(directory):

#     arr = os.listdir(directory)
#     arr = [os.path.join(directory, x) for x in arr]
#     for file in arr:
#         os.remove(file)

def _create_dir():
    os.mkdir(input_file)
    os.mkdir(output_file)

def _remove_dir():
    shutil.rmtree(input_file)
    shutil.rmtree(output_file) 

def test_remove_files():
    _create_dir()

    copy_tree(raw_img_file, input_file)
    arr = os.listdir(raw_img_file)
    arr = [x for x in arr if 'cor' not in x]
    pv.remove_files(input_file, 'cor')
    actual = os.listdir(input_file)

    # _remove_all(input_file)

    np.array(actual)
    np.array(arr)

    _remove_dir()

    npt.assert_equal(actual, arr)

def test_move_files():
    _create_dir()

    copy_tree(raw_img_file, input_file)
    arr = os.listdir(raw_img_file)
    arr1 = [x for x in arr if 'hipca' in x]
    arr2 = [x for x in arr if 'hipca' not in x]
    pv.move_files(input_file, output_file, 'hipca')
    check1 = os.listdir(output_file)
    check2 = os.listdir(input_file)

    # _remove_all(input_file)
    # _remove_all(output_file)

    _remove_dir()

    npt.assert_equal(arr1, check1)
    npt.assert_equal(arr2, check2)


def test_take_channel():
    _create_dir()

    copy_tree(raw_img_file, input_file)
    img, name = pv.take_channel(input_file)
    img = np.array(img)
    name = np.array(name)
    img_assert = np.load('./prevampire/tests/data/assertdata/denoised_img_arr.npy')
    name_assert = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')

    flattened_img = np.concatenate([arr.flatten() for arr in img])
    flattened_img_assert = np.concatenate([arr.flatten() for arr in img_assert])

    # _remove_all(input_file)
    _remove_dir()
    
    npt.assert_equal(np.sort(name), np.sort(name_assert))
    npt.assert_equal(np.sort(flattened_img), np.sort(flattened_img_assert))
    # npt.assert_equal(name, name_assert)


def test_save_npy():
    _create_dir()

    imgs = np.load('./prevampire/tests/data/assertdata/denoised_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')
    pv.save_npy(imgs, name, output_file)
    arr = os.listdir(output_file)

    # _remove_all(output_file)
    _remove_dir()

    np.array(arr)

    npt.assert_equal(np.sort(name), np.sort(arr))


def test_save_tif():
    _create_dir()

    warnings.filterwarnings("ignore", category=UserWarning, message=".*low contrast image.*")
    imgs = np.load('./prevampire/tests/data/assertdata/denoised_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')
    pv.save_tif(imgs, name, output_file)

    for i in range(len(name)):
        basename, extension = os.path.splitext(name[i])
        name[i] = basename + '.tif'

    arr = os.listdir(output_file)

    # _remove_all(output_file)
    _remove_dir()

    npt.assert_equal(np.sort(name), np.sort(arr))


def test_apply_and_save_all_thresholds():
    _create_dir()

    imgs = np.load('./prevampire/tests/data/assertdata/denoised_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')

    pv.apply_and_save_all_thresholds(imgs, name, output_file)

    check = os.listdir(output_file)

    # _remove_all(output_file)
    _remove_dir()

    npt.assert_equal(len(check), 5)


def test_apply_threshold():

    imgs = np.load('./prevampire/tests/data/assertdata/denoised_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')
 
    seg1, name1 = pv.apply_threshold(imgs, name)

    seg2 = np.load('./prevampire/tests/data/assertdata/threshli_img_arr.npy')
    name2 = np.load('./prevampire/tests/data/assertdata/threshli_names.npy')

    np.array(seg1)
    np.array(name1)

    npt.assert_equal(seg1, seg2)
    npt.assert_equal(np.sort(name1), np.sort(name2))

    


def test_skeletonize_images():
    imgs = np.load('./prevampire/tests/data/assertdata/threshli_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')

    skel1, name1 = pv.skeletonize_images(imgs, name)

    skel2 = np.load('./prevampire/tests/data/assertdata/skel_img_arr.npy')
    name2 = np.load('./prevampire/tests/data/assertdata/skel_names.npy')
    
    npt.assert_equal(skel1, skel2)
    npt.assert_equal(name1, name2)
 

def test_load_npy_imgs():
    _create_dir()

    copy_tree('./prevampire/tests/data/denoisednpy', input_file)
    data, names = pv.load_npy_imgs(input_file)

    imgs = np.load('./prevampire/tests/data/assertdata/denoised_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')

    # _remove_all(input_file) 
    _remove_dir()

    np.array(data)
    np.array(names)
    
    flattened_data = np.concatenate([arr.flatten() for arr in data])
    flattened_imgs = np.concatenate([arr.flatten() for arr in imgs])
    
    npt.assert_array_equal(np.sort(names), np.sort(name))
    npt.assert_array_equal(np.sort(flattened_data), np.sort(flattened_imgs))


def test_load_tif_imgs():
    _create_dir()

    copy_tree('./prevampire/tests/data/denoisedtif', input_file)
    data, names = pv.load_tif_imgs(input_file)

    imgs = np.load('./prevampire/tests/data/assertdata/denoised_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/denoised_names.npy')

    flattened_data = np.concatenate([arr.flatten() for arr in data])
    flattened_imgs = np.concatenate([arr.flatten() for arr in imgs])

    # _remove_all(input_file)
    _remove_dir()

    npt.assert_equal(np.sort(flattened_data), np.sort(flattened_imgs))
    npt.assert_equal(np.sort(names), np.sort(name))


def test_get_skel_df():
    imgs = np.load('./prevampire/tests/data/assertdata/skel_img_arr.npy')
    name = np.load('./prevampire/tests/data/assertdata/skel_names.npy')

    df1 = pv.get_skel_df(imgs, name)

    df2 = pd.read_csv('./prevampire/tests/data/assertdata/skel_df.csv')

    assert_frame_equal(df1, df1)


     







