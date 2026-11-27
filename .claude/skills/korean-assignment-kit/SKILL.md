---
name: korean-assignment-kit
description: 한국 대학 과제(학술적 글쓰기, 토론 자료)를 처리하는 도구 모음. 교수님 한글(.hwp) 양식에 글을 채우고, 진짜 각주와 클릭 가능한 출처 링크를 넣고, PDF로 바꾸고, 신문 기사·판례 출처를 원문으로 확인하고, 찬성·반대 토론 자료를 보기 좋은 PDF로 만든다. 사용자가 한글 파일, 각주, 참고문헌, 기사 출처 확인, 토론 입론·반론, "보기 쉽게 PDF"를 말할 때 쓴다.
---

# 한국어 과제 도구 모음

이전 과제(플랫폼 노동자 학술적 글쓰기, 근로자 추정제 토론)에서 만든 코드와 절차다. 새로 짜지 말고 아래 스크립트를 그대로 쓴다. 스크립트는 `<skill>/scripts/`, 서식은 `<skill>/templates/`.

## 사용자 규칙 (반드시 지킴)

- **각주 형식**: 본문 문장 안에 기사 제목을 넣는다. `「기사 제목」에 따르면, …` 또는 `…라고 「기사 제목」에서 전하고 있다.` 그리고 문장 끝에 진짜 각주(페이지 아래). 판례·법령은 본문에 이름만, 각주는 정식 표기.
- **각주·참고문헌 표기**: `저자, "기사명", 매체명, 게재일., URL (검색일: YYYY.MM.DD.)`. 판례: `대법원 2024. 7. 25. 선고 2024두32973 판결.` 같은 기사 반복은 `저자, 앞의 기사.`
- **분량**: "4000자 내외(공백 포함)"는 **본문 기준**(제목·각주·참고문헌 제외, 장 제목 포함). 늘리거나 줄일 때 확인된 사실만 쓰고, 줄일 땐 반복·과장 문장부터.
- **출처 원칙**: 원문을 직접 연 사실만 단정한다. 검색 요약으로만 본 사실은 `S`(미확인)로 표시하고 사용자에게 알린다. 숫자를 지어내지 않는다.
- **문체**: 대학 1학년이 쓴 평범한 학술문. 과장 표현("방패", "울타리", "외주화에 불과", "~임은 분명하다") 금지. AI 판독기를 피하도록 다듬는 작업은 하지 않는다.
- **사용자가 고친 파일을 받으면** 고친 내용은 그대로 두고, 바뀐 곳을 먼저 표로 보고한 뒤 요청한 것만 바꾼다. 오류는 "고친 것"과 "확인만 할 것"을 나눠 보고한다.
- 결과물은 .hwp와 예비용 .hwpx를 함께 준다(.hwp 저장은 라이브러리가 실험 단계).

## 1. 출처 원문 확인

1. `WebSearch`로 기사 찾기 (요약은 틀릴 수 있음: 날짜·숫자·연도가 자주 어긋난다).
2. 기사 사이트가 네트워크 허용 목록에 없으면 `get_environment` 후 `update_environment`로 그 호스트만 추가(사용자 승인). 이미 허용된 주요 매체: 한국경제, 매일노동뉴스, 서울신문(m.), 파이낸셜뉴스, 아시아경제(view.), 노동법률, 세계일보, 한국일보, 경향신문, 국가법령정보센터, CEO스코어데일리(m.), 데일리안.
3. `curl -sL -A 'Mozilla/5.0' URL -o a.html` 후:
   - 제목·날짜·기자: `python3 -I <skill>/scripts/article_meta.py a.html`
   - 본문에서 필요한 줄: html 태그 제거 후 키워드로 grep (EUC-KR 사이트는 `iconv -f cp949 -t utf-8`).
4. WebFetch 도구는 이 환경에서 DNS 실패가 잦다. curl을 쓴다.

## 2. 교수님 한글 양식에 글 채우기

라이브러리: `uv pip install --system -q python-hwpx` (import 이름 `hwpx`). 업로드된 .hwp 양식을 그대로 열 수 있다(손실 없음).

내용 파일(JSON):
```json
{"cells": [[0,1,"OO학부    (학번) 000    (성명) 홍길동"], [1,1,"OOO 교수님"], [1,3,"분반"]],
 "paras": [
   {"style":"HEADING_1","text":"제목","fns":[]},
   {"style":"HEADING_2","text":"Ⅰ. 서론","fns":[]},
   {"style":"NORMAL_TEXT","text":"본문 문장.","fns":[[5,"각주 내용"]]},
   {"style":"HEADING_2","text":"참고문헌","fns":[]},
   {"style":"NORMAL_TEXT","text":"법령·판례","fns":[]}
 ]}
```
- `fns`의 숫자는 각주를 붙일 글자 위치(그 글자 뒤). 본문 문자열 안에 `{1}` 같은 표시를 넣고 파이썬으로 위치를 계산해 만들면 편하다.
- HEADING_1=제목(가운데 15pt 굵게), HEADING_2/3=장 제목(13pt 굵게), 참고문헌 이후 문단은 왼쪽 정렬.

