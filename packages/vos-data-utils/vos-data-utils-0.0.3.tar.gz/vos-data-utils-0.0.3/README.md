vos-data-utils <br>
[![PyPI version](https://badge.fury.io/py/vos-data-utils.svg)](https://pypi.org/project/vos-data-utils/)
========

vos-data-utils is a shared utility library essential for 'Value of Space' data works

</br>

# Notable Changes

<details>
<summary><strong>Version 0.0.1 - 2024.01</strong></summary>

<div style="color: gray;">

-   공간의가치 데이터 작업 공용 유틸리티 라이브러리 최초 배포
-   구성원의 개별 라이브러리([vos-mjjo](https://pypi.org/project/vos-mjjo/), [nqnq](https://pypi.org/project/nqnq/)) 기능 통합
-   업데이트
    -   법정동 데이터 업데이트(행정구역 변경사항 반영)

</details>

</br>

# Install

```python
pip install vos-data-utils
```

</br>

# Usage

## Cordate(Correct Date)

8자리의 날짜(`YYYYMMDD`) 형식으로 작성되어 있지 못하고 6자리(`YYYYMM` or `YYMMDD`, ...) 혹은 다른 자리수로 날짜와 오타 혹은 오기입으로 현재시점에서 부적절한 날짜가 제공되었을 경우, 이를 교정하여 8자리의 날짜(`YYYYMMDD`) 형식으로 전달하는 모듈\
해당 날짜 교정 모듈은 **건축물대장 날짜**(`착공연월`, `허가연월`, `준공연월`)를 교정하기 위해 개발되었으며 건축물대장 날짜 특성상 현재 기준으로 미래 날짜는 존재할 수 없기 때문에 현재를 기준으로 과거 날짜로만 교정됨

해당 날짜 교정 모듈에서 날짜를 교정하는 알고리즘은 2가지로\
첫번째는 연, 월, 일의 범위와 규칙을 이용하여 `현재 날짜` 까지 생성 가능한 모든 날짜 리스트와 최신 날짜로 교정하는 방법\
두번째는 미리 생성되어 있는 건축물대장 날짜 빈도 딕셔너리(`data.date_dictionary.txt`)에서 거리(날짜 문자열간의 차이 문자열 개수)와 빈도를 이용하여 가장 유사한 리스트와 최유사 날짜로 교정하는 방법으로 구성되어 있음

<details>
<summary><strong>Show instructions</strong></summary>
<br></br>

**`cordate.get_correct_array`**

-   입력된 문자열을 이용해 날짜 생성 규칙에 따라 현재 날짜까지 생성 가능한 모든 날짜를 리스트로 리턴
-   날짜 생성 규칙이란 연, 월, 일의 범위를 이용하는것으로 연도는 올해연도까지, 월은 1부터 12월까지, 일은 월별로 지정된 일까지를 의미하며 `YYYYMMDD` 형식의 날짜에서 연도는 4자리, 월, 일은 2자리로 표기하지만 자리수 범위는 각 [0:4],[0:2],[0:2] 차지함
-   Example

    -   Run

        ```python
        from vdutils import cordate

        cordate.get_correct_array("99990101")
        cordate.get_correct_array("9990101")
        cordate.get_correct_array("990101")
        cordate.get_correct_array("199901")
        cordate.get_correct_array("019991")
        cordate.get_correct_array("19991")
        cordate.get_correct_array("1999")
        cordate.get_correct_array("9901")

        ```

    -   Output

        ```python
        []
        ["19990101"]
        ["19900101", "19901001", "19990101"]
        ["01990901", "19990101"]
        ["01990901", "19990101"]
        ["01990901", "19990101"]
        ["01990109", "00190909", "01990901", "19990101"]
        ["19900101", "00090901", "19990101"]
        ```

</br>

**`cordate.get_correct_one`**

-   입력된 문자열을 이용해 날짜 생성 규칙에 따라 현재 날짜까지 생성 가능한 모든 날짜 리스트중 가장 최신날짜를 리턴
-   날짜 생성 규칙이란 연,월,일의 범위를 이용하는것으로 연도는 올해연도까지, 월은 1부터 12월까지, 일은 월별로 지정된 일까지를 의미하며 YYYYMMDD 형식의 날짜에서 연도는 4자리, 월, 일은 2자리로 표기하지만 자리수 범위는 각 [0:4],[0:2],[0:2] 차지
-   Example

    -   Run

        ```python
        from vdutils import cordate

        cordate.get_correct_one("99990101")
        cordate.get_correct_one("9990101")
        cordate.get_correct_one("990101")
        cordate.get_correct_one("199901")
        cordate.get_correct_one("019991")
        cordate.get_correct_one("19991")
        cordate.get_correct_one("1999")
        cordate.get_correct_one("9901")

        ```

    -   Output

        ```python
        None
        "19990101"
        "19990101"
        "19990101"
        "19990101"
        "19990101"
        "19990101"
        "19990101"
        ```

</br>

**`cordate.look_up_array`**

-   건축물대장 날짜 빈도 딕셔너리(`data.date_dictionary.txt`) 로드 필요
-   입력된 문자열을 이용해 data 건축물대장 날짜 빈도 딕셔너리(`data.date_dictionary.txt`) 에서 Symspellpy(`max_distance=2`) 알고리즘 적용하여 유사한 날짜 리스트 리턴
-   유사도 가중은 거리, 빈도 순으로 거리가 가까운 순서로 빈도수가 많은 순서로 정렬
-   Example

    -   Run

        ```python
        from vdutils import cordate

        CD = cordate.CorDate()
        CD.load_date_dictionary() # 라이브러리 배포 폴더에 있는 date_dictionary.txt 로드
        CD.look_up_array("99990101")
        ```

    -   Output

        ```python
        [<symspellpy.suggest_item.SuggestItem at 0x7fe5facdab60>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad145e0>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad15960>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad14220>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad164a0>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad151e0>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad155a0>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5facf5870>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad0c4c0>,
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad0c520>,
        ...]
        ```

    -   Run

        ```python
        from vdutils import cordate

        CD = cordate.CorDate()
        CD.load_date_dictionary() # 라이브러리 배포 폴더에 있는 date_dictionary.txt 로드

        suggestions = CD.look_up_array("99990101")
        for sugg in suggestions: # symspellpy.suggest_item 타입의 리스트는 반복문을 이용해 값을 확인 가능
            print(sugg)
        ```

    -   Output

        ```python
        19990101, 1, 716 # term, distance, count
        19980101, 2, 1361
        19960101, 2, 1351
        19970101, 2, 1317
        19950101, 2, 1286
        19940101, 2, 1236
        19920101, 2, 870
        19930101, 2, 843
        19910101, 2, 816
        19990901, 2, 743
        ...
        ```

</br>

**`cordate.look_up_one`**

-   건축물대장 날짜 빈도 딕셔너리(`data.date_dictionary.txt`) 로드 필요
-   입력된 문자열을 이용해 data 건축물대장 날짜 빈도 딕셔너리(`data.date_dictionary.txt`) 에서 Symspellpy(`max_distance=2`) 알고리즘 적용하여 거리, 빈도 순으로 유사도 정렬된 날짜 리스트 중 첫번째 날짜(최유사)를 리턴
-   Example

    -   Run

        ```python
        from vdutils import cordate

        CD = cordate.CorDate()
        CD.load_date_dictionary() # 라이브러리 배포 폴더에 있는 date_dictionary.txt 로드
        CD.look_up_one("99990101")
        ```

    -   Output

        ```python
        <symspellpy.suggest_item.SuggestItem at 0x7fe5fad0c190>
        ```

    -   Run

        ```python
        from vdutils import cordate

        CD = cordate.CorDate()
        CD.load_date_dictionary() # 라이브러리 배포 폴더에 있는 date_dictionary.txt 로드
        print(CD.look_up_one("99990101")) # symspellpy.suggest_item 타입의 값 출력문을 이용해 확인 가능
        ```

    -   Output

        ```python
        19990101, 1, 158 # term, distance, count
        ```

</br>

**`cordate.look_up_array_clean`**

-   cordate.look_up_array 와 동일하지만 symspellypy.suggest_item.SuggestItem 타입 리스트를 정렬을 유지한 날짜값만 추출하여 리스트 리턴
-   Example

    -   Run

        ```python
        from vdutils import cordate

        CD = cordate.CorDate()
        CD.load_date_dictionary() # 라이브러리 배포 폴더에 있는 date_dictionary.txt 로드
        CD.look_up_array_clean("99990101")
        ```

    -   Output

        ```python
        ['19990101',
        '19980101',
        '19960101',
        '19970101',
        '19950101',
        '19940101',
        '19920101',
        '19930101',
        '19910101',
        ...]
        ```

</br>

**`cordate.look_up_one_clean`**

-   cordate.look_up_one 과 동일하지만 symspellypy.suggest_item.SuggestItem 타입 리스트를 정렬을 유지한 날짜값만 추출하여 리스트 리턴
-   Example

    -   Run

        ```python
        from vdutils import cordate

        CD = cordate.CorDate()
        CD.load_date_dictionary() # 라이브러리 배포 폴더에 있는 date_dictionary.txt 로드
        CD.look_up_one_clean("99990101")
        ```

    -   Output

        ```python
        '19990101'
        ```

</br>

</details><br>

## ConvAddr(Convert Address)

법정동 변경내역을 기반으로 과거 법정동명의 주소를 입력시에 현행 법정동으로 변환하여 전달하는 모듈\
입력되는 주소는 시도, 시군구, 읍면동, 동리, 번지 순으로 기재되는 지번 체계를 기반으로 하며 해당 법정동 교정 모듈에서는 법정동(시도, 시군구, 읍면동, 동리)와 번지 사이의 공백을 일부 교정하고 과거 법정동명으로 입력되었을 경우 현행 법정동명으로 교체함\
법정동명 교체 예시로는 `인천직할시` -> `인천광역시`, `강원도` -> `강원특별자치도`, `경북 군위군` -> `대구 군위군` 등을 들 수 있으며 시도, 시군구, 읍면동, 동리 모든 변경사항에 적용됨

<details>
<summary><strong>Show instructions</strong></summary>
<br></br>

**`convaddr.correct_simple_spacing`**

-   입력된 주소 문자열(한글로 이루어진 지번 체계 주소)의 2개 이상의 연속된 공백을 단일 공백으로 변환하여 리턴
-   Example

    -   Run

        ```python
        from vdutils import convaddr

        CA = convaddr.ConvAddr()
        print(CA.correct_simple_spacing(addr="서울시 강남구  삼성동 1"))
        ```

    -   Output

        ```python
        서울시 강남구 삼성동 1
        ```

</br>

**`convaddr.correct_smallest_bjd_spacing`**

-   입력된 주소 문자열(한글로 이루어진 지번 체계 주소)의 최소 단위 법정동명("가", "동", "로", "리")과 번지 사이의 공백이 없을경우 단일 공백을 추가하여 리턴
-   Example

    -   Run

        ```python
        from vdutils import convaddr

        CA = convaddr.ConvAddr()
        print(CA.correct_smallest_bjd_spacing(addr="서울시 강남구 삼성동1"))
        ```

    -   Output

        ```python
        서울시 강남구 삼성동 1
        ```

</br>

**`convaddr.correct_changed_bjd`**

-   입력된 주소 문자열(한글로 이루어진 지번 체계 주소)의 과거 법정동명이 존재하면 변경 후 법정동명으로 변환하여 리턴
-   is_log == True 일 경우, 변경 전 후 법정동명을 출력
-   Example

    -   Run

        ```python
        from vdutils import convaddr

        CA = convaddr.ConvAddr()
        print(CA.correct_changed_bjd(addr="강원도 춘천시 서면 현암리 1-1", is_log=False))
        ```

    -   Output

        ```python
        강원특별자치도 춘천시 서면 현암리 1-1
        ```

    -   Run

        ```python
        from vdutils import convaddr

        CA = convaddr.ConvAddr()
        print(CA.correct_changed_bjd(addr="강원도 춘천시 서면 현암리 1-1", is_log=True))
        ```

    -   Output

        ```python
        2024-01-17 14:03:27 | [INFO] | 강원도 춘천시 서면 현암리
        2024-01-17 14:03:27 | [INFO] | 해당 법정동명은 변경되었습니다. 변경전 : [ 강원도 춘천시 서면 현암리 ] 변경후 : [ 강원특별자치도 춘천시 서면 현암리 ]
        강원특별자치도 춘천시 서면 현암리
        ```

</br>

**`convaddr.correct_bjd`**

-   입력된 주소 문자열(한글로 이루어진 지번 체계 주소)의 correct_simple_spacing(법정동 사이 2개 이상의 연속된 공백을 단일 공백으로 변경하는 함수), correct_smallest_bjd_spacing(최소단위 법정동과 번지 사이 공백 수정하는 함수), correct_changed_bjd(과거 법정동명 현행 법정동명으로 교정하는 함수) 순차적으로 실행하여 교정된 현행 주소 문자열을 리턴
-   is_log == True 일 경우, 변경 전 후 법정동명을 출력
-   Example

    -   Run

        ```python
        from vdutils import convaddr

        CA = convaddr.ConvAddr()
        print(CA.correct_bjd(addr="서울시 강남구 삼성동 1", is_log=False))
        ```

    -   Output

        ```python
        서울시 강남구 삼성동 1
        ```

    -   Run

        ```python
        from vdutils import convaddr

        CA = convaddr.ConvAddr()
        print(CA.correct_bjd(addr="강원도춘천시 서면 현암리 1-1", is_log=False))
        print(CA.correct_bjd(addr="강원도 춘천 시 서면 현암리 1-1", is_log=False))
        print(CA.correct_bjd(addr="강원도 춘천시 서면 현암리", is_log=False))
        print(CA.correct_bjd(addr="강원도 춘천시 서면 현암리 1-1", is_log=False))
        print(CA.correct_bjd(addr="강원도 춘천시 서면 현암리1-1", is_log=False))
        print(CA.correct_bjd(addr="강원도   춘천시 서면 현암리 1-1", is_log=False))
        ```

    -   Output

        ```python
        강원도춘천시 서면 현암리 1-1 # 시도, 시군구와 같이 최소단위 법정동의 띄어쓰기가 올바르지 않을 경우, 변환 불가
        강원도 춘천 시 서면 현암리 1-1 # 시도, 시군구와 같이 최소단위 법정동의 띄어쓰기가 올바르지 않을 경우, 변환 불가
        강원특별자치도 춘천시 서면 현암리
        강원특별자치도 춘천시 서면 현암리 1-1
        강원특별자치도 춘천시 서면 현암리 1-1
        강원특별자치도 춘천시 서면 현암리 1-1
        ```

    </details><br>

## BjdConnector

관리중인 전체기간(1988-)의 법정동의 전체 및 단위(시도, 시군구, 읍면동, 동리) 법정동을 오브젝트(Object)화하고 이를 법정동 체계에 따라 단위 법정동(시도, 시군구, 읍면동, 동리)간의 관계와 변경내역을 기반으로 변경 전 후 법정동의 관계를 그래프(Graph)화하여 딕셔너리로 생성하는 모듈\
법정동의 전체 및 단위 오브젝트 예시로는 `서울특별시 강남구 삼성동`의 경우,

-   전체 법정동은 `서울특별시 강남구 삼성동`
-   단위 법정동은 시도 단위의 `서울특별시`, 시군구 단위의 `강남구`, 읍면동 단위의 `삼성동`, 동리 단위는 `없음(Null)`
-   단위 법정동은 시도 단위 > 시군구 단위 > 읍면동 단위 > 동리 단위 순으로 포함관계, 부모자식관계이며 BjdConnectorGraph는 위와 같은 단위 법정동 관계들을 구조적으로 형성한 딕셔너리임

변경 전 후 법정동의 관계 그래프(Graph)는 전체 법정동을 오브젝트로 관리하며

<details>
<summary><strong>Show instructions</strong></summary>
<br></br>

**`BjdConnectorGraph`**

-   단위 법정동 커넥터 그래프(Graph) 클래스
-   단위 법정동 커넥터 그래프(Graph) 는 **단위 법정동간의 관계**를 정의한 그래프
    ```
    |-- 시도 (Node)
    |   |
    |   |-- 시군구 (Node)
    |   |   |
    |   |   |-- 읍면동 (Node)
    |   |   |   |
    |   |   |   |-- 동리 (Node)
    |   |   |   |-- 동리 (Node)
    |   |   |   |-- ...
    |   |   |-- 읍면동 (Node)
    |   |   |   |
    |   |   |   |-- 동리 (Node)
    |   |   |   |-- 동리 (Node)
    |   |   |   |-- ...
    |   |   |-- ...
    |   |
    |   |-- 시군구 (Node)
    |   |   |
    |   |   |-- 읍면동 (Node)
    |   |   |-- 읍면동 (Node)
    |   |   |-- ...
    |   |-- ...
    |-- ...
    ```
-   단위 법정동 커넥터 그래프(Graph) 는 단위 법정동 커넥터(Connector)들을 생성하고 관계를 설정하여 각 단위 법정동 커넥터(Connector)의 값을 업데이트 함. 또한 결과물을 key, value{단위 법정동 코드: 단위 법정동 커넥터(Connector)} 형태의 딕셔너리(dictionary) `bjd_connectors` 와 데이터프레임(pandas.DataFrame()) `bjd_current_df` 로 생성하고 편집하여 보유함
-   Example

    -   Run

        ```python
        from vdutils.bjdconnector import BjdConnectorGraph

        BCG = BjdConnectorGraph()
        BCG.bjd_connectors
        ```

    -   Output

        ```
        {'1100000000': BjdConnector(),
        '1111000000': BjdConnector(),
        '1111010100': BjdConnector(),
        '1111010200': BjdConnector(),
        '1111010300': BjdConnector(),
        '1111010400': BjdConnector(),
        '1111010500': BjdConnector(),
        '1111010600': BjdConnector(),
        '1111010700': BjdConnector(),
        '1111010800': BjdConnector(),
        '1111010900': BjdConnector(),
        ...}
        ```

</br>

**`BjdConnector`**

-   단위 법정동 커넥터(Connector) 클래스
-   단위 법정동 커넥터(Connector) 는 해당 단위 법정동의 오브젝트(Object)를 메타데이터(metadata)로 보유하며, 단위 법정동 코드(`bjd_cd`), 단위 법정동 명(`bjd_nm`), 단위 법정동 타입(`typ`), 상위 법정동 코드 리스트(`top_bjd_cd`), 상위 법정동 명 리스트(`top_bjd_nm`), 상위 법정동 커넥터(`top_bjd`), 하위 법정동 코드(`bottom_bjd_cd`), 하위 법정동 명(`bottom_bjd_nm`), 하위 법정동 커넥터(`bottom_bjd`) 등의 데이터를 포함하고 있음
-   단위 법정동 커넥터 구조는 아래와 같음

    -   Class

        ```python
        @dataclass
        class BjdConnector():

            def __init__(
                self,
                bjd_cd: str,
                full_bjd_nm: str
            ):
                self.typ: str = None
                self.bjd_cd: str = bjd_cd
                self.bjd_nm: str = None
                self.full_bjd_nm: str = full_bjd_nm
                self.metadata: BjdObject() = None
                self.top_bjd_typ: Optional[str] = None
                self.top_bjd_cd: List[str] = []
                self.top_bjd_nm: List[str] = []
                self.top_bjd: List[BjdConnector()] = []
                self.bottom_bjd_cd: List[str] = []
                self.bottom_bjd_nm: List[str] = []
                self.bottom_bjd: List[BjdConnector()] = []
                self.is_smallest: bool = None
                self._update_metadata()
                self._update_top_bjd()
        ```

-   Example

    -   Run

        ```python
        from vdutils.bjdconnector import BjdConnectorGraph

        BCG = BjdConnectorGraph()
        BCG.bjd_connectors.get('1100000000')._print()
        ```

    -   Output

        ```
        typ: sido
        bjd_cd: 1100000000
        bjd_nm: 서울특별시
        full_bjd_nm: 서울특별시
        metadata: BjdObject()
        top_bjd_typ: None
        top_bjd_cd: []
        top_bjd_nm: []
        top_bjd: []
        bottom_bjd_cd: ['1111000000', '1114000000', '1117000000', '1120000000', '1121500000', '1123000000', '1126000000', '1129000000', '1130500000', '1132000000', '1135000000', '1138000000', '1141000000', '1144000000', '1147000000', '1150000000', '1153000000', '1154500000', '1156000000', '1159000000', '1162000000', '1165000000', '1168000000', '1171000000', '1174000000']
        bottom_bjd_nm: ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
        bottom_bjd: [BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector()]
        is_smallest: False
        ```

</br>

**`BjdObject`**

-   단위 법정동 오브젝트(Object) 클래스
-   단위 법정동 오브젝트(Object) 는 해당 단위 법정동의 단위 법정동 코드(`bjd_cd`), 단위 법정동 명(`bjd_nm`), 단위 법정동 타입(`typ`) 등의 데이터를 포함하고 있음
-   BjdConnector 의 메타데이터(metadata) 값으로 되어있음
-   단위 법정동 오브젝트(Object) 구조는 아래와 같음

    -   Class

        ```python
        @dataclass
        class BjdObject():

            def __init__(
                self,
                bjd_cd: str,
                full_bjd_nm: str
            ):
                self.bjd_cd: str = bjd_cd
                self.full_bjd_nm: str = full_bjd_nm
                self.typ: str = None
                self.sido: Optional[bool] = None
                self.sgg: Optional[bool] = None
                self.emd: Optional[bool] = None
                self.ri: Optional[bool] = None
                self.sido_nm: Optional[str] = None
                self.sgg_nm: Optional[str] = None
                self.emd_nm: Optional[str] = None
                self.ri_nm: Optional[str] = None
                self.sido_cd: Optional[str] = None
                self.sgg_cd: Optional[str] = None
                self.emd_cd: Optional[str] = None
                self.ri_cd: Optional[str] = None
                self.bjd_nm: str = None
                self._prepare()
        ```

-   Example

    -   Run

        ```python
        from vdutils.bjdconnector import BjdConnectorGraph

        BCG = BjdConnectorGraph()
        BCG.bjd_connectors.get('1100000000').metadata._print()
        ```

    -   Output

        ```
        bjd_cd: 1100000000
        bjd_nm: 서울특별시
        full_bjd_nm: 서울특별시
        typ: sido
        sido: True
        sgg: None
        emd: None
        ri: None
        sido_nm: 서울특별시
        sgg_nm: None
        emd_nm: None
        ri_nm: None
        sido_cd: 1100000000
        sgg_cd: None
        emd_cd: None
        ri_cd: None
        ```

</br>

**`FullBjdConnectorGraph`**

-   법정동 커넥터 그래프(Graph) 클래스
-   법정동 커넥터 그래프(Graph) 는 BjdConnectorGraph 에 **변경 전 후 관계**를 추가한 그래프
-   법정동 커넥터 그래프(Graph) 는 법정동 커넥터(Connector)들을 생성하고 관계를 설정하여 각 법정동 커넥터(Connector)의 값을 업데이트 함. 또한 결과물을 key, value{법정동 코드: 법정동 커넥터(Connector)} 형태의 딕셔너리(dictionary) `full_bjd_connectors` 와 데이터프레임(pandas.DataFrame()) `bjd_df` 로 생성하고 편집하여 보유함
-   Example

    -   Run

        ```python
        from vdutils.bjdconnector import FullBjdConnectorGraph

        FBCG = FullBjdConnectorGraph()
        FBCG.bjd_connectors
        ```

    -   Output

        ```
        {'1100000000': FullBjdConnector(),
        '1111000000': FullBjdConnector(),
        '1111010100': FullBjdConnector(),
        '1111010200': FullBjdConnector(),
        '1111010300': FullBjdConnector(),
        '1111010400': FullBjdConnector(),
        '1111010500': FullBjdConnector(),
        '1111010600': FullBjdConnector(),
        '1111010700': FullBjdConnector(),
        '1111010800': FullBjdConnector(),
        '1111010900': FullBjdConnector(),
        ...}
        ```

</br>

**`FullBjdConnector`**

-   법정동 커넥터(Connector) 클래스
-   법정동 커넥터(Connector) 는 법정동 코드(`full_bjd_cd`), 법정동 명(`full_bjd_nm`), 현재 존재 여부(`is_exist`), 생성일(`created_dt`), 삭제일(`deleted_dt`), 변경 전 법정동 코드(`before_bjd_cd`), 변경 전 법정동 커넥터 리스트(`before`), 변경 후 법정동 커넥터 리스트(`after`), 각 단위 법정동별 BjdConnector(`sido_bjd_connector`, `sgg_bjd_connector`, `emd_bjd_connector`, `ri_bjd_connector`) 등의 데이터를 포함하고 있음
-   변경 전 법정동 커넥터 리스트(`before`)와 변경 후 법정동 커넥터 리스트(`after`)가 리스트 타입인 이유는 여러 법정동의 일정 영역을 분리해서 새로운 법정동이 생성되거나 사라지는 등의 법정동의 관계가 일대일 관계가 일대다 혹은 다대일 관계와 같은 예외적인 경우도 존재하기 때문
-   법정동 커넥터 구조는 아래와 같음

    -   Class

        ```python
        @dataclass
        class FullBjdConnector():

            def __init__(
                self,
                full_bjd_cd: str,
                full_bjd_nm: str,
                created_dt: str,
                deleted_dt: str,
                before_bjd_cd: str
            ):
                self.full_bjd_cd: str = full_bjd_cd
                self.full_bjd_nm: str = full_bjd_nm
                self.is_exist: bool = None
                self.created_dt: Optional[str] = created_dt
                self.deleted_dt: Optional[str] = deleted_dt
                self.before_bjd_cd: Optional[str] = before_bjd_cd
                self.before: List[FullBjdConnector] = []
                self.after: List[FullBjdConnector] = []
                self.is_smallest: bool = None
                self.sido: Optional[bool] = None
                self.sgg: Optional[bool] = None
                self.emd: Optional[bool] = None
                self.ri: Optional[bool] = None
                self.sido_nm: Optional[str] = None
                self.sgg_nm: Optional[str] = None
                self.emd_nm: Optional[str] = None
                self.ri_nm: Optional[str] = None
                self.sido_cd: Optional[str] = None
                self.sgg_cd: Optional[str] = None
                self.emd_cd: Optional[str] = None
                self.ri_cd: Optional[str] = None
                self.sido_bjd_connector: Optional[BjdConnector] = None
                self.sgg_bjd_connector: Optional[BjdConnector] = None
                self.emd_bjd_connector: Optional[BjdConnector] = None
                self.ri_bjd_connector: Optional[BjdConnector] = None
                self.is_exist = self._get_is_exist()
                self._get_bjd_connectors()
        ```

-   Example

    -   Run

        ```python
        from vdutils.bjdconnector import FullBjdConnectorGraph

        FBCG = FullBjdConnectorGraph()
        FBCG.full_bjd_connectors.get('5100000000')._print()
        ```

    -   Output

        ```
        full_bjd_cd: 5100000000
        full_bjd_nm: 강원특별자치도
        is_exist: True
        created_dt: 2023-06-09
        deleted_dt: None
        before: [FullBjdConnector()]
        after: []
        is_smallest: None
        sido: True
        sgg: None
        emd: None
        ri: None
        sido_nm: 강원특별자치도
        sgg_nm: None
        emd_nm: None
        ri_nm: None
        sido_cd: 5100000000
        sgg_cd: None
        emd_cd: None
        ri_cd: None
        sido_bjd_connector: BjdConnector()
        sgg_bjd_connector: None
        emd_bjd_connector: None
        ri_bjd_connector: None
        ```

    -   Run

        ```python
        # 5100000000 의 단위 법정동별 BjdConnector 또한 조회 가능하며 5100000000 의 경우, 시도 단위 법정동이므로 시도 단위 BjdConnector 를 조회하면 아래와 같은 출력을 확인가능 함
        FBCG.full_bjd_connectors.get('5100000000').sido_bjd_connector._print()
        ```

    -   Output

        ```
        typ: sido
        bjd_cd: 5100000000
        bjd_nm: 강원특별자치도
        full_bjd_nm: 강원특별자치도
        metadata: BjdObject()
        top_bjd_typ: None
        top_bjd_cd: []
        top_bjd_nm: []
        top_bjd: []
        bottom_bjd_cd: ['5111000000', '5113000000', '5115000000', '5117000000', '5119000000', '5121000000', '5123000000', '5172000000', '5173000000', '5175000000', '5176000000', '5177000000', '5178000000', '5179000000', '5180000000', '5181000000', '5182000000', '5183000000']
        bottom_bjd_nm: ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군']
        bottom_bjd: [BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector()]
        is_smallest: False
        ```

    -   Run

        ```python
        # 5100000000 의 변경 전 법정동 데이터는 .before 를 통해서 조회 가능하며 해당 데이터는 리스트 타입이기 때문에 순서값을 지정해줘야 함
        # 다수의 법정동의 일부 영역에서 분리되어 생성된 예외적인 경우도 존재하나 일반적으로는 첫번째 값으로 조회가능 함
        FBCG.full_bjd_connectors.get('5100000000').before[0]._print()
        ```

    -   Output

        ```
        full_bjd_cd: 4200000000
        full_bjd_nm: 강원도
        is_exist: False
        created_dt: 1988-04-23
        deleted_dt: 2023-06-09
        before: []
        after: [FullBjdConnector()] # 변경 전 법정동 데이터이므로 after 에 변경 후 법정동 데이터가 존재
        is_smallest: None
        sido: True
        sgg: None
        emd: None
        ri: None
        sido_nm: 강원도
        sgg_nm: None
        emd_nm: None
        ri_nm: None
        sido_cd: 4200000000
        sgg_cd: None
        emd_cd: None
        ri_cd: None
        sido_bjd_connector: BjdConnector()
        sgg_bjd_connector: None
        emd_bjd_connector: None
        ri_bjd_connector: None
        ```

    -   Run

        ```python
        # 5100000000 의 변경 전 법정동 데이터의 단위 법정동별 BjdConnector 또한 조회 가능하며 5100000000 의 변경 전 법정동 데이터 경우도 시도 단위 법정동이므로 시도 단위 BjdConnector 를 조회하면 아래와 같은 출력을 확인가능 함
        FBCG.full_bjd_connectors.get('5100000000').before[0].sido_bjd_connector._print()
        ```

    -   Output

        ```
        typ: sido
        bjd_cd: 4200000000
        bjd_nm: 강원도
        full_bjd_nm: 강원도
        metadata: BjdObject()
        top_bjd_typ: None
        top_bjd_cd: []
        top_bjd_nm: []
        top_bjd: []
        bottom_bjd_cd: ['4205000000', '4211000000', '4213000000', '4215000000', '4217000000', '4219000000', '4221000000', '4223000000', '4271000000', '4271500000', '4272000000', '4273000000', '4274000000', '4274500000', '4275000000', '4276000000', '4277000000', '4278000000', '4279000000', '4280000000', '4281000000', '4282000000', '4283000000', '4284000000', '4285000000']
        bottom_bjd_nm: ['울진군', '춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '춘성군', '춘천군', '홍천군', '횡성군', '원성군', '원주군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군', '명주군', '삼척군']
        bottom_bjd: [BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector(), BjdConnector()]
        is_smallest: False
        ```

</details><br>
<br>

# Usage(Administrator Only)

## Bjd

공공데이터 법정동 관련 API 를 수집하고 자체 관리중인 보조 데이터들을 이용하여 BjdConnector, ConvAddr 에 사용하는 법정동 관련 데이터프레임을 생성 및 편집하고 텍스트 형식으로 저장하는 모듈\
관리중인 법정동 데이터 파일 목록

-   `bjd.txt`: 공공데이터에서 제공중인 전체기간(1988-)의 법정동 개요 데이터이며 과거법정동코드, 법정동코드, 삭제일자, 생성일자, 순위, 시도명, 시군구명, 읍면동명, 리명, 법정동명이 포함됨
-   `bjd_current.txt`: 공공데이터에서 제공중인 전체기간(1988-)의 법정동 개요 데이터 중 삭제되거나 변경된 법정동을 제외한 **현행 법정동** 개요 데이터
-   `bjd_changed.txt`: 공공데이터에서 제공중인 전체기간(1988-)의 법정동 변경사항 데이터이며 법정동코드*변경후, 법정동명*변경후, 생성일자*변경후, 삭제일자*변경후, 법정동코드*변경전, 법정동명*변경전, 생성일자*변경전, 삭제일자*변경전, 변경내역이 포함됨
-   `bjd_smallest.txt`: 현행 법정동 개요 데이터 중 최소 단위 법정동명 데이터
-   `bjd_frequency_dictionary.txt`: 현행 법정동 개요 데이터의 단위 법정동명별 빈도수 딕셔너리

공공데이터 법정동 관련 API 수집은 관리자가 보유중인 api-key 를 이용하여 법정동 변경사항 및 업데이트 필요한 시점에 재수집 및 재새성하여 배포하며, 배포 시점의 법정동 데이터 파일은 /data 를 통해 확인가능
