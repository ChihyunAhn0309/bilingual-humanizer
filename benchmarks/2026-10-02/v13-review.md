# v1.3.0 독립 재작성 검토 기록

## 범위와 방법

- 적용 지침: `outputs/bilingual-humanizer/SKILL.md` v1.3.0 및 structural-rewrite, iterative-review, fidelity-and-documents, korean, english, genres-and-voice references.
- 내용의 유일한 근거: `corpus/en-cache-source.txt`, `en-library-source.txt`, `ko-cache-source.txt`, `ko-library-source.txt`.
- 다른 버전의 재작성, 기존 평가 보고, 서비스 결과, receipts는 읽지 않았다. 네트워크 접근이나 외부 업로드를 하지 않았다.
- 원문의 의미·조건·양태·독자 행위를 먼저 묶고 문단을 다시 작성했다. 분량 목표나 축약률을 정하지 않았다. 한국어 평서형 문어체와 영어 업무 문어체를 유지했다.
- 아래 P1, P2 등은 각 최종 재작성의 빈 줄로 구분한 문단 번호이다.
- 보존 확인은 원문과의 의미 비교 및 독자 관점 검토로 실시했다. 별도로 로컬 `scripts/audit_preservation.py`를 사용했다. 이 스크립트는 의미 검토를 대체하지 않는다.

## 의미 및 독자 행위 coverage

### en-cache

| 원문의 distinct point / function | 재작성 위치와 보존 방식 |
| --- | --- |
| Fictional software cache trial; 48 runs | P1에 시험의 가상 성격과 횟수를 명시 |
| Median latency 120ms → 90ms; memory 256MB → 288MB | P1에 두 측정을 나란히 제시; 평균으로 바꾸지 않음 |
| Lower median relevant to further evaluation | P1의 worth further evaluation에 유지 |
| Median not every run; full distribution missing | P1에서 중앙값 바로 뒤에 결합 |
| Review must avoid invented consistency or exceptional cases | P1의 should not assume / speculate에 독자 행위 유지 |
| Measurements should be presented together | P2 첫 문장에 present 의무 유지 |
| Next decision should weigh both; latency-only view omits memory and harms context | P2에 별도 decision 행위와 그 이유를 결합 |
| Memory tradeoff acceptability requires an operating context absent from summary | P2에서 acceptable 여부의 조건과 정보 부재를 함께 명시 |
| Mobile clients excluded; findings tied to actual scope; mobile behavior open | P3에서 사실과 review/decision 범위 지시를 함께 보존 |
| Correlation, not causal production proof | P3에 그대로 보존 |
| Premature to confirm production benefit or generalize latency/memory balance to untested conditions | P3에서 이익과 비시험 조건 두 가지 일반화 금지를 각각 유지 |
| Rollout unapproved | P4 첫 문장 |
| Specified rollback: failure rate above 2%; further review should explicitly state it | P4에 기준과 후속 검토 행위를 통합; above를 at least로 바꾸지 않음 |
| Rollback neither approves deployment nor resolves evidence limits | P4에 두 독립 한계 유지 |
| Approval separate from interpretation of preliminary results | P4 마지막 문장 |

### en-library

