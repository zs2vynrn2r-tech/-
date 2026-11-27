# Graph Report - -  (2026-11-27)

## Corpus Check
- 63 files · ~407,927 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: .css 3, .xml 1, (none) 1)

## Summary
- 801 nodes · 1284 edges · 68 communities (65 shown, 3 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 82 edges (avg confidence: 0.85)
- Token cost: 532,773 input · 0 output

## Graph Freshness
- Built from commit: `c3f9ae1e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Image Asset Fetcher
- Direction Dealer Script
- Headless Browser Driver
- Chart Helpers Library
- App Screen Dealer
- Page Inspector Script
- TypeScript MCP SDK v1
- Imagery Sourcing Rules
- evaluation.py
- connections.py
- Words (copy reference)
- App Screen Data Rules
- No-Slop House Rules
- Motion Reference
- Part 3 — 익명조합(영업자의 의무 ~ 종료) / 합자조합(총설 ~ 조합계약) (pp.308–313)
- Design Linter Script
- 제5절 익명조합
- Picture Placements
- Copy and Motion Budget
- MCP Security and Formats
- MCP Evaluation Guide
- Multi-Agent Mode Skills
- MCP Errors and Pagination
- Scroll Stage Runtime
- Dashboard Tells
- Inspector Rule Checks
- 제4절 상호계산
- Colour Reference
- p.313
- LARP Startup Teardown
- Layout Reference
- MCP Server Best Practices
- Python FastMCP Guide
- Part 2 (spreads 05–08) — 상행위법 총론: 상호계산(계속) ~
- Agent Browser Skill
- 모든 프로젝트에서 쓰는 기본 스킬
- Inspector Gate Checks
- Scroll Scenes
- MCP Server Hosting v2
- App Style Manifest
- The study (research reference)
- Analytics Screen Pattern
- Direction Sheet Assets
- Find Skills Skill
- Apache License
- Builder Screen Pattern
- Commerce Screen Pattern
- Community Screen Pattern
- Creator Screen Pattern
- Devtools Screen Pattern
- Finance Screen Pattern
- Markets Screen Pattern
- Report Screen Pattern
- SMB Admin Screen Pattern
- Support Screen Pattern
- Wallet Screen Pattern
- Workspace Screen Pattern
- 교재_293-313_필기전사.md
- exam-pack — 교재 + 모의고사 PDF 파이프라인 (토큰 절약판)
- TASK BRIEF (identical for all six agents)
- p.307
- 제3절 유가증권에 관한 규칙
- TASK BRIEF — ROUND 2 (identical for all six agents)
- Output schema (JSON, UTF-8). Write valid JSON only.
- Additions to schema.md (round 2)
- 2. 적극적 효력
- pdf.js

## God Nodes (most connected - your core abstractions)
1. `getOne()` - 31 edges
2. `search()` - 22 edges
3. `getVideo()` - 19 edges
4. `App screens reference` - 17 edges
5. `kinds` - 14 edges
6. `MCP Builder Skill` - 14 edges
7. `MCPConnection` - 13 edges
8. `deal()` - 13 edges
9. `line()` - 13 edges
10. `diverging()` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Slop audit before shipping` --semantically_similar_to--> `Fourteen look passes`  [INFERRED] [semantically similar]
  .claude/skills/aura-farming/SKILL.md → .claude/skills/design-taste-frontend/references/critique.md
- `Self-Check Smoke Script (scripts/smoke.ts)` --semantically_similar_to--> `Evaluation Harness (scripts/evaluation.py)`  [INFERRED] [semantically similar]
  .claude/skills/mcp-builder/reference/node_mcp_server_v2.md → .claude/skills/mcp-builder/reference/evaluation.md
- `First-screen title saying what this is` --semantically_similar_to--> `Fourteen look passes`  [INFERRED] [semantically similar]
  .claude/skills/design-taste-frontend/references/layout.md → .claude/skills/design-taste-frontend/references/critique.md
- `FastMCP Context Injection (progress, logging, elicitation)` --conceptually_related_to--> `createServer() Server Factory`  [AMBIGUOUS]
  .claude/skills/mcp-builder/reference/python_mcp_server.md → .claude/skills/mcp-builder/reference/node_mcp_server_v2.md
- `Awwwards-weighted score (design 40, usability 30, creativity 20, content 10)` --conceptually_related_to--> `Gallery study of 247 sites (One Page Love and Awwwards)`  [INFERRED]
  .claude/skills/design-taste-frontend/references/critique.md → .claude/skills/design-taste-frontend/references/research.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Found-picture sourcing, honesty and credit pipeline** — _claude_skills_design_taste_frontend_skill_assets_script, _claude_skills_design_taste_frontend_references_imagery_open_collections, _claude_skills_design_taste_frontend_references_imagery_honesty, _claude_skills_design_taste_frontend_references_imagery_credits_licences, _claude_skills_design_taste_frontend_references_imagery_video [EXTRACTED 1.00]
- **Page build run: inventory to report** — _claude_skills_design_taste_frontend_skill_subject_inventory, _claude_skills_design_taste_frontend_skill_argument, _claude_skills_design_taste_frontend_skill_direction_sheet, _claude_skills_design_taste_frontend_skill_idea_sentence, _claude_skills_design_taste_frontend_skill_copy_deck, _claude_skills_design_taste_frontend_skill_gate, _claude_skills_design_taste_frontend_skill_look_loop, _claude_skills_design_taste_frontend_skill_motion_layer, _claude_skills_design_taste_frontend_skill_report_step [EXTRACTED 1.00]
- **MCP Builder Reference Documentation Library** — _claude_skills_mcp_builder_skill_mcp_builder_skill, _claude_skills_mcp_builder_reference_mcp_best_practices_mcp_best_practices, _claude_skills_mcp_builder_reference_node_mcp_server_v2_typescript_guide_v2, _claude_skills_mcp_builder_reference_node_mcp_server_typescript_guide_v1, _claude_skills_mcp_builder_reference_python_mcp_server_python_guide, _claude_skills_mcp_builder_reference_evaluation_evaluation_guide [EXTRACTED 1.00]
- **tasteskill look-and-fix critique loop** — _claude_skills_design_taste_frontend_readme_look_and_fix_loop, _claude_skills_design_taste_frontend_references_critique_fourteen_passes, _claude_skills_design_taste_frontend_references_critique_awwwards_score, _claude_skills_design_taste_frontend_references_critique_score_caps, _claude_skills_design_taste_frontend_references_critique_fix_order [EXTRACTED 1.00]
- **tasteskill house-rule gate (lint, inspect, tells registry, house style)** — claude_skills_design_taste_frontend_scripts_lint, claude_skills_design_taste_frontend_scripts_inspect, _claude_skills_design_taste_frontend_references_tells_tells_registry, _claude_skills_design_taste_frontend_readme_house_style, _claude_skills_design_taste_frontend_references_colour_cream_terracotta_ban, _claude_skills_design_taste_frontend_references_copy_two_line_headline [EXTRACTED 1.00]
- **Anti-AI-slop rule sets across skills** — _claude_skills_aura_farming_skill_banned_list, _claude_skills_design_taste_frontend_references_tells_first_wave, _claude_skills_design_taste_frontend_references_tells_second_wave, _claude_skills_design_taste_frontend_references_copy_generated_copy_tells [INFERRED 0.85]
- **Automated quality checks run by the gate tools** — claude_skills_design_taste_frontend_scripts_lint, _claude_skills_design_taste_frontend_skill_inspect_script, claude_skills_design_taste_frontend_scripts_scenes, _claude_skills_design_taste_frontend_references_app_screens_ragged_row, _claude_skills_design_taste_frontend_references_app_screens_panel_void, _claude_skills_design_taste_frontend_references_app_screens_no_data_hue [INFERRED 0.85]
- **Actionable Error Message Handling Across SDKs** — _claude_skills_mcp_builder_reference_node_mcp_server_handleapierror, _claude_skills_mcp_builder_reference_node_mcp_server_v2_apierror, _claude_skills_mcp_builder_reference_python_mcp_server_handle_api_error, _claude_skills_mcp_builder_reference_mcp_best_practices_error_handling [INFERRED 0.85]
- **Shared Upstream API Client Helper Pattern (v1, v2, Python)** — _claude_skills_mcp_builder_reference_node_mcp_server_makeapirequest, _claude_skills_mcp_builder_reference_node_mcp_server_v2_apirequest, _claude_skills_mcp_builder_reference_python_mcp_server_make_api_request [INFERRED 0.85]

## Communities (68 total, 3 thin omitted)

### Community 0 - "Image Asset Fetcher"
Cohesion: 0.07
Nodes (85): AIC_FIELDS, AIC_HEADERS, applyThumb(), ARCHIVE_LICENCE, args, argv, base(), clock() (+77 more)

### Community 1 - "Direction Dealer Script"
Cohesion: 0.10
Nodes (41): adjustments(), argv, assetQueries(), ASSETS_PATH, briefStop(), briefWords(), deal(), dealHero() (+33 more)

### Community 2 - "Headless Browser Driver"
Cohesion: 0.10
Nodes (15): alive(), Browser, findChrome(), Page, sleep(), sweepProfiles(), args, go() (+7 more)

### Community 3 - "Chart Helpers Library"
Cohesion: 0.21
Nodes (24): axes(), bars(), dayHeads(), diverging(), frame(), hits(), kindStyle(), lane() (+16 more)

### Community 4 - "App Screen Dealer"
Cohesion: 0.11
Nodes (22): argv, deal(), dealScreen(), dealShell(), dealStyle(), fontLink(), HERE, kebab() (+14 more)

### Community 5 - "Page Inspector Script"
Cohesion: 0.09
Nodes (21): allow, appMode, args, asJson, dealtFonts, fails, film, HEIGHT (+13 more)

### Community 6 - "TypeScript MCP SDK v1"
Cohesion: 0.14
Nodes (15): Deprecated v1 APIs (server.tool, setRequestHandler), TypeScript v1 Quality Checklist, server.registerTool (v1 modern API), Resource Registration and Resources vs Tools (v1), Per-request StreamableHTTPServerTransport (stateless, v1), Node/TypeScript MCP Server Guide (SDK v1), v1-to-v2 Codemod (@modelcontextprotocol/codemod), TypeScript v2 Quality Checklist (+7 more)

### Community 7 - "Imagery Sourcing Rules"
Cohesion: 0.17
Nodes (7): Credits and licences, Imagery reference, Open collections (Openverse, Wikimedia Commons, Art Institute of Chicago, the Met), Study of 91 Awwwards Sites of the Day (imagery), Type and colour alone, Video and footage, scripts/assets.mjs (open collection search)

### Community 8 - "evaluation.py"
Cohesion: 0.09
Nodes (16): build_guide(), build_mock(), _clip(), cover(), diagram(), dots(), md(), wrap() (+8 more)

### Community 9 - "connections.py"
Cohesion: 0.07
Nodes (5): create_connection(), MCPConnection, MCPConnectionHTTP, MCPConnectionSSE, MCPConnectionStdio

### Community 10 - "Words (copy reference)"
Cohesion: 0.22
Nodes (7): Headline character budget formula, Headline shapes that work, Micro-typography, Words (copy reference), Setting display type (tracking, leading, optical alignment), Loading the fonts properly, Type reference

### Community 11 - "App Screen Data Rules"
Cohesion: 0.16
Nodes (7): assets/app.css neutral app shell, App screens reference, assets/charts.js chart helpers, Default app tokens, The screen's one finding, Five shell archetypes, Page vs app screen distinction

### Community 12 - "No-Slop House Rules"
Cohesion: 0.16
Nodes (3): data-ui interface fragment attribute, Study of 247 curated gallery sites, tasteskill v2 (design-taste-frontend skill)

### Community 13 - "Motion Reference"
Cohesion: 0.18
Nodes (10): Study of 99 Awwwards Sites of the Day (motion), --ease-expo curve, html.js gate for hidden states, Load sequence in 1.2 seconds, Masked line reveal, Motion reference, Reveal on scroll (once), Scroll behaviours, ranked (+2 more)

### Community 14 - "Part 3 — 익명조합(영업자의 의무 ~ 종료) / 합자조합(총설 ~ 조합계약) (pp.308–313)"
Cohesion: 0.11
Nodes (18): 1) 계약의 해지, 1) 영업수행의무, 1. 영업자와 제3자의 관계, 1. 익명조합의 종료원인, 2) 법정종료사유, 2. 영업자의 의무, 2) 이익분배의무, 2. 익명조합원과 제3자의 관계 (+10 more)

