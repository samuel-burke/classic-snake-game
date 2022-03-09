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
from endmessage import EndMessage
from scoreboard import ScoreBoard
from snake import Snake, CrashedIntoTail


music = True


def format_screen(s):
    s.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    s.bgcolor(BG_COLOR)
    s.title('Snake Game 🐍')
    s.tracer(0)


def crashed_into_wall(snake):
    head_x, head_y = snake.head.position()
    heading = snake.head.heading()

    # check if snake crashed into right wall
    if heading == RIGHT:
        return head_x + BLOCK_SIZE/2 + STEP > RIGHT_WALL
    # check if snake crashed into top wall
    elif heading == UP:
        return head_y + BLOCK_SIZE/2 + STEP > TOP_WALL
    # check if snake crashed into left wall
    elif heading == LEFT:
        return head_x - BLOCK_SIZE/2 - STEP < LEFT_WALL
    # check if snake crashed into bottom wall
    else:
        return head_y - BLOCK_SIZE/2 - STEP < BOTTOM_WALL


def toggle_background_music():
    global music
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        music = False
    else:
        pygame.mixer.music.load("resources/audio/background-music.wav")
        pygame.mixer.music.play(-1)
        music = True


def main():
    def reset_score():
        def yes():
            score_display.reset_high_score()
            end_message.display("High score reset")
            score_display.update_score()
            screen.update()

        def no():
            end_message.display("Press Space to play again!")
            screen.update()

        end_message.display("Reset high score? y/n")
        screen.update()
        screen.onkey(yes, 'y')
        screen.onkey(no, 'n')

    pygame.mixer.init()
    eat = pygame.mixer.Sound("resources/audio/eat.wav")
    collect_10 = pygame.mixer.Sound("resources/audio/collect-10.wav")
    hit = pygame.mixer.Sound("resources/audio/hit.wav")
    pygame.mixer.music.load("resources/audio/background-music.wav")
    if music:
        pygame.mixer.music.play(-1)
    screen = Screen()
    screen.clear()
    format_screen(screen)
    draw_border()

    snake = Snake(screen)
    food = Food()
    score_display = ScoreBoard()
    end_message = EndMessage()
    screen.listen()
    screen.onkey(toggle_background_music, "m")

    first_iteration = True
    while True:
        screen.onkey(None, 'space')
        screen.onkey(None, "r")

        if first_iteration:
            screen.update()
            sleep(1)
            pygame.mixer.Sound.play(pygame.mixer.Sound("resources/audio/game-start.wav"))
            first_iteration = False

        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        screen.onkey(snake.up, "w")
        screen.onkey(snake.down, "s")
        screen.onkey(snake.left, "a")
        screen.onkey(snake.right, "d")

        if crashed_into_wall(snake):
            pygame.mixer.Sound.play(hit)
            snake.kill()
            break

        try:
            snake.move()
            if snake.head.distance(food) <= BLOCK_SIZE/2:
                pygame.mixer.Sound.play(eat)
                snake.grow()
                food.move()
                score_display.add_to_score(1)
                score_display.update_score()
                if score_display.points % 10 == 0:
                    pygame.mixer.Sound.play(collect_10)

        except CrashedIntoTail:
            pygame.mixer.Sound.play(hit)
            break

        screen.update()
        sleep(0.05)

    food.hideturtle()
    if score_display.points > score_display.high_score:
        pygame.mixer.music.load("resources/audio/new-record.mp3")
        if music:
            pygame.mixer.music.play()
        end_message.display(f"Score: {score_display.points} New Record!")
    else: 
        pygame.mixer.music.load("resources/audio/game-over.mp3")
        if music:
            pygame.mixer.music.play()
        end_message.display("Press Space to play again!")

    screen.update()
    score_display.update_high_score()
    screen.onkey(main, "space")
    screen.onkey(reset_score, "r")
    screen.exitonclick()


if __name__ == "__main__":
    main()
