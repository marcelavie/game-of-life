import time
import pygame
import numpy

cor_background = (10, 10, 10)
cor_tabuleiro = (40, 40, 40)
cor_cel_morta = (68, 4, 142)
cor_cel_viva = (216, 162, 247)

pygame.init()
pygame.display.set_caption("joguinho da vida")


def update(tela, cells, progresso=False):
    tamanho = 10 
    updated_cells = numpy.zeros((cells.shape[0], cells.shape[1]))

    for row, col in numpy.ndindex(cells.shape):
        alive = numpy.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = cor_background if cells[row, col] == 0 else cor_cel_viva

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if progresso:
                    color = cor_cel_morta
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if progresso:
                    color = cor_cel_viva
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if progresso:
                    color = cor_cel_viva

        pygame.draw.rect(tela, color, (col * tamanho, row * tamanho, tamanho - 1, tamanho - 1))

    return updated_cells


def main():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))

    cells = numpy.zeros((60, 80))
    tela.fill(cor_tabuleiro)
    update(tela, cells)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for saida in pygame.event.get():
            if saida.type == pygame.QUIT:
                pygame.quit()
                return
            elif saida.type == pygame.KEYDOWN:
                if saida.key == pygame.K_SPACE:
                    running = not running
                    update(tela, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(tela, cells)
                pygame.display.update()

        tela.fill(cor_tabuleiro)

        if running:
            cells = update(tela, cells, progresso=True)
            pygame.display.update()

        time.sleep(0.1)


if __name__ == "__main__":
    main()