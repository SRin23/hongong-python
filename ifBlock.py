#블럭
#콜론다음 들여쓰기된 코드 -> 블럭
#같은 실행 흐름에서 순서대로 실행되는 코드덩어리이다
#블럭의 특징---------------------------------
#블럭은 반드시 콜론문자뒤에서 들여쓰기하여 나타난다.
#여러줄로 쓰일 수 있다.
#들여쓰기가 맞지 않으면 eroor가 발생한다.
#내부의 블럭은 외부의 블럭에 종속적이다.
#파이썬 코드 전체를 하나의 블럴긍로도 볼 수 있다.

#아래 if True로 감싸진 코드는 하나의 블럭이다
if True : 
  print('블럭에 속한 코드')
  print('한줄더')
  print('모든 줄의 들여쓰기가 같아야 한다.(다르면 error)')
  if False :
    print('블럭안에 블럭 생성이 가능하다')
    print('이 문장은 실행되지 않는다.')
  if True :
    print('이렇게 적으면 실행된다')
    if True : 
      print('계속해서 블럭안에 블럭을 생성할 수 있다.')
  print('블럭의 끝코드')

print('블럭 끝')
print('이건 들여쓰기가 없으므로 위의 코드블럭과는 무관하다')
print('위의 코드블럭을 닫았으므로 다시 열거나 이어적을 수 없다')

if False : 
  print('조건이 맞지 않는 코드')
  if True : 
    print('조건이 맞는 코드')
    print('어쨌든 이 블럭 내부의 모든 값을 실행되지 않는다.')

print('위 블럭은 실행되지 않았습니다.')