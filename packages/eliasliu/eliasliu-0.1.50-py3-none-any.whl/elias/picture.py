# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:21:49 2024

@author: Isabel.Xu
"""

from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np


def new_pic_name(pic_origin):
    from elias import usual as u
    
    pic_name = u.file_get(path=pic_origin)
    pic_name_new = "repaired_"+pic_name
    
    import os 
    pic_dir = os.path.dirname(pic_origin)
    pic_target = os.path.join(pic_dir,pic_name_new)
    return pic_target

def adjust_temperature(image, temp):
    """
    调整图片的色温。
    :param image: OpenCV图像对象
    :param temp: 色温调整量，负值为冷色调，正值为暖色调
    """
    # 根据图像大小创建一个全1的数组
    warmer = np.ones(image.shape, dtype=np.uint8) * abs(int(temp * 255 / 100))
    # 根据色温是增加还是减少来调整蓝色或红色通道
    if temp < 0:
        image[:, :, 0] = cv2.add(image[:, :, 0], warmer[:, :, 0])
    else:
        image[:, :, 2] = cv2.add(image[:, :, 2], warmer[:, :, 2])
    return image

def enhance_highlights_shadows(image, alpha_highlights, beta_shadows):
    """
    增强图片中的高光和阴影。
    :param image: OpenCV图像对象
    :param alpha_highlights: 高光增强系数
    :param beta_shadows: 阴影增强系数
    """
    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 创建高光区域的掩膜
    mask = cv2.inRange(hsv, (0, 0, 255*0.8), (180, 255, 255))
    inv_mask = cv2.bitwise_not(mask)
    # 调整高光区域
    image_highlights = cv2.addWeighted(image, alpha_highlights, image, 0, 0)
    image = np.where(mask[:,:,None] == 255, image_highlights, image)
    # 调整阴影区域
    image_shadows = cv2.addWeighted(image, beta_shadows, image, 0, 0)
    image = np.where(inv_mask[:,:,None] == 255, image_shadows, image)
    return image

# def adjust_image(image_path, output_path):
#     """
#     调整图片的亮度、对比度、饱和度、高光、色温、阴影和锐化。
#     :param image_path: 输入图片的路径
#     :param output_path: 输出图片的路径
#     """
#     # 使用Pillow打开图片
#     img = Image.open(image_path)

#     # 调整亮度（增加15%）
#     img = ImageEnhance.Brightness(img).enhance(1.10)
#     # 调整对比度（增加10%）
#     img = ImageEnhance.Contrast(img).enhance(1.10)
#     # 调整饱和度（增加25%）
#     img = ImageEnhance.Color(img).enhance(1.25)
#     # 调整锐化（增加76%）
#     img = ImageEnhance.Sharpness(img).enhance(1.76)

#     # 将Pillow图像转换为OpenCV格式
#     img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

#     # 调整高光（增强系数1.2）和阴影（增强系数1.2）
#     # img_cv = enhance_highlights_shadows(img_cv, 1.2, 1.2)

#     # 调整色温（降低10单位）
#     img_cv = adjust_temperature(img_cv, -5)

#     # 将OpenCV图像转换回Pillow格式
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))

#     # 保存调整后的图片
#     img_pil.save(output_path)


# def ins_adjust_image(image_path, output_path):
#     # 使用Pillow打开图片
#     img = Image.open(image_path)

#     # 调整亮度（增加10%）
#     img = ImageEnhance.Brightness(img).enhance(1.10)
#     # 调整对比度（增加30%）
#     img = ImageEnhance.Contrast(img).enhance(1.20)
#     # 调整饱和度（增加20%）
#     img = ImageEnhance.Color(img).enhance(1.20)
#     # 调整锐化（增加50%）
#     img = ImageEnhance.Sharpness(img).enhance(1.50)

#     # 将Pillow图像转换为OpenCV格式
#     img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

#     # 调整高光（增强系数1.15）和阴影（增强系数1.15）
#     # img_cv = enhance_highlights_shadows(img_cv, 1.15, 1.15)

#     # 调整色温（降低5单位）
#     img_cv = adjust_temperature(img_cv, -5)

#     # 将OpenCV图像转换回Pillow格式
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))

#     # 保存调整后的图片
#     img_pil.save(output_path)


def adjust_image_parameters(image_path, output_path, brightness=1, contrast=1, color=1, sharpness=1, alpha_highlights=1, beta_shadows=1, temperature=0):
    """
    调整图片的各项参数。
    :param image_path: 输入图片的路径。
    :param output_path: 输出图片的路径。
    :param brightness: 亮度调整比例。
    :param contrast: 对比度调整比例。
    :param color: 饱和度调整比例。
    :param sharpness: 锐化调整比例。
    :param alpha_highlights: 高光增强系数。
    :param beta_shadows: 阴影增强系数。
    :param temperature: 色温调整值。
    """
    # 使用Pillow打开图片并调整
    img = Image.open(image_path)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Color(img).enhance(color)
    img = ImageEnhance.Sharpness(img).enhance(sharpness)

    # 将Pillow图像转换为OpenCV格式
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # 调整高光和阴影
    img_cv = enhance_highlights_shadows(img_cv, alpha_highlights, beta_shadows)

    # 调整色温
    img_cv = adjust_temperature(img_cv, temperature)

    # 将OpenCV图像转换回Pillow格式
    img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))

    # 保存调整后的图片
    img_pil.save(output_path)

def apply_ins_style(image_path, output_path):
    """
    将图片调整为INS风格。
    :param image_path: 输入图片的路径。
    :param output_path: 输出图片的路径。
    """
    adjust_image_parameters(image_path, output_path, 
                            brightness=1.10,  # 亮度调整比例
                            contrast=1.20,  # 对比度调整比例
                            color=1.20,  # 饱和度调整比例
                            sharpness=1.50,  # 锐化调整比例
                            # alpha_highlights=1.15,  # 高光增强系数
                            # beta_shadows=1.15,  # 阴影增强系数
                            temperature=-5 # 色温调整值
                            )


def adjust_image(image_path,output_path,style = "ins"):
    if output_path == None:
        output_path = new_pic_name(image_path)
    else:
        pass
    
    if style == "ins":
        apply_ins_style(image_path,output_path)
    else:
        pass
    
    