### Community 15 - "Design Linter Script"
Cohesion: 0.11
Nodes (18): Aura Farming banned list (AI-slop tells), Things that read as generated (copy), First wave tells (2023-2024), Second wave tells (2025), Tells: the dated registry, APP_LEVEL, appMode, args (+10 more)

### Community 16 - "제5절 익명조합"
Cohesion: 0.13
Nodes (15): 1. 익명조합원의 권리의무, 1. 익명조합의 의의, 1) 출자의무, 2. 익명조합의 경제적 기능, Ⅰ. 총 설, Ⅱ. 익명조합의 법적 성질, Ⅲ. 익명조합의 내부관계, p.303 (+7 more)

### Community 17 - "Picture Placements"
Cohesion: 0.18
Nodes (11): Index with hover preview (placement), Inset frame that grows, Picture placements, ranked, Split placement (picture in a half or two-thirds), Index with preview, anchored to the row, Ink fill statement, Opening window recipe, Page to page view transitions (+3 more)

### Community 18 - "Copy and Motion Budget"
Cohesion: 0.20
Nodes (5): Copy deck, Motion layer (step 9), One live thing, Report step, Scroll scenes

### Community 19 - "MCP Security and Formats"
Cohesion: 0.23
Nodes (12): JSON vs Markdown Response Formats, MCP Security Best Practices (OAuth 2.1, API keys, input validation), example_search_users (TypeScript v1), handleApiError (TypeScript v1), makeApiRequest (axios, TypeScript v1), requireBearerAuth (OAuth token verification), structuredContent and outputSchema Rules, Zod 3 Input Validation Schemas (.strict()) (+4 more)

