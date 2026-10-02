# bilingual-humanizer v1.5.1 독립 최종 감사

평가일: 2026-10-03. 별도 AI 세션에서 지정된 원문·후보·스킬·스크립트를 읽었다. 과거 평가 결과나 작성자의 자체 평가는 제공받지 않았다. 사실 보존, 문서 목적/결정 단계, 엄격한 임계값, 단위 구분이라는 검사 주제는 지정받았다. 이는 독립 컨텍스트의 AI 평가이며 인간 평가 또는 서로 다른 모델 간 검증은 아니다. 검토 대상 파일은 수정하지 않았다.

**검토한 범위에서 수정이 필요한 실질적 결함을 발견하지 못했다.** 이 판정은 아래 파일과 도서관 사례 한 쌍에 한정된다. 스킬의 모든 후속 실행이 의미를 보존한다거나 외부 탐지기를 통과한다는 판정이 아니다.

읽은 자료는 `outputs/bilingual-humanizer/SKILL.md`, `references/fidelity-and-documents.md`, `references/iterative-review.md`, `references/detector-report-format.md`, `scripts/check_detector_report.py`, `evals/test_iteration.py`이며, 두 한국어 도서관 파일을 별도로 대조했다. 경로가 축약된 스킬 내부 자료는 모두 `outputs/bilingual-humanizer/` 아래에 있다.

| 검사항목 | 관찰한 증거 | 판정 |
| --- | --- | --- |
| 검토 목적과 결정 단계 | 원문 첫 문단의 “접수된 의견을 살펴보고, 운영안을 구체화하기 전에 확인해야 할 조건을 정리한다”가 후보 첫 문단의 “접수된 의견을 살피고, 운영안을 구체화하기 전에 확인할 조건을 정리한다”로 남아 있다. 의견 검토와 사전 조건 정리라는 기능, 운영안 구체화 전이라는 순서가 유지된다. | 보존 |
| 기간·요일·시각·미확정 상태 | 6주, 화요일과 목요일, 20:00, 기간이 정해진 시범 운영이며 영구 정책으로 확정되지 않았다는 내용이 후보 첫 문단에 있다. | 보존 |
| 응답 수와 해석 제한 | 42건 중 28건/9건/5건의 배분, 전체 이용자로 일반화할 수 없음, 응답 수로 이유를 알 수 없음, 현행 일정 선호도 고려할 필요가 후보 둘째 문단에 있다. | 보존 |
| 선호와 인과관계 구분 | 지지가 실제 방문의 증거는 아니라는 제한과 방문 증가를 일으킨다는 인과적 근거가 없다는 주장이 둘째 문단으로 함께 이동했다. 근거가 없음을 효과가 없음으로 바꾸지 않았다. | 보존 |
| 자원봉사 조건 | 해당 시간 참여 가능성이 미해결이며 운영 가능성 판단에 필요하고 시작 후로 미루기 어렵다는 내용, 관심을 인정하며 참여 가능성을 확인해야 한다는 후속 판단이 셋째 문단에 있다. | 보존 |
| 정원과 제공 범위 | 조용한 열람실 정원 12명, 연장 개관으로 정원이 늘지 않음, 시간과 수용 인원을 함께 검토할 필요가 셋째 문단에 있다. | 보존 |
| 논의와 안내의 기능 | 저녁 연장과 상시 운영 시간의 논의를 구분할 필요, 안내에서 차이를 전달할 의무, 영구 변경 확정으로 읽히지 않도록 표현을 점검할 필요, 이용 시간과 동시 수용 인원을 각각 안내할 의무가 마지막 문단에 남아 있다. | 보존 |
| 목적을 빈 서론으로 삭제할 위험 | `SKILL.md:50`이 문서 목적과 결정 단계도 실질적 의미임을 명시하며, `fidelity-and-documents.md`에도 해당 기능 누락의 예가 있다. 지침과 이번 후보가 일치한다. | 해당 사례에서 문제 없음 |
| 엄격한 50% 경계 | `iterative-review.md:39`와 `detector-report-format.md:39`가 `Human > 50%`에 정확히 50%를 허용하지 않는다. 구현 `check_detector_report.py:105–107`의 `gt`는 실제 `>` 비교다. 독립 실행에서도 경계가 배제됐다. | 올바름 |
| 점수 종류·단위 구분 | `iterative-review.md:37–39`가 Human 확률, Human 작성 텍스트 비중, AI 점수를 구분하고 100에서 AI 점수를 빼 Human 확률을 만들지 말라고 한다. 구현은 결과의 `metric`과 `unit`을 목표와 대조한다. | 검사 가능한 불일치 차단 |
| 무조건 통과 또는 저자 증명 약속 | `SKILL.md:77`, `iterative-review.md:53`이 보편적 비탐지·인간 저자 인증을 금지한다. 구현 반환값은 `authorship_assessed: false`, `receipt_authenticity_verified: false`, `semantic_review_required: true`다. | 해당 약속 없음 |

