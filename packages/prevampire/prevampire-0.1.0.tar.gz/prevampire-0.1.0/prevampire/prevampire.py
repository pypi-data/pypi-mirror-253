# prevampire/prevampire.py
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
import skimage
import vampire as vp
import skan
import random
import pandas as pd

from scipy import ndimage
from skimage import io, filters, morphology
from skimage.filters import try_all_threshold
from skan.csr import Skeleton, summarize
from skan import draw

threshold_functions = {
    'li': filters.threshold_li,
    'otsu': filters.threshold_otsu,
    'yen': filters.threshold_yen,
    'isodata': filters.threshold_isodata,
    'minimum': filters.threshold_minimum,
    'mean': filters.threshold_mean,
    'triangle': filters.threshold_triangle
}

class UnequalLengthError(Exception):
    """
    Custom exception class for unequal lengths of arrays.

    This exception is raised when two arrays or sequences are expected to have
    the same length, but their lengths are found to be unequal.
    """
    pass

def _check_equal_lengths(arr1, arr2):
    """
    Check if the lengths of two arrays are equal.

    Parameters:
    - arr1 (list or array-like): First array to compare.
    - arr2 (list or array-like): Second array to compare.

    Raises:
    - UnequalLengthError: If the lengths of the two arrays are not equal.
    """
    if len(arr1) != len(arr2):
         raise UnequalLengthError("Image and name arrays must have the same length.")

def _get_file_path_list(file_dir, keyword = None, fullpath = True):
    """
    Get a list of files in a given directory.

    Parameters:
    - file_dir (str): The directory to retrieve files from.
    - keyword (str, optional): A keyword to filter files. Defaults to None.
    - fullpath (bool, optional): Whether to include the full path in the result. Defaults to True.

    Returns:
    - list: A list of file names in the directory.
    """
    arr = os.listdir(file_dir)

    if keyword is not None:
        arr = [x for x in arr if keyword in x]
    
    arr = [x for x in arr if not x.startswith('.')]

    if fullpath:
        arr = [os.path.join(file_dir, x) for x in arr]

    return arr

def _create_prop_df(skel_img_name, props):
    dataframe = pd.DataFrame(props)
    dataframe['filename'] = skel_img_name
    
    return dataframe

def _draw_branch_type(skel_img, dataframe):
    draw.overlay_euclidean_skeleton_2d(skel_img, dataframe,
        skeleton_color_source='branch-type');

def remove_files(file_dir, delete):
    """
    Remove specific files from a given file directory.

    Parameters:
    - file_dir (str): The directory to remove files from.
    - delete (str): Substring to match files for deletion.
    """
    file_path_list = _get_file_path_list(file_dir, delete)

    for file_path in file_path_list:
        os.remove(file_path)

def move_files(file_dir, target_dir, takeout):
    """
    Move specific files from one directory to another.

    Parameters:
    - file_dir (str): The directory to take files from.
    - takeout (str): Substring to match files to take out.
    - target_dir (str): The directory to place files in.
    """
    file_path_list = _get_file_path_list(file_dir, takeout)

    for file_path in file_path_list:
        shutil.move(file_path, target_dir)

## THINK ABOUT THE LABEL AND HOW IT WORKS OR SOMETHING CUTTING IT OUT????? DONE
## literally all inputs should come from this img name list
def take_channel (img_dir, print_image = 0):
    """
    Process images from a given directory, creating maximum intensity projections.

    Parameters:
    - img_dir (str): The directory containing raw tif images.
    - print_image (int, optional): Number of images to display. Defaults to 0.

    Returns:
    - tuple: A tuple containing two elements:
        - result_images (list): A list of 2D arrays representing maximum intensity projection images.
        - img_name_list (list): A 1D array of corresponding image names.
    """
    img_name_list = _get_file_path_list(img_dir, fullpath = False)
    for i in range(len(img_name_list)):
        basename, extension = os.path.splitext(img_name_list[i])
        img_name_list[i] = basename + '.npy'
    
    img_path_list = _get_file_path_list(img_dir)
    result_images = []
    for img_dir in img_path_list:
        img_max = io.imread(img_dir)
        img = img_max[:, 1, :, :]
        img_max = np.max(img, axis=0) 

        result_images.append(np.array(img_max))
        
    

    if print_image > 0:
        for i in range(print_image):
            plt.imshow(result_images[i])
            plt.show()  

    return result_images, img_name_list

