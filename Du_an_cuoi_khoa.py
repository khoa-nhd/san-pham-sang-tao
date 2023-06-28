import pygame
import random
import time
import turtle

# Class thể hiện đối tượng Câu hỏi
# Một đối tượng Question gồm có 2 fields: .
# - question: đề bài
# - answer: đáp án

# che_do = int(input("Hãy chọn chế độ dễ, bình thường, khó hoặc khác, dễ nhập 1, bình thường nhập 2, khó nhập 3, khác nhập 4: "))
# if che_do == 1:
#     game_nummath = 3
#     game_numdd = 2
#     math_digit = 1
# elif che_do == 2:
#     game_nummath = 10
#     game_numdd = 5
#     math_digit = 2
# elif che_do == 3:
#     game_nummath = 20
#     game_numdd = 10
#     math_digit = 3
# else:
#     game_numath = int(input("Số câu hỏi về Toán Học: "))
#     game_numdd = int(input("Số câu hỏi về Đoàn Đội tối đa 20 câu: "))
#     math_digit = int(input("Số lượng chữ số trong phép tính: "))
che_do = 2
game_nummath = 5
game_numdd = 10
math_digit = 2

# Tên màn hình hiện tại (menu, main)
screen_name = ""

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

        
# Class thể hiện trạng thái hiện tại của trò chơi
class GameState:
    # Điểm số hiện tại
    score = 0
    # Khởi động lại đồng hồ bấm giờ: cho giá trị bằng thời gian hiện tại
    def reset_timer(self):
        self.start_time = time.time()
    # Trả về thời gian trả lời câu hỏi (tính bằng giây), bằng cách lấy
    # thời gian đồng hồ trừ đi thời gian start_time đã lưu.
    def get_timer(self):
        return time.time() - self.start_time

# Khởi tạo đối tượng cụ thể lưu trạng thái của trò chơi.
state = GameState()

# Dùng thư viện pygame để chơi âm thanh. 
def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    
def play_sound(file):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
# gavatar = None
avatar = turtle.Turtle()
# Vẽ hình nhân vật.
def draw_avatar(image):
    # Phải gọi lệnh turtle.addshape trước khi vẽ ảnh.
    turtle.addshape(image)  
    avatar.clear()
    avatar.penup()
    avatar.setposition(0, 0)
    # Lưu ý: turtle chỉ vẽ được ảnh có định dạng .gif
    avatar.shape(image)

# Khởi tạo cây bút chuyên dùng để vẽ thời gian.
pen_timer = turtle.Turtle()
def draw_timer():
    if screen_name == 'main':
        # Ẩn con rùa.
        pen_timer.hideturtle()
        # Nhấc bút lên.
        pen_timer.penup()
        # Xoá, để khi vẽ điểm không bị đè lên nhau.
        pen_timer.clear()
        # Đổi màu.
        pen_timer.color('blue')
        # Đặt vị trí.
        pen_timer.setposition(-470, -20)
        # Viết điểm số ra màn hình.
        pen_timer.write(round(state.get_timer()), font=get_font(40))
        # Vẽ lại điểm số sau 1000ms (1 giây) nữa
    turtle.Screen().ontimer(draw_timer, 1000)
# Khai báo dữ liệu câu hỏi và đáp án
def read_data():
    # Đọc câu hỏi và đáp án từ Files.
    # Số lượng câu hỏi
    num_questions = int(game_numdd)
    # Ban đầu, mảng dữ liệu là trống
    data = []
    # Các file câu hỏi đánh số là q1.txt, q2.txt, q3.txt,...
    # Các file câu trả lời đánh số là a1.txt, a2.txt, a3.txt,...
    # Ta dùng hàm range(1, x + 1) để duyệt qua các số 1, 2, ..., x
    all_list = [*range(1,20)]
    random.shuffle(all_list)
    # for i in range(1, num_questions + 1):
    for i in all_list[0:num_questions]:
        rand_index = random.randint(1, 20)
        # Đọc câu hỏi, dùng encoding='utf-8' để đọc tiếng Việt
        filename = 'q' + str(i) + '.txt'
        f = open(filename, 'r', encoding='utf-8')
        question = f.read()
        f.close()    
        
        # Đọc đáp án
        filename = 'a' + str(i) + '.txt'
        f = open(filename, 'r', encoding='utf-8')
        answer = f.read()
        f.close()    

        # Tạo đối tượng Question và thêm vào mảng dữ liệu data
        data.append(Question(question, answer))
    # Trả về mảng dữ liệu data     
    return data


