# SPACESHIPS - AULA 24 (Versão com Finn)
# Execute: python aula_24.py
import pygame

pygame.init()

# 1. CONFIGURAÇÕES
LARGURA, ALTURA = 800, 500
FPS = 60
COR_FUNDO = (10, 15, 35)
COR_NAVE = (80, 220, 255)
COR_TEXTO = (255, 255, 255)
COR_TIRO = (255, 230, 100)
VELOCIDADE_NAVE = 6

# PALETA DE CORES DO FINN
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
PELE = (255, 220, 175)
VERDE = (85, 170, 75)
AZUL_CLARO = (0, 175, 225)
AZUL_ESCURO = (0, 120, 195)

TAMANHO_PIXEL = 3
# O Finn possui 16x16 pixels
LARGURA_ALIEN, ALTURA_ALIEN = 16 * TAMANHO_PIXEL, 16 * TAMANHO_PIXEL
COLUNAS, LINHAS = 8, 3
ESPACO_X, ESPACO_Y = 15, 15

# 2. MATRIZES DE PIXEL ART DO FINN (16x16)
# Legenda: 0=Vazio, 1=Preto, 2=Branco (Touca), 3=Pele, 4=Verde (Alças), 5=Azul Claro (T-shirt), 6=Azul Escuro (Calções)

FINN_FRAME_1 = [
    "0011000000011000",
    "0122100000122100",
    "0122111111122100",
    "0122222222222100",
    "0121111111112100",
    "0121333333122100",
    "0121313313122100",
    "0121331133122100",
    "0121333333122100",
    "1411333333114100",
    "1415111111514100",
    "1415555555514100",
    "0115555555511000",
    "0016666666610000",
    "0016611116610000",
    "0011110011110000",
]

# Frame 2 com ligeira variação nos braços/calções para animação
FINN_FRAME_2 = [
    "0011000000011000",
    "0122100000122100",
    "0122111111122100",
    "0122222222222100",
    "0121111111112100",
    "0121333333122100",
    "0121313313122100",
    "0121331133122100",
    "0121333333122100",
    "1411333333114100",
    "1415111111514100",
    "1415555555514100",
    "0115555555511000",
    "0016666666610000",
    "0016611116610000",
    "0111100001111000",
]

# MAPA DE CORES
CORES_FINN = {
    "1": PRETO,
    "2": BRANCO,
    "3": PELE,
    "4": VERDE,
    "5": AZUL_CLARO,
    "6": AZUL_ESCURO
}

# 3. CONVERTER A MATRIZ EM UMA IMAGEM TRANSPARENTE
def gerar_sprite(desenho):
    imagem = pygame.Surface((LARGURA_ALIEN, ALTURA_ALIEN), pygame.SRCALPHA)
    for linha, texto in enumerate(desenho):
        for coluna, simbolo in enumerate(texto):
            if simbolo in CORES_FINN:
                cor_pixel = CORES_FINN[simbolo]
                pygame.draw.rect(imagem, cor_pixel, (
                    coluna * TAMANHO_PIXEL, linha * TAMANHO_PIXEL,
                    TAMANHO_PIXEL, TAMANHO_PIXEL
                ))
    return imagem

# 4. MONTAR A FORMAÇÃO
def criar_frota():
    largura_frota = COLUNAS * LARGURA_ALIEN + (COLUNAS - 1) * ESPACO_X
    x_inicial = (LARGURA - largura_frota) // 2
    inimigos = []
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            x = x_inicial + coluna * (LARGURA_ALIEN + ESPACO_X)
            y = 50 + linha * (ALTURA_ALIEN + ESPACO_Y)
            inimigos.append(pygame.Rect(x, y, LARGURA_ALIEN, ALTURA_ALIEN))
    return inimigos

# 5. PREPARAR A JANELA E OBJETOS
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("SPACESHIPS - Versão Finn")
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 30)

nave = pygame.Rect(380, 425, 40, 40)
tiros = []
inimigos = criar_frota()
sprites = [gerar_sprite(FINN_FRAME_1), gerar_sprite(FINN_FRAME_2)]

# 6. LOOP PRINCIPAL
rodando = True
while rodando:
    relogio.tick(FPS)
    agora = pygame.time.get_ticks()
    
    # EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                tiro = pygame.Rect(nave.centerx - 3, nave.top, 6, 16)
                tiros.append(tiro)

    # ATUALIZAR O JOGO
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        nave.x -= VELOCIDADE_NAVE
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        nave.x += VELOCIDADE_NAVE
    nave.x = max(0, min(nave.x, LARGURA - nave.width))
    
    for tiro in tiros[:]:
        tiro.y -= 9
        if tiro.bottom < 0:
            tiros.remove(tiro)

    # DESENHAR
    tela.fill(COR_FUNDO)
    pygame.draw.polygon(tela, COR_NAVE, [
        (nave.centerx, nave.top),
        (nave.left, nave.bottom),
        (nave.right, nave.bottom)
    ])
    
    animacao = (agora // 300) % 2
    for alien in inimigos:
        tela.blit(sprites[animacao], alien.topleft)
        
    for tiro in tiros:
        pygame.draw.rect(tela, COR_TIRO, tiro)
        
    mensagem = ""
    if nave.left == 0:
        mensagem = "Limite esquerdo!"
    elif nave.right == LARGURA:
        mensagem = "Limite direito!"
    if mensagem:
        texto = fonte.render(mensagem, True, COR_TEXTO)
        tela.blit(texto, (20, 465))
        
    pygame.display.flip()

pygame.quit()