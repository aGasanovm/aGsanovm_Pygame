import pygame
import random
pygame.init()
clock = pygame.time.Clock()
back = (255,219,139)
mw = pygame.display.set_mode((600, 550))
mw.fill(back)

WHITE = (255,255, 255)
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def set_text(self, text, fsize=12, text_color=WHITE):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
cart1 = TextArea(0, 100, 600, 100, (222,211,211))
cart1.set_text('Вопрос', 24)

cart2 = TextArea(0, 250, 600, 100, (222,211,211))
cart2.set_text('Ответ', 24)
cart1.draw(10, 10)
cart2.draw(10, 10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = random.randint(1, 3)
                if num == 1:
                    cart1.set_text('Почему у зебр всегда грустные лица?', 24)
                if num == 2:
                    cart1.set_text(' В чём заключается секрет долголетия и здоровья?', 24)
                if num == 3:
                    cart1.set_text('Зачем кошке интернет?', 24)
                cart1.draw(10, 10)
            if event.key == pygame.K_a:
                num = random.randint(1, 3)
                if num == 1:
                    cart2.set_text('Потому что они знают, что все будут пытаться их разделить!', 24)
                if num == 2:
                    cart2.set_text('В ежедневном употреблениитрёх литров молока и килограмма печенья!',24)
                if num == 3:
                    cart2.set_text('Чтобы ловить виртуальных мышей и играть в игры!', 24)
                cart2.draw(10, 10)

    pygame.display.update()
    clock.tick(120)