# Sinh ra các câu hỏi tính nhẩm ngẫu nhiên Siêu Trí Tuệ
def generate_math_questions():
    # Ban đầu, danh sách câu hỏi trống.
    data = []
    # Số lượng câu hỏi sinh ra.
    num_questions = game_nummath
    # Hai phép toán: cộng và nhân
    operators = ["+", "x", ":", "-"]    
    # Số lượng chữ số tối đa khi sinh câu hỏi ngẫu nhiên
    max_digits = math_digit
    for i in range(num_questions):
        # Chọn số ngẫu nhiên từ 0 đến 10^max_digits - 1
        a = random.randint(1, 10**max_digits)
        b = random.randint(1, 10**max_digits)
        # Chọn một phép toán ngẫu nhiên
        op = random.choice(operators)
        
        if op == ':':
            # while a % b != 0:
            #     a = random.randint(1, 10**(max_digits-1))
            #     b = random.randint(1, 10**(max_digits-1))
            #     a = a * b
            while a < 10**max_digits: 
                b = random.randint(1, 10**(max_digits-1))
                a = b * random.randint(1, 10**(max_digits))
        elif op == "-":
            if b > a:
                a, b = b, a
        
        # Sinh ra đề bài
        question = str(a) + " " + op + " " + str(b) + " = ?"
        # Sinh ra đáp án
        if op == "+":
            answer = a + b
        elif op == "x":
            answer = a * b
        elif op == ":":
            answer = int(a / b)
        elif op == "-":
            answer = a - b
        # Thêm câu hỏi vào danh sách
        data.append(Question(question, str(answer)))
    # Trả về danh sách câu hỏi tính nhẩm Siêu Trí Tuệ.
    return data



# Trả về font chữ với kích thước được cho.
def get_font(font_size):
    return ("Arial", font_size, "normal")

# Khởi tạo cây bút chuyên dùng để vẽ Điểm số.
pen_score = turtle.Turtle()
global final_score
def draw_score():
    global score
    global final_score
    # Ẩn con rùa.
    pen_score.hideturtle()
    # Nhấc bút lên.
    pen_score.penup()
    # Xoá, để khi vẽ điểm không bị đè lên nhau.
    pen_score.clear()
    # Đổi màu.
    pen_score.color('white')
    # Đặt vị trí.
    pen_score.setposition(-136, -183)
    # Viết điểm số ra màn hình.
    pen_score.write(state.score, font=get_font(28))
    print(state.score)

# In câu hỏi ra màn hình
def ask_question(question, lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat):
    # In ra dấu * ngăn cách giữa hai câu hỏi
    print("***************************")
    print(question.question)
    # Xoá màn hình trước khi vẽ để chữ khỏi bị viết đè lên nhau
    turtle.clear()
    # Ẩn con rùa (hình tam giác) 
    turtle.hideturtle()
    # Nhấc bút lên (để khỏi để lại dấu vết)
    turtle.penup()
    # Vẽ hình nhân vật trạng thái bình thường 
    draw_avatar('normal.gif')
    # Đặt vị trí bút (để viết câu hỏi)
    # turtle.setposition(40, 20)
    question_text_left = 40
    text_font_size = 18
    font = get_font(text_font_size)
    turtle.setposition(question_text_left, 225)
    # In câu hỏi ra màn hình Turtle và cho biết cỡ font chữ.
    # turtle.write(question.question, font=get_font(18))
    lines = question.question.splitlines()
    for line in lines:
        turtle.write(line, font = font)
        turtle.goto(question_text_left, turtle.ycor() - text_font_size - 10)
    # Gọi hàm viết điểm số ra màn hình.
    draw_score()
    # Trước khi hỏi câu hỏi mới, cần khởi động lại đồng hồ bấm giờ
    state.reset_timer()
    draw_timer()
    # Hỏi người dùng nhập câu trả lời qua giao diện Turtle
    result = turtle.textinput("Siêu trả lời", "Câu trả lời của bạn là gì???\n")
    # So sánh kết quả của người chơi nhập vào với đáp án
    lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat = check_result(result, question.answer, lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat)
    return (lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat)
    
