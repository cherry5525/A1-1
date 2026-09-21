# ===== 기본 데이터 (이전 미션 프롬프트 3개 이상) =====
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다...",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "매력적인 썸네일 이미지를 생성해주세요...",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다...",
        "category": "페르소나",
        "favorite": False
    },
]

categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# ===== 메뉴 출력 =====
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


# ===== 프롬프트 추가 =====
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    while title == "":
        title = input("제목을 입력하세요: ").strip()

    content = input("내용: ").strip()
    while content == "":
        content = input("내용을 입력하세요: ").strip()

    print("카테고리 선택:")
    for i, c in enumerate(categories, 1):
        print(f"{i}) {c}")
    choice = input("선택: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        category = categories[int(choice) - 1]
    else:
        category = choice  # 직접 입력

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("프롬프트가 추가되었습니다!")


# ===== 목록 출력 (브랜치에서 작업할 기능) =====
def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"\n총 {len(prompts)}개의 프롬프트")

