import os
from openai import OpenAI
from dotenv import load_dotenv

from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage

load_dotenv()
client = OpenAI(
    api_key=os.environ["UPSTAGE_API_KEY"], base_url="https://api.upstage.ai/v1/solar"
)

foo = [
        ("system", "포춘 쿠키 문구를 생성해줘. 포춘 쿠키 문구는 한 줄이어야하고, 오타가 나면 안돼. 그리고 되도록이면 격식있는 문구였으면 좋겠어."),
        ("system", "아래는 포춘쿠키 문구 예시들이야"),
        ("system", "스스로에 대한 믿음이 당신을 자유롭게 할 것입니다"),
        ("system", "오늘 할 일을 내일로 미룰 줄 아는 여유를 가지세요"),
        ("system", "독서와 글쓰기가 당신의 인생을 더 나은 곳으로 이끌 것입니다"),
        ("system", "이웃의 불행을 모른 척하지 말고, 불의는 가능한 참지 마세요"),
        ("system", "고전을 통해 삶의 지혜를 얻을 것입니다."),
        ("system", "때론 상대에게 단호함을 보여주세요"),
        ("system", "기약 없는운보다 삶을 긍정적으로 바라보는 시선을 믿으세요"),
        ("system", "건강이 무엇보다 중요하다는 사실을 너무 늦게 깨닫지 마세요."),
        ("system", "태어난 건 우연이지만 운명을 사랑하는 건 필연입니다."),
        ("system", "인생은 지옥과 천국의 어디쯤에 있다는 걸 명심하세요"),
    ]

llm = ChatUpstage()
template = ChatPromptTemplate.from_messages(foo)
generator = template | llm | StrOutputParser()

def generate():
    return generator.invoke({"input": ""})