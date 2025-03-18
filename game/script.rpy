image bg museum_scene = "/Users/sojian/Desktop/renpy-8.3.6-sdk/test project/image/background/museum_scene.png"
define gui.text_font = "fonts/NanumGothic.ttf"


label start:
    # 블랙 화면에서 시작
    scene black with fade
    "..."

    # 배경 이미지 출력
    scene bg museum_scene with fade
    "눈앞이 밝아졌다. 박물관 내부가 희미하게 보인다."

    return