## CHANGE THIS FOR LABEL OR SOMETHING DONE
def save_npy(img_arr, img_name_list, save_location):
    """
    Save NumPy arrays as .npy files in the specified location.

    Parameters:
    - img_arr (list): A list of NumPy arrays representing images.
    - img_name_list (list): A list of image names corresponding to the arrays.
    - save_location (str): The directory where the .npy files will be saved.

    Raises:
    - UnequalLengthError: If the lengths of the input arrays are not equal.

    Note:
    - The function first checks if the lengths of `img_arr` and `img_name_list` are equal.
    - It then modifies the image names to include the save location and iteratively saves each array.
    """
    _check_equal_lengths(img_arr, img_name_list)

    modified_name_list = img_name_list.copy()
    modified_name_list = [os.path.join(save_location, x) for x in modified_name_list]

    for i in range(len(img_arr)):
        np.save(modified_name_list[i], img_arr[i])

## assumng arr are .npy files
## CHANGE THIS FOR LABEL OR SOMETHING?? DONE
## change name .npy to .tif DONE
def save_tif(img_arr, img_name_list, save_location):
    """
    Save images as .tif files in the specified location.

    Parameters:
    - img_arr (list): A list of NumPy arrays representing images.
    - img_name_list (list): A list of image names corresponding to the arrays.
    - save_location (str): The directory where the .tif files will be saved.

    Raises:
    - UnequalLengthError: If the lengths of the input arrays are not equal.

    Note:
    - The function first checks if the lengths of `img_arr` and `img_name_list` are equal.
    - It then modifies the image names to include the save location and iteratively saves each image as a .tif file.
    """
    _check_equal_lengths(img_arr, img_name_list)
    modified_name_list = img_name_list.copy()
    modified_name_list = [os.path.join(save_location, x) for x in modified_name_list]

    for i in range(len(img_arr)):
        basename, extension = os.path.splitext(modified_name_list[i])
        name = basename + '.tif'
        io.imsave(name, img_arr[i])

## assuming name is just name not whole path
def apply_and_save_all_thresholds(img_arr, img_name_list, output_dir, num_imgs = 5):
    """
    Apply various thresholding methods and save the results as .tif files.

    Parameters:
    - img_arr (list): A list of NumPy arrays representing the intensified images.
    - img_name_list (list): A list of image names corresponding to the arrays.
    - output_dir (str): The directory where the thresholded images will be saved.
    - num_imgs (int, optional): The number of images to select for thresholding and saving. Defaults to 5.

    Raises:
    - UnequalLengthError: If the lengths of the input arrays are not equal.

    Note:
    - The function first checks if the lengths of `img_arr` and `img_name_list` are equal.
    - It randomly selects a specified number of images from the input arrays.
    - For each selected image, it applies various thresholding methods and saves the resulting plots as .tif files.
    """
    _check_equal_lengths(img_arr, img_name_list)
    if len(img_arr) >= num_imgs:
        selected_img_indices = random.sample(range(len(img_arr)), num_imgs)
    elif len(img_arr >= 2):
        selected_img_indices = random.sample(range(len(img_arr)), 2)
    else: 
        selected_img_indices = random.sample(range(len(img_arr)), 1)

    selected_img = [img_arr[i] for i in selected_img_indices]
    selected_img_names = [img_name_list[i] for i in selected_img_indices]

    for i in range(len(selected_img)):
        fig, ax = try_all_threshold(selected_img[i], figsize = (10, 8), verbose = False)
        basename, extension = os.path.splitext(selected_img_names[i])
        fig_name = basename + '_all_thresh.tif'
        
        fig_path = os.path.join(output_dir, fig_name)
        fig.savefig(fig_path)
        plt.close('all')

