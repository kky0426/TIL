## DI 와 IOC

### IOC (Inversion Of Control)

- 제어의 역전
- 프로그램의 흐름을 개발자가 아닌 프레임워크가 제어한다
- 개발자가 객체를 직접 생성, 관리하지 않고 객체의 생명주기를 컨테이너가 관리
- 의존성을 역전시켜 객체간의 결합도를 줄이고 유연한 코드를 작성할 수 있다


ex)
```java
class Player{
    private SoccerBall soccerBall = new SoccerBall();
    
    public void drrible(){
        System.out.println("player drrible"+soccerBall);
    }
    
}

Player 클래스에서 SoccerBall 객체를 직접 생성한다. -> 제어권이 Player에게 있다.
Player 가 SoccerBall에 의존하고 있어 유연하지 못함.
```

```java
class Player{
    private SoccerBall  soccerBall;
    
    public Player(SoccerBall soccerBall){
        this.SoccerBall = soccerBall;
    }
    
    public void drrible(){
        System.out.println("player drrible"+soccerBall);
    }
    
}

외부에서 SoccerBall 클래스를 주입받는다(DI) -> 제어권이 DI를 수행하는 스프링 IoC 컨테이너에게 넘어감
```
<br>

객체 생성 -> 의존성 객체 생성 -> 의존성 객체 메소드 수행 의 과정이 아닌 <br>
객체 생성 -> 의존성 객체 주입 -> 의존성 객체 메소드 수행 이 일어난다. <br>
개발자가 의존성 객체를 관리하지 않고 스프링이 IoC 컨테이너에 의존성 객체들을 생성하고 필요한곳에 주입해준다

---

## DI (Dependency Injection)
- 객체를 내부에서 생성하지 않고 외부에서 주입받는 방식.
- IoC 의 대표적인 예
- 객체간의 결합도를 줄이고 유연한 코드를 작성해 유지보수에 용이하다.

```java

class Player{
    private SoccerBall soccerBall = new SoccerBall();

    public void drrible(){
        System.out.println("player drrible"+soccerBall);
    }

}

객체 내부에서 의존성 객체를 생성한다. Player 와 SoccerBall 은 강하게 결합 되어 확장이 어렵다.
축구공뿐만 아니라 농구공 등 다른 공이 추가되어야 한다면?
```

```java
class Player{
    private Ball ball;
    
    public Player(Ball soccerBall){
        this.ball = soccerBall;
    }
    
    public void drrible(){
        System.out.println("player drrible"+ball);
    }
}

의존성을 외부에서 주입받아 결합도를 낮췄다.
Ball 인터페이스를 구현한 다른 공들을 주입해주면 축구공 뿐만아니라 다른 공들에 대한 확장도 가능하다
```
<br>

### Spring의 DI 방식

1. Filed 주입 방식

```java
@Component
public class A{
    @Autowired
    private B b;
}
```
- final 을 선언할 수 없어 객체가 변할 수 있다.
- 순환 참조를 알기 어렵다.

2. Setter 주입 방식
```java
@Component
public class A{
    private B b;
    
    @Autowired
    public void setB(B b){
        this.b = b;
    }
    
}
```
- 선택적인 의존성 주입이 가능하다.
- 객체가 생성되어도 의존성 주입이 되지 않으면 NPE 이 발생할 수 있다.

3. Constructor 주입 방식
```java
@Component
public class A{
    private final B b;
    
    @Autowired
    public A(B b){
        this.b = b;
    }
}
```
- 스프링에서 권장하는 주입 방식
- final 선언으로 객체의 불변성이 보장된다.
- 순환 참조를 컴파일 타임에 알 수 있다.
- null을 주입하지 않는 이상 NPE 이 발생하지 않는다.ㅑ