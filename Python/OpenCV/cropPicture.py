from PIL import Image
import os
import sys
sys.path.append(os.getcwd())


class cropPictureFunction:
    def __init__(self, save_crop_picture_path, image_path_list, image_x, image_y,
                 crop_upper_proportion=1.80, crop_lower_proportion=1.62):

        self.save_crop_picture_path = save_crop_picture_path  # 儲存切格好的位置 str
        self.image_path_list = image_path_list  # 取得手機擷取圖片的全部絕對路徑位置 list
        self.image_x, self.image_y = image_x, image_y  # 取得 image 的x,y軸 int
        self.crop_upper_proportion = crop_upper_proportion  # 切格比例的上方 float
        self.crop_lower_proportion = crop_lower_proportion  # 切格比例的下方 float

        print('Image X軸：%s, Y軸: %s' % (self.image_x, self.image_y))
        print('切割圖片比例上方： %s, 下方: %s' % (self.crop_upper_proportion, self.crop_lower_proportion))
        print('切割圖片儲存位置:\n%s' % '\n'.join(self.image_path_list))
        print('切割圖片儲存位置: %s' % save_crop_picture_path)
        cropPictureFunction.cropPicture(self)

    def cropPicture(self):
        for image_path in self.image_path_list:
            img = Image.open(image_path)
            cropped = img.crop((0, self.image_y / self.crop_upper_proportion,
                                self.image_x, self.image_y / self.crop_lower_proportion))  # (left, upper, right, lower) 左、上、右、下
            cropped.save(self.save_crop_picture_path + os.path.basename(image_path))  # 儲存在你的指定位置，檔案名稱相同
            print('Mark: %s' % self.save_crop_picture_path + os.path.basename(image_path))