# So sánh câu trả lời với đáp án
def check_result(result, answer, lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat):
    # Thời gian người chơi trả lời câu hỏi (tính bằng giây).
    time_taken = state.get_timer()
    # Tính điểm thưởng nếu trả lời nhanh.
    if time_taken < 5:
        bonus = 100
    else:
        bonus = 0
    if result == answer:
        lanDung = lanDung + 1
        if lanDung > lanDungNhieuNhat:
            lanDungNhieuNhat = lanDung
        thoiGian = time_taken
        if thoiGian < thoiGianItNhat:
            thoiGianItNhat = thoiGian
        # Cộng điểm nếu người chơi trả lời đúng
        # Cộng điểm trả lời đúng và cả điểm thưởng nữa.
        state.score += 100 + bonus    
        # Chơi âm thanh cho biết trả lời đúng.
        play_sound("correct_answer.wav")
        play_sound("corect1.mp3")

        # Vẽ hình nhân vật khi trả lời đúng.
        draw_avatar('correct.gif')
        print("Đúng rồi")
    else:
        lanDung = 0
        # Chơi âm thanh cho biết trả lời sai.
        state.score -= 50
        play_sound("wrong.mp3")
        play_sound("wrong_answer.wav")
        play_sound("wrong1.mp3")

        # Vẽ hình nhân vật khi trả lời sai.
        draw_avatar('wrong.gif')
        print("Sai rồi")

    # Chờ một chút để thấy rõ nhân vật cử động.
    time.sleep(0.5)
    print("Thời gian trả lời câu hỏi là:", round(time_taken), "giây")
    if bonus > 0:
        print("Bạn nhận được điểm thưởng là", bonus, "vì trả lời nhanh")            
    print("Điểm hiện tại của bạn là: ", state.score)
    return (lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat)

def clickPosition(x, y):
    print("click: ", screen_name, "(", x, "," ,y,")")
    
    # chỉ xử lý cho màn hình menu
    if screen_name != 'menu':
        return
    
    # button position
    btn_start_left = -156
    btn_start_top = 138
    btn_start_right = 143
    btn_start_bottom = 74
    
    btn_setting_left = -181
    btn_setting_top = 46
    btn_setting_right = 179
    btn_setting_bottom = -19
    
    btn_exit_left = -128
    btn_exit_top = -64
    btn_exit_right = 107
    btn_exit_bottom = -116
    
    # check click position 
    if btn_start_left <= x and x <= btn_start_right and btn_start_bottom <= y and y <= btn_start_top:
        print('Click bắt đầu')
        setup_main_screen()
        start_main_game()
    elif btn_setting_left <= x and x <= btn_setting_right and btn_setting_bottom <= y and y <= btn_setting_top:
        print('Click thiết lập')
        input_setting()
    elif btn_exit_left <= x and x <= btn_exit_right and btn_exit_bottom <= y and y <= btn_exit_top:
        print('Click thoát')
        exit()
    return

# Thiết lập màn hình giao diện turtle
def setup_main_screen():
    global screen_name
    global avatar
    score = 0
    screen_name = "main"
    turtle.resetscreen()
    # Màn hình Turtle
    screen = turtle.Screen()
    # Thiết lập kích thước màn hình 
    screen.setup(1190, 666)
    # Thiết lập ảnh nền cho màn hình
    screen.bgpic('background.png')
    # Gỡ sự kiện nhấn chuột
    # screen.onclick(None)
    # Thiết lập tiêu đề cho cửa sổ chương trình
    turtle.title("Siêu câu đố")
    # khởi tạo lại avatar
    avatar = turtle.Turtle()
    
def setup_menu_screen():
    global screen_name
    screen_name = "menu"
    turtle.resetscreen()
    # Màn hình Turtle
    screen = turtle.Screen()
    # Thiết lập kích thước màn hình 
    screen.setup(1190, 666)
    # Thiết lập ảnh nền cho màn hình
    screen.bgpic('background_menu.png')
    # Thiết lập tiêu đề cho cửa sổ chương trình
    turtle.title("Siêu câu đố - MENU")
    # Thiết lập sự kiện nhấn chuột
    screen.onclick(clickPosition)
    turtle.mainloop()


