import torch
import torchvision
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np

# 載入預訓練 DeepLabV3 模型
model = torchvision.models.segmentation.deeplabv3_resnet50(pretrained=True).eval()

# 載入影像
img = Image.open("images.jpeg").convert("RGB")
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
input_tensor = transform(img).unsqueeze(0)

# 推論
with torch.no_grad():
    output = model(input_tensor)["out"][0]
segmentation = output.argmax(0).byte().cpu().numpy()

# 建立顏色 map（隨機給顏色）
num_classes = segmentation.max() + 1
colors = np.random.randint(0, 255, size=(num_classes, 3), dtype=np.uint8)
color_seg = colors[segmentation]

# 顯示原圖 & segmentation
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img)

plt.subplot(1,2,2)
plt.title("Segmentation")
plt.imshow(color_seg)

plt.show()
