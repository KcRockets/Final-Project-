import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Shooter")

clock = pygame.time.Clock()

BUBBLE_RADIUS = 16
SHOOT_SPEED = 6

shooter_x = WIDTH // 2
shooter_y = HEIGHT - 40

angle = 0
current_bubble = None
fired_bubbles = []
grid = []

colors = [
    (255, 0, 0),
    (255, 255, 0),
    (0, 0, 255),
    (0, 255, 0),
    (128, 0, 128),
    (255, 165, 0)
]


class Bubble:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.radius = BUBBLE_RADIUS
        self.color = color if color else random.choice(colors)
        self.vx = 0
        self.vy = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.vx *= -1

        if self.y < self.radius:
            snap_to_grid(self)
            pop_matching(self) 
            reload_bubble()

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


def create_new_bubble():
    return Bubble(shooter_x, shooter_y)


def snap_to_grid(bubble):
    spacing = BUBBLE_RADIUS * 2
    bubble.x = round((bubble.x - BUBBLE_RADIUS) / spacing) * spacing + BUBBLE_RADIUS
    bubble.y = round((bubble.y - BUBBLE_RADIUS) / spacing) * spacing + BUBBLE_RADIUS
    grid.append(bubble)


def pop_matching(start_bubble):
    visited = []
    stack = [start_bubble]
    cluster = []

    while stack:
        b = stack.pop()
        if b in visited:
            continue
        visited.append(b)

        if b.color == start_bubble.color:
            cluster.append(b)

            for other in grid:
                if other not in visited and check_collision(b, other):
                    stack.append(other)

    if len(cluster) >= 3:
        for b in cluster:
            if b in grid:
                grid.remove(b)


def check_collision(b1, b2):
    dx = b1.x - b2.x
    dy = b1.y - b2.y
    dist = math.sqrt(dx * dx + dy * dy)
    return dist <= b1.radius + b2.radius + 1


def reload_bubble():
    global current_bubble
    current_bubble = create_new_bubble()


def create_starting_rows(rows=5):
    spacing = BUBBLE_RADIUS * 2
    for row in range(rows):
        for col in range(WIDTH // spacing):
            x = col * spacing + BUBBLE_RADIUS
            y = row * spacing + BUBBLE_RADIUS
            grid.append(Bubble(x, y))


current_bubble = create_new_bubble()
create_starting_rows()

running = True
while running:
    screen.fill((30, 30, 30))

    mx, my = pygame.mouse.get_pos()
    angle = math.atan2(my - shooter_y, mx - shooter_x)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_bubble:
                current_bubble.vx = math.cos(angle) * SHOOT_SPEED
                current_bubble.vy = math.sin(angle) * SHOOT_SPEED
                fired_bubbles.append(current_bubble)
                current_bubble = None

    for b in fired_bubbles[:]:
        b.move()

        for g in grid:
            if check_collision(b, g):
                snap_to_grid(b)
                pop_matching(b)
                
                fired_bubbles.remove(b)
                reload_bubble()
                break

    for b in grid:
        b.draw()

    for b in fired_bubbles:
        b.draw()

    if current_bubble:
        current_bubble.draw()

    end_x = shooter_x + math.cos(angle) * 40
    end_y = shooter_y + math.sin(angle) * 40
    pygame.draw.line(screen, (255, 255, 255), (shooter_x, shooter_y), (end_x, end_y), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()