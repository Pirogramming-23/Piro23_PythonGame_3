import random

friends = []
name = ""
player_status = {}

def mock_loser(name):
    messages = [
        f"🤣 {name}, 그걸 틀려? 초딩도 맞추겠다~ 🍶",
        f"💀 {name}, 아니 대체 어디서 '짝'을 놓친 거야? 뇌세포 알코올에 다 녹았나~?",
        f"🐢 {name}, 속도도 느린데 정답도 느려~",
        f"📉 {name}의 지능 지수 급강하! 지금은 바닥을 뚫는 중... 🕳️",
        f"🫠 {name}, 망신살이 전국구야~",
        f"👋 {name}님 탈락입니다~ 보내드릴게요~ 버스 여기요~ 🚌💨",
        f"🤡 {name}, 진심으로 박수... 짝짝짝 대신... '짤'~ 🫴",
        f"🙄 {name}, 아 그건 너무했다 진짜ㅋㅋㅋ 실화냐?ㅋㅋ",
        f"🫳 {name}, 게임은 실력으로~ 술은 책임지고~ 잔 드세요~ 🍷",
        f"👻 {name}, 이제 유령으로 관전하시겠어요? 히히히~"
    ]
    print(random.choice(messages))
    

# ============ 1. 게임 타이틀 ============ #
def print_game_title():
    print(r'''
     _    _       _     _       _    _       _     _       _    _       _     _       _    _       _     _       _    _
    (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)
   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \
   \________/   \________/   \________/   \________/   \________/   \________/   \________/   \________/   \________/   \________/

      _____  _        ___     __     __   ___    _         ___    _       ___   ___   ___   ___   ___
     |  __ \| |      / _ \    \ \   / /  / _ \  | |       / _ \  | |     / _ \ |  _ \ |  _ \ |  _ \ |  _ \
     | |__) | |     / /_\ \    \ \_/ /  / /_\ \ | |      / /_\ \ | |    / /_\ \| |_| || |_| || |_| || |_| |
     |  ___/| |     |  _  |     \   /   |  _  | | |      |  _  | | |    |  _  ||  __/ |  __/ |  __/ |    /
     | |    | |____ | | | |      | |    | | | | | |____  | | | | | |____| | | || |    | |    | |    | |\ \
     |_|    |______||_| |_|      |_|    |_| |_| |______| |_| |_| |______|_| |_||_|    |_|    |_|    |_| \_\

     _    _       _     _       _    _       _     _       _    _       _     _       _    _       _     _       _    _
    (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)     (o)--(o)
   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \   /.______. \
   \________/   \________/   \________/   \________/   \________/   \________/   \________/   \________/   \________/   \________/

    ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ🍗 안주 먹을 🍺 시간이 ❌ 없어요 ❌ 마시면서 배우는 술게임🐤🏠 ───⊂(・﹏・⊂)
    ''')

# ============ 2. 게임 시작 여부 + 이름 ============ #
def ask_to_start():
    
    global name
    answer = input("게임을 진행할까요? (y/n) : ").strip().lower()

    if answer == 'y':
        name = input("오늘 거하게 취해볼 당신의 이름은? : ")
        print(f"\n환영합니다, {name}님! 🍻\n")
        return True
    elif answer == 'n':
        print("다음에 만나요! 👋")
        return False
    else:
        print("잘못된 입력입니다. y 또는 n으로 입력해주세요.")
        return ask_to_start()

# ============ 3. 주량 선택 ============ #
def choose_drink_level():
    print(r'''
🍺 소주 기준 당신의 주량은? 🍺
╭──────────────────────────────────────────╮
🍶 1. 소주 반병 (2잔)
🍶 2. 소주 반병에서 한병 (4잔)
🍶 3. 소주 한병에서 한병 반 (6잔)
🍶 4. 소주 한병 반에서 두병 (8잔)
🍶 5. 소주 두병 이상 (10잔 이상)
╰──────────────────────────────────────────╯
''')

    while True:
        choice = input("당신의 치사량(주량)은 얼마만큼인가요? (1~5를 선택해주세요) : ")
        if choice in ['1', '2', '3', '4', '5']:
            drink_table = { '1': 2, '2': 4, '3': 6, '4': 8, '5': 10 }
            print(f"\n좋아요! 선택한 주량은 {drink_table[choice]}잔입니다. 🍶\n")
            return drink_table[choice]
        else:
            print("⚠️ 잘못된 입력입니다. 1~5 사이 숫자를 입력해주세요.")