### Community 20 - "MCP Evaluation Guide"
Cohesion: 0.20
Nodes (8): MCP Server Evaluation Guide, Evaluation Harness (scripts/evaluation.py), Evaluation Report (accuracy, durations, tool feedback), QA Pair XML Evaluation Format, Evaluation Answer Verification Process, anthropic>=0.39.0, mcp>=1.1.0, Evaluation Script Requirements (requirements.txt)

### Community 21 - "Multi-Agent Mode Skills"
Cohesion: 0.20
Nodes (7): 67 skill, Seventh judge agent, Six strategy lenses (minimalist to wildcard), China Maxing skill, Never-translate rule (code, paths, identifiers), Claim verdicts (SURVIVED, SHAKY, BUSTED), Crash Out skill

### Community 22 - "MCP Errors and Pagination"
Cohesion: 0.20
Nodes (8): MCP Error Handling (tool errors in result objects), Pagination (limit, has_more, next_offset, total_count), CHARACTER_LIMIT Truncation (v1), ApiError / httpErrorMessage (v2), apiRequest (fetch + AbortSignal, v2), example_search_users (TypeScript v2), Tool Errors vs Protocol Errors, Evaluation Question Requirements (10 independent read-only questions)

### Community 24 - "Dashboard Tells"
Cohesion: 0.25
Nodes (5): Tells of generated dashboards, no-data-hue inspector check, Signature element (one element only this product has), Study of 23 real product screens, What gives generated motion away

