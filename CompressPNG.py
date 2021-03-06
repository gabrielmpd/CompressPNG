import os
from PIL import Image

#funçao para converter imagens png para jpg
# image1 = Image.open("C:\Users\Gabriel\Documents\GitHub\CompressPNG\wow.png)
# rgb = image1.convert('RGB')
# rgb.save('wow1.jpg)

#funçao para verificar se os arquivos do diretório sao imagens
def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    return False

def reduzir_tamanho_imagens(input_dir, output_dir, ext='.png'):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        redimensionada = imagem.resize((1280, 720))
        nome_sem_ext = os.path.splitext(nome)[0]
        redimensionada.save(os.path.join(output_dir, nome_sem_ext + ext))

if __name__ == "__main__":
    diretorio = '/Users/Gabriel/Documents/GitHub/CompressPNG'

    reduzir_tamanho_imagens(diretorio, 'output')

#Link do github: https://github.com/gabrielmpd/CompressPNG
#link para os videos: https://posinatel-my.sharepoint.com/:f:/g/personal/gabrielmoreira_gec_inatel_br/EkrJswmnt-dKvBNGs33OybsBrWSSTucUbb_pV6HgOunTsQ?e=YUxUUb