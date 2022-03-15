## Context Switching


#### Context 란 무엇인가?
* CPU가 해당 프로세스를 실행하기 위한 해당 프로세스의 정보들.
* Context는 프로세스의 PCB(Process Control Block)에 저장된다.

##### PCB 
![pcb](https://github.com/kky0426/TIL/blob/master/CS/images/pcb.png?raw=true)

<br>

1. Process ID
    - 프로세스 식별자
2. Process State 
    - 생성(create),준비(ready),실행(running),대기(waiting),완료(terminated)
3. Program Counter
    - 프로세스가 다음에 실행할 명령어의 주소
4. Registers
    - 사용중인 레지스터 정보
5. Scheduling information
    - 우선순위, 최종 실행시각, CPU 점유시간 등
6. Memory limits
    - 사용가능한 메모리 공간 정보
7. Pointer
    - 부모,자식 프로세스에 대한 포인터, 프로세스가 위치한 메모리 주소에 대한 포인터, 할당된 자원에 대한 포인터 정보
 
<br>

---

#### Context Switching 이란?
* 하나의 프로세스가 CPU 를 사용중인 상태에서 다른 프로세스를 실행하기 위해 사용중인 프로세스의 상태를 저장하고 새로운 프로세스의 상태를 적재하는 작업.
* Context Switching 중에는 CPU는 아무런 작업을 할 수없다 -> 오버헤드 발생
* 매번 하나의 Task 만 실행된다면 Task가 끝날때 까지 기다릴 수 밖에 없다. --> Context Switching 을 통해 빠른 속도로
Task를 바꿔가며 실행하여 실시간처럼 보이게 한다.

##### - Context Switching Cost

    1. Cache 초기화
    2. Memory Mapping 초기화

##### - Context Switching 발생 시점

1. 멀티태스킹(Multitasking)  

    * 실행 가능한 프로세스들이 운영체제의 스케줄러에 의해 조금씩 번갈아가며 수행되는 것을 말한다.
    * 번갈아 가며 프로세스가 CPU 를 할당 받는데 이때 Context Switching 이 발생한다.
2. 인터럽트 핸들링(Interrupt handling)  
    * I/O request : 입출력 요청
    * Time slice expried : CPU 사용시간 만료
    * Fork a child : 자식 프로세스 생성
    * Wait for an interrupt : 인터럽트 처리 대기
    
3. 사용자와 커널 모드 전환(User and kernel mode switching)  
    * 필수는 아니지만 운영체제에 따라 발생할 수 있다.
    

##### - Context Switching 진행 과정

         1. 인터럽트 또는 트랩에 의한 요청 발생
         2. 운영체제는 현재 실행중인 프로세스의 정보를 PCB에 저장
         3. 운영체제는 다음 실행할 프로세스의 정보를 PCB에서 가져와 CPU를 할당 
