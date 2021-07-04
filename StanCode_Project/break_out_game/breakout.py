"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    graphics.set_ball_velocity()  # choose one speed for ball
    lives = NUM_LIVES  # three lives in total (When three lives use up, game over.)

    # Add animation loop here!
    while True:
        graphics.ball_move()  # make ball move
        graphics.hit_three_side_wall()  # When ball hits wall, ball changes direction.
        if graphics.ball_fall():
            # When ball falls outside of window, one life lost and ball appears on the starting point.
            lives -= 1
            if lives > 0:
                graphics.set_ball_position()  # ball appears on the starting point
                graphics.set_ball_velocity()  # choose another speed for a new start
                pause(FRAME_RATE)
            else:
                graphics.set_ball_position()
                graphics.game_over()  # Game Over sign appears
                break

        # When ball hits brick, brick disappears; when ball hits paddle, ball changes direction.
        graphics.hit_brick_or_paddle()
        if graphics.hit_all_brick():  # When all bricks are hit, game over.
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