def apply_threshold(img_arr, img_name_list, label = 'threshli', method = 'li', print_image = 0):
    """
    Apply a thresholding method to a list of images and return segmented images.

    Parameters:
    - img_arr (list): A list of NumPy arrays representing the indensified images.
    - img_name_list (list): A list of image names corresponding to the arrays.
    - label (str, optional): A label to append to the segmented image names. Defaults to 'threshli'.
    - print_image (int, optional): Number of segmented images to display. Defaults to 0.
    - method (str, optional): The thresholding method to use. Defaults to 'li'.

    Returns:
    - tuple: A tuple containing two elements:
        - segmented_images (list): A list of segmented images.
        - seg_name_list (list): A list of corresponding segmented image names.

    Raises:
    - UnequalLengthError: If the lengths of the input arrays are not equal.

    Note:
    - The function first checks if the lengths of `img_arr` and `img_name_list` are equal.
    - It applies the specified thresholding method to each image, removes small objects, and fills holes.
    - The segmented images and their names are returned as lists.
    - Optionally, a specified number of segmented images can be displayed.

    - The returned name list should only be used for saving. Unless the name BASENAME_threshli_skel.npy is 
    - desired, use the original name list from the take_channel method when passing the img_name_list
    - to to skeletonize_images method.
    """
    _check_equal_lengths(img_arr, img_name_list)
    thresh_function = threshold_functions.get(method, filters.threshold_li)
    
    seg_name_list = []

    for i in range(len(img_name_list)):
        base_name, extension = os.path.splitext(img_name_list[i])
        name = base_name + '_' + label + extension
        seg_name_list.append(name)

    segmented_images = []

    for i in range(len(img_arr)):
        thresh = thresh_function(img_arr[i])
        binary = img_arr[i] > thresh
        new_binary = morphology.remove_small_objects(binary, min_size = 71)
        new_binary = ndimage.binary_fill_holes(new_binary)

        segmented_images.append(np.array(new_binary))
        

    if print_image > 0:
        for i in range(print_image):
            plt.imshow(segmented_images[i])
            plt.show() 

    return segmented_images, seg_name_list

def skeletonize_images(thresh_arr, img_name_list, label = 'skel', print_image = 0):
    """
    Skeletonize a list of binary images and return the skeletonized images.

    Parameters:
    - thresh_arr (list): A list of thresholded binary images.
    - img_name_list (list): A list of image names corresponding to the arrays (use the name list from take_channel).
    - label (str, optional): A label to append to the skeletonized image names. Defaults to 'skel'.
    - print_image (int, optional): Number of skeletonized images to display. Defaults to 0.

    Returns:
    - tuple: A tuple containing two elements:
        - skel_imgs (list): A list of skeletonized images.
        - skel_name_list (list): A list of corresponding skeletonized image names.

    Raises:
    - UnequalLengthError: If the lengths of the input arrays are not equal.

    Note:
    - The function first checks if the lengths of `thresh_arr` and `img_name_list` are equal.
    - It skeletonizes each binary image using morphology.skeletonize.
    - The skeletonized images and their names are returned as lists.
    - Optionally, a specified number of skeletonized images can be displayed.
    """
    _check_equal_lengths(thresh_arr, img_name_list)

    skel_name_list = []

    for i in range(len(img_name_list)):
        base_name, extension = os.path.splitext(img_name_list[i])
        name = base_name + '_' + label + extension
        skel_name_list.append(name)

    skel_imgs = []

    for i in range(len(thresh_arr)):
        skel_img = morphology.skeletonize(thresh_arr[i])
        skel_imgs.append(skel_img)

    if print_image > 0:
        for i in range(print_image):
            plt.imshow(skel_imgs[i])
            plt.show()  

    return skel_imgs, skel_name_list