def setup_gameover_screen():
    global screen_name
    global final_score
    final_score = 0
    if final_score <= 0:
        state.score = final_score * -1 + final_score
    else:
        state.score = final_score - final_score
    screen_name = "Game over"
    turtle.resetscreen()
    turtle.clearscreen()
    # Màn hình Turtle
    screen = turtle.Screen()
    # Thiết lập kích thước màn hình 
    screen.setup(1190, 666)
    # Thiết lập ảnh nền cho màn hình
    screen.bgpic('backgroundgameover.png')
    # Thiết lập tiêu đề cho cửa sổ chương trình
    turtle.title("Siêu câu đố - You lost")
    # Thiết lập sự kiện nhấn chuột
    screen.onclick(clickPosition2)
    turtle.mainloop()

def clickPosition2(x, y):
    print("click: ", screen_name, "(", x, "," ,y,")")
    # chỉ xử lý cho màn hình menu
    if screen_name != 'Game over':
        return
    
    # button position   
    btn_playagain_left = -240
    btn_playagain_top = 120
    btn_playagain_right = 230
    btn_playagain_bottom = 6
    
    btn_thoat_left = -212
    btn_thoat_top = -29
    btn_thoat_right = 208
    btn_thoat_bottom = -135
    
    # check click position 
    if btn_playagain_left <= x and x <= btn_playagain_right and btn_playagain_bottom <= y and y <= btn_playagain_top:
        print('Click chơi lại')
        setup_menu_screen()
    elif btn_thoat_left <= x and x <= btn_thoat_right and btn_thoat_bottom <= y and y <= btn_thoat_top:
        print('Click thoát')
        exit()
    return


def input_number(title, prompt):
    while True:
        input_value = turtle.textinput(title, prompt)
        print(input_value)
        print(input_value !=None)
        print(input_value.isnumeric())
        if input_value !=None and input_value.isnumeric():
            return int(input_value)

def input_setting():
    global che_do
    global game_nummath
    global game_numdd
    global math_digit
    che_do = turtle.textinput("Thiết lập", "Hãy chọn chế độ dễ, bình thường, khó hoặc khác, dễ nhập 1, bình thường nhập 2, khó nhập 3, khác nhập 4: ")
    if che_do == '1':
        game_nummath = 2
        game_numdd = 3
        math_digit = 1
    elif che_do == '2':
        game_nummath = 5
        game_numdd = 10

        math_digit = 2
    elif che_do == '3':
        game_nummath = 10
        game_numdd = 20
        math_digit = 3
    else:
        # game_numath = int(turtle.textinput("Thiết lập", "Số câu hỏi về Toán Học:"))
        # game_numdd = int(turtle.textinput("Thiết lập", "Số câu hỏi về Đoàn Đội tối đa 20 câu:"))
        # math_digit = int(turtle.textinput("Thiết lập", "Số lượng chữ số trong phép tính: "))
        game_numath = input_number("Thiết lập", "Số câu hỏi về Toán Học:")
        game_numdd = input_number("Thiết lập", "Số câu hỏi về Đoàn Đội tối đa 20 câu:")
        math_digit = input_number("Thiết lập", "Số lượng chữ số trong phép tính: ")
        if game_numdd > 20:
            game_numdd = 20
    return

# Vẽ thời gian
#state.reset_timer()
#draw_timer()

