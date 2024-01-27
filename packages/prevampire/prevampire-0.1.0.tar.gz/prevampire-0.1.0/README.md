# `prevampire`

![GitHub](https://img.shields.io/github/license/onoderamia/prevampire)
![Tests](https://github.com/onoderamia/prevampire/actions/workflows/python-package.yml/badge.svg?branch=main)

PREVAMPIRE is a package made to work in supplementary with the [VAMPIRE package](https://github.com/tengjuilin/vampire-analysis). This package contains methods that expedite the user's preparation for the VAMPIRE pipeline, and limits the amount of code interaction needed for someone new to python. 

The package was made to turn raw tif images of microglia into numpy arrays so that the vampire package could be applied succesfully. This package also applies and outputs skeletonization on the images after thresholding. 

The VAMPIRE package returns a dataframe containing characteristics of each microglia identified within the dataset and return average shape modes. 

Cell morphology is used as a support to show the effectivity of therapudics.   

## Installation

If Python is installed on your machine, type the following line into your command prompt to install via [PyPI](ADDHERE):

```bash
pip install vampire-analysis
```

Otherwise, clone the package locally and execute below in bash while in the prevampire directory.

```bash
python setup.py install
```

## Getting started

Create a file which has all the .tif images you want to analyze.

```python
import prevampire as pv  # recommended import signature
raw_dir = 'file/path'  # file path to .tif images
```

## Applying PREVAMPIRE Package

Below are a list of methods you want to apply to get to the desired skeletonization and vampire df and shape modes. Check out [prevampire.py](https://github.com/onoderamia/prevampire/blob/main/prevampire/prevampire.py) for more in depth method comments. 

For a specific dataset, the code uses two .npy arrays to keep track of images while applying thresholding and skeletonization. The image array and the name array. These two arrays are always returned in a specific method. 

To go more in depth to skeletonization, check out the [Skan package](https://skeleton-analysis.org/stable/index.html#) used to find the method desired. 

 ```python

max_imgs, org_names = pv.take_channel(raw_dir, print_image = 1) # maximize image to only include iba

threshall_dir = 'new/file/path' # new file
pv.apply_and_save_all_thresholds(max_imgs, org_names, threshall_dir) # apply all thresholds to a specific subset in the dataset and save them to a defined directory

thresh_imgs, thresh_names = pv.apply_threshold(max_imgs, org_names, label = 'label', method = 'method' print_image = 1) # apply chosen threshold to maximized images (defaults to li)

skel_imgs, skel_names = pv.skeletonize_images(thresh_imgs, thresh_names, print_image = 1) 

skel_df = pv.get_skel_df(skel_imgs, skel_name, show = 1) # get dataframe for skeletonized images

```

Below are a list of supplementary methods you can use throughout the prevampire pipeline. 

 ```python

thresh_tif_dir = 'new/new/file/path' # new file
pv.save_tif(thresh_imgs, thresh_names, thresh_tif_dir) # save .npy arrays as .tif images in a defined directory

thresh_npy_dir = 'new/new/new/file/path' # new file
pv.save_npy(thresh_imgs, thresh_names, thresh_npy_dir) # save .npy arrays as .npy arrays in a defined directory

thresh_imgs, thresh_names = pv.load_tif_imgs(thresh_tif_dir) # load .tif images as .npy arrays in a defined directory

thresh_imgs, thresh_names = pv.load_npy_imgs(thresh_npy_dir) # load .npy arrays as .npy arrays in a defined directory

pv.display_img_side(thresh_imgs, skel_imgs, 0, 'thresh', 'skel') # put images from respective .npy arrays side to side for comparison

output_dir = 'new/new/new/new/file/path' # new file
pv.save_df(skel_df, 'skel_df', output_dir) # save dataframe in defined directory

```

## Applying to VAMPIRE package

Once you get the thresholded images and names, you can then choose to apply these images to the [VAMPIRE package](https://vampire.readthedocs.io/en/latest/index.html). 

 ```python

import vampire as vp
from vampire import quickstart

## Get VAMPIRE dataframe
copy_thresh_arr = thresh_imgs.copy()
copy_thresh_arr = [item.astype('uint8') for item in copy_thresh_arr] # change to compatible type
vampire_df = vp.extraction.extract_properties_from_img_set(copy_thresh_arr, thresh_names) # get df
pv.save_df(vampire_df, 'vampire_df', output_dir) # saved as .csv file (optionial)

## Get VAMPIRE shape mode
build_info_df = pd.DataFrame({
    'img_set_path': [thresh_tif_dir], # define image directory
    'output_path': [output_dir], # define output directory; saved as .png and .pickle file
    'model_name': ['NAME'],
    'num_points': [np.nan],
    'num_clusters': [np.nan],
    'num_pc': [np.nan],
})

quickstart.build_models(build_info_df, random_state=1) # get shape mode

```

## References
[1] Lin, O. VAMPIRE, (2020), GitHub repository, https://github.com/tengjuilin/vampire-analysis

[2] Lin, C. (2021). Skeletonization and fractal analysis of microglial cells in the neonatal brain. [Doctoral dissertation, University of Washington]. ResearchWorks Archive at the University of Washington. https://digital.lib.washington.edu/researchworks/bitstream/handle/1773/47957/Lin_washington_0250O_23542.pdf?sequence=1&isAllowed=y

[3] Juan Nunez-Iglesias, Adam J. Blanch, Oliver Looker, Matthew W. Dixon, and Leann Tilley. A new Python library to analyse skeleton images confirms malaria parasite remodelling of the red blood cell membrane skeleton. PeerJ, 6:e4312, 2018. doi:10.7717/peerj.4312.