| 원문의 distinct point / function | 재작성 위치와 보존 방식 |
| --- | --- |
| Proposed community-library pilot, 6 weeks, Tuesday and Thursday until 20:00 | P1에 제안의 양태 would 및 일정 유지 |
| Pilot temporary, not permanent policy; future-hours discussion must preserve distinction | P1에서 설명과 향후 논의 지시를 함께 보존 |
| Pilot decision separate from discussion of permanent change | P1 마지막 문장 |
| 42 forms: 28 later hours, 9 current schedule, 5 no preference | P2에 대상과 각 수치 대응 유지 |
| Submitted distribution useful starting point, not every user's needs | P2에 수치 바로 뒤 직접 한계 배치 |
| Consider support alongside reasons some prefer current schedule; neither speaks for everyone | P2에 두 집단 고려와 대표성 제한 유지; 실제 이유를 지어내지 않음 |
| Preference not resulting visit; no causal evidence longer hours increase attendance | P3에 두 관계 구분 |
| Review should keep attendance-evidence limit visible when weighing proposal | P3 마지막 문장에 실제 review 행위 유지 |
| Volunteer availability unresolved; not an after-start detail | P4에서 상태와 시점의 중요성 보존 |
| Decision can acknowledge interest while requiring coverage clarity | P4에서 can 양태와 clarity 요구를 함께 유지 |
| Volunteer issue affects whether proposed evening schedule is workable | P4 마지막 문장 |
| Quiet room capacity 12 unchanged by later hours | P5 첫 문장에 관계 단위로 결합 |
| Descriptions should consider capacity; communications should distinguish hours and quiet-use space | P5에서 두 행위를 같은 대상에 연결하되 각각 유지 |

### ko-cache

| 원문의 distinct point / function | 재작성 위치와 보존 방식 |
| --- | --- |
| 가상 소프트웨어 캐시 시험 48회 | P1 첫 문장 |
| 지연 시간 중앙값 120ms → 90ms; 메모리 256MB → 288MB | P1에서 측정 대상·단위·방향 유지 |
| 중앙값 하락은 추가 검토 참고 가능 | P1의 참고할 수 있다에 양태 유지 |
| 모든 실행이 같다는 뜻 아님; 전체 분포 없음; 일관성·예외 임의 설명 금지 | P1에 중앙값의 직접적 한계와 독자 행위를 묶음 |
| 평가 시 두 측정 함께 제시; 다음 판단에서도 함께 검토 | P2 첫 문장에 제시와 검토 두 행위를 유지 |
| 지연 시간만 강조하면 메모리 증가가 빠질 수 있음 | P2에 가능성 양태 유지 |
| 메모리 증가 수용 여부는 운영 환경과 조건에 달림 | P2에서 증가 수치 해석에 필요한 조건 유지 |
| 요약에 없는 조건을 확인된 사실로 보태지 않아야 함 | P2 마지막 절 |
| 모바일 제외; 설명은 시험 범위 내; 이후 판단은 모바일 결론 유보 | P3에 사실 및 설명·판단 지시 결합 |
| 관찰은 상관관계, 운영 환경 재현의 인과 증거 아님 | P3 가운데 |
| 실제 서비스 이익 확정과 미시험 조건 일반화 어려움 | P3에 두 한계 유지 |
| 긍정적인 수치를 소개할 때 한계를 함께 전달할 필요 | P3 마지막 문장에 전달 행위 유지 |
| 운영 도입 미승인 | P4 첫 문장 |
| 실패율 2% 초과 롤백; 후속 검토에 명시 의무 | P4 두 번째 문장; 초과 경계 유지 |
| 롤백 기준은 배포 승인 대체 불가 및 시험 범위 한계 해결 불가 | P4 마지막 문장 앞부분 |
| 결과 해석과 실제 도입 승인 각각 필요한 판단으로 다루는 것이 적절 | P4 마지막 절에 권고 강도 유지 |

### ko-library