### Community 25 - "Inspector Rule Checks"
Cohesion: 0.31
Nodes (8): APP_SKIP, colourFamily(), hexToHsl(), inRange(), judge(), judgeApp(), judgeLayout(), RULE_IDS

### Community 26 - "제4절 상호계산"
Cohesion: 0.17
Nodes (12): 1) 상호계산불가분의 원칙, 1. 상호계산의 경제적 기능, 1. 소극적 효력, 2) 상호계산불가분원칙의 예외, 2. 상호계산의 법적 성질, Ⅰ. 상호계산의 의의, Ⅱ. 상호계산의 경제적 기능 및 법적 성질, Ⅲ. 상호계산의 효력 (+4 more)

### Community 27 - "Colour Reference"
Cohesion: 0.20
Nodes (5): Colour reference, Colour fields (section grounds), Neutral scrim (only allowed gradient), Palette roles (bg, surface, ink, muted, accent tokens), Third wave tells: warm editorial fix (2025-2026)

### Community 28 - "p.313"
Cohesion: 0.29
Nodes (7): 1. 조합계약, 1. 합자조합의 의의, 2. 합자조합의 경제적 기능, Ⅰ. 총 설, Ⅱ. 합자조합의 설립, p.313, 제6절 합자조합

### Community 29 - "LARP Startup Teardown"
Cohesion: 0.17
Nodes (8): Awwwards-weighted score (design 40, usability 30, creativity 20, content 10), Competitor test and live thing, Critique: judging the render, Fourteen look passes, The Kill Shot (fatal risk and cheapest test), LARP skill, Nine-section startup teardown, Verdict stamps (LARP, Fundable LARP, Actual Company)

### Community 30 - "Layout Reference"
Cohesion: 0.33
Nodes (5): Off-centre anchor line, Designed endings, Layout reference, Rests vs holes (empty space), October 2026 study: 100 Sites of the Day

