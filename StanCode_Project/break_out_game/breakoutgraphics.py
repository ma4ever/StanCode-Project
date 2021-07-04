"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout') -> object:
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # position for game over sign
        self.sign_width = brick_cols * (brick_width - 22)
        self.sign_height = brick_offset + 3 * (brick_rows * brick_height)

        # Create a paddle
        self.paddle_width = PADDLE_WIDTH
        self.paddle_height = PADDLE_HEIGHT
        self.paddle = GRect(self.paddle_width, self.paddle_height, x=(self.window_width - self.paddle_width) // 2,
                            y=self.window_height - paddle_offset - self.paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_radius = BALL_RADIUS
        self.ball = GOval(2 * self.ball_radius, 2 * self.ball_radius, x=(self.window_width - 2 * self.ball_radius) // 2,
                          y=(self.window_height - 2 * self.ball_radius) // 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width - self.ball_radius) // 2,
                        y=(self.window_height - self.ball_radius) // 2)

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Draw bricks
        for i in range(0, brick_cols + 1):
            for j in range(0, brick_rows + 1):
                if j < 2:
                    color = 'red'
                elif 2 <= j < 4:
                    color = 'orange'
                elif 4 <= j < 6:
                    color = 'yellow'
                elif 6 <= j < 8:
                    color = 'green'
                else:
                    color = 'blue'
                brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing) * (i - 1),
                              y=brick_offset + (brick_height + brick_spacing) * (j - 1))
                brick.filled = True
                brick.fill_color = color
                brick.color = color
                self.window.add(brick)
                self.all_brick_number = brick_cols * brick_rows

        # use switch to let ball not be interrupted when you click mouse more than once
        self.switch = 1

        # Initialize our mouse listeners
        onmouseclicked(self.click)
        onmousemoved(self.stick_paddle)

    def click(self, mouse):
        if self.switch == 1:
            self.switch = -self.switch

    def stick_paddle(self, event):
        self.paddle.x = event.x - self.paddle.width // 2
        if event.x + self.paddle.width // 2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if event.x - self.paddle.width // 2 < 0:
            self.paddle.x = 0

    def set_ball_position(self):
        self.window.add(self.ball, x=(self.window_width - self.ball_radius) // 2,
                        y=(self.window_height - self.ball_radius) // 2)

    def set_ball_velocity(self):
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if (random.random() > 0.5):
            self._dx = -self._dx

    def ball_move(self):
        if self.switch == -1:
            self.ball.move(self._dx, self._dy)

    def hit_three_side_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball_radius * 2 >= self.window_width:
            self._dx = -self._dx
        if self.ball.y <= 0:
            self._dy = -self._dy

    def hit_brick_or_paddle(self):
        object1 = self.window.get_object_at(self.ball.x, self.ball.y)
        object2 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        object3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        object4 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)
        if object1 is not None and object1.y + self.ball_radius * 2 <= self.paddle.y:
            self._dy = -self._dy
            if object1 is not self.paddle:
                self.all_brick_number -= 1
                self.window.remove(object1)
        elif object2 is not None and object2.y + self.ball_radius * 2 <= self.paddle.y:
            self._dy = -self._dy
            if object2 is not self.paddle:
                self.all_brick_number -= 1
                self.window.remove(object2)
        elif object3 is not None and object3.y <= self.paddle.y:
            self._dy = -self._dy
            if object3 is not self.paddle:
                self.all_brick_number -= 1
                self.window.remove(object3)
        elif object4 is not None and object4.y <= self.paddle.y:
            self._dy = -self._dy
            if object4 is not self.paddle:
                self.all_brick_number -= 1
                self.window.remove(object4)

    def hit_all_brick(self):
        if self.all_brick_number == 0:
            return True

    def ball_fall(self):
        if self.ball.y + self.ball.height >= self.window.height:
            self.switch = 1
            return True

    def game_over(self):
        label = GLabel('Game Over :(', x=self.sign_width, y=self.sign_height)
        label.font = '-20'
        label.color = 'magenta'
        self.window.add(label)

    def y_speed(self):
        return self._dy

    def x_speed(self):
        return self._dx
