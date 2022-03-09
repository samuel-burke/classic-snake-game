#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################

from time import sleep
from turtle import Screen
import pygame

from board import *
from food import Food
from lossmessage import LossMessage
from scoreboard import ScoreBoard
from snake import Snake, CrashedIntoTail


def format_screen(s):
    s.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    s.bgcolor('gray8')
    s.title('Snake Game 🐍')
    s.tracer(0)


def crashed_into_wall(snake):
    head_x, head_y = snake.head.position()
    heading = snake.head.heading()

    # check if snake crashed into right wall
    if heading == 0:
        return head_x + TURTLE_SIZE / 2 + STEP > RIGHT_WALL
    # check if snake crashed into top wall
    elif heading == 90:
        return head_y + TURTLE_SIZE / 2 + STEP > TOP_WALL
    # check if snake crashed into left wall
    elif heading == 180:
        return head_x - TURTLE_SIZE / 2 - STEP < LEFT_WALL
    # check if snake crashed into bottom wall
    else:
        return head_y - TURTLE_SIZE / 2 - STEP < BOTTOM_WALL


def play_game():
    pygame.mixer.init()
    eat = pygame.mixer.Sound("resources/audio/eat.wav")
    collect_10 = pygame.mixer.Sound("resources/audio/collect-10.wav")
    pygame.mixer.music.load("resources/audio/background-music.wav")
    pygame.mixer.music.play(-1)
    screen = Screen()
    screen.clear()
    format_screen(screen)
    draw_border()

    snake = Snake(screen)
    food = Food()
    score_display = ScoreBoard()
    screen.listen()

    t = 0

    while True:
        screen.onkey(None, 'space')
        screen.onkey(snake.up, 'Up')
        screen.onkey(snake.down, 'Down')
        screen.onkey(snake.left, 'Left')
        screen.onkey(snake.right, 'Right')

        if t == 0:
            screen.update()
            sleep(1)
            t += 1
            pygame.mixer.Sound.play(pygame.mixer.Sound("resources/audio/game-start.wav"))

        if crashed_into_wall(snake):
            snake.kill()
            break

        try:
            snake.move()
            if snake.head.distance(food) <= 10:
                pygame.mixer.Sound.play(eat)
                snake.grow()
                food.move()
                score_display.add_to_score(1)
                score_display.update_score()
                if score_display.points % 10 == 0:
                    pygame.mixer.Sound.play(collect_10)

        except CrashedIntoTail:
            break

        screen.update()
        sleep(0.05)

    food.hideturtle()
    if score_display.points > score_display.high_score:
        pygame.mixer.music.load("resources/audio/new-record.mp3")
        pygame.mixer.music.play()
        LossMessage().display(f"Score: {score_display.points} New Record!")
    else: 
        pygame.mixer.music.load("resources/audio/game-over.mp3")
        pygame.mixer.music.play()
        LossMessage().display("Press Space to play again!")
    screen.update()
    screen.onkey(play_game, 'space')
    score_display.update_high_score()
    screen.exitonclick()


def main():
    play_game()


if __name__ == "__main__":
    main()
