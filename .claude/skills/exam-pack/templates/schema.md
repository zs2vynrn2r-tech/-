# Output schema (JSON, UTF-8). Write valid JSON only.

## guide.json — 기말 대비 교재
{
  "meta": {
    "subject": "상법", "kicker": "Final", "title2": "기말고사 대비",
    "term": "2026-2학기 · 서지민 교수님",
    "info": [["범위","..."],["형식","..."],["시험","..."],["근거","..."]]
  },
  "units": [
    {
      "no": "9",                         // unit number shown big
      "title": "상사매매 보충 · 유가증권",
      "pages": "교재 292~293쪽",           // shown under unit title
      "sections": [
        {
          "id": "9-1", "title": "...",
          "keywords": "키워드 · 키워드 · 키워드",   // one line, for unit overview table
          "frame": [["출발","..."],["그런데","..."],["그래서","..."],["비교","..."]],   // 3-5 rows, 왜 필요한가 story
          "list": [ {"id":"L1","tag":"필기|뜻|조문|판례|주의|비교|구조","text":"..."} ],  // 8-14 items. **bold** allowed. tag 필기 = student's handwriting on the page
          "terms": [ {"q":"설명","L":"L1","a":"용어","diff":1} ],   // 용어 적기, 5-7
          "ox":    [ {"q":"문장","L":"L2 · L3","a":"O","why":"해설 1-2문장","diff":2} ], // 7-10
          "cases": [ {"q":"사례/객관식 지문","options":["①..","②..","③..","④..","⑤.."],"L":"L4","a":"③","why":"정답 근거 + 오답 포인트 (①…⑤ 짧게)","diff":3} ] // 3-5; options may be omitted for 서술형 짧은답 (then a = 답 텍스트)
        }
      ]
    }
  ]
}
Problem numbering is automatic per section (terms → ox → cases, 01..). diff = 1..3 (●○○).
"why" for terms optional (short).

## mock.json — 기말 모의고사
{
  "meta": {"subject":"상법","kicker":"Mock Test","title2":"모의고사","term":"2026-2학기 · 서지민 교수님",
           "info":[["범위","..."],["형식","..."],["시험","..."]]},
  "exams": [
    {"id":"M-1","title":"모의고사 1회",
     "questions":[
       {"unit":"9단원","type":"ox","stem":"...","a":"O","why":"..."},
       {"unit":"10단원","type":"mc","stem":"...","options":["...","...","...","...","..."],"a":"③","why":"정답 근거. ① … ② … (오답 이유 짧게)"}
     ]}
  ]
}
Each exam: exactly 30 questions; first 10 OX, then 20 객관식(5지선다), like the midterm mock. Mix 판례 questions in.
Tone: 해설 in friendly 해요체 ("~예요", "~해요"), like the samples.
