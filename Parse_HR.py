#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by HanhNguyen
'''
Extract all **HR** information.
'''

from csv import DictReader, writer
import re


rem_chars = "<>"
rem_rgx = re.compile('[%s]' % rem_chars)


def numerize_hr(hr_str='* HR     101 >100  Generated at 00:23:29.'):
    if "**HR" in hr_str:
        hr_str = hr_str.replace("**HR", "*  HR")
    #print(hr_str.split())
    _,hr, n1, n2, *_ = hr_str.split()
    hr = hr.strip()
    n1, n2 = rem_rgx.sub('', n1), rem_rgx.sub('', n2)
    hr_uniq = int(n1)*1000+int(n2)
    hr_label = "{0}_{1} vs {0}_{2}".format(hr,n1,n2)
    return [hr_uniq,hr_label]


def csv_dict(csv_file='Sample.csv'):
    with open(csv_file, 'r') as csvf:
        reader = DictReader(csvf)
        for row in reader:
            hr_string = row['ALARM']
            hr_pin = row['PIN']
            hr_uniq,hr_label = numerize_hr(hr_str=hr_string)
            yield [hr_pin, hr_string, hr_uniq,hr_label]


if __name__=='__main__':
    hr_dict = csv_dict()
    with open("Sample-Result.csv", "w") as csv_file:
        csv_writer = writer(csv_file, delimiter=',')
        csv_writer.writerow(["PIN", "ALARM", "ENCODE", "HR LABEL"])
        for x, y, z, w in hr_dict:
            csv_writer.writerow([x, y, z, w])
            #print([hr_uniq, hr_label, n])