#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/31
# @Name    : create_topology.py.py
# @email   : winter741258@126.com
# @Author  : Winter.Yu

from shapely.geometry import Point, LineString
import numpy as np
import cv2
import itertools
from functools import wraps, partial
from math_tools import lcm
from scipy.optimize import linear_sum_assignment
import warnings
from shapely.errors import ShapelyDeprecationWarning
import matplotlib.pyplot as plt


def showImage(image, method = 'plt',title=''):
    if method == 'plt':
        plt.title(title) 
        try:
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.show()
        except cv2.error:
            plt.imshow(image)
            plt.show()

    else:
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class topology_match():
    
    def __init__(self, img_path, lines=[], points=[], show=False):
        self.raw_lines = lines
        self.raw_points = points
        self.lines = [LineString(line) for line in lines] if lines else []
        self.points = [Point((xmin + xmax)//2, (ymin + ymax)//2)
                       for xmin, ymin, xmax, ymax in points] if points else []
        self.line_num = len(lines)
        self.point_num = len(points)
        self.img_path = img_path
       

    @property
    def get_line_num(self):
        return self.line_num

    @property
    def get_point_num(self):
        return self.point_num
    

    def hungarian_match_with_cost(self, distance_threshold=60, show=False):
        if all([self.lines, self.points]):
            least = lcm(self.line_num, self.point_num)
            lines_object = list(itertools.repeat(self.lines, least // self.line_num))
            points_object = list(itertools.repeat(self.points, least // self.point_num))
            # lines_ = np.array(lines_, dtype=object).flatten()
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)
                lines_ = np.empty((len(lines_object), self.line_num), dtype=object)
                lines_[:] = lines_object
                lines_ = lines_.flatten()
            # points_ = np.array(points_, dtype=object).flatten()
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)
                points_ = np.empty((len(points_object), self.point_num), dtype=object)
                points_[:] = points_object
                points_ = points_.flatten()
            cost = np.array([p.distance(l) for p in points_ for l in lines_]).reshape(least, least)
            row_ind, col_ind = linear_sum_assignment(cost)
            col_ind_res = [i % self.line_num for i in col_ind]
            row_ind_res = [j % self.point_num for j in row_ind]
            # print(col_ind_res, row_ind_res, sep='\n')
            match_res = set(zip(row_ind_res, col_ind_res))
            # post processing
            match_map = {}
            for i, j in match_res:
                if match_map.get(i, None):
                    match_map[i] += [j]
                else:
                    match_map[i] = [j]
            # print(match_map)
            # filter distance with respect to cost matrix
            for k, v in match_map.items():
                for i, col in enumerate(v):
                    if cost[k, col] > distance_threshold:
                        v[i] += float("inf")
            match_map = {k: list(filter(lambda x: x != float("inf"), v)) for k, v in match_map.items()}
            if show:
                colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 200, 255),
                    (80, 127, 255), (255, 0, 255), (255, 255, 0), (96, 164, 244)]
                image = cv2.imread(self.img_path)
            # draw bbox
                for i, (xmin, ymin, xmax, ymax) in enumerate(self.raw_points):
                    cv2.rectangle(image, (xmin, ymin), (xmax, ymax),
                                colors[i % len(colors)])
                    cv2.putText(image, str(i), ((xmin + xmax)//2 + 20, (ymin + ymax)//2 + 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[i % len(colors)], 2)
                    # draw line
                    for j in match_map[i]:
                        cv2.line(image, self.raw_lines[j][0], self.raw_lines[j][1],
                                color=colors[i % len(colors)], thickness=2)
                        cv2.putText(image, str(j), ((self.raw_lines[j][0][0] + self.raw_lines[j][1][0])//2, (self.raw_lines[j][0][1] + self.raw_lines[j][1][1])//2),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[i % len(colors)], 2)
                
                # show image
                # cv2.imshow('match_image', image)
                showImage(image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            return match_map
        else:
            raise Exception('Please lines or points are empty!')

   
if __name__ == '__main__':
    
    xmin, ymin, xmax, ymax = [97, 348, 533, 620], [131, 133, 180, 50], [197, 451, 581, 660], [186, 209, 281, 120]
    test_points = list(zip(xmin, ymin, xmax, ymax))
    test_lines = [((638, 2), (638, 47)),((455, 159), (638, 159)), ((638, 124), (638, 159)), ((639, 159), (713, 159)), ((3, 159), (93, 159)),
                  ((201, 159), (344, 159)), ((557, 161), (557, 176))]
    tm = topology_match(img_path='./img/test2.png', lines=test_lines, points=test_points)
    print("the number of lines: " ,tm.get_line_num)
    print("the number of points: ", tm.get_point_num)
    match_map = tm.hungarian_match_with_cost(distance_threshold=60, show=False)
    print(match_map)