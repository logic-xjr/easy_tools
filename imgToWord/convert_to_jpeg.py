from PIL import Image
from io import BytesIO

def convert_to_jpeg(image_stream):
    """
    将图片流转换为JPEG格式并返回JPEG文件流。
    
    参数:
    - image_stream: 包含图片数据的BytesIO对象或文件流。
    
    返回:
    - 一个BytesIO对象，其中包含JPEG格式的图片数据。
    """
    # 将文件流转换为BytesIO对象（如果它还不是BytesIO对象）
    if not isinstance(image_stream, BytesIO):
        raise ValueError("The image_stream must be a BytesIO object or file stream.")

    # 重置文件流指针到开始位置
    image_stream.seek(0)

    # 使用Pillow打开图片
    with Image.open(image_stream) as img:
      # 检查图片的原始格式
      if img.format in ('JPEG', 'JPG', 'PNG'):
          # 图片已经是JPEG/JPG/PNG格式，直接返回原文件流
          image_stream.seek(0)
          return image_stream
      else:
          # 将图片转换为RGB模式以保存为JPEG
          img = img.convert('RGB')
          
          # 创建一个新的BytesIO对象来保存JPEG数据
          jpeg_stream = BytesIO()
          
          # 保存图片为JPEG格式到新的BytesIO对象
          img.save(jpeg_stream, format='JPEG')
          
          # 重置BytesIO对象的指针到开始位置
          jpeg_stream.seek(0)
          
          return jpeg_stream