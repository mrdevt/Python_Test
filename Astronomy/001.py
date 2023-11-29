from astropy.io import fits
file = fits.open('D:\Python\Astronomy\SN2023vyl_B_20231104124628_150s_0061.fits')
print(type(file))
# 输出fits文件信息
print (file.info())
# 输出fits头部信息
print (file[0].header)
# 输出SIMPLE值
print (file[0].header['SIMPLE'])
# 输出BITPIX值
print (file[0].header['BITPIX'])
# 输出BITPIX的注释信息
print (file[0].header.comments['BITPIX'])
# 获取数据 file[0].data
# print (file[0].data[])