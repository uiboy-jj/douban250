#!/user/bin/env python3
#-*-coding:utf-8 -*-
from shutil import copyfile
import csv
import os
# 相对路径
if __name__ == '__main__':

 copyfile("movie.csv", "movie2.csv") #留一份原始数据做参照


if __name__ == '__main__':

 file_old = 'movie.csv'
 file_temp = 'movie_data.csv'

 with open(file_old, 'r', newline='', encoding='utf-8-sig') as f_old, \
         open(file_temp, 'w', newline='', encoding='utf-8-sig') as f_temp:
  f_csv_old = csv.reader(f_old)
  f_csv_temp = csv.writer(f_temp)
  for i, rows in enumerate(f_csv_old):  # 保留header
   if i == 0:
    f_csv_temp.writerow(rows)
    break
  for rows in f_csv_old:
   if rows[0] != 'comments_num':  # 删除第一列值为comments_num的行
    f_csv_temp.writerow(rows)

 os.remove(file_old)
 os.rename(file_temp, file_old)


#剩下还有一些分列操作 用excel工具