def start_main_game():
    # Reset
    # TODO:
    global score
    score = 0

    # Kết hợp các câu đố vui đọc từ File với các câu tính nhẩm Siêu Trí Tuệ.
    data = read_data() + generate_math_questions()

    # Xáo trộn các câu hỏi một cách ngẫu nhiên
    random.shuffle(data)
    lanDung = 0
    thoiGianItNhat = 100
    thoiGian = 0
    lanDungNhieuNhat = 0
    for question in data:
        lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat = ask_question(question, lanDung, thoiGianItNhat, thoiGian, lanDungNhieuNhat)
    print("Bạn có lần đúng liên tiếp nhều nhất là: " + str(lanDungNhieuNhat) + " lần.")
    print("final score: " + str(state.score))
    global final_score
    final_score = state.score
    
    print("Thời gian suy nghĩ nhanh nhất mà có câu trả lời chính xác là: " + str(thoiGianItNhat) + " giây.")

    if state.score >= 300:
        #Chúc mừng
        print("Bạn thật giỏi! Chúc mừng!")
        import pygame as pg
        import sys, os
        pg.init()
        clock = pg.time.Clock()


        WIDTH = 724 
        HEIGHT = 540 

        FPS = 60

        IMAGE_WIDTH = 720 
        IMAGE_HEIGHT = 540
        OFFSET = 100

        ASSETS_PATH = './'
        timeBetweenPicture = 0.95
        timeBetweenPicture1 = 0.5
        moves = {
            'move0': {
                'time': 0,
                'sprites': [
                    '0.png'
                    ]
                },
            'move1': {
                'time': timeBetweenPicture,
                'sprites': [
                    '1.1.png',
                    '1.2.png',
                    '1.3.png'
                    ]
                },
            'move2': {
                'time': timeBetweenPicture,
                'sprites': [
                    '2.1.png',
                    '2.2.png'
                    ]
                },
            'move3': {
                'time': timeBetweenPicture,
                'sprites': [
                    '3.1.png',
                    '3.2.png'
                    ]
                },
            'move4': {
                'time': timeBetweenPicture,
                'sprites': [
                    '4.1.png',
                    '4.2.png'
                    ]
                },
            'move5': {
                'time': timeBetweenPicture,
                'sprites': [
                    '5.1.png',
                    '5.2.png'
                    ]
                },
            'move6': {
                'time': timeBetweenPicture,
                'sprites': [
                    '6.1.png',
                    '6.2.png'
                    ]
                },
            'move7': {
                'time': timeBetweenPicture1,
                'sprites': [
                    '7.1.png',
                    '7.2.png',
                    '7.3.png'
                    ]
                }
            }
        procedure = [
            'move0',
            'move1',
            'move2',
            'move3',
            'move4',
            'move1',
            'move2',
            'move3',
            'move4',
            'move5',
            'move6',
            'move3',
            'move4',
            'move5',
            'move6',
            'move3',
            'move7',
            'move7',
            'move7'
            ]

        class Dancer(pg.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.moves = {}
                self.current_move = 0
                self.current_sprite = 0
                self.frames_per_image = 0
                self.count = 0
                self.image = None
                self.rect = None
                
            def init(self):
                self.load_images()
                self.draw_image(self.moves[procedure[self.current_move]]['sprites'][self.current_sprite])
            
            def load_images(self):
                count = 0
                for move in moves:
                    count+=1
                    sprites = []
                    for sprite in moves[move]['sprites']:
                        sprites.append(pg.image.load(os.path.join(ASSETS_PATH+move,sprite)))
                    self.moves[move]= {
                        'time': moves[move]['time'],
                        'sprites': sprites
                        }
            def draw_image(self,sprite):
                self.image = sprite
                self.image = pg.transform.scale(self.image, (IMAGE_WIDTH, IMAGE_HEIGHT))
                self.rect = self.image.get_rect()
                self.rect.topleft = [0,0]
            
            def update(self):
                number_of_moves = len(procedure)
                if self.current_move < number_of_moves:
                    number_of_sprites = len(self.moves[procedure[self.current_move]]['sprites'])
                    time_of_move = self.moves[procedure[self.current_move]]['time']
                    self.frames_per_image = FPS*time_of_move//number_of_sprites
                    
                    if self.count >= self.frames_per_image:
                        if self.current_sprite < number_of_sprites:
                            self.next_sprite()
                        else:
                            self.next_move()
                            
                    self.count += 1
                    

            def next_sprite(self):
                sprite = self.moves[procedure[self.current_move]]['sprites'][self.current_sprite]
                self.draw_image(sprite)
                self.count = 0
                self.current_sprite += 1
            
            def next_move(self):
                self.current_move += 1
                self.current_sprite = 0
            

        def main():
            screen = pg.display.set_mode((WIDTH,HEIGHT))
            pg.display.set_caption("Bạn thật giỏi! Chúc mừng!")
            moving_sprites = pg.sprite.Group()
            dancer = Dancer()
            dancer.init()
            moving_sprites.add(dancer)

            pg.mixer.init()
            pg.mixer.music.load(os.path.join(ASSETS_PATH,'music1.wav'))
            pg.mixer.music.play(-1)
            import datetime 
            start_time = datetime.datetime.now() 
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                moving_sprites.update()
                moving_sprites.draw(screen)
                now_time = datetime.datetime.now() 
                pg.display.flip()
                clock.tick(FPS)
                if now_time.second - start_time.second > 17:
                    break


        if __name__ == "__main__":
            main()
            

        print("Mình có 1 trò chơi tặng bạn bạn hãy vượt qua các robot và đến đích nhé!")
        # Game né robot

        class Door:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                sprite = pygame.image.load("sprites/door.png")
                self.image = pygame.transform.scale(sprite, (80, 80))

        class Robot:
            def __init__(self, x, y, x_heading, y_heading, hinh_anh):
                self.x = x
                self.y = y
                self.x_heading = x_heading
                self.y_heading = y_heading
                sprite = pygame.image.load(hinh_anh)
                self.image = pygame.transform.scale(sprite, (60, 60))

            def move(self):
                self.x = self.x + self.x_heading
                self.y = self.y + self.y_heading
                
                if self.x > 440: self.x_heading = - self.x_heading
                if self.x < 0:   self.x_heading = - self.x_heading
                if self.y > 440: self.y_heading = - self.y_heading
                if self.y < 0:   self.y_heading = - self.y_heading

        class Player:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                sprite = pygame.image.load("sprites/trau.png")
                self.image = pygame.transform.scale(sprite, (50, 80))
            
            def move(self, change_x, change_y):
                new_x = self.x + change_x
                new_y = self.y + change_y

                if new_x > 0 and new_x < 450:
                    self.x = new_x
                if new_y > 0 and new_y < 420:
                    self.y = new_y

            def touch(self, obj):
                mask1 = pygame.mask.from_surface(self.image)
                mask2 = pygame.mask.from_surface(obj.image)
                offset_x = obj.x - self.x
                offset_y = obj.y - self.y
                if mask1.overlap(mask2, (offset_x, offset_y)):
                    return True
                else:
                    return False

        class Game:
            def __init__(self):
                pygame.init()
                self.WIDTH = 500  
                self.HEIGHT = 500  
                self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])

                self.clock = pygame.time.Clock()
                self.FPS = 100    
                self.font = pygame.font.SysFont("Times New Roman", 30, bold=True)

            def draw_background(self):
                BLACK = (0, 0, 0)
                self.screen.fill(BLACK)
                background = pygame.image.load("sprites/background.png").convert_alpha()
                background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
                self.screen.blit(background, (0, 0))
            
            def draw_new_frame(self):
                pygame.display.flip()
                self.clock.tick(self.FPS)

            def draw_object(self, obj):
                self.screen.blit(obj.image, (obj.x, obj.y))

            def draw_result(self, win):

                YELLOW = (255, 255, 0)
                if win:
                    text = self.font.render("YOU WON!! YOU THE BEST!!", 1, YELLOW)
                    self.screen.blit(text, (50, 250))
                else:
                    text = self.font.render("GAME OVER!!", 1, YELLOW)
                    self.screen.blit(text, (150, 250))

            def is_quit(self):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return True
                return False

            def start(self):
                trau = Player(100, 250)
                door = Door(375, 20)

                robots = [
                    Robot(100, 400, 5, 0, "sprites/robot1.png"),
                    Robot(300, 300, 0, 5, "sprites/robot2.png"),
                    Robot(200, 200, 10, 2, "sprites/robot3.png"),
                    Robot(100, 100, -2, -5, "sprites/robot4.png")
                ]

                end_game = False
                is_won = False

                running = True
                while running:
                    if self.is_quit():
                        running = False

                    self.draw_background()
                    
                    if not end_game:
                        pressed = pygame.key.get_pressed()
                        if pressed[pygame.K_UP]:    trau.move( 0, -5)
                        if pressed[pygame.K_DOWN]:  trau.move( 0,  5)
                        if pressed[pygame.K_LEFT]:  trau.move(-5,  0)
                        if pressed[pygame.K_RIGHT]: trau.move( 5,  0)

                        if trau.touch(door):
                            print("YOU WON!! YOU THE BEST!!")
                            end_game = True
                            is_won = True

                        for robot in robots:
                            robot.move()

                            if trau.touch(robot):
                                print("GAME OVER!!")
                                end_game = True
                                is_won = False
                    
                    self.draw_object(trau)
                    for robot in robots:
                        self.draw_object(robot)
                    self.draw_object(door)
                    
                    if end_game:
                        self.draw_result(is_won)

                    self.draw_new_frame()
                    
                pygame.quit()

        game = Game()
        game.start()
    else:
        print("You lost")
        setup_gameover_screen()

# Gọi hàm thiết lập màn hình    
# setup_main_screen()

# Chơi nhạc
play_music("music.wav")

# Gọi hàm thiết lập menu
setup_menu_screen()
# Bắt đầu game chính
# start_main_game()