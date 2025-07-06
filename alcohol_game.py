import random
friends = []
name = ""

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
    answer = input("게임을 진행할까요? (y/n) : ").strip().lower()

    if answer == 'y':
        name = input("오늘 거하게 취해볼 당신의 이름은? : ")
        print(f"\n환영합니다, {name}님! 🍻\n")
        return name
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
        choice = input("당신의 **치사량(주량)**은 얼마만큼인가요? (1~5를 선택해주세요) : ")
        if choice in ['1', '2', '3', '4', '5']:
            drink_table = { '1': 2, '2': 4, '3': 6, '4': 8, '5': 10 }
            print(f"\n좋아요! 선택한 주량은 {drink_table[choice]}잔입니다. 🍶\n")
            return drink_table[choice]
        else:
            print("⚠️ 잘못된 입력입니다. 1~5 사이 숫자를 입력해주세요.")

# ============ 4. 친구 초대 + 상태 요약 ============ #
def invite_friends():
    characters = {
        "은서": 2,
        "하연": 6,
        "연서": 6,
        "예진": 8,
        "헌도": 10
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

    return selected
# ============ 5. 게임 리스트 출력 ============ #
def show_game_list():
    print(r'''
┏━━━━━━━━━━━ 오늘의 Alcohol GAME 🍺 ━━━━━━━━━━━┓
  1. 사망의 총알 게임
  2. 쪼야 게임
  3. 369 게임
  4. 두부 게임
  5. 시장에 가면 게임
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')

# ============ 6. 게임 선택 및 실행 ============ #
def select_and_play_game(name, friends):
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
            # 3번 게임 코드 작성: 369 게임
            print("369 게임 시작! (여기에 게임 코드 작성)")
            break
        elif choice == '4':
            # 4번 게임 코드 작성: 두부 게임
            print("두부 게임 시작! (여기에 게임 코드 작성)")
            break
        elif choice == '5':
            # 5번 게임 코드 작성: 초성 게임
            print("\n🛒 시장에 가면~ 게임 시작!")
            item_pool = ['사과', '배', '수박', '감자', '고등어', '김치', '콩나물', '생선', '고추장', '호박','꽃','나물','바지']
            used_items = []
            turn = 0
            players = [name] + [friend for friend, _ in friends]
            random.shuffle(players)    

            while True:
                current_player = players[turn % len(players)]
                print(f"\n🎯 {current_player} 차례입니다!")

                if current_player == name:
                    print("지금까지 나온 물건:", ", ".join(used_items) if used_items else "(없음)")
                    answer = input("👉 시장에 가면 무엇을 사요? (전체 순서대로 입력, 쉼표로 구분): ").strip()
                    items = [i.strip() for i in answer.split(",")]

                else:
                    # 컴퓨터 플레이어 - 일정 확률로 맞춤
                    if random.random() < 0.3:
                        # 정답 시: 기존 순서 + 새로운 아이템
                        available = [item for item in item_pool if item not in used_items]
                        if not available:
                            print(f"{current_player}은(는) 더 이상 살 게 없어요~ 자동 탈락!")
                            break
                        new_item = random.choice(available)
                        items = used_items + [new_item]
                        print(f"{current_player} ▶ 시장에 가면 {'도 사고, '.join(items)}도 사고")
                    else:
                        # 일부러 틀리기
                        items = used_items.copy()
                        random.shuffle(items)
                        print(f"{current_player} ▶ 시장에 가면 {'도 사고, '.join(items)}도 사고")

                # 정답 확인
                if items[:len(used_items)] != used_items:
                    print(f"❌ {current_player} 틀렸습니다! 벌주~ 🍺")
                    mock_loser(current_player)
                    break

                if len(items) != len(set(items)):
                    print(f"❌ 중복된 물건을 말했어요! 벌주~ 🍺")
                    mock_loser(current_player)
                    break

                if len(items) <= len(used_items):
                    print(f"❌ 새로운 물건을 추가하지 않았어요! 벌주~ 🍺")
                    mock_loser(current_player)
                    break

                used_items = items
                print("✅ 통과!")
                turn += 1

        else:
            print("⚠️ 1부터 5 사이의 숫자를 입력해주세요.")

# ============ 전체 실행 흐름 ============ #
print_game_title()
name = ask_to_start()
if name:
    choose_drink_level()
    friends = invite_friends()
    show_game_list()
    select_and_play_game(name, friends)
