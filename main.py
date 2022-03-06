#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
from time import sleep
from turtle import Screen

from board import *
from food import Food
from lossmessage import LossMessage
from scoreboard import ScoreBoard
from snake import Snake, CrashedIntoTail

NUM_FOOD = 3


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
    screen = Screen()
    screen.clear()
    format_screen(screen)
    draw_border()

    snake = Snake()
    all_food = [Food() for _ in range(NUM_FOOD)]
    score_display = ScoreBoard()

    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(snake.up, 'w')
    screen.onkey(snake.down, 's')
    screen.onkey(snake.left, 'a')
    screen.onkey(snake.right, 'd')

    screen.listen()

    t = 0

    while True:
        screen.onkey(None, 'space')

        t += 1
        if t == 1:
            screen.update()
            sleep(1)

        if crashed_into_wall(snake):
            snake.kill()
            break

        try:
            snake.move()
            for food in all_food:
                food.forward()
                if snake.head.distance(food) <= 30:
                    snake.grow()
                    food.move()
                    score_display.add_to_score(50)
                    score_display.update_score()

        except CrashedIntoTail:
            break

        if t % 20 == 0:
            score_display.add_to_score(1)
            score_display.update_score()

        screen.update()

    for food in all_food:
        food.hideturtle()

    LossMessage().display()
    screen.update()
    screen.onkey(play_game, 'space')
    score_display.update_high_score()
    screen.exitonclick()


def main():
    play_game()


if __name__ == "__main__":
    main()