def display_img_side(array1, array2, index, label1, label2):
    """
    Display two images side by side for visual comparison.

    Parameters:
    - array1 (list): A list of images or arrays.
    - array2 (list): Another list of images or arrays.
    - index (int): Index of the images to display.
    - label1 (str): Label for the first set of images.
    - label2 (str): Label for the second set of images.

    Returns:
    - None: Displays the images using Matplotlib.

    Note:
    - The function creates a side-by-side comparison of two images from the input arrays.
    - The specified index determines which images to display.
    - Labels for each set of images are provided.
    - The images are shown using Matplotlib's plt.show().

    - This should be usually used when comparing with raw vs thresh or thresh vs skel. 
    """

    image1 = array1[index]
    image2 = array2[index]

    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (8,4), sharex = True, sharey = True)
    ax = axes.ravel()

    ax[0].imshow(image1, cmap=plt.cm.gray)
    ax[0].axis('off')
    ax[0].set_title(f'{label1} - Image {index}', fontsize=12)

    ax[1].imshow(image2, cmap=plt.cm.gray)
    ax[1].axis('off')
    ax[1].set_title(f'{label2} - Image {index}', fontsize=12)

    fig.tight_layout()
    plt.show()

## load tif array
## load np array
## EDIT THIS BECUASE THE TIF MAY BE DIFF DONE
## THIS SHOULD NOT BE USED FOR THE BRIGHTENING FR
## SEPARATE FORLESS CONFUSION DONE

## FOR HAWLEY SINICE SHE MAKES .npy for ebery image
def load_npy_imgs(directory):
    """
    Load files from a given directory of .npy files.

    Parameters:
    - directory (str): The directory containing files.

    Returns:
    - list: A list of loaded NumPy arrays or images.
    """
    file_paths = _get_file_path_list(directory)
    img_name_list = _get_file_path_list(directory, fullpath = False)

    loaded_data = []
    for file_path in file_paths:
        loaded_data.append(np.load(file_path))
        

    return loaded_data, img_name_list

## assume that the brightning has alr been done... 
## coming from a thresh or etc... 
def load_tif_imgs(directory):
    """
    Load files from a given directory of .tif files.

    Parameters:
    - directory (str): The directory containing files.

    Returns:
    - list: A list of loaded NumPy arrays or images.

    Note:
    - The tif files should be images that have alreldy been intensified.
    - Use the take_channel images if they are raw. 
    - This should only be used if the user wants to put intensified, segmented, or skeletonized
    - images save on a computer into a numpy array to collect data from. 
    """
    file_paths = _get_file_path_list(directory)
    img_name_list = _get_file_path_list(directory, fullpath = False)

    loaded_data = []
    for file_path in file_paths:
        loaded_data.append(io.imread(file_path))
        
    loaded_data = np.array(loaded_data)
    
    for i in range(len(img_name_list)):
        basename, extension = os.path.splitext(img_name_list[i])
        img_name_list[i] = basename + '.npy'

    return loaded_data, img_name_list

## get data for skel
def get_skel_df(skel_arr, skel_name_list, show = 0):
    """
    Process a list of skeletonized images, extract properties, and display branch types.

    Parameters:
    - skel_arr (list): A list of skeletonized images or arrays.
    - skel_name_list (list): A list of names corresponding to the skeletonized images.
    - show (int, optional): The number of images to display branch types. Defaults to 0.

    Returns:
    - pd.DataFrame: A Pandas DataFrame containing skeletonization properties.

    Note:
    - The function processes a list of skeletonized images and extracts properties using the skan library.
    - Skeletonization properties are summarized, and a Pandas DataFrame is created.
    - The show parameter determines the number of images for which branch types are displayed.

    - To print out the dataframe, type the name of the df you set and press enter. 
    """
    for i in range(len(skel_arr)):
        new_skel_img = skel_arr[i].astype('uint8')
        props_v1 = skan.csr.Skeleton(new_skel_img)
        props = skan.csr.summarize(props_v1)

        if i == 0:
            df_skel = _create_prop_df(skel_name_list[i], props)
            if show > 0:
                _draw_branch_type(new_skel_img, props)
        else:
            df_skel2 = _create_prop_df(skel_name_list[i], props)
            frames = [df_skel, df_skel2]
            df_skel = pd.concat(frames)
            if show > i:
                _draw_branch_type(new_skel_img, props)
        
    return df_skel

def save_df(dataframe, name, output_dir):
    name = name + '.csv'
    dataframe.to_csv(os.path.join(output_dir, name))