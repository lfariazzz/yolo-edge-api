"""Gera comparativo visual BGR vs RGB para inspeção."""
import cv2
import numpy as np
from pathlib import Path

img_path = sorted(Path("dataset/exports/epi-v6/valid/images").glob("*.jpg"))[0]
frame    = cv2.imread(str(img_path))

rgb_display = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # correto

# frame já está em BGR --- é isso que cv2.imwrite espera, então sai correto
cv2.imwrite("preprocessing/outputs/e1_rgb_correto.jpg", frame)

# rgb_display está em ordem RGB --- escrever direto via imwrite (que assume BGR)
# faz os canais R e B aparecerem trocados na imagem final, simulando o erro visual
cv2.imwrite("preprocessing/outputs/e1_bgr_errado.jpg", rgb_display)

print("Imagens salvas em preprocessing/outputs/")
print("Do seu computador, rode:")
print("scp lfariazzz@100.103.254.101:~/Documents/yolo-edge-api/preprocessing/outputs/e1_*.jpg .")