# ============ 4. 친구 초대 + 상태 요약 ============ #
def invite_friends():
    
    global friends
    
    characters = {
        "민지": 2,
        "가람": 4,
        "보윤": 6,
        "유석": 8,
        "정민": 10
    }

    print("함께 취할 친구들을 몇 명 초대할까요? (최대 3명)")

    while True:
        try:
            num = int(input("초대할 인원 수 (1~3): "))
            if 1 <= num <= 3:
                break
            else:
                print("⚠️ 1~3명까지만 초대할 수 있습니다.")
        except ValueError:
            print("⚠️ 숫자만 입력해주세요.")

    selected = random.sample(list(characters.items()), num)
    print("\n오늘 함께 취할 친구들입니다!")
    for name, limit in selected:
        print(f"🍺 오늘 함께 취할 친구는 {name}입니다! (치사량: {limit}잔)")

    print("\n현재 상태 요약 🔻")
    for name, limit in selected:
        print(f"{name}은(는) 지금까지 ⚠️ 마신 잔 수: 0 / 치사량까지: {limit}잔")
        
    friends = random.sample(list(characters.items()), num)

# ============ 5. 게임 리스트 출력 ============ #
def show_game_list():
    print(r'''
┏━━━━━━━━━━━ 오늘의 Alcohol GAME 🍺 ━━━━━━━━━━━┓
  1. 사망의 총알 게임
  2. 쪼야 게임
  3. 369 게임
  4. 두부 게임
  5. 초성 게임
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')


def main_game_loop():
    players = [name] + [friend_name for friend_name, _ in friends]
    friend_limits = dict(friends)

    global player_status
    player_status = {}
    for p in players:
        limit = my_drink_limit if p == name else friend_limits.get(p, 3)
        player_status[p] = {
            'drunk': 0,
            'limit': limit,
            'alive': True
        }

    turn_index = 0

    while True:
        alive_players = [p for p in players if player_status[p]['alive']]
        if len(alive_players) == 1:
            print(f"\n🎉 {alive_players[0]}님이 마지막까지 살아남았습니다! 게임 종료! 🏆")
            break

        current_player = alive_players[turn_index % len(alive_players)]

        print_game_status()

        if current_player == name:
            print("\n그만하고 싶으면 'exit', 계속하려면 아무 키나 누르세요!")
            cont = input("계속 진행할까요? : ").strip().lower()
            if cont == 'exit':
                print("🍺 다음에 또 만나요~ 👋")
                break

        game_number = select_game(current_player)
        print(f"\n🎮 {current_player}님이 {game_number}번 게임을 선택했습니다!\n")

        died = play_game(game_number, current_player)  
        if died:
            print(f"\n💀 누군가 사망하여 해당 게임은 종료됩니다. 다음 플레이어로 넘어갑니다.\n")
        else:
            print("\n🎮 게임이 종료되었습니다. 다음 플레이어로 넘어갑니다...\n")

        turn_index += 1

def select_game(player):
    if player == name:
        show_game_list()
        while True:
            choice = input("플레이할 게임 번호를 입력하세요 (1~5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return int(choice)
            else:
                print("⚠️ 1~5 숫자 중 하나를 골라주세요.")
    else:
        return random.randint(1, 5)

# ============ 6. 게임 선택 및 실행 ============ #
def select_and_play_game():
    while True:
        choice = input("플레이할 게임 번호를 입력하세요 (1~5): ").strip()
        if choice == '1':
            # 1번 게임 코드 작성: 사망의 총알 게임
            print("사망의 총알 게임 시작! (여기에 게임 코드 작성)")
            break
        elif choice == '2':
            # 2번 게임 코드 작성: 쪼야 게임
            print("쪼야 게임 시작! (여기에 게임 코드 작성)")
            break
        elif choice == '3':
            break
               
        elif choice == '4':
            # 4번 게임 코드 작성: 두부 게임
            print("두부 게임 시작! (여기에 게임 코드 작성)")
            break
        elif choice == '5':
            # 5번 게임 코드 작성: 초성 게임
            print("초성 게임 시작! (여기에 게임 코드 작성)")
            break
        else:
            print("⚠️ 1부터 5 사이의 숫자를 입력해주세요.")

def play_369_game(current_player):
    print("\n삼 육구~ 3 6 9~! 삼 육구~ 3 6 9~!\n")
    print("🎉 369 게임을 시작합니다! 숫자에 3,6,9가 들어가면 '짝'이라고 말하세요.\n")

    players = [name] + [friend_name for friend_name, _ in friends]
    current_number = 1
    current_index = 0

    while True:
        alive = [p for p in players if player_status[p]['alive']]
        if len(alive) == 1:
            print(f"\n🎉 {alive[0]}님이 마지막까지 살아남았습니다! 🏆")
            return True

        current_player = alive[current_index % len(alive)]
        clap = sum(1 for digit in str(current_number) if digit in '369')
        correct = "짝" * clap if clap > 0 else str(current_number)

        if current_player == name:
            user_input = input(f"👉 {name}!! 너 차례!! ").strip()
            if user_input != correct:
                print(f"❌ 오답! 정답은 '{correct}'야!")
                mock_loser(current_player)
                died = drink(current_player)
                if died:
                    return False
        else:
            fail_chance = 0.05
            fail = random.random() < fail_chance
            said = correct if not fail else ("짝" if correct != "짝" else str(current_number))
            print(f"🤖 {current_player}: {said}")
            if said != correct:
                print(f"❌ 오답! 정답은 '{correct}'야!")
                mock_loser(current_player)
                died = drink(current_player)
                if died:
                    return False

        current_number += 1
        current_index += 1

        alive_now = [p for p in players if player_status[p]['alive']]
        if len(alive_now) == 1:
            print(f"\n🎉 {alive_now[0]}님이 마지막까지 살아남았습니다! 🏆")
            return True
def play_game(game_number, current_player):
    # 여기서 모든 플레이어가 함께 게임을 하도록 변경
    return play_game_for_all(game_number)

def play_game_for_all(game_number):
    alive_players = [p for p, v in player_status.items() if v['alive']]

    if game_number == 3:
        current_number = 1
        current_index = 0
        while True:
            alive_now = [p for p in alive_players if player_status[p]['alive']]
            if len(alive_now) == 1:
                print(f"\n🎉 {alive_now[0]}님이 마지막까지 살아남았습니다! 🏆")
                return True

            current_player = alive_now[current_index % len(alive_now)]
            clap = sum(1 for digit in str(current_number) if digit in '369')
            correct = "짝" * clap if clap > 0 else str(current_number)

            if current_player == name:
                user_input = input(f"👉 {name}!! 너 차례!!: ").strip()
                if user_input != correct:
                    print(f"❌ 오답! 정답은 '{correct}'야!")
                    mock_loser(current_player)
                    died = drink(current_player)
                    return True
            else:
                fail_chance = 0.05
                fail = random.random() < fail_chance
                said = correct if not fail else ("짝" if correct != "짝" else str(current_number))
                print(f"🤖 {current_player}: {said}")
                if said != correct:
                    print(f"❌ 오답! 정답은 '{correct}'야!")
                    mock_loser(current_player)
                    died = drink(current_player)
                    return True

            current_number += 1
            current_index += 1

    else:
        print("아직 구현되지 않은 게임입니다.")
        return False


def drink(pname):
    amount = random.randint(1, 3)
    player_status[pname]['drunk'] += amount

    limit = player_status[pname]['limit']
    drunk = player_status[pname]['drunk']
    remain = max(0, limit - drunk)

    print(f"\n{pname}(은)는 지금까지 {drunk}🍺! 치사량까지 {remain}")

    if drunk >= limit:
        player_status[pname]['alive'] = False
        print_game_over(pname)
        return True

    return False  # 수정: 아직 살아있으면 False 반환하여 게임 계속 진행 가능


def print_game_over(name):
    print(r'''
   ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▓    ▓█████ ▒██   ██▒ ▓█████  ██▀███  
  ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██▒    ▓█   ▀ ▒▒ █ █ ▒░ ▓█   ▀ ▓██ ▒ ██▒
 ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒▒██░    ▒███   ░░  █   ░ ▒███   ▓██ ░▄█ ▒
 ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░▒██░    ▒▓█  ▄  ░ █ █ ▒  ▒▓█  ▄ ▒██▀▀█▄  
 ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░░██████▒░▒████▒▒██▒ ▒██▒░▒████▒░██▓ ▒██▒
  ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░ ░ ░ ▒  ░ ░ ░  ░░░   ░▒ ░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒    ░ ░      ░    ░    ░     ░     ░░   ░ 
       ░       ░  ░       ░      ░  ░       ░ ░      ░  ░   ░  ░ ░    ░     ░  ░   ░     
                                                                                        
    ''')
    print(f"\n💀 {name}님은 치사량을 초과해 GAME OVER입니다... 🪦\n")


def print_game_status():
    print("\n" + "~" * 60)
    for pname, info in player_status.items():
        drunk = info['drunk']
        limit = info['limit']
        remain = max(0, limit - drunk)
        print(f"{pname} (은)는  지금까지  {drunk}🍺! 치사량까지 {remain}")
    print("~" * 60)

# ============ 전체 실행 흐름 ============ #
print_game_title()
if ask_to_start():
    my_drink_limit = choose_drink_level()
    invite_friends()
    main_game_loop()
