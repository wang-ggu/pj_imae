init python:
    style.default.font = "fonts/NanumGothic.ttf"
    style.say_dialogue.font = "fonts/NanumGothic.ttf"
    style.say_label.font = "fonts/NanumGothic.ttf"
    style.say_thought.font = "fonts/NanumGothic.ttf"

define 하비 = Character('하비')
define 자청 = Character('자청')
define 남강 = Character('남강')
define 만인혈석 = Character('만인혈석')

label start:

    scene black
    play sound "sword_clash.ogg"
    with dissolve  # flash 대신 dissolve 효과 사용 (렌파이 기본 지원)
    # 칼 부딪치는 소리와 화면 깜빡임 반복 (여러 번)

    play sound "big_boom.ogg"
    scene bg museum_scene with fade
    # 박물관 내부 푸르스름한 조명

    show 하비 흐트러진모습 at left
    show 자청 여유로운표정 at right

    하비 "청! 똑바로 안 싸울래?!"
    자청 "옙! 똑바로 싸우고 있습니다!"
    하비 "나 지금 장난칠 기분 아니거든?"
    자청 "나도 지금 장난치는 거 아니거든? 재해급이라고요, 재해!"

    하비 "칫…."
    자청 "어엇, 또 온다! 피해!"

    play sound "small_explosions.ogg"
    scene shake
    show 하비 화난표정

    자청 "이러다 우리가 퇴마 당하는 거 아냐?!"
    하비 "됐어! 더 이상은 못 참아! 청! 10초야! 무조건 막아!"
    자청 "네~ 네~ 쇤내 주둥이를 딱 틀어막겠습니다요."

    play sound "clash_block.ogg"
    show 하비 클로즈업
    하비 "여시아문일시불 천황대제수명장 지황대제증복수…. 급급여율령…. 사바하!"

    show 연꽃빛발사
    play sound "laser_blast.ogg"
    show 만인혈석 등장
    만인혈석 "끼에에에…!!"

    하비 "신벌이다, 이 뱀 자식아!"
    자청 "오~~ 웬일이야. 제대로 먹였는데?"
    하비 "시끄러워! 저 녀석 회복하기 전에 얼른 끝내버리자."
    자청 "옙! 바로 살풀이 작업 들어가겠습니다! 쿵짝짝, 쿵짝짝…."

    scene black with dissolve
    play sound "speaker_break.ogg"
    show 남강 가면클로즈업

    하비 "남강… 서생…!"
    남강 "못난 놈."

    show 만인혈석 그을린모습 남강옆에
    남강 "내 너를 저런 허섭스레기들에게 당하도록 기르지 않았거늘."

    하비 "뭐, 뭐라고? 나를… 잊었어…?"
    자청 "암, 우리가 좀 밋밋하게 생기기는 했지."
    하비 "청. 닥쳐."
    자청 "넵."

    하비 "…남강. 네가 여기는 웬일이냐."
    남강 "글쎄…. 네깟 게 알아서 무엇하지?"
    하비 "네놈…!"

    남강 "주제도 모르고, 평생 메우지도 못할 호수를 갈망하던 천치 같은 계집 아니더냐! 골계! 골계로다!"
    하비 "미친 새끼…."

    남강 "그만 되었으니 썩 물러가거라. 오늘 밤은 이매와 망량의 시간."
    하비 "청."
    자청 "그래."
    하비 "나… 참을 만큼 참았어. 이해하지?"
    자청 "어, 인정."
    하비 "가자."

    하비 "청사원사진군 육정육갑제대신장… 급급여율령 사하바!"
    하비 "수라멸망꽃!!!"

    show 붉은꽃빛발사
    play sound "explosion.ogg"

    show 남강 과 만인혈석
    남강 "어리석은 계집이로고…. 가라. 가서, 먹어치워라."
    show 만인혈석 그림자 하비자청위로

    자청 "젠장…! 비야…! 정신 차려, 비야…!"

    return

