# Gera os recortes reais da capa. Uso (na raiz do projeto): python3 -I tools/gerar_recortes.py
import numpy as np
from PIL import Image, ImageFilter
im = Image.open('assets/cover.jpg').convert('RGB')
W = im.size[0]
im.resize((640, 640), Image.LANCZOS).save('assets/cover-640.jpg', quality=90)
im.resize((256, 256), Image.LANCZOS).save('assets/cover-256.jpg', quality=88)
im.resize((512, 512), Image.LANCZOS).save('assets/cover-512.jpg', quality=90)
# faixa de rocha do chão da capa (divisória)
im.crop((0, 1352, 1400, 1400)).resize((1400, 48)).save('assets/rocha.jpg', quality=88)
# máscara do nome (letras pretas sobre o céu): x 880–1360, y 70–235 da capa de 1400 px
x0, y0, x1, y1 = 880, 70, 1360, 235
box = im.crop((x0, y0, x1, y1))
l = np.asarray(box.convert('L')).astype(float)
bg = 219.0   # luminância do céu (#D3DEEE)
alpha = np.clip((bg - l - 22) / (bg - 70 - 22), 0, 1)
alpha[alpha < 0.12] = 0
out = np.zeros((y1 - y0, x1 - x0, 4), np.uint8); out[..., 3] = (alpha * 255).astype(np.uint8)
Image.fromarray(out, 'RGBA').resize((960, 330), Image.LANCZOS).save('assets/nome-mask.webp', quality=92, lossless=False)
