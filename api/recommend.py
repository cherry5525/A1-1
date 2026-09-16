from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일에서 API 키 불러오기
load_dotenv()

# OpenAI 연결하기
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://copa.codyssey.kr/v1"   # 👈 이 줄 추가!
)

# Flask 앱(웹 서버) 만들기
app = Flask(__name__)

# 식단 추천 요청을 처리하는 곳
@app.route("/api/recommend", methods=["POST"])
def recommend():
    # 1. 사용자가 보낸 정보 받기
    data = request.json
    gender = data["gender"]
    age = data["age"]
    period = data["period"]
    goal = data["goal"]
    food = data["food"]
    allergy = data.get('allergy')
    height = data.get('height') # 없으면 None
    weight = data.get('weight')

# 프롬프트 조립 (있을 때만 추가!)
    body_info = ""
    if height and weight:
        body_info = f"키는 {height}cm, 몸무게는 {weight}kg입니다. "
        # BMI 계산도 가능!
        bmi = round(float(weight) / ((float(height)/100) ** 2), 1)
        body_info += f"(BMI: {bmi}) "

        if bmi < 18.5:
            body_info += "저체중이니 건강한 증량 식단이 필요합니다. "
        elif bmi < 23:
            body_info += "정상 체중입니다. "
        elif bmi < 25:
            body_info += "과체중이니 균형 잡힌 식단이 좋습니다. "
        else:
            body_info += "체중 관리를 위한 식단이 필요합니다. "

 # 알레르기가 있을 때만 문장 만들기!
    if allergy:
        allergy_text = f"{allergy}에 알레르기가 있으니 이 재료는 반드시 빼주세요."
    else:
        allergy_text = ""

    # 2. AI에게 보낼 질문 만들기
    prompt = f"당신은 전문 영양사입니다. {gender}, {age}살이고, {period}일 동안 {goal}을(를) 목표로 해요. {food}을(를) 좋아합니다. {allergy_text} {body_info} 이 사람에게 맞는 식단을 추천해주세요."

    # 3. AI에게 질문 보내고 답변 받기
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # 4. AI의 답변 꺼내기
    result = response.choices[0].message.content

    # 5. 답변을 브라우저로 돌려주기
    return jsonify({"result": result})


