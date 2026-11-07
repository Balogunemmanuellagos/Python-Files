"""Starfall: collect stardust and dodge the falling meteors."""

import math
import random

import pygame


WIDTH = 900
HEIGHT = 600
FPS = 60

BACKGROUND = (8, 12, 32)
WHITE = (240, 246, 255)
CYAN = (69, 224, 255)
GOLD = (255, 207, 79)
PINK = (255, 91, 135)


def draw_text(surface, font, text, color, center):
    image = font.render(text, True, color)
    surface.blit(image, image.get_rect(center=center))


def make_background_stars():
    return [
        (random.randrange(WIDTH), random.randrange(HEIGHT), random.choice((1, 1, 2, 3)))
        for _ in range(100)
    ]


def draw_background(surface, stars, elapsed):
    surface.fill(BACKGROUND)
    for index, (x, y, size) in enumerate(stars):
        brightness = 120 + int(100 * (0.5 + 0.5 * math.sin(elapsed * 2 + index)))
        color = (brightness // 2, brightness // 2, brightness)
        pygame.draw.circle(surface, color, (x, y), size)


def draw_ship(surface, rect, elapsed, invulnerable):
    if invulnerable and int(elapsed * 14) % 2 == 0:
        return

    center_x = rect.centerx
    top = rect.top
    flame_height = 10 + int(5 * (0.5 + 0.5 * math.sin(elapsed * 18)))
    pygame.draw.polygon(
        surface,
        GOLD,
        [(center_x - 8, rect.bottom - 3), (center_x, rect.bottom + flame_height),
         (center_x + 8, rect.bottom - 3)],
    )
    pygame.draw.polygon(
        surface,
        CYAN,
        [(center_x, top), (rect.right, rect.bottom - 3),
         (center_x, rect.bottom - 10), (rect.left, rect.bottom - 3)],
    )
    pygame.draw.polygon(
        surface,
        (30, 94, 160),
        [(center_x, top + 13), (center_x + 12, rect.bottom - 9),
         (center_x, rect.bottom - 14), (center_x - 12, rect.bottom - 9)],
    )
    pygame.draw.ellipse(
        surface, WHITE, (center_x - 5, top + 12, 10, 15)
    )


def draw_meteor(surface, meteor):
    x, y, radius = int(meteor["x"]), int(meteor["y"]), meteor["radius"]
    pygame.draw.circle(surface, (91, 43, 76), (x, y), radius + 5)
    pygame.draw.circle(surface, (194, 80, 85), (x, y), radius)
    pygame.draw.circle(
        surface, (235, 125, 99), (x - radius // 3, y - radius // 4),
        max(3, radius // 4),
    )
    pygame.draw.circle(
        surface, (123, 53, 74), (x + radius // 3, y + radius // 3),
        max(3, radius // 5),
    )


def star_points(center, outer_radius, inner_radius, rotation=0):
    points = []
    for point in range(10):
        angle = rotation + point * math.pi / 5 - math.pi / 2
        radius = outer_radius if point % 2 == 0 else inner_radius
        points.append(
            (center[0] + math.cos(angle) * radius,
             center[1] + math.sin(angle) * radius)
        )
    return points


def draw_collectible(surface, collectible, elapsed):
    center = (int(collectible["x"]), int(collectible["y"]))
    pulse = 2 * math.sin(elapsed * 6 + collectible["phase"])
    pygame.draw.circle(surface, (77, 74, 47), center, int(17 + pulse))
    pygame.draw.polygon(
        surface, GOLD, star_points(center, 13 + pulse, 6 + pulse / 2, elapsed * 1.5)
    )
    pygame.draw.polygon(
        surface, WHITE, star_points(center, 6, 3, elapsed * 1.5)
    )


def new_game():
    return {
        "player": pygame.Rect(WIDTH // 2 - 20, HEIGHT - 85, 40, 48),
        "meteors": [],
        "collectibles": [],
        "meteor_timer": 0.5,
        "collectible_timer": 1.2,
        "elapsed": 0.0,
        "score": 0,
        "lives": 3,
        "invulnerable": 0.0,
    }


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("STARFALL  |  A tiny space adventure")
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 76)
    large_font = pygame.font.Font(None, 48)
    medium_font = pygame.font.Font(None, 32)
    small_font = pygame.font.Font(None, 24)

    stars = make_background_stars()
    state = "title"
    game = new_game()
    high_score = 0
    running = True
    total_time = 0.0

    while running:
        dt = min(clock.tick(FPS) / 1000, 0.05)
        total_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif state == "title" and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    game = new_game()
                    state = "playing"
                elif state == "game_over" and event.key in (pygame.K_r, pygame.K_SPACE):
                    game = new_game()
                    state = "playing"

        if state == "playing":
            game["elapsed"] += dt
            game["invulnerable"] = max(0, game["invulnerable"] - dt)
            player = game["player"]
            keys = pygame.key.get_pressed()
            horizontal = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(
                keys[pygame.K_LEFT] or keys[pygame.K_a]
            )
            vertical = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(
                keys[pygame.K_UP] or keys[pygame.K_w]
            )
            player.x += int(horizontal * 390 * dt)
            player.y += int(vertical * 330 * dt)
            player.clamp_ip(pygame.Rect(12, 80, WIDTH - 24, HEIGHT - 95))

            game["meteor_timer"] -= dt
            if game["meteor_timer"] <= 0:
                radius = random.randint(15, 29)
                game["meteors"].append({
                    "x": random.randint(radius, WIDTH - radius),
                    "y": -radius,
                    "radius": radius,
                    "speed": random.randint(175, 245) + game["elapsed"] * 2.2,
                    "drift": random.uniform(-55, 55),
                })
                game["meteor_timer"] = max(0.25, 0.8 - game["elapsed"] * 0.006)

            game["collectible_timer"] -= dt
            if game["collectible_timer"] <= 0:
                game["collectibles"].append({
                    "x": random.randint(22, WIDTH - 22),
                    "y": -20,
                    "speed": random.randint(130, 185),
                    "phase": random.random() * math.tau,
                })
                game["collectible_timer"] = random.uniform(1.7, 2.7)

            for meteor in game["meteors"]:
                meteor["x"] += meteor["drift"] * dt
                meteor["y"] += meteor["speed"] * dt

            for collectible in game["collectibles"]:
                collectible["y"] += collectible["speed"] * dt

            game["meteors"] = [
                meteor for meteor in game["meteors"]
                if meteor["y"] < HEIGHT + meteor["radius"]
            ]
            game["collectibles"] = [
                item for item in game["collectibles"] if item["y"] < HEIGHT + 20
            ]

            for item in game["collectibles"][:]:
                if math.hypot(player.centerx - item["x"], player.centery - item["y"]) < 30:
                    game["collectibles"].remove(item)
                    game["score"] += 10

            if game["invulnerable"] == 0:
                for meteor in game["meteors"][:]:
                    closest_x = max(player.left, min(meteor["x"], player.right))
                    closest_y = max(player.top, min(meteor["y"], player.bottom))
                    distance = math.hypot(meteor["x"] - closest_x, meteor["y"] - closest_y)
                    if distance < meteor["radius"]:
                        game["meteors"].remove(meteor)
                        game["lives"] -= 1
                        game["invulnerable"] = 1.2
                        if game["lives"] <= 0:
                            high_score = max(high_score, game["score"])
                            state = "game_over"
                        break

        draw_background(screen, stars, total_time)

        if state == "playing":
            for item in game["collectibles"]:
                draw_collectible(screen, item, total_time)
            for meteor in game["meteors"]:
                draw_meteor(screen, meteor)
            draw_ship(
                screen, game["player"], total_time, game["invulnerable"] > 0
            )

            pygame.draw.rect(screen, (15, 23, 49), (0, 0, WIDTH, 66))
            pygame.draw.line(screen, (42, 61, 99), (0, 65), (WIDTH, 65), 2)
            screen.blit(medium_font.render(f"DUST  {game['score']}", True, GOLD), (24, 20))
            screen.blit(medium_font.render(f"BEST  {max(high_score, game['score'])}", True, WHITE), (150, 20))
            for life in range(3):
                color = PINK if life < game["lives"] else (75, 58, 78)
                pygame.draw.circle(screen, color, (WIDTH - 38 - life * 30, 32), 9)
            draw_text(screen, small_font, "MOVE  WASD / ARROWS", (166, 192, 224), (WIDTH // 2, HEIGHT - 19))

        elif state == "title":
            draw_text(screen, title_font, "STARFALL", WHITE, (WIDTH // 2, 205))
            draw_text(screen, medium_font, "A tiny space adventure", CYAN, (WIDTH // 2, 258))
            draw_text(screen, small_font, "Collect golden stardust. Dodge the meteors.", (190, 207, 235), (WIDTH // 2, 322))
            draw_text(screen, large_font, "PRESS SPACE TO PLAY", GOLD, (WIDTH // 2, 405))
            draw_text(screen, small_font, "Move with WASD or the arrow keys     |     Esc to quit", (166, 192, 224), (WIDTH // 2, 465))

        else:
            draw_text(screen, title_font, "SHIP DOWN!", WHITE, (WIDTH // 2, 205))
            draw_text(screen, large_font, f"Stardust collected: {game['score']}", GOLD, (WIDTH // 2, 285))
            draw_text(screen, medium_font, f"Best this session: {high_score}", CYAN, (WIDTH // 2, 335))
            draw_text(screen, large_font, "PRESS R TO PLAY AGAIN", WHITE, (WIDTH // 2, 420))
            draw_text(screen, small_font, "Esc to quit", (166, 192, 224), (WIDTH // 2, 470))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
