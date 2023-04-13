#### REST API

**HTTP**

- 웹상 통신규약

- 웹에서 이루어지는 모든 데이터 교환의 기초

- 특징 : 무상태, 비연결성

- HTTP Request Methods
  
  - 리소스에 대한 행위(수행하고자 하는 동작)를 정의
  
  - CRUD
    
    GET(R)
    
    POST(C)
    
    PUT(U)
    
    DELETE(D)

- HTTP response status codes
  
  - Successful responses(200-299)- 정상
  
  - Client error response(400-499)
  
  - Server error respinses(500-599)



**Identifying resources on the Web**

- 웹에서의 리소스 식별
  
  \> 각 리소스는 식별을 위해 URI로 식별됨



##### URI(Uniform Resource Identifier, 통합 자원 식별자)

- 인터넷에서 리소스를 식별하는 문자열

- 가장 일반적인 URI는 웹 주소로 알려진 **URL**(Uniform Resource Locator, 통합 자원 위치)
  
  - 웹에서 주어진 리소스의 주소
  
  - 네트워크 상에 리소스(HTML, CSS, 이미지 등)가 어디 있는지(주소)를 알려주기 위한 약속
  
  - URL의 구성은 일부는 필수이고 나머지는 선택사항

- 특정 이름공간에서 이름으로 리소스를 식별하는 URI는 **URN**(Uniform Resource Name) - 위치가 바뀌어도 이름은 변하지않음



##### URL 구조

- Scheme(or protocol)
  
  - 브라우저가 리소스를 요청하는데 사용해야 하는 프로토콜
  
  - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
  
  - 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 mailto: 파일 전송 위한 ftp:등 다른 프로토콜도 존재

- Authority
  
  - Scheme 다음은 문자패턴 **://** 으로 구분된 권한이 작성됨
  
  - authority는 domain과 port를 모두 포함하며 둘은 :(콜론)으로 구별됨
  1. Domain Name
     
     요청 중인 웹 서버를 나타냄
  
  2. Port
     
     웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
     
     HTTP 프로토콜의 표준 포트는 다음과 같고 생략이 가능(나머지는 생략 불가능) : HTTP-80, HTTP-443
     
     장고의 경우 8000(80+00)이 기본 포트로 설정되어 있음

- Path
  
  - 웹 서버의 리소스 경로
  
  - 초기 : 실제 파일이 위치한 물리적 위치
    
    현대 : 실제 위치가 아닌 추상화된 형태의 구조를 표현

- Parameters
  
  - 웹 서버에 제공하는 추가적인 데이터

- Anchor
  
  - 리소스의 다른 부분에 대한 앵커
  
  - 리소스 내부 일종의 북마크를 나타냄



#### REST API

#### API

- Application Programming Interface

- 애플리케이션과 프로그래밍으로 소통하는 방법

- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)이라고 볼 수 있음

- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇가지 더 쉬운 구문을 제공



##### Web API

- 웹 서버 또는 웹 브라우저를 위한 API

- 현재 웹 개발은 여러 Open API를 활용하는 추세

- API는 다양한 타입의 데이터를 응답
  
  : HTML, XML, **JSON**등



##### REST

- Representational State Transfer

- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론

- REST원리를 따르는 시스템을 RESTful(자원-자원식별자- 따로 행동-HTTP메서드- 따로) 하다고 부름

- REST의 기본 아이디어는 리소스, 즉 자원
  
  \> 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

- (수업~~!)HTTP프로토콜을 기반으로 자원 식별자와 HTTP메서드를 사용하여 제한된 인터페이스상에서 클라이언트와 서버간의 상호작용을 하게 해주는 아키텍쳐(구조)



- REST에서 자원을 정의하고 주소를 지정하는 방법
  
  1. 자원의 식별
     
     \> URI
  
  2. 자원의 행위
     
     \> HTTP Method
  
  3. 자원의 표현
     
     \> 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
     
     \> JSON으로 표현된 데이터를 제공



##### JSON

- lightweight data-interchange format

- 자바스크립트의 표기법을 따른 단순 문자열

- 파이썬의 딕셔너리, 자바스크립트의 object처럼 C계열의 언어가 가지고 있는 자료구조로 쉽게 변환 가능한 **key-value**형태의 구조를 가지고 있음

- 사람이 읽고 쓰기 쉽고 기계가 파싱(해석, 분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터타입



**Serialization**(직렬화)

- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
  
  \> 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변경하는 과정



##### Django REST framework(DRF)

- django RESTful API서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

- DRF의 serializer는 장고의 form 및 modelform과 매우 유사하게 작동