실행한 회귀 테스트: `python -B -m unittest discover -s outputs/bilingual-humanizer/evals -p test_*.py -v`. **45개 테스트 모두 통과**, 종료 코드 0. `test_iteration.py`의 경계·누락 결과·오래된 후보 해시·점수/단위 불일치·소수 정밀도·입력 덮어쓰기 방지 검사와 기존 보존 검사들이 포함된다.

기존 테스트와 별도로 `evaluate()`에 합성 자료를 전달한 독립 확인 10건도 모두 예상 결과와 일치했다. 이 자료는 스키마 동작을 확인하기 위한 가상 입력이며 실제 탐지기 점수가 아니다.

| 독립 확인 | 실제 반환 |
| --- | --- |
| Human >50 percent, 값 49.99 | `targets_unmet` |
| Human >50 percent, 값 50 | `targets_unmet` |
| Human >50 percent, 값 50.01 | `configured_targets_met` |
| Human >=50 percent, 값 50 | `configured_targets_met` |
| percent 목표에 fraction 결과 | `incomplete`, `unit_mismatch` |
| Human 문서 확률 목표에 Human 작성 비중 결과 | `incomplete`, `metric_mismatch` |
| Human 목표에 AI 확률 결과 | `incomplete`, `metric_mismatch` |
| 반올림된 51 percent | `incomplete`, `numeric_precision_unconfirmed` |
| Human >0.5 fraction, 값 0.5 | `targets_unmet` |
| Human >0.5 fraction, 값 0.5001 | `configured_targets_met` |

두 도서관 파일에 `audit_preservation.py`를 실행한 결과는 종료 코드 0, `no_surface_change_found`, 검토 후보 0개였다. 원문 1,069자, 후보 926자. 이 결과와 별개로 위 표의 의미·기능 비교를 직접 수행했다. 문자열 검사의 정상 결과만으로 의미 보존을 판정하지 않았다.

확인하지 못한 범위는 다음과 같다.

- 외부 탐지기에 문서를 제출하지 않았고 실제 영수증이나 점수도 평가하지 않았다. 보편적 탐지기 통과는 보장할 수 없다.
- 검사기는 양쪽에 같은 잘못된 `metric` 또는 `unit`을 적은 자료, 가짜 영수증, 제공자가 노출하지 않은 점수 정의를 독자적으로 검증할 수 없다. 문서가 이 제한을 명시하고 실제 제공자 출력과 대조하도록 요구하므로, 여기서는 숨겨진 기능 결함으로 분류하지 않는다.
- 이번 작업은 지정된 한국어 후보의 보존과 관련 지침·검사기 동작을 평가했다. 새 문서를 직접 다시 쓰게 한 행동 시험, 영어/혼합 언어 품질, 장문·서식 문서 성능, 인간의 자연스러움 평가는 실행하지 않았다.
- 후보는 읽을 수 있는 업무 검토문이며 정보 이동에 따른 명백한 연결 오류를 찾지 못했다. 한 사례에 대한 AI 독자의 판단으로 광범위한 문체 품질을 입증할 수는 없다.

검토 파일 식별값(SHA-256):

```text
SKILL.md
0a88f9718cd9005899f77864471d6b5cc0a45c3f7c6769ecce0539c93aebcacb
scripts/check_detector_report.py
d3d3cbf14133ccc6c6c3271c0e381da7f6d2ec4f55b6b39ac5fede3ede2843f1
work/deeper-trial/sources/ko-library.txt
b82f92389cf1c42ded62184eb359c87d81848723d44a2b9790b9fa0eb6dfd5b0
work/deeper-trial/v151-check/ko-library.txt
acaa27ffca3a17b28453b457572f6a838379ab5dc68c55330c6544e88b41cafb
```
