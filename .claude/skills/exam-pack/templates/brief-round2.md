# TASK BRIEF — ROUND 2 (identical for all six agents)

You are improving an existing Korean 상법 기말 study guide (guide.json) and mock exam (mock.json) for a university student.
Base files (current final, already good — start from them, don't start over):
- /tmp/claude-0/-home-user--/1ac6a10d-142f-5ce7-847e-845b42b0175b/scratchpad/runs2/guide.json
- /tmp/claude-0/-home-user--/1ac6a10d-142f-5ce7-847e-845b42b0175b/scratchpad/runs2/mock.json
Schema: .../scratchpad/schema.md (base) + .../scratchpad/schema2.md (NEW: diagram + box). Read both.
Ground truth: .../scratchpad/src/source.md (textbook pp.293–313 transcription; handwriting = `> ✍ 필기`, underline = **bold**). Range is pp.293–313 — p.292 (FOB/CIF) was removed on the student's request; do NOT reintroduce FOB/CIF/인코텀즈.
Handwriting photos (to copy the layout of hand-drawn diagrams): .../scratchpad/q/*.jpg — name = <spread NN><L|R page><t|b half>. Spreads: 01=pp.292–293, 02=294–295, 03=296–297, 04=298–299, 05=300–301, 06=302–303, 07=304–305, 08=306–307, 09=308–309, 10=310–311, 11=312–313. Look at the crops that contain diagrams (at least 02R, 05R, 06L/06R, 08R, 10L) before drawing.
(All paths are under /tmp/claude-0/-home-user--/1ac6a10d-142f-5ce7-847e-845b42b0175b/scratchpad/)

## What the student asked (verbatim intent)
1. "교재에 있는 필기에 대한 설명은 구조도도 넣어서 해주고 … 구조도는 필기를 따라하되 좀 더 보기 쉽게" → every 필기 list item that is a diagram/arrow/calculation/comparison gets a clean "diagram" (schema2) that follows the student's drawing but is easier to read. Pure text notes (e.g., a circled word) may skip a diagram or be folded into a related diagram. Improve the 필기 explanation text too where needed so text + diagram explain together.
2. "시험을 쳐 보니까 사례랑 판례에 예를 들어서 내용을 접목시키는 시험이라, 교재나 모의고사에 이러한 사례들을 접목시킨 문제들을 넣어줘" → the real exam applies rules to fact patterns (갑·을·병 사례) and to 판례 facts. So:
   - Guide: each section's "cases" becomes 4–6 사례·판례 적용형 questions (boxed facts in "box"; 5지선다 or ㄱㄴㄷ 고르기 or short answer). Keep terms (5–6) and OX (8–10) but rewrite ≥ half of the OX as short 사례형 statements ("갑이 …한 경우, …할 수 있다").
   - Every 판례 in the source (71도2032 + 동지 72도2704·91도2390, 2010도5014, 4290민상616, 62다660(81다650), 서울고법 66나400, etc.) must appear in the guide as a list item (tag 판례) with 사실관계 → 쟁점 → 결론, and be applied in at least one guide case AND one mock question with changed facts (not copy of the 판례 facts).
   - Mock: still 2회 × 30, Q1–10 OX + Q11–30 5지선다 (midterm format). At least 22 of 30 per 회 must be 사례·판례 적용형 (boxed facts or 갑·을 stem). OX roughly 5:5, ①~⑤ roughly 4 each. 해설 says why the answer is right and briefly why each wrong option is wrong.
3. Keep: student reads the guide once then solves the mock → every mock question must be answerable from the guide. Accuracy beats everything (조문 번호, 학설, 판례 결론 exactly as the source). Never test a (?) uncertain reading. Friendly 해요체 in 해설. Units 9(유가증권 pp.293–294)/10 상호계산/11 익명조합/12 합자조합; keep section ids.

## Deliverables
Write to .../scratchpad/runs2/aN/guide.json and mock.json (N = your number). Validate JSON. RENDER and visually check (this is mandatory for diagrams):
  python3 .../scratchpad/build/build.py guide <abs json> <abs html> && node .../scratchpad/build/pdf.js <abs html> <abs pdf>
  then pdftoppm -r 70 -png -f A -l B <pdf> <prefix> and Read the PNGs of pages with diagrams; fix overlaps/cut-offs.
Write runs2/aN/notes.md (5–10 lines: strategy, strongest element). Return a 3-line summary.
