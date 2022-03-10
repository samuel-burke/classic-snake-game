"""
Controls the main functionality of the Snake, Food, and Screen to all be integrated together in the main program

Author: Samuel Burke
Created: 03.05.2022
"""
from time import sleep
from turtle import Screen

import pygame

from board import *
from endmessage import EndMessage
from food import Food
from scoreboard import ScoreBoard
from snake import Snake, CrashedIntoTail

music = True  # User option to toggle background music


def format_screen(s):
    """
    Set up a basic window dimensions, background color, and title
    :param s: the Screen object
    """
    s.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    s.bgcolor(BG_COLOR)
    s.title('Snake Game 🐍')
    s.tracer(0)


def crashed_into_wall(position, heading):
    """
    Checks if the snake has crashed into one of the walls
    :param position: The snake head's current position
    :param heading: The snake's current direction of movement
    :return: True if the snake has crashed into a wall
    """
    x, y = position

    # check if snake crashed into right wall
    if heading == RIGHT:
        return x + BLOCK_SIZE / 2 + STEP > RIGHT_WALL
    # check if snake crashed into top wall
    elif heading == UP:
        return y + BLOCK_SIZE / 2 + STEP > TOP_WALL
    # check if snake crashed into left wall
    elif heading == LEFT:
        return x - BLOCK_SIZE / 2 - STEP < LEFT_WALL
    # check if snake crashed into bottom wall
    else:
        return y - BLOCK_SIZE / 2 - STEP < BOTTOM_WALL


def toggle_background_music():
    """Toggles the background music during gameplay"""
    global music
    # if the music is currently playing, pause the music
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        music = False
    # if the music is currently paused, start the music
    else:
        pygame.mixer.music.load("resources/audio/background-music.wav")
        pygame.mixer.music.play(-1)
        music = True


def main():
    """Set's up and runs the main program."""
    def disable_key_input():
        """disables movement keys while currently in a step to prevent more than one movement request per interval"""
        screen.onkey(None, 'Up')
        screen.onkey(None, 'Down')
        screen.onkey(None, 'Left')
        screen.onkey(None, 'Right')
        screen.onkey(None, 'w')
        screen.onkey(None, 'a')
        screen.onkey(None, 's')
        screen.onkey(None, 'd')

    def enable_key_input():
        """enables movement keys once the interval is completed"""
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        screen.onkey(snake.up, "w")
        screen.onkey(snake.down, "s")
        screen.onkey(snake.left, "a")
        screen.onkey(snake.right, "d")

    def reset_score():
        """Resets the high score with user confirmation"""

        def yes():
            """Resets the high score"""
            score_display.reset_high_score()
            end_message.display("High score reset")
            score_display.update_score()
            screen.update()

        def no():
            """Cancels score reset"""
            end_message.display("Press Space to play again!")
            screen.update()

        end_message.display("Reset high score? y/n")
        screen.update()
        screen.onkey(yes, 'y')
        screen.onkey(no, 'n')

    # set up the sound/music for the program
    pygame.mixer.init()
    eat = pygame.mixer.Sound("resources/audio/eat.wav")
    collect_10 = pygame.mixer.Sound("resources/audio/collect-10.wav")
    hit = pygame.mixer.Sound("resources/audio/hit.wav")
    pygame.mixer.music.load("resources/audio/background-music.wav")

    # if the music toggle is set to true, play background music
    if music:
        pygame.mixer.music.play(-1)

    # set up the screen
    screen = Screen()
    screen.clear()
    format_screen(screen)
    draw_border()

    # set up the snake, food, and messages
    snake = Snake(disable_key_input)
    food = Food()
    score_display = ScoreBoard()
    end_message = EndMessage()
    screen.listen()
    screen.onkey(toggle_background_music, "m")

    first_iteration = True
    while True:
        # disable replay and reset score while in the game loop
        screen.onkey(None, 'space')
        screen.onkey(None, "r")

        if first_iteration:
            screen.update()
            sleep(1)
            pygame.mixer.Sound.play(pygame.mixer.Sound("resources/audio/game-start.wav"))
            first_iteration = False

        # enable snake heading movement
        enable_key_input()

        # check if the snake has crashed into a wall
        if crashed_into_wall(snake.head.position(), snake.head.heading()):
            pygame.mixer.Sound.play(hit)
            snake.kill()
            break

        try:
            snake.move()

            # check if the snake touches a piece of food
            if snake.head.distance(food) <= BLOCK_SIZE / 2:
                pygame.mixer.Sound.play(eat)
                snake.grow()
                food.move()
                score_display.increment_score()
                score_display.update_score()
                if score_display.points % 10 == 0:
                    pygame.mixer.Sound.play(collect_10)

        except CrashedIntoTail:
            pygame.mixer.Sound.play(hit)
            break

        screen.update()
        sleep(0.05)

    food.hideturtle()  # hide food

    # new high score ending
    if score_display.points > score_display.high_score:
        pygame.mixer.music.load("resources/audio/new-record.mp3")
        if music:
            pygame.mixer.music.play()
        end_message.display(f"Score: {score_display.points} New Record!")

    # try again ending
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
