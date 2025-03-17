from turtle import Turtle, Screen
import time
from food import Food
from Snake import Snake
from scoreboard import Score

def main():
    # Setup screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("My Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)

    # Create game objects
    snake = Snake()
    food = Food()
    score = Score()

    # Listen for keyboard input
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    # Game loop
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Collision with wall
        if (
            snake.head.xcor() < -280 or snake.head.xcor() > 280 or
            snake.head.ycor() < -280 or snake.head.ycor() > 280
        ):
            score.reset()
            save_high_score(score.high_score)
            snake.reset()

        # Collision with self
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                save_high_score(score.high_score)
                snake.reset()

    screen.exitonclick()

# Function to save high score to a file
def save_high_score(high_score):
    with open("data.txt", mode="w") as file:
        file.write(str(high_score))

# Run the game
if __name__ == "__main__":
    main()
