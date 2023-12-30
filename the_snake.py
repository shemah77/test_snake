from random import choice, randint


import pygame

# Инициализация PyGame
pygame.init()

# Константы для размеров
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета фона - черный
BOARD_BACKGROUND_COLOR: tuple[int, int, int] = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки
SPEED = 3

# Настройка игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля
pygame.display.set_caption('Змейка')

# Настройка времени
clock = pygame.time.Clock()



# Тут опишите все классы игры
class GameObject:
    """Базовый класс длы игровых объектов"""

    def __init__(self, bd_color=None):
        self.body_color = bd_color
        self.position = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2)

    def draw(self):
        pass


class Snake(GameObject):
    ''' Подкласс змейка '''

    def __init__(self, body_color=SNAKE_COLOR):
        super().__init__()
        self.length = 2
        self.positions = [(560,20),(540,20),(520,20), (500,20),(480,20),(460,20),(440,20),(420,20),(400,20), (380,20), (360,20), (340,20), (320,20),(300,20), (280,20), (260,20), (240,20), (220,20), (200,20), (180, 20), (160, 20),(140,20),(120,20),(100,20),(80,20),(60,20),(40,20),(20,20)]
        self.direction = RIGHT
        self.next_direction = None
        self.color = body_color
        self.last = None

    # Метод get_head_position в Snake
    def get_head_position(self):
        '''Метод возвращает позицию головы змейки
        (первый элемент в списке positions) '''

        head_position = self.positions[0]
        return head_position




    # Метод move класса Snake
    def move(self):
        a=1
        b=2
        head = self.get_head_position()
        self.last = self.positions[-1]
        new_head = (
                (head[0] + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH,
                (head[1] + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT
            )
        if new_head  in self.positions[2:]:
              self.reset()
        else:
             self.positions.insert(0, new_head)
             self.positions.pop()






    # Метод draw класса Snake
    def draw(self, surface):
        for position in self.positions[:-1]:
            rect = (
                pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            )
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, (93, 216, 228), rect, 1)

                # Отрисовка головы змейки
        head = self.positions[0]
        head_rect = pygame.Rect((head[0], head[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, head_rect)
        pygame.draw.rect(surface, (93, 216, 228), head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(
                (self.last[0], self.last[1]), (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)


    def reset(self):
        self.length = 1
        self.positions = [(320,240)]
        # self.direction = random(UP,DOWN,LEFT,RIGHT)
        screen.fill(BOARD_BACKGROUND_COLOR)








    # Метод обновления направления после нажатия на кнопку
    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None


class Apple(GameObject):
    '''Подкласс яблоко '''

    # color = APPLE_COLOR

    def __init__(self, body_color=APPLE_COLOR):
        super().__init__()
        self.body_color = body_color
        self.position = self.randomize_position()

    def randomize_position(self):
        self.position = (randint(0, GRID_WIDTH - 2),
                         randint(0, GRID_HEIGHT - 2))
        return self.position

    # Метод draw класса Apple
    def draw(self, surface):
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, (93, 216, 228), rect, 1)


# Функция обработки действий пользователя
import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print ("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp


@timer
def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                print (f"UP: {game_object.direction}")

                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                print(f"DOWN: {game_object.direction}")
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                print(f"LEFT: {game_object.direction}")
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                print(f"RIGHT: {game_object.direction}")
                game_object.next_direction = RIGHT


def main():



    # Тут нужно создать экземпляры классов
    apple = Apple()
    snake = Snake()

    print(apple.__dict__)
    print(snake.__dict__)

    running = True

    # Описание главного цикла игры.
    # Этот цикл работает до тех пор, пока пользователь не закроет окно.
    while running:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False

        clock.tick(SPEED)

        handle_keys(snake)
        apple.draw(screen)

        snake.update_direction()

        snake.move()
        snake.draw(screen)

        print(snake.__dict__)

        pygame.display.update()





if __name__ == '__main__':
    main()

# Метод draw класса Apple
# def draw(self, surface):
#     rect = pygame.Rect(
#         (self.position[0], self.position[1]),
#         (GRID_SIZE, GRID_SIZE)
#     )
#     pygame.draw.rect(surface, self.body_color, rect)
#     pygame.draw.rect(surface, (93, 216, 228), rect, 1)

# # Метод draw класса Snake
# def draw(self, surface):
#     for position in self.positions[:-1]:
#         rect = (
#             pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
#         )
#         pygame.draw.rect(surface, self.body_color, rect)
#         pygame.draw.rect(surface, (93, 216, 228), rect, 1)

#     # Отрисовка головы змейки
#     head = self.positions[0]
#     head_rect = pygame.Rect((head[0], head[1]), (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(surface, self.body_color, head_rect)
#     pygame.draw.rect(surface, (93, 216, 228), head_rect, 1)

#     # Затирание последнего сегмента
#     if self.last:
#         last_rect = pygame.Rect(
#             (self.last[0], self.last[1]),
#             (GRID_SIZE, GRID_SIZE)
#         )
#         pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

# Функция обработки действий пользователя
# def handle_keys(game_object):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and game_object.direction != DOWN:
#                 game_object.next_direction = UP
#             elif event.key == pygame.K_DOWN and game_object.direction != UP:
#                 game_object.next_direction = DOWN
#             elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
#                 game_object.next_direction = LEFT
#             elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
#                 game_object.next_direction = RIGHT

# Метод обновления направления после нажатия на кнопку
# def update_direction(self):
#     if self.next_direction:
#         self.direction = self.next_direction
#         self.next_direction = None
