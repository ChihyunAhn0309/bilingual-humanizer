# 게시 전 증빙 정합성 감사

감사일: 2026-10-02. 대상은 `outputs/github-repo`의 영·한 루트 README, `benchmarks/2026-10-02/results.json`, `REPORT.md`, `v14-review.md`, `corpus/`, `receipts/`다. 허용된 `benchmarks/verify_evidence.py`를 읽고 로컬에서 실행했다. 후속 요청에 따라 새로 추가된 `input-verification-log.json`과 보고서의 수정 문장도 확인했다. 네트워크·외부 검사·후보 재작성은 하지 않았으며, 감사자는 이 보고서 외에는 파일을 쓰거나 수정하지 않았다.

## 결론

**공개 묶음 내부의 36개 표시값·입력 해시·영수증 해시는 일치한다. 최종 v1.4의 12개 결과도 GPTZero 4개, QuillBot 4개, Sapling 2개, ZeroGPT 2개로 일치한다.** 미검사를 0점이나 통과로 바꾼 사례, 다른 후보의 유리한 결과를 최종본에 합친 사례, 확인한 파일 내 비공개 계정·이메일·자격증명·로컬 사용자 경로 노출은 발견하지 못했다.

최초 검토에서는 최종 QuillBot 결과의 입력 연결 근거가 공개 묶음에서 재구성되지 않는다는 한계의 설명이 부족했다. 작성자가 이를 명시하고 사후 관측 기록의 성격을 구분했으므로, **현재 미해결 actionable finding은 없다.** 다만 입력과 외부 결과의 연결을 독립 인증할 수 없다는 증빙의 실제 한계는 그대로 남아 있다. 이 감사는 원격 검사 실행이나 업체 응답의 진위를 인증하지 않는다.

## 최초 발견 및 후속 확인

### [P2, 설명 보완 확인] 최종 QuillBot 영수증의 입력 연결 근거 누락

- 최초 위치: `benchmarks/2026-10-02/REPORT.md:66`.
- 관련 영수증: `receipts/quillbot-en-library-v14.txt`, `quillbot-en-cache-v14.txt`, `quillbot-ko-library-v14.txt`, `quillbot-ko-cache-v14.txt`의 1–21행.
- 관찰: 네 영수증은 점수, 모델 버전, 남은 검사 횟수 등을 보관하지만 입력 본문, 입력 파일명, 입력 해시 또는 입력 비교 결과를 포함하지 않는다. `results.json`의 해시가 파일과 일치해도, 그 사실만으로 어느 파일을 검사한 결과인지 독립적으로 재구성할 수 없다. 특히 두 영어 결과는 모두 0%여서 표시값 자체로 서로 구별할 수 없다.
- 최초 문제: 보고서는 최종 입력의 공백 정규화 대조를 수행했다고 설명했지만, 공개 영수증에 그 입력이 보존되지 않았으며 연결이 실행자의 관측에 의존한다는 제한을 구체적으로 밝히지 않았다. 점수가 틀리거나 검사를 수행하지 않았다는 발견은 아니다.
- 후속 수정: `REPORT.md:66`은 결과 패널 발췌본의 입력 누락, agent 관측에 의존하는 연결, 공개 묶음만으로 독립 인증할 수 없다는 한계를 명시한다. 추가된 `input-verification-log.json:2-3`은 `kind: agent_attestation`, 사후 작성 및 정확한 비교 시각 미보존을 밝힌다. QuillBot 네 건은 50–91행에 있으며, 각 항목은 `vendor_authenticated_input_binding: false`, `comparison_timestamp: null`로 기록된다.
- 후속 검사: 새 로그의 UI 입력 확인 10건(GPTZero 4, QuillBot 4, ZeroGPT 2)은 기존 `results.json`의 최종 후보·입력 해시·영수증 경로와 모두 일치했다. 원래 36개 영수증 해시도 계속 일치한다.
- 판정: 공개 설명의 부족은 해결되었다. 로그는 기존 실행자의 사후 진술이며, 이번 감사자는 원래 tool transcript를 열어 관측 사실을 독립 재검증하지 않았다. 따라서 이를 새로운 업체 증빙이나 독립 입력 인증으로 세지 않는다.

## 수치와 파일 대조 결과

| 서비스 | 전체 완료 기록 | 최종 v1.4 기록 |
| --- | ---: | ---: |
| GPTZero | 11 | 4 |
| QuillBot | 9 | 4 |
| Sapling | 8 | 2 |
| ZeroGPT | 8 | 2 |
| 합계 | 36 | 12 |

버전별 완료 기록은 원문 8, v1.1(`rewrite`) 8, v1.2 7, v1.3 1, v1.4 12다. 36개는 36개의 서로 다른 문서를 뜻하지 않는다. 문서·버전·서비스 조합별 관측 횟수다.

| 최종 후보 | GPTZero | QuillBot | Sapling | ZeroGPT |
| --- | ---: | ---: | ---: | ---: |
| en-library | 100% | 0% | 96.2% | 미검사 |
| ko-library | 11% | 86% | 미검사 | 100% |
| en-cache | 100% | 0% | 93% | 미검사 |
| ko-cache | 100% | 92% | 미검사 | 100% |

각 열은 업체별 서로 다른 표시 지표다. 이 표는 통과율이나 인간 작성 확률의 공통 척도가 아니다.

실행·대조한 내용:

1. `python -B benchmarks/verify_evidence.py`: 종료 코드 0, `PASS: 36 unique observations; input and receipt hashes match.`
2. 별도 읽기 전용 검사에서 영수증의 실제 표시값을 서비스별 형식으로 추출: `results.json`과 **36/36 일치**. Sapling JSON은 JSON 문자열 안에 JSON이 있는 형식까지 해석했다.
3. `REPORT.md`의 서비스별 전체 표에 있는 숫자·영수증 링크를 `results.json`과 대조: **36/36 일치**. 완료 기록이 있는 칸을 N/A로 표시하거나, N/A 칸에 기록을 잘못 배정한 사례 없음.
4. 36개 기록의 `input_characters`, `input_whitespace_words`를 corpus 파일에서 다시 계산: 모두 일치.
5. `v14-review.md:139-149`의 최종 길이와 원문·최종 해시는 현재 corpus와 일치. 독립 검토 당시의 중간 해시와 최종 해시를 문서가 명확히 구분한다.
6. Sapling의 WebMCP JSON 영수증 7개는 반환된 모든 문장을 공백 정규화해 연결했을 때 각각의 입력 본문과 일치하며, `truncated: false`다. 원문 UI 영수증 1건과는 형식이 다르다.
7. 일반 텍스트 형태의 ZeroGPT 영수증 7개에는 대응 corpus 본문 전체가 포함된다. 최초 Korean library 원문 영수증은 별도의 UI 트리 형식이다.
8. 영수증은 총 39개다. 완료 기록에서 제외된 3개 파일은 `gptzero-blocked-after-free-limit.txt`, `gptzero-ko-library-rewrite.txt`, `zerogpt-ko-library-invalid-attempt.txt`이며, 보고서가 제외 이유를 설명한다. 원래 영수증이 보존되지 않은 Advanced Scan 재시도도 완료 비교에 포함하지 않는다.

## 해석·과장·개인정보 점검

- `REPORT.md:3`은 여러 탐지기에서의 수용 목표 미달을 명확히 밝힌다. 0%를 확정된 실제 0이나 인간 저자 증명으로 해석하지 않고 업체 표시값으로 다룬다.
- N/A는 미검사로 정의하며, 미지원 언어나 낮은 제품 성능이라고 추론하지 않는다. 서로 다른 업체 점수를 평균하지 않는다.
- README와 보고서는 모든 시험 글이 AI 생성이며, 인간 대조군·대표 표본·독립 인간 평가가 없고 개발 과정에서 이전 점수를 봤음을 밝힌다. 따라서 36개 관측을 정확도 평가나 우월한 스킬 성능으로 제시하지 않는다.
- `v14-review.md`는 자체 검토, fresh-context 모델 검토 1회, 동일 리뷰어 후속 검토 1회를 구분한다. 과교정 자체 사례 3개도 독립 평가로 세지 않는다. 보고서의 요약 횟수와 일치한다. 이번 감사로 실제 하위 에이전트 호출 이력을 독립 증명한 것은 아니다.
- 허용된 초기 파일 65개를 대상으로 이메일, Windows 사용자 경로, OAuth·토큰·비밀번호·API 키 형태, JWT, 한국 휴대전화 형태를 탐색하고 계정 문구와 URL 문맥을 검토했다. 추가 관측 로그도 읽었다. 비공개 계정 식별자나 자격증명 노출은 발견하지 못했다. REPORT의 `OAuth URLs ... are not published` 문장은 민감정보 자체가 아니며, GPTZero UI에 보이는 전문가 이름과 서비스 홍보 링크도 개인 계정 정보로 분류하지 않았다. 공개 저장소 소유자 핸들은 README의 설치 주소에 의도적으로 들어 있다.

## 후속 확인 시점의 주요 해시

| 파일 | SHA-256 |
| --- | --- |
| `results.json` | `f7bb5f9b580388d6bcffa1dfe626556be95c6cb03fc29aee2b0c6ff3f4c59ca6` |
| `REPORT.md` | `e4fba1da11bbfd4f71b260e763f535a3ae6ef606a52b30d92a981fc52c30cf7e` |
| `v14-review.md` | `1293d5e66e53c410a22a9fe68ea5010f7e3701e3b08c9b4ba1e4aa113d86eb5f` |
| `input-verification-log.json` | `b14f4617bf7fb5e2abce1f9d15b0a21b4549425334a667d691f3dd2aee1704b6` |
| `README.md` | `4b33ed39caa46ccb233b992079a9e18165e792da80d7acf4d683db98a76d47ef` |
| `README.ko.md` | `349cc6026c6d6224dc9a4b891e3dd8bcb3cfe2040a68e4fa96d29a8c8cf312fd` |

## 범위의 한계

이 감사는 로컬 자료 사이의 정합성과 표현을 확인한다. 원격 서비스 재실행, 업체의 현재 지표 정의 확인, 원시 네트워크 요청·응답 또는 계정 이용 이력 확인을 하지 않았다. corpus-manifest 자체, 역사적 리뷰 문서 전체, 이미지·PowerPoint와 도표, Git 이력, 저장소의 다른 파일은 이번 요청의 직접 검토 범위에 포함하지 않았다. 따라서 전체 저장소의 개인정보 부재나 모든 게시 산출물의 정확성을 보증하지 않는다. 일반 글쓰기 성능, detector 우회 성능, 인간 저자 여부도 판단하지 않았다.
