# pygame_line_art/screen.py
from pygame import init, display, draw, time, event, mouse, QUIT
from random import randint, random, uniform
from math import sin, cos, dist, atan2, pi

class AlphaSetter:
    def __init__(self):
        self.value = (120, 120, 120)

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

class Screen:
    def __init__(self):
        init()
        self.lines = []
        self.width = 1500
        self.height = 700
        self.surface = display.set_mode((self.width, self.height))
        self.clock = time.Clock()
        self.alpha = AlphaSetter()
        self.lines_connection = True
        self.line_spawn_time = 1  # in seconds
        self.line_dispose_time = 1  # in seconds
        self.move_speed = 5
        self.rotate_speed = uniform(-0.01, 0.01)
        self.mouse_magnet = True
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def quit(self):
        display.quit()
        self.running = False
        self.lines.clear()

    def update(self, interval):
        while self.running:
            for e in event.get(QUIT):
                self.quit()
            self.surface.fill((0, 0, 0))
            if random() < 0.07:
                self.lines.append({'x': randint(0, self.width), 'y': randint(0, self.height), 'fade-out': False,
                                   'angle': uniform(0, 2 * pi), 'timer': 1, 'rotation_speed': self.rotate_speed})
            temp = 0
            for line in self.lines:
                line['angle'] += line['rotation_speed']
                if line['angle'] > 2 * pi:
                    line['angle'] -= 2 * pi
                if line['timer'] == 0:
                    self.lines.remove(line)
                    continue
                alpha = min([120, line['timer']])
                end_x = line['x'] + line['timer'] // 5 * cos(line['angle'])
                end_y = line['y'] + line['timer'] // 5 * sin(line['angle'])
                draw.line(self.surface, self.alpha.get(), (line['x'], line['y']), (end_x, end_y), 1)
                if self.lines_connection:
                    for other_line in self.lines:
                        if line != other_line:
                            if dist((line['x'], line['y']), (other_line['x'], other_line['y'])) < 50:
                                draw.line(self.surface, self.alpha.get(), (line['x'], line['y']),
                                          (other_line['x'], other_line['y']), 1)
                                draw.circle(self.surface, self.alpha.get(), (line['x'], line['y']), 2)
                                draw.circle(self.surface, self.alpha.get(), (other_line['x'], other_line['y']), 2)
                            # ... other connection conditions
                line['x'] += cos(line['angle']) * self.move_speed
                line['y'] += sin(line['angle']) * self.move_speed
                if line['x'] < 0 or line['x'] > self.width or line['y'] < 0 or line['y'] > self.height:
                    self.lines.remove(line)
                    continue
                if line['timer'] > 500:
                    line['fade-out'] = True
                if line['fade-out']:
                    line['timer'] -= 1
                else:
                    line['timer'] += 1
                mouse_x, mouse_y = mouse.get_pos()
                if self.mouse_magnet and dist((line['x'], line['y']), (mouse_x, mouse_y)) < 100:
                    if temp > 50:
                        self.lines.remove(line)
                    else:
                        temp += 1
                    line['fade-out'] = False
                    angle_to_mouse = atan2(mouse_y - line['y'], mouse_x - line['x'])
                    line['x'] += cos(angle_to_mouse) * self.move_speed
                    line['y'] += sin(angle_to_mouse) * self.move_speed
            display.flip()
            self.clock.tick(100)
            time.delay(interval)

    def set_move_speed(self, speed=5):
        self.move_speed = speed

    def set_rotate_speed(self, speed=uniform(-0.01, 0.01)):
        self.rotate_speed = speed

    def set_line_spawn_time(self, time_seconds=1):
        self.line_spawn_time = time_seconds

    def set_line_dispose_time(self, time_seconds=1):
        self.line_dispose_time = time_seconds

    def set_surface(self, surface):
        self.surface = surface

if __name__ == "__main__":
    s = Screen()
    s.start()
    s.update(100)