| 원문의 distinct point / function | 재작성 위치와 보존 방식 |
| --- | --- |
| 지역 도서관 시범 운영안: 6주, 화·목 저녁, 20:00까지 연장 | P1에 일정·제안 지위 유지 |
| 한시적 방안; 영구 정책 확정 아님 | P1에 임시 범위와 미확정 지위 유지 |
| 연장 운영과 향후 상시 운영 논의 구분 필요 | P1 가운데 |
| 안내 시 구분 명확히 전달 의무 | P1에 안내 행위 유지 |
| 시범 결정이 영구 일정 변경 확정으로 읽히지 않게 문서 점검 필요 | P1 마지막 문장에 점검 권고 유지 |
| 의견서 42건: 28 연장 지지, 9 현행 선호, 5 선호 없음 | P2 첫 문장 |
| 분포는 알 수 있으나 모든 이용자 요구 대표 불가 | P2에서 수치와 직접 한계 결합 |
| 응답 수로 각 의견 이유까지 알 수 있다고 가정 금지 | P2 세 번째 문장에 명시적 금지 유지 |
| 연장 관심 인정 및 현행 선호 함께 고려 | P2 네 번째 문장 |
| 지지는 선호이며 실제 방문 증거와 구분; 연장→방문 증가 인과 근거 없음 | P2에 구분과 인과 한계 유지 |
| 검토에서 한계를 유지하면 과잉 해석 없이 논의 가능 | P2 마지막 문장의 조건·가능성 유지 |
| 자원봉사 참여 미해결; 운영 가능 판단에 필요; 운영 이후로 넘기기 어려움 | P3에서 상태·의존관계·시점 유지 |
| 이후 판단에서 자원봉사 참여 가능성 확인 의무 | P3 첫 문장에 구체화 전 확인 행위 배치 |
| 조용한 열람실 12명; 시간 연장으로 정원 증가하지 않음 | P4 첫 문장에 관계 결합 |
| 제공 범위 검토 시 시간·정원 함께 고려 필요 | P4 두 번째 문장에 검토 행위 유지 |
| 이용 안내에 시간·동시 수용 인원 각각 설명 의무 | P4 마지막 문장에 안내 행위 유지 |

## 구조와 독자 품질 검토

- 두 cache 문서에서 중앙값 설명과 실행별 분포 부재를 P1로 묶었다. 결과 전체를 보고하라는 지시와 다음 판단에서 두 변화를 함께 검토하라는 지시는 P2의 한 대상에 연결했다. 모바일 범위에 관한 설명·판단 지시는 P3에, 롤백 명시와 승인 구분은 P4에 배치했다.
- en-library는 의견 분포와 방문 증거의 한계를 연속 문단으로 분리하고, 자원봉사 문제와 열람실 정원을 각각 독립 문단으로 정리했다. 마지막 문단은 일반적인 결론 대신 안내에 필요한 시간·공간 구분으로 끝난다.
- ko-library는 시범/영구 구분을 P1에 묶고 안내·문서 점검을 같은 대상에 연결했다. 의견 분포와 대표성·이유·방문 증거 한계를 P2에 두었다. 자원봉사 확인은 P3, 시간·정원 검토와 안내는 P4로 나눴다.
- 정량 목표를 맞추기 위한 삭제, 구어체 삽입, 경험·주체·이유·효과의 창작은 하지 않았다. 자체 초안 검토에서 ko-library에 잠시 들어간 도서관이 직접 검토한다는 주체를 제거했으며, 원문의 가능성 표현을 강한 의무로 바꾸었던 구절도 바로잡았다.

## 독립 검토 및 최종 확인

동일 모델의 신규 문맥 subagent `/root/v13_rewrite_eval/reader_review`가 원문과 당시 후보 8개를 1회 비교했다. 기존 평가나 작성자의 자체 점수는 전달하지 않았으며, reviewer는 파일 수정이나 외부 접근을 하지 않았다. 사람의 독립 검증이나 다른 모델의 검증으로 보고하지 않는다.

독립 검토 결과, en-cache, en-library, ko-cache에는 구체적 결함이 없었다. ko-library에는 낮은 중요도의 실제 결함 두 가지가 있었다.

1. 원문의 안내 의무 `전달해야 한다`가 후보의 `밝히고, … 점검할 필요가 있다`에 통합되어 안내와 점검의 양태가 같아졌다. 최종본은 `안내에서도 이 구분을 분명히 밝혀야 하며, … 문서 표현을 점검할 필요가 있다`로 분리해 두 행위의 강도를 복원했다.
2. `응답 수만으로 각 의견의 이유까지 알 수 있다고 가정해서는 안 된다`는 독자의 추론을 금하는 지시가 수치의 설명력 한계라는 사실 설명으로만 남았다. 최종본에 원문의 명시적 금지 문장을 복원했다.

이 수정과 함께 첫 문장에 개관 시간의 **연장**을 명시하고, 첫 문단에 영구적인 운영 정책으로 **확정되지 않았음**을 직접 적었다. 기존 의미를 더 명확히 드러내는 보존 보강이며 새로운 정책이나 주체를 추가하지 않았다.

초기 후보 작성 후 자체 fidelity 점검, 신규 문맥 reader/fidelity 검토 1회, 그 결과에 따른 ko-library 수정 1회, 최종 원문 대조 및 reader 자체 검토를 완료했다. 최종 후보에 대한 두 번째 독립 검토는 실시하지 않았다. 실제 독립 검토에 사용된 ko-library 후보의 SHA-256은 `f621e5f3b3f7cf3aa9d2756d505fb129bf10880094e6e603d9937e1c1a1b9782`이며, 수정된 최종본의 해시는 아래에 별도로 기록한다. 나머지 세 후보는 독립 검토 이후 변경하지 않았다.

최종 자체 검토에서 원문과 다른 수치·주체·조건·양태, 지시 행위 누락, 부자연스러운 문장 연결은 발견하지 못했다. 미해결 fidelity 또는 reader-quality finding은 없다. 이는 실제 검토 결과이며 보편적인 문체 점수나 저자 판정은 아니다.


## 최종 파일 식별자와 단어 수

단어 수는 UTF-8 본문을 공백으로 분리한 토큰 수이다. 한국어에서는 어절 수이며 형태소 단어 수를 뜻하지 않는다. 해시는 파일 바이트 기준 SHA-256이다.

| 문서 | 원문 단어/어절 수 | 최종 단어/어절 수 | 최종 문단 수 | 표면 보존 감사 |
| --- | ---: | ---: | ---: | --- |
| en-cache | 302 | 224 | 4 | exit 0; no_surface_change_found |
| en-library | 302 | 249 | 5 | exit 0; no_surface_change_found |
| ko-cache | 264 | 192 | 4 | exit 0; no_surface_change_found |
| ko-library | 264 | 214 | 4 | exit 0; no_surface_change_found |

네 파일 모두 숫자·단위 등 표면 특징에 대한 review_candidates가 없었다. 수치의 대상, 범위, 인과관계와 실제 지시 행위는 위의 별도 의미 검토로 확인했다. 변경되지 않은 세 파일은 최초 감사 결과를 유지했고, ko-library만 수정 후 재실행했다.

| 파일 | SHA-256 |
| --- | --- |
| `en-cache-source.txt` | `4411dc7c9875e0a6455d3dc9a1790e68ea371f38d2a750599b2444c9bc2ec509` |
| `en-cache-v13.txt` | `d7a2732e5f9051c6126ebaeaf350ab3a6fd2f7f51ac7bb34feaacceb6b95a20e` |
| `en-library-source.txt` | `bdcb854f5676ebff48f3a958d11ae3209ee42f8ece11f4ba933488c6d0b6029f` |
| `en-library-v13.txt` | `527e6f55ec652c20592f6d00d6681d4e61c47d68aa2ead23fb93a60fd067ab45` |
| `ko-cache-source.txt` | `8c6997b3b5a9bce066216fa41bd84feeb357975e7ec1e6cf51bd7765dfa7dc7b` |
| `ko-cache-v13.txt` | `e61a16d568044df0447988afd6d033dfa2f946d04c753a4308a52b8c6652475a` |
| `ko-library-source.txt` | `b82f92389cf1c42ded62184eb359c87d81848723d44a2b9790b9fa0eb6dfd5b0` |
| `ko-library-v13.txt` | `fa8f7b7bfdc27a1ff87d9bb5483a89617cc18f0e95f40cc93ae4cbe2cd4aacb3` |
