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
    
    ██████╗  █████╗  ███╗   ███╗███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
    ██║  ███╗███████║██╔████╔██║█████╗      ███████╗   ██║   ███████║██████╔╝   ██║   
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   
     ██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                            
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
        
    friends = selected

# ============ 5. 게임 리스트 출력 ============ #
def show_game_list():
    print(r'''
┏━━━━━━━━━━━ 오늘의 Alcohol GAME 🍺 ━━━━━━━━━━━┓
  1. 사랑의 총알 게임
  2. 좋아 게임
  3. 369 게임
  4. 더 게임 오브데스
  5. 시장에 가면 게임
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')

def print_nice_game_banner():
    print(r'''
███╗   ██╗██╗ ██████╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
████╗  ██║██║██╔════╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██╔██╗ ██║██║██║     █████╗      ██║  ███╗███████║██╔████╔██║█████╗  
██║╚██╗██║██║██║     ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║ ╚████║██║╚██████╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
''')

def main_game_loop():
    print_nice_game_banner()

    show_game_list()

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
    first_turn = True  # 첫 번째 턴 여부 플래그

    while True:
        alive_players = [p for p in players if player_status[p]['alive']]
        if len(alive_players) == 1:
            print(f"\n🎉 {alive_players[0]}님이 마지막까지 살아남았습니다! 게임 종료! 🏆")
            break

        current_player = alive_players[turn_index % len(alive_players)]

        if not first_turn:
            print_game_status()

        game_number = select_game(current_player, first_turn=first_turn)
        

        print(f"\n🎮 {current_player}님이 {game_number}번 게임을 선택했습니다!\n")

        died = play_game(game_number, current_player)
        if died:
            print(f"\n💀 누군가 사망하여 해당 게임은 종료됩니다. 다음 플레이어로 넘어갑니다.\n")
            print("\n그만하고 싶으면 'exit', 계속하려면 아무 키나 누르세요!")
            cont = input("계속 진행할까요? : ").strip().lower()
            if cont == 'exit':
                print("🍺 다음에 또 만나요~ 👋")
                exit()  # 전체 프로그램 종료
        else:
            print("\n🎮 게임이 종료되었습니다. 다음 플레이어로 넘어갑니다...\n")

        for p in player_status:
            player_status[p]['alive'] = True

        turn_index += 1
        first_turn = False  # 첫 턴 끝났다고 표시


def select_game(player, first_turn=False):
    if player == name:

        while True:
            choice = input("플레이할 게임 번호를 입력하세요 (1~5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return int(choice)
            else:
                print("⚠️ 1~5 숫자 중 하나를 골라주세요.")
    else:
        return random.randint(1, 5)


def play_game(game_number, current_player):
    alive_players = [p for p, v in player_status.items() if v['alive']]

    if game_number == 1:
        print("\n💘 사랑의 총알 게임 시작! 💘")
        directions = ['왼쪽', '오른쪽', '앞', '뒤']
        players = [p for p in player_status if player_status[p]['alive']]
        random.shuffle(players)
        players.insert(0, name)
        turn = 0

        is_first_turn = True
        while True:
            current_player = players[turn % len(players)]
            expected = random.choice(directions)

            print(f"\n🎯 {current_player} 차례입니다!")
            print("사랑의 총알~💘")

            if is_first_turn:
                answer = input(f"👉 {current_player}!! 방향을 외쳐주세요! (왼쪽/오른쪽/앞/뒤): ").strip()
                is_first_turn = False
            else:
                fail = random.random() < 0.15
                answer = expected if not fail else random.choice(directions)
                print(f"🤖 {current_player}: {answer}")


            if answer != expected:
                print(f"❌ 틀렸습니다! 정답은 '{expected}'! 벌주~ 🍺")
                mock_loser(current_player)
                drink(current_player)
                return True
            else:
                print("✅ 통과!")
                turn += 1

    elif game_number == 2:
        print("\n😊 좋아~ 좋아~ 좋아~ 게임 시작! 😊")
        players = [p for p in player_status if player_status[p]['alive']]
        random.shuffle(players)
        turn = 0

        while True:
            current_player = players[turn % len(players)]
            print(f"\n🎯 {current_player} 차례입니다!")

            if current_player == name:
                user_input = input("👉 '좋아'를 외치세요! : ").strip()
                if user_input != "좋아":
                    print("❌ 틀렸습니다! '좋아'라고 외쳐야 해요! 벌주~ 🍺")
                    mock_loser(current_player)
                    drink(current_player)
                    return True
            else:
                fail = random.random() < 0.15
                said = "좋아" if not fail else random.choice(["조아", "아니야", "", "굿"])
                print(f"🤖 {current_player}: {said}")
                if said != "좋아":
                    print("❌ 틀렸습니다! 벌주~ 🍺")
                    mock_loser(current_player)
                    drink(current_player)
                    return True

            print("✅ 통과!")
            turn += 1


    elif game_number == 3:
        # 369 게임
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
                    return drink(current_player)
            else:
                fail_chance = 0.05
                fail = random.random() < fail_chance
                said = correct if not fail else ("짝" if correct != "짝" else str(current_number))
                print(f"🤖 {current_player}: {said}")
                if said != correct:
                    print(f"❌ 오답! 정답은 '{correct}'야!")
                    mock_loser(current_player)
                    return drink(current_player)

            current_number += 1
            current_index += 1

    elif game_number == 4:
        #더 게임 오브 데스
        
            print(r'''
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃        ☠ 더 게임 오브 데스 ☠        ┃
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    누가 누구를 노렸는지, 다 공개합니다! 😈
                    ''')

            players = [p for p in player_status if player_status[p]['alive']]
            vote_targets = {}

            print("🔎 각 플레이어가 누굴 지목할지 정합니다!")
            for p in players:
                available_targets = [t for t in players if t != p]
                if not available_targets:
                    available_targets = [p]
                target = random.choice(available_targets)
                vote_targets[p] = target
                print(f"👉 {p} → {target}")

            hops_input = input(f"\n{current_player}님, 숫자를 외쳐주세요 (기본 3): ").strip()
            try:
                hops = int(hops_input)
            except:
                hops = 3

            print(f"\n📣 숫자 {hops}만큼 이동을 시작합니다!\n")

            current = current_player
            path = [current]
            for _ in range(hops):
                current = vote_targets.get(current, current)
                path.append(current)

            print("🧭 이동 경로:")
            print(" ➡️  " + " → ".join(path))

            loser = current
            print(f"\n💀 최종 도착지: {loser}님! 벌주 당첨~ 🍻")

            died = drink(loser)
            return died


    elif game_number == 5:
        print("\n🛒 시장에 가면~ 게임 시작!")
        item_pool = ['사과', '배', '수박', '감자', '고등어', '김치', '콩나물', '생선', '고추장', '호박', '꽃', '나물', '바지']
        used_items = []
        turn = 0
        players = [p for p in player_status if player_status[p]['alive']]
        random.shuffle(players)    

        while True:
            current_player = players[turn % len(players)]
            print(f"\n🎯 {current_player} 차례입니다!")

            if current_player == name:
                print("지금까지 나온 물건:", ", ".join(used_items) if used_items else "(없음)")
                answer = input("👉 시장에 가면 무엇을 사요? (전체 순서대로 입력, 쉼표로 구분): ").strip()
                items = [i.strip() for i in answer.split(",")]
            else:
                if random.random() < 0.3:
                    available = [item for item in item_pool if item not in used_items]
                    if not available:
                        print(f"{current_player}은(는) 더 이상 살 게 없어요~ 자동 탈락!")
                        mock_loser(current_player)
                        drink(current_player)
                        return True
                    new_item = random.choice(available)
                    items = used_items + [new_item]
                    print(f"{current_player} ▶ 시장에 가면 {'도 사고, '.join(items)}도 사고")
                else:
                    items = used_items.copy()
                    random.shuffle(items)
                    print(f"{current_player} ▶ 시장에 가면 {'도 사고, '.join(items)}도 사고")

            if items[:len(used_items)] != used_items:
                print(f"❌ {current_player} 틀렸습니다! 벌주~ 🍺")
                mock_loser(current_player)
                drink(current_player)
                return True

            if len(items) != len(set(items)):
                print(f"❌ 중복된 물건을 말했어요! 벌주~ 🍺")
                mock_loser(current_player)
                drink(current_player)
                return True

            if len(items) <= len(used_items):
                print(f"❌ 새로운 물건을 추가하지 않았어요! 벌주~ 🍺")
                mock_loser(current_player)
                drink(current_player)
                return True

            used_items = items
            print("✅ 통과!")
            turn += 1


    else:
        print("아직 구현되지 않은 게임입니다.")
        return False


def drink(pname):
    amount = random.randint(1, 3)
    player_status[pname]['drunk'] += amount

    limit = player_status[pname]['limit']
    drunk = player_status[pname]['drunk']
    remain = max(0, limit - drunk)

    print_game_status()

    if drunk >= limit:
        player_status[pname]['alive'] = False
        print_game_over(pname)
        exit()

    return False  # 수정: 아직 살아있으면 False 반환하여 게임 계속 진행 가능


def print_game_over(name):
    print(r'''
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║ 
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝  
                                                                         
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
    
