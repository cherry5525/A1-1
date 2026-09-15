# 🧞 MealGenie - AI 맞춤 식단 추천 서비스

성별, 나이, 목적에 맞는 **개인 맞춤 식단**을  
AI가 추천해주는 웹 서비스입니다! 🥗✨

---

## ✨ 주요 기능

- 🍽️ **개인 맞춤 식단 추천** - 성별, 나이, 목적 기반
- ⚠️ **알레르기 재료 자동 제외** - 안전한 식단 제공
- 📋 **결과 복사 기능** - 클릭 한 번으로 복사
- 💾 **입력값 자동 저장** - 새로고침해도 유지
- ⏳ **로딩 애니메이션** - 부드러운 사용자 경험

---

## 🛠️ 기술 스택

| 구분 | 기술 |
|------|------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask (Python) |
| AI | Codyssey API (GPT) |

---

## 🚀 실행 방법

### 1. 저장소 복제
```bash
git clone https://github.com/cherry5525@nate.com/MealGenie.git
cd MealGenie
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정
`.env` 파일을 만들고 API 키를 입력하세요:
```
OPENAI_API_KEY=your_api_key_here
```

### 4. 서버 실행
```bash
python recommend.py
```

### 5. 브라우저 접속
```
http://localhost:5000
```

---

## 📝 사용 방법

1. 성별, 나이, 기간을 입력해요 👤
2. 목적(다이어트, 벌크업 등)을 선택해요 🎯
3. 좋아하는 음식과 알레르기를 입력해요 🥗
4. **추천받기** 버튼 클릭! 🖱️
5. AI가 맞춤 식단을 추천해줘요! ✨

---

## 💚 만든 사람

- 프로젝트: MealGenie 🧞
- AI 식단 추천 서비스