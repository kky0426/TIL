
## 프로세스 vs 스레드
<br>

### 프로세스 
* 메모리에 올라와 실행되고 있는 프로그램
* 운영체제로부터 시스템 자원을 할당받는 작업의 단위
  * 할당받는 시스템자원?<br>
  -- CPU 시간<br>
  -- 운영되기 위해 필요한 주소공간 <br>
  -- code,data,stack,heap 구조로 되어있는 독립된 메모리 영역
  <br>


<br>

![process_image](https://github.com/kky0426/TIL/blob/master/CS/images/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EB%A9%94%EB%AA%A8%EB%A6%AC.png?raw=true)

* 프로세스는 각각 독립된 메모리 영역을 할당받는다
* 프로세스는 최소 1개의 스레드(메인 스레드)를 가지고 있다
* 각 프로세스는 별도의 주소 공간에서 실행되며, 한 프로세스는 다른 프로세스의 변수나 자료구조에 접근 할 수 없다. (접근하려면 IPC 사용)

<br>

### 스레드 
* 프로세스 내에서 실행되는 흐름의 단위
* 프로세스가 할당받은 자원을 이용하는 실행의 단위

![thread_image](https://github.com/kky0426/TIL/blob/master/CS/images/%EC%8A%A4%EB%A0%88%EB%93%9C%EB%A9%94%EB%AA%A8%EB%A6%AC.png?raw=true)
* 스레드는 각각의 PC register 와 stack 을 갖고있다.
* 스레드는 프로세스의 code,data,heap 영역을 공유한다.