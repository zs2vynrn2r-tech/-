# TASK BRIEF (identical for all six agents)

Make a Korean 상법 final-exam study guide (기말 대비 교재) and mock exam (모의고사) for a university student.

## Source (read ALL of it first)
/tmp/claude-0/-home-user--/1ac6a10d-142f-5ce7-847e-845b42b0175b/scratchpad/src/source.md
= transcription of textbook pp.292~313 (상행위법 총론: CIF/FOB 끝, 제3절 유가증권, 제4절 상호계산, 제5절 익명조합, 제6절 합자조합 앞부분) with the student's handwriting marked `> ✍ 필기:` and their underlines marked **bold**.

## Student's requirements (verbatim intent)
- "최대한 필기 위주로 정리해줘" → the handwritten notes and underlined parts are the backbone. Every `✍ 필기` must appear somewhere in the guide as a list item with tag "필기" (rewritten clearly; diagrams explained in words/arrows), and underlined (**bold**) points must be covered by list items and problems. Things neither written nor underlined get less space.
- "한 번 정독하고 문제를 풀 거라, 그 정도의 상식을 배경으로" → the student reads the guide once, then solves the mock exam. So the guide must be self-sufficient: every fact the mock exam tests must be explained in the guide. Don't test anything not in the guide. Assume no prior knowledge beyond the midterm range (상법 총칙~상사매매).
- Format must follow the samples: guide = 통계학 기말 대비 교재 style (Unit → sections; each section has Frame(왜 필요한가: 출발/그런데/그래서/비교), List L1..Ln with tags, Term Check 용어 적기, Problems OX, and instead of 계산 → 사례·객관식; answers + 해설 after each section). Mock = 상법 모의고사 style (2회 × 30문제; each 회: Q1–10 OX, Q11–30 5지선다; many 사례형 "갑은…을은…" stems and 판례 questions; 정답·해설 table with 단원).
- This is the 1차분 of the final range (more ranges will come later), so meta.info should say so.
- Professor: 서지민 교수님, 2026-2학기. Midterm covered 교재 35~291쪽 (1~8단원). Use these unit numbers:
  - 9단원 정형거래조건 · 유가증권 (pp.292–294) — small unit, 1 section is enough (student wrote "판례도 볼 것" at p.292)
  - 10단원 상호계산 (pp.295–301)
  - 11단원 익명조합 (pp.302–312)
  - 12단원 합자조합 (pp.312–313, only 의의·기능·설립 part)
  Section ids like "10-1", "10-2"…; you decide how to split sections (aim for 2–4 sections per big unit).
- Korean, friendly 해요체 in explanations ("~예요", "~해요"). Law must be accurate to the source (조문 번호, 학설 대립, 판례 결론). If the source is unclear (marked (?)), don't build questions on the uncertain part.

## Deliverables (follow the schema exactly)
Schema: /tmp/claude-0/-home-user--/1ac6a10d-142f-5ce7-847e-845b42b0175b/scratchpad/schema.md
Write:
- /tmp/claude-0/-home-user--/1ac6a10d-142f-5ce7-847e-845b42b0175b/scratchpad/runs/aN/guide.json
- /tmp/claude-0/-home-user--/1ac6a10d-142f-5ce7-847e-845b42b0175b/scratchpad/runs/aN/mock.json
(N = your agent number). Validate both with `python3 -c "import json;json.load(open(PATH))"` and fix until valid.
Optionally render to check layout: `python3 .../scratchpad/build/build.py guide guide.json /abs/out.html && node .../scratchpad/build/pdf.js /abs/out.html /abs/out.pdf` (same for mock with `mock`).
Then also write runs/aN/notes.md: 5–10 lines on your strategy and what you think is strongest in your version.
Return a 3-line summary only (counts of sections/problems, and your strongest element).