### Community 31 - "MCP Server Best Practices"
Cohesion: 0.29
Nodes (5): Evaluation Transport Types (stdio, sse, http), MCP Server Best Practices, MCP Testing Requirements, Tool Annotations Table (hints, not security guarantees), Tool Annotations (readOnly/destructive/idempotent/openWorld hints)

### Community 32 - "Python FastMCP Guide"
Cohesion: 0.33
Nodes (6): FastMCP Context Injection (progress, logging, elicitation), FastMCP (@mcp.tool decorator), FastMCP Lifespan Management, Python MCP Server Implementation Guide, Python Quality Checklist, Structured Output Types (TypedDict, Pydantic)

### Community 33 - "Part 2 (spreads 05–08) — 상행위법 총론: 상호계산(계속) ~"
Cohesion: 0.29
Nodes (7): (3) 잔액채권승인의 효력, (4) 계산의 부정확과 승인행위의 하자, Ⅳ. 상호계산의 종료, p.300, p.301, p.302, Part 2 (spreads 05–08) — 상행위법 총론: 상호계산(계속) ~

### Community 34 - "Agent Browser Skill"
Cohesion: 0.33
Nodes (6): agent-browser skill, agent-browser CLI (Rust), Chrome DevTools Protocol (CDP), Observability dashboard (port 4848), agent-browser skills get core, Specialized skills (electron, slack, dogfood, agentcore ...)

### Community 35 - "모든 프로젝트에서 쓰는 기본 스킬"
Cohesion: 0.33
Nodes (5): Headroom (스킬은 아니지만 함께 쓰는 도구), 모든 프로젝트에서 쓰는 기본 스킬, 스킬 목록, 클라우드 세션(claude.ai/code)에서 쓰려면, 한 번에 설치 (macOS / Linux)

### Community 36 - "Inspector Gate Checks"
Cohesion: 0.40
Nodes (5): panel-void inspector check, ragged-row inspector check, Gate step, scripts/inspect.mjs (real-browser inspector), Redesign, restyle or review special case

### Community 37 - "Scroll Scenes"
Cohesion: 0.22
Nodes (7): Devices: strong vs weak sites, Finished composition fallback (reduced motion, no script), GSAP and ScrollTrigger, Lenis smooth scroll, Scroll scenes reference, stage.js (Stage.smooth, Stage.init, Stage.scene), Sticky stage with scrubbed timeline

### Community 38 - "MCP Server Hosting v2"
Cohesion: 0.33
Nodes (5): DNS Rebinding Protection, createMcpExpressApp (Host/Origin validation), createMcpHandler + toNodeHandler, list_changed Notifications (v2 handles, handler.notify), serveStdio

### Community 39 - "App Style Manifest"
Cohesion: 0.33
Nodes (5): about, patterns, shells, styles, version

### Community 40 - "The study (research reference)"
Cohesion: 0.18
Nodes (10): Aura Farming skill, Slop audit before shipping, Direction library (20 directions), tasteskill v2 (design-taste-frontend), App-screen study, Blind test rounds (skill vs baseline vs atelier), Gallery study of 247 sites (One Page Love and Awwwards), Idea engines taken from the subject (+2 more)

### Community 41 - "Analytics Screen Pattern"
Cohesion: 0.40
Nodes (5): note, screens, styles, kinds, analytics

### Community 42 - "Direction Sheet Assets"
Cohesion: 0.50
Nodes (4): App styles library (seven styles), Dealt photographs (Lorem Picsum / Unsplash), Direction sheet, scripts/draw.mjs (direction dealer)

### Community 43 - "Find Skills Skill"
Cohesion: 0.67
Nodes (3): Find Skills skill, Skills CLI (npx skills), skills.sh leaderboard

### Community 44 - "Apache License"
Cohesion: 0.50
Nodes (4): Anthropic, PBC (copyright holder), Apache License 2.0, Patent License Grant (terminates on patent litigation), Redistribution Conditions (license copy, change notices, NOTICE file)

### Community 45 - "Builder Screen Pattern"
Cohesion: 0.50
Nodes (4): note, screens, styles, builder

### Community 46 - "Commerce Screen Pattern"
Cohesion: 0.50
Nodes (4): note, screens, styles, commerce

### Community 47 - "Community Screen Pattern"
Cohesion: 0.50
Nodes (4): note, screens, styles, community

### Community 48 - "Creator Screen Pattern"
Cohesion: 0.50
Nodes (4): note, screens, styles, creator

### Community 49 - "Devtools Screen Pattern"
Cohesion: 0.50
Nodes (4): note, screens, styles, devtools