실행:
```bash
python3 -I <skill>/scripts/build_hwp.py 양식.hwp content.json base.hwpx
python3 -I <skill>/scripts/link_hwp.py base.hwpx 결과.hwp 결과.hwpx   # 각주·참고문헌 URL을 클릭 가능한 링크로
```
- `build_hwp.py`는 양식의 본문 서식(charPr 20 = 휴먼명조 13pt, paraPr 1 = 양쪽 정렬 160%)을 쓰고 여백을 좌우 25·상하 15·머리말/꼬리말 15mm로 맞춘다. 양식이 다르면 `BODY_CHAR`, `BODY_PARA` 값과 여백을 그 양식에 맞게 확인한다.
- 사용자가 고친 .hwp에 링크만 넣을 땐 `link_hwp.py`만 그 파일에 바로 돌린다.
- 검증: 다시 열어 `[p.text for p in d.paragraphs]`, `d.notes.footnotes`, `d.refs.hyperlinks`, `d.page.margins()`, 표 셀을 확인하고 본문 글자 수를 센다.
- 문단 삭제: `p.element.getparent().remove(p.element)` 후 저장.

## 3. 한글 파일을 PDF로

이 컨테이너의 LibreOffice는 .hwp를 못 연다. 내용을 뽑아 LibreOffice(UNO)로 다시 짜서 PDF로 낸다.
```bash
apt-get install -y -q fonts-nanum   # 한글 명조 글꼴(나눔명조)
python3 -I <skill>/scripts/hwp_extract.py 결과.hwpx struct.json
soffice --headless --invisible --norestore --accept='socket,host=localhost,port=2002;urp;' &  # 몇 초 대기
python3 <skill>/scripts/hwp_to_pdf_uno.py struct.json /절대경로/out.pdf   # 경로에 한글 넣지 말 것(쓰기 오류). 끝나고 이름 변경
pkill -f 'soffice.*2002'
```
- 결과를 `pdftoppm -r 60 -png`로 이미지로 만들어 직접 보고 확인한다(링크 번짐, 들여쓰기 누락 등).
- 각주는 페이지 아래, 링크는 파란 밑줄로 클릭 가능.

## 4. 토론 자료 (찬성·반대 입론·반론)

1. 양측 사례를 검색하고 **사실 목록(F1~Fn, V/S 표시)**을 만든다. 반대 측 근거를 일부러 찾아 균형을 맞춘다. 형식은 `templates/debate_brief_example.md`.
2. `/67`: 같은 brief로 6개 에이전트(최소, 최대, 핵심 쟁점, 토론대회 형식, 오류 사냥, 상대 사례 뒤집기)를 동시에 돌리고, 각자 내부에서 "상대 팀이 되어 공격 → 수정"을 하게 한다. 7번째가 채점·합성.
3. 맞대결: 찬성 팀·반대 팀 에이전트가 합성본의 상대 측을 공격(오류 이름 + 인용 + F 근거) → 정리 에이전트가 반영하고 "맞대결에서 드러난 허점" 표 추가.
4. 산출물 섹션: 논제·정의 / 찬성 입론 / 반대 입론 / 찬성 반론 / 반대 반론(상대 주장 → 허점(오류명) → 재반박) / 교차조사 Q&A / 약점과 방어 / 토론 전 확인할 사실 / 맞대결 허점 / 부록 사실 목록.
5. 보기 쉬운 PDF:
```bash
python3 -I <skill>/scripts/debate_pdf_html.py <작업폴더>   # 작업폴더에 final2.md, brief.md, style.css(templates/debate_style.css 복사) 필요 → pretty.html
node <skill>/scripts/html_to_pdf.js <작업폴더>/pretty.html out.pdf   # Playwright, A4, 쪽번호
```
   첫 장은 한 장 요약(양측 3줄, 결정타 질문, 하지 말 것)을 손으로 써서 넣는다(`debate_pdf_html.py`의 cover 부분 수정). 찬성=파랑, 반대=주황빨강, 반론=카드, 교차조사=표, `(F7)`=회색 배지, `·S`=주황.
6. 구글 문서로 줄 땐 markdown→HTML 변환 전에 **목록 앞에 빈 줄**을 넣는다(안 그러면 목록이 한 문단으로 뭉친다).

## 자주 걸린 문제

- PDF(크롬 인쇄본)에서 `pdftotext`로 글을 뽑으면 문장부호 위치가 뒤섞인다 → `pdftoppm -r 100`으로 페이지 이미지를 보고 옮겨 적는다.
- 같은 각주 번호가 두 번 나오면 두 번째는 `앞의 기사` 각주로 분리한다.
- `rm -rf 디렉터리/*` 같은 삭제는 안전 검사에 막힌다 → 다른 파일 이름으로 새로 쓴다.
- 검색 요약의 수치·연도는 자주 틀린다(예: 산재 신청 2,961→15,028은 2020→2024, 15,804는 2025년 다른 집계). 반드시 원문 확인.
- 구글 문서 각주는 Docs API로 `createFootnote` 후 `insertText`(segmentId) + 첫 공백 삭제. 큰 문서 `read_doc` 결과는 파일로 저장되니 python으로 읽는다.
