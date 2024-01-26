import glob
from typing import List, Union, Optional
try:
    from typing import Literal
except:
    from typing_extensions import Literal
import numpy as np
from shapely.geometry import Polygon, MultiPolygon
from simba.utils.errors import InvalidInputError
from simba.utils.enums import GeometryEnum
from copy import deepcopy
from simba.utils.checks import check_iterable_length, check_instance
from simba.mixins.geometry_mixin import GeometryMixin
import cv2
import pandas as pd
from simba.utils.errors import CountError


def geometry_histocomparison(imgs: List[np.ndarray],
                             shapes: Optional[List[Union[Polygon, MultiPolygon]]] = None,
                             method: Optional[Literal['chi_square', 'correlation', 'intersection', 'bhattacharyya', 'hellinger', 'chi_square_alternative', 'kl_divergence']] = 'correlation') -> float:

    """
    Compare the histograms of N polygons geometries in N images. Returns the mean difference between the histogram of the shape in the last image and each of the histograms of the polygons in the prior image.

    For example, the polygon may represent an area around a rodents head. While the front paws are not pose-estimated, computing the histograms of the N shapes in the N images can indicate if the front paws are static, or non-static.

    .. note::
       The method first computes the intersection of all the polygons and use the intersection to compute histogram comparisons. Thus, changes in the polygon shape across the images per se cannot account for differences in output results.
       If shapes is None, the entire images in ``imgs`` will be compared.
       `Documentation <https://docs.opencv.org/4.x/d6/dc7/group__imgproc__hist.html#gga994f53817d621e2e4228fc646342d386ad75f6e8385d2e29479cf61ba87b57450>`__.

    .. image:: _static/img/geometry_histocomparison.png
       :width: 700
       :align: center

    :parameter List[np.ndarray] imgs: List of N input images.
    :parameter List[Union[Polygon, MultiPolygon]] shapes: If not None, then List of N polygons to compare with the images (one shape per image)
    :parameter Literal['correlation', 'chi_square'] method: The method used for comparison. E.g., if `correlation`, then small output values suggest large differences between the current versus prior images. If `chi_square`, then large output values  suggest large differences between the current versus prior images
    :return float: Value representing the current image similarity to the prior images.

    :example:
    >>> frm_dir = '/Users/simon/Desktop/envs/troubleshooting/Emergence/project_folder/videos/img_comparisons_4'
    >>> data_path = '/Users/simon/Desktop/envs/troubleshooting/Emergence/project_folder/csv/outlier_corrected_movement_location/Example_1.csv'
    >>> data = pd.read_csv(data_path, nrows=4, usecols=['Nose_x', 'Nose_y']).fillna(-1).values.astype(np.int64)
    >>> imgs, polygons = [], []
    >>> for file_path in sorted(glob.glob(frm_dir + '/*.png')): imgs.append(cv2.imread(file_path))
    >>> for frm_data in data: polygons.append(GeometryMixin().bodyparts_to_circle(frm_data, 100))
    >>> geometry_histocomparison(imgs=imgs, shapes=polygons, method='correlation')
    """

    check_instance(source=f'{geometry_histocomparison.__name__} imgs', instance=imgs, accepted_types=list)
    check_iterable_length(f'{geometry_histocomparison.__name__} imgs', val=len(imgs), min=2)
    if method not in GeometryEnum.HISTOGRAM_COMPARISON_MAP.value.keys(): raise InvalidInputError(msg=f'Method {method} is not supported. Accepted options: {GeometryEnum.HISTOGRAM_COMPARISON_MAP.value.keys()}', source=geometry_histocomparison.__name__)
    for i in range(len(imgs)): check_instance(source=f'{geometry_histocomparison.__name__} imgs {i}', instance=imgs[i], accepted_types=np.ndarray)
    if shapes:
        check_instance(source=f'{geometry_histocomparison.__name__} shapes', instance=shapes, accepted_types=list)
        if len(imgs) != len(shapes): raise CountError(msg=f'Images and shapes have to be the same size. imgs size: {len(imgs)}, shapes size: {len(shapes)}', source=geometry_histocomparison.__name__)
        for i in range(len(shapes)): check_instance(source=f'{geometry_histocomparison.__name__} shapes {i}', instance=shapes[i], accepted_types=(Polygon, MultiPolygon))
        shared_shape = shapes[0]
        for i in range(1, len(shapes)+1): shared_shape = shapes[1].intersection(shared_shape)
        shared_shape_arr = np.array(shared_shape.exterior.coords).astype(np.int64)
        roi_imgs = []
        for img_cnt, img in enumerate(imgs):
            x, y, w, h = cv2.boundingRect(shared_shape_arr)
            roi_img = img[y:y + h, x:x + w].copy()
            mask = np.zeros(roi_img.shape[:2], np.uint8)
            cv2.drawContours(mask, [shared_shape_arr - shared_shape_arr.min(axis=0)], -1, (255, 255, 255), -1, cv2.LINE_AA)
            bg = np.ones_like(roi_img, np.uint8)
            cv2.bitwise_not(bg, bg, mask=mask)
            roi_img = bg + cv2.bitwise_and(roi_img, roi_img, mask=mask)
            if len(roi_img) > 2:
                roi_img = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
            roi_imgs.append(roi_img)
            # cv2.imshow('roi_img', roi_img)
            # print(img_cnt)
            # cv2.waitKey(5000)

    else:
        roi_imgs = deepcopy(imgs)

    method = GeometryEnum.HISTOGRAM_COMPARISON_MAP.value[method]
    current_roi_img = roi_imgs[-1]
    mask_current_roi_img, diff = (current_roi_img != 0), 0
    for img_cnt in range(0, len(roi_imgs)-1):
        mask_previous = (roi_imgs[img_cnt] != 0)
        combined_mask = np.logical_or(mask_current_roi_img, mask_previous)
        non_zero_current, non_zero_previous = current_roi_img[combined_mask], roi_imgs[img_cnt][combined_mask]
        diff += cv2.compareHist(non_zero_current.astype(np.float32), non_zero_previous.astype(np.float32), method)

    result = diff / (len(roi_imgs)-1)
    return result



# frm_dir = '/Users/simon/Desktop/envs/troubleshooting/Emergence/project_folder/videos/img_comparisons_4'
# data_path = '/Users/simon/Desktop/envs/troubleshooting/Emergence/project_folder/csv/outlier_corrected_movement_location/Example_1.csv'
# data = pd.read_csv(data_path, nrows=4, usecols=['Nose_x', 'Nose_y']).fillna(-1).values.astype(np.int64)
# imgs, polygons = [], []
# for file_path in sorted(glob.glob(frm_dir + '/*.png')): imgs.append(cv2.imread(file_path))
# for frm_data in data: polygons.append(GeometryMixin().bodyparts_to_circle(frm_data, 100))
# geometry_histocomparison(imgs=imgs, shapes=polygons, method='correlation')
#
#
# import time
# start = time.time()
# similarity = geometry_histocomparison(imgs=imgs, shapes=polygons, method='chi_square_alternative')
# print(time.time() - start)
# print(similarity)