### Community 50 - "Finance Screen Pattern"
Cohesion: 0.50
Nodes (4): note, screens, styles, finance

### Community 51 - "Markets Screen Pattern"
Cohesion: 0.50
Nodes (4): markets, note, screens, styles

### Community 52 - "Report Screen Pattern"
Cohesion: 0.50
Nodes (4): report, note, screens, styles

### Community 53 - "SMB Admin Screen Pattern"
Cohesion: 0.50
Nodes (4): smb-admin, note, screens, styles

### Community 54 - "Support Screen Pattern"
Cohesion: 0.50
Nodes (4): support, note, screens, styles

### Community 55 - "Wallet Screen Pattern"
Cohesion: 0.50
Nodes (4): wallet, note, screens, styles

### Community 56 - "Workspace Screen Pattern"
Cohesion: 0.50
Nodes (4): workspace, note, screens, styles

### Community 57 - "교재_293-313_필기전사.md"
Cohesion: 0.33
Nodes (5): (1) FOB조건, (2) CIF조건, p.292, p.293, Part 1 (spreads 01–04)

### Community 59 - "exam-pack — 교재 + 모의고사 PDF 파이프라인 (토큰 절약판)"
Cohesion: 0.40
Nodes (4): exam-pack — 교재 + 모의고사 PDF 파이프라인 (토큰 절약판), 빠른 절차 (가장 싼 순서), 사용자 선호 (이 사용자 기준), 토큰 절약 규칙

### Community 60 - "TASK BRIEF (identical for all six agents)"
Cohesion: 0.40
Nodes (4): Deliverables (follow the schema exactly), Source (read ALL of it first), Student's requirements (verbatim intent), TASK BRIEF (identical for all six agents)

### Community 61 - "p.307"
Cohesion: 0.40
Nodes (5): 2) 손실분담의무, 3) 지위불양도의무, 4) 감시권, p.307, [판례] + 대법원 1971.12.28. 선고 71도2032 판결

### Community 62 - "제3절 유가증권에 관한 규칙"
Cohesion: 0.40
Nodes (5): Ⅰ. 서 설, Ⅱ. 준용규정의 내용, p.294, p.295, 제3절 유가증권에 관한 규칙

### Community 63 - "TASK BRIEF — ROUND 2 (identical for all six agents)"
Cohesion: 0.50
Nodes (3): Deliverables, TASK BRIEF — ROUND 2 (identical for all six agents), What the student asked (verbatim intent)

### Community 64 - "Output schema (JSON, UTF-8). Write valid JSON only."
Cohesion: 0.50
Nodes (3): guide.json — 기말 대비 교재, mock.json — 기말 모의고사, Output schema (JSON, UTF-8). Write valid JSON only.

### Community 65 - "Additions to schema.md (round 2)"
Cohesion: 0.50
Nodes (3): 1) Diagram on a list item, 2) Boxed 사례 text, Additions to schema.md (round 2)

### Community 66 - "2. 적극적 효력"
Cohesion: 0.50
Nodes (4): 1) 잔액채권의 성립, 2) 계산서의 승인, 2. 적극적 효력, p.299

## Ambiguous Edges - Review These
- `FastMCP Context Injection (progress, logging, elicitation)` → `createServer() Server Factory`  [AMBIGUOUS]
  .claude/skills/mcp-builder/reference/python_mcp_server.md · relation: conceptually_related_to

## Knowledge Gaps
- **53 isolated node(s):** `Default app tokens`, `The screen's one finding`, `Five shell archetypes`, `Reveal on scroll (once)`, `Stage.smooth() smoothing` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 326 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Gate step` connect `Inspector Gate Checks` to `Headless Browser Driver`, `Copy and Motion Budget`, `Design Linter Script`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `search()` (e.g. with `searchAic()` and `searchArchive()`) actually correct?**
  _`search()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Default app tokens`, `The screen's one finding`, `Five shell archetypes` to the rest of the system?**
  _53 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Image Asset Fetcher` be split into smaller, more focused modules?**
  _Cohesion score 0.06648426812585499 - nodes in this community are weakly interconnected._
- **Why does `Motion budget` connect `Copy and Motion Budget` to `App Screen Data Rules`, `Inspector Gate Checks`, `Motion Reference`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `App screens reference` (e.g. with `Motion budget` and `Showing software as real HTML fragments`) actually correct?**
  _`App screens reference` has 2 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `FastMCP Context Injection (progress, logging, elicitation)` and `createServer() Server Factory`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._